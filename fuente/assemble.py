#!/usr/bin/env python3
"""Arma el kit final en ../kit: control, panel MIDI, gráficos, transiciones y fuentes."""
import base64, os, shutil, glob
OUT = '/home/claude/imperial/kit'
B = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
F = 'node_modules/@fontsource/'
FONTS = ''.join('@font-face{font-family:"%s";font-weight:%d;src:url(data:font/woff2;base64,%s) format("woff2");}' % (f, w, B(F + p)) for f, p, w in [
    ('Roboto', 'roboto/files/roboto-latin-400-normal.woff2', 400),
    ('Roboto', 'roboto/files/roboto-latin-500-normal.woff2', 500),
    ('Roboto', 'roboto/files/roboto-latin-700-normal.woff2', 700),
    ('Roboto Condensed', 'roboto-condensed/files/roboto-condensed-latin-700-normal.woff2', 700),
    ('Roboto Condensed', 'roboto-condensed/files/roboto-condensed-latin-900-normal.woff2', 900)])
LOGO = 'data:image/png;base64,' + B('../Logo_Imperial_web.png')
for d in ['Paneles', 'fuente', 'Logos']:
    os.makedirs(OUT + '/' + d, exist_ok=True)
for src, dst in [('control_template.html', 'CONTROL_EN_VIVO.html'), ('midi_template.html', 'PANEL_MIDI.html')]:
    open(OUT + '/' + dst, 'w').write(open(src).read().replace('__FONTS__', FONTS).replace('__LOGO__', LOGO))
for f in glob.glob('out/IMP_*.html'):
    shutil.copy(f, OUT + '/Paneles/')
shutil.copy('../Logo_Imperial_web.png', OUT + '/Logos/Imperial_logo_blanco_web.png')
for f in ['build.py', 'build_stingers.py', 'rebrand.py', 'make_control.py', 'make_midi.py', 'control_head.html', 'control_a.js', 'hst.js', 'assemble.py']:
    shutil.copy(f, OUT + '/fuente/')
print('ok')
