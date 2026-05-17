# Run this inside TouchDesigner: File > Run Script, or paste into Textport with:
# exec(open(r"C:\Users\kidis\Documents\Codex\2026-05-17\fill-in-this-sequencer\fix_sequencer_switch.py").read())

p = op('/project1')

# Create or reuse a TOP Switch for the movie/image TOPs.
sw = p.op('switch_top_movies')
if sw is not None and sw.family != 'TOP':
    sw.destroy()
    sw = None

if sw is None:
    sw = p.create(switchTOP, 'switch_top_movies')

sw.nodeX = 450
sw.nodeY = -350

sources = [
    p.op('moviefilein6'),
    p.op('moviefilein7'),
    p.op('moviefilein8'),
    p.op('moviefilein9'),
    p.op('moviefilein10'),
]

for i, src in enumerate(sources):
    if src is not None:
        sw.inputConnectors[i].connect(src)

# Use the first Sequencer CHOP channel if it exists; otherwise keep index at 0.
# int(...) prevents blend/interpolation values from confusing the Switch TOP.
sw.par.index.expr = (
    "int(op('/project1/sequencer1').chan(0).eval()) "
    "if op('/project1/sequencer1').numChans else 0"
)

# Add a clean output TOP after the switch.
out = p.op('sequenced_movie_out')
if out is None:
    out = p.create(nullTOP, 'sequenced_movie_out')

out.nodeX = sw.nodeX + 180
out.nodeY = sw.nodeY
out.inputConnectors[0].connect(sw)

print('Done: moviefilein6-10 -> switch_top_movies -> sequenced_movie_out')
