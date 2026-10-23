# Mag het op Collectie Nederland?

Klikbare keuzehulp bij de vraag: *mag ik dit auteursrechtelijk beschermde werk op CollectieNederland.nl tonen?*

De keuzehulp volgt het stroomdiagram van de RCE en de toelichting uit het rapport ‘Auteursrecht x CollectieNederland’. Je beantwoordt hooguit vier vragen. Daarna krijg je een uitkomst met de reden en de vervolgstappen.

## Wat de keuzehulp vraagt

1. Hoe ga je het werk tonen: embedden of framen, of zelf hosten?
2. Toont de bronhouder het werk zelf op diens eigen website?
3. Heeft de bronhouder maatregelen genomen om embedding tegen te houden?
4. Heeft de bronhouder een overeenkomst met Pictoright?
5. Heb je toestemming van de rechthebbende?

Welke vragen je krijgt, hangt af van je antwoorden.

## Mogelijke uitkomsten

| Uitkomst | Betekenis |
| --- | --- |
| Toegestaan | Je mag het werk tonen, met toestemming van de rechthebbende (overeenkomst of CC-licentie). |
| Zeer laag risico | Embedden van materiaal dat vrij online staat bij de bronhouder. |
| Eerst controleren | De bronhouder heeft een overeenkomst met Pictoright. Vraag na of die embedden toestaat. |
| Niet embedden | De bronhouder heeft maatregelen genomen om embedding tegen te houden. |
| Niet tonen | Er is geen toestemming en het werk staat niet vrij online. |

Bij elke uitkomst staan het risico voor RCE, de juridische grondslag en wat je daarna doet. Met **Kopieer advies** neem je de route en de uitkomst als tekst over, bijvoorbeeld voor een mail of ticket.

## Bestanden

| Bestand | Doel |
| --- | --- |
| `index.html` | De keuzehulp voor GitHub Pages. Dit is één statisch bestand, zonder build-stap of server. |
| `keuzehulp.html` | Dezelfde pagina als bron voor het Claude-artifact op claude.ai. Het artifact voegt zelf het HTML-skelet toe. |
| `.gitignore` | Houdt de originele brondocumenten (`*.pdf`, `*.docx`) buiten de repository. |

Wijzig je de inhoud, pas dan beide HTML-bestanden aan. De vragen, uitleg en uitkomsten staan bovenaan het script in het object `N`.

## Lokaal bekijken

Open `index.html` in een browser. De lettertypen komen van Google Fonts. Zonder internetverbinding valt de pagina terug op systeemlettertypen.

## Publiceren op GitHub Pages

1. Push de repository naar GitHub.
2. Ga naar *Settings → Pages*.
3. Kies bij *Source* de hoofdbranch en de map `/ (root)`.

## Let op

De keuzehulp geeft richting bij de keuze, maar is geen juridisch advies voor een concreet werk. Twijfel je, overleg dan met een jurist.
