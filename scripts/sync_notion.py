#!/usr/bin/env python3
"""Sync TouchDesigner journal pages from Notion into this repo.

Required environment:
  NOTION_TOKEN: Notion integration token with read access.
  NOTION_DATA_SOURCE_ID or NOTION_DATABASE_ID: source containing day pages.

Optional environment:
  NOTION_VERSION: defaults to 2026-03-11.

The script exports each Notion page as Markdown, HTML, and PDF when Playwright is
available. It also rewrites the README section between the Notion sync markers.
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "notion-sync.config.json"
README_PATH = ROOT / "README.md"
START_MARKER = "<!-- notion-sync:start -->"
END_MARKER = "<!-- notion-sync:end -->"


@dataclass
class SyncPage:
    page_id: str
    title: str
    day: int | None
    folder: Path | None
    toe_file: Path | None
    markdown_path: Path
    html_path: Path
    pdf_path: Path


def load_config() -> dict[str, Any]:
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


def notion_request(method: str, path: str, body: dict[str, Any] | None = None) -> dict[str, Any]:
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        raise SystemExit("Missing NOTION_TOKEN.")

    version = os.environ.get("NOTION_VERSION", "2026-03-11")
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        "https://api.notion.com" + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": version,
            "Content-Type": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Notion API error {exc.code} for {path}: {detail}") from exc


def paged_post(path: str, body: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    body = dict(body or {})
    results: list[dict[str, Any]] = []
    while True:
        payload = notion_request("POST", path, body)
        results.extend(payload.get("results", []))
        if not payload.get("has_more"):
            return results
        body["start_cursor"] = payload["next_cursor"]


def plain_text(rich_text: list[dict[str, Any]]) -> str:
    return "".join(part.get("plain_text", "") for part in rich_text or [])


def prop_to_text(prop: dict[str, Any] | None) -> str:
    if not prop:
        return ""
    typ = prop.get("type")
    value = prop.get(typ)
    if typ == "title":
        return plain_text(value)
    if typ == "rich_text":
        return plain_text(value)
    if typ == "url":
        return value or ""
    if typ == "select":
        return (value or {}).get("name", "")
    if typ == "multi_select":
        return ", ".join(item.get("name", "") for item in value or [])
    if typ == "files":
        return ", ".join(item.get("name", "") for item in value or [])
    if typ == "number":
        return "" if value is None else str(value)
    if typ == "formula":
        return prop_to_text(value)
    return str(value or "")


def page_title(page: dict[str, Any], title_property: str | None) -> str:
    props = page.get("properties", {})
    if title_property and title_property in props:
        title = prop_to_text(props[title_property])
        if title:
            return title
    for prop in props.values():
        if prop.get("type") == "title":
            title = prop_to_text(prop)
            if title:
                return title
    return page.get("id", "Untitled")


def normalize_day_folder_name(path: Path) -> int | None:
    match = re.search(r"\bday\s*[-_ ]*(\d+)\b", path.name, flags=re.I)
    return int(match.group(1)) if match else None


def infer_day(title: str, page: dict[str, Any], config: dict[str, Any]) -> int | None:
    day_property = config.get("day_property", "day")
    props = page.get("properties", {})
    candidates = [title]
    if day_property in props:
        candidates.insert(0, prop_to_text(props[day_property]))
    for prop_name in config.get("extra_day_properties", ["Tags"]):
        if prop_name in props:
            candidates.append(prop_to_text(props[prop_name]))
    for text in candidates:
        match = re.search(r"\bday\s*[:#-]?\s*(\d+)\b", text, flags=re.I)
        if match:
            return int(match.group(1))
        if text.strip().isdigit():
            return int(text.strip())
    return None


def all_day_folders() -> dict[int, Path]:
    folders: dict[int, Path] = {}
    for child in ROOT.iterdir():
        if child.is_dir():
            day = normalize_day_folder_name(child)
            if day is not None:
                folders[day] = child
    return folders


def find_toe_file(folder: Path | None, page: dict[str, Any], config: dict[str, Any]) -> Path | None:
    if folder is None:
        return None
    toe_prop = config.get("toe_property", ".TOE")
    requested = prop_to_text(page.get("properties", {}).get(toe_prop))
    toe_files = sorted(folder.glob("*.toe"))
    if requested:
        requested_lower = requested.lower()
        for toe in toe_files:
            if toe.name.lower() == requested_lower or toe.stem.lower() == Path(requested_lower).stem:
                return toe
    return toe_files[0] if toe_files else None


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "notion-page"


def retrieve_markdown(page_id: str) -> str:
    payload = notion_request("GET", f"/v1/pages/{page_id}/markdown")
    markdown = payload.get("markdown", "")
    if payload.get("truncated"):
        markdown += "\n\n> Note: Notion reported this export was truncated.\n"
    return markdown


def markdown_to_html(title: str, markdown: str, page: SyncPage) -> str:
    escaped = html.escape(markdown)
    body = re.sub(r"^### (.*)$", r"<h3>\1</h3>", escaped, flags=re.M)
    body = re.sub(r"^## (.*)$", r"<h2>\1</h2>", body, flags=re.M)
    body = re.sub(r"^# (.*)$", r"<h1>\1</h1>", body, flags=re.M)
    body = body.replace("\n\n", "</p><p>").replace("\n", "<br>")
    toe = html.escape(page.toe_file.name if page.toe_file else "No .toe file found")
    return f"""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 48px; line-height: 1.5; color: #171717; }}
    h1, h2, h3 {{ line-height: 1.15; }}
    .meta {{ color: #555; border-bottom: 1px solid #ddd; padding-bottom: 16px; margin-bottom: 28px; }}
    code, pre {{ background: #f4f4f4; padding: 2px 4px; }}
  </style>
</head>
<body>
  <h1>{html.escape(title)}</h1>
  <div class="meta">TouchDesigner file: {toe}</div>
  <p>{body}</p>
</body>
</html>
"""


async def pdf_with_playwright(html_path: Path, pdf_path: Path) -> bool:
    try:
        from playwright.async_api import async_playwright
    except Exception:
        return False

    async with async_playwright() as pw:
        browser = await pw.chromium.launch()
        page = await browser.new_page()
        await page.goto(html_path.as_uri(), wait_until="networkidle")
        await page.pdf(path=str(pdf_path), format="Letter", print_background=True)
        await browser.close()
    return True


def write_pdf(html_path: Path, pdf_path: Path) -> bool:
    import asyncio

    try:
        return asyncio.run(pdf_with_playwright(html_path, pdf_path))
    except Exception as exc:
        print(f"PDF skipped for {html_path.name}: {exc}", file=sys.stderr)
        return False


def relative(path: Path | None) -> str:
    if path is None:
        return ""
    return path.relative_to(ROOT).as_posix().replace(" ", "%20")


def build_readme_section(pages: list[SyncPage]) -> str:
    lines = [START_MARKER, "## Notion exports", ""]
    if not pages:
        lines += ["No Notion pages were exported.", "", END_MARKER]
        return "\n".join(lines)

    for page in sorted(pages, key=lambda p: (p.day or 9999, p.title.lower())):
        label = f"Day {page.day}" if page.day is not None else "Unsorted"
        lines.append(f"### {label}: {page.title}")
        links = [f"[Markdown]({relative(page.markdown_path)})", f"[HTML]({relative(page.html_path)})"]
        if page.pdf_path.exists():
            links.append(f"[PDF]({relative(page.pdf_path)})")
        if page.toe_file:
            links.append(f"[.toe]({relative(page.toe_file)})")
        lines.append(" | ".join(links))
        lines.append("")
    lines.append(END_MARKER)
    return "\n".join(lines)


def update_readme(pages: list[SyncPage]) -> None:
    section = build_readme_section(pages)
    existing = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else "# taw-002\n"
    if START_MARKER in existing and END_MARKER in existing:
        pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.S)
        updated = pattern.sub(section, existing)
    else:
        updated = existing.rstrip() + "\n\n" + section + "\n"
    README_PATH.write_text(updated, encoding="utf-8")


def query_pages(config: dict[str, Any]) -> list[dict[str, Any]]:
    source_id = os.environ.get("NOTION_DATA_SOURCE_ID")
    database_id = os.environ.get("NOTION_DATABASE_ID")
    body = {"page_size": 100}
    if config.get("filter"):
        body["filter"] = config["filter"]
    if config.get("sorts"):
        body["sorts"] = config["sorts"]
    if source_id:
        return paged_post(f"/v1/data_sources/{source_id}/query", body)
    if database_id:
        return paged_post(f"/v1/databases/{database_id}/query", body)
    raise SystemExit("Missing NOTION_DATA_SOURCE_ID or NOTION_DATABASE_ID.")


def main() -> None:
    config = load_config()
    folders = all_day_folders()
    export_root = ROOT / config.get("export_dir", "notion_exports")
    export_root.mkdir(exist_ok=True)

    synced: list[SyncPage] = []
    for page in query_pages(config):
        title = page_title(page, config.get("title_property"))
        day = infer_day(title, page, config)
        folder = folders.get(day) if day is not None else None
        toe_file = find_toe_file(folder, page, config)
        target_dir = export_root / (f"day-{day}" if day is not None else "unsorted")
        target_dir.mkdir(parents=True, exist_ok=True)

        slug = slugify(title)
        markdown_path = target_dir / f"{slug}.md"
        html_path = target_dir / f"{slug}.html"
        pdf_path = target_dir / f"{slug}.pdf"
        sync_page = SyncPage(page["id"], title, day, folder, toe_file, markdown_path, html_path, pdf_path)

        markdown = retrieve_markdown(page["id"])
        header = [f"# {title}", ""]
        if toe_file:
            header += [f"TouchDesigner file: [{toe_file.name}](../{relative(toe_file)})", ""]
        markdown_path.write_text("\n".join(header) + markdown.rstrip() + "\n", encoding="utf-8")
        html_path.write_text(markdown_to_html(title, markdown, sync_page), encoding="utf-8")
        write_pdf(html_path, pdf_path)
        synced.append(sync_page)

    update_readme(synced)
    print(f"Synced {len(synced)} Notion page(s).")


if __name__ == "__main__":
    main()
