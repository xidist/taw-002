# Run this inside TouchDesigner: File > Run Script, or paste into Textport with:
# exec(open(r"C:\Users\kidis\Documents\td\taw-002\day 7 - open_cv hand proj\fix_sequencer_switch.py").read())

p = op('/project1')

# Create one-channel Constant CHOPs that the Sequencer can step through.
# Each source outputs a clean integer index for the TOP Switch.
seq_sources = []
for i in range(5):
    c = p.op('seq_index{}'.format(i))
    if c is None:
        c = p.create(constantCHOP, 'seq_index{}'.format(i))
    c.nodeX = 450 + i * 100
    c.nodeY = -520
    c.par.name0 = 'index'
    c.par.value0 = i
    seq_sources.append(c)

# Fill the Sequencer DAT with CHOP paths, not TOP paths.
dat = p.op('sequencer1_list')
if dat is None:
    dat = p.create(tableDAT, 'sequencer1_list')

dat.clear()
for src in seq_sources:
    dat.appendRow([src.path])

seq = p.op('sequencer1')
if seq is not None:
    seq.par.datlist = dat
    seq.par.blendscope = ''
    seq.par.addscope = ''

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
        if hasattr(src.par, 'play'):
            src.par.play = 1
        sw.inputConnectors[i].connect(src)

# Animate the image sequence directly. This changes image every 60 frames.
# If you want it faster/slower, change 60 to another frame count.
sw.par.index.expr = "int(absTime.frame / 60) % 5"

# Add a clean output TOP after the switch.
out = p.op('sequenced_movie_out')
if out is None:
    out = p.create(nullTOP, 'sequenced_movie_out')

out.nodeX = sw.nodeX + 180
out.nodeY = sw.nodeY
out.inputConnectors[0].connect(sw)
out.viewer = True
out.display = True

print('Done: switch_top_movies cycles moviefilein6-10, and sequenced_movie_out shows the animated sequence.')
