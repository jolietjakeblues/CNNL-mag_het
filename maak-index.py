"""Maak de GitHub Pages-versies uit de bronbestanden van de Claude-artifacts.

De bronbestanden missen bewust het HTML-skelet, omdat het artifact dat zelf toevoegt.
Dit script zet het skelet en een kleine basisreset eromheen.

Gebruik:  python maak-index.py
"""
from pathlib import Path

HIER = Path(__file__).parent

# bronbestand -> (Pages-bestand, beschrijving)
PAGINAS = {
    "keuzehulp.html": (
        "index.html",
        "Keuzehulp: mag een auteursrechtelijk beschermd werk getoond worden op Collectie Nederland?",
    ),
    "beeldroutes.html": (
        "beeldroutes/index.html",
        "Embedden, framen, thumbnails en hosten naast elkaar, met het NDE-datasetregister en de freeze.",
    ),
}

RESET = """
/* Basisreset (op claude.ai voegt het artifact-skelet dit zelf toe) */
:root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
body { margin: 0; }
img { max-width: 100%; }
[hidden] { display: none !important; }
"""

HEAD = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{beschrijving}">
"""

for bron, (doel, beschrijving) in PAGINAS.items():
    src = (HIER / bron).read_text(encoding="utf-8")
    head, body = src.split("</style>\n", 1)
    head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
    head = head.replace("<style>\n", "<style>" + RESET, 1)

    out = HEAD.format(beschrijving=beschrijving) + head + "</style>\n</head>\n<body>\n" + body.rstrip() + "\n</body>\n</html>\n"
    pad = HIER / doel
    pad.parent.mkdir(parents=True, exist_ok=True)
    pad.write_text(out, encoding="utf-8", newline="\n")
    print(f"{doel} bijgewerkt")
