# Mag het op Collectie Nederland?

Klikbare keuzehulp bij de vraag: *mag ik dit werk op CollectieNederland.nl tonen?*

De keuzehulp volgt het stroomdiagram van de RCE en de toelichting uit het rapport ‘Auteursrecht x CollectieNederland’. Daarna krijg je een uitkomst met de reden, de vervolgstappen en eventuele signalen over het rechtenveld.

## Opbouw

De keuzehulp heeft twee delen.

**Deel 1 · Welke rechten**: dit is een aanvulling op het stroomdiagram, op basis van hetzelfde rapport.

1. Wat staat er in het rechtenveld? Publiek domein, CC0 of een CC-licentie, In Copyright, of niet beoordeeld/leeg.
2. Is het werk zelf nog beschermd? Het peiljaar rekent de pagina zelf uit: 70 jaar na het sterfjaar van de maker.
3. Is het werk publiek domein? Dan volgt de vraag of de afbeelding een plat werk laat zien of een 3D-object. Bij een 3D-object kan de foto eigen rechten van de fotograaf hebben.
4. Staat er een CC-licentie? Dan volgt de vraag of de rechthebbende die zelf heeft gegeven.

**Deel 2 · Stroomdiagram RCE**: dit deel is ongewijzigd.

1. Hoe ga je het werk tonen: embedden of framen, of zelf hosten?
2. Toont de bronhouder het werk zelf op diens eigen website?
3. Heeft de bronhouder maatregelen genomen om embedding tegen te houden?
4. Heeft de bronhouder een overeenkomst met Pictoright?
5. Heb je toestemming van de rechthebbende?

Welke vragen je krijgt, hangt af van je antwoorden.

## Mogelijke uitkomsten

| Uitkomst | Betekenis |
| --- | --- |
| Publiek domein | Het werk is vrij en de afbeelding is een getrouwe reproductie van een plat werk. |
| Toegestaan (CC) | De rechthebbende heeft een CC-licentie of CC0-verklaring gegeven. |
| Toegestaan | Je hebt toestemming van de rechthebbende (overeenkomst of CC-licentie). |
| Zeer laag risico | Embedden van materiaal dat vrij online staat bij de bronhouder. |
| Eerst controleren | De bronhouder heeft een overeenkomst met Pictoright. Vraag na of die embedden toestaat. |
| Niet embedden | De bronhouder heeft maatregelen genomen om embedding tegen te houden. |
| Niet tonen | Er is geen toestemming en het werk staat niet vrij online. |

Bij elke uitkomst staan het risico voor RCE, de juridische grondslag en wat je daarna doet. Klopt het rechtenveld volgens je antwoorden niet, dan staat er ook een **signaal voor het rechtenveld**. Een voorbeeld: het veld zegt publiek domein, maar het werk is nog beschermd. Met **Kopieer advies** neem je de route, de uitkomst en de signalen als tekst over, bijvoorbeeld voor een mail of ticket.

## Rechtenstatements vertaald

Onder het schema staat een tabel met de rechtenstatements die Europeana accepteert: PDM, NoC-NC, NoC-OKLR, CC0, de CC-licenties, InC, InC-EDU, InC-OW-EU, CNE en UND, plus een leeg veld. Per statement zie je wat het betekent, of het toestemming geeft en waar je in de keuzehulp terechtkomt. Met **Start** begin je direct met dat statement.

## Bestanden

| Bestand | Doel |
| --- | --- |
| `keuzehulp.html` | De bron. Hieruit wordt ook het Claude-artifact op claude.ai gepubliceerd; dat voegt zelf het HTML-skelet toe. |
| `index.html` | De keuzehulp voor GitHub Pages, gemaakt door `maak-index.py`. Pas dit bestand niet met de hand aan. |
| `maak-index.py` | Zet het HTML-skelet om `keuzehulp.html` heen en schrijft `index.html`. |
| `.gitignore` | Houdt de originele brondocumenten (`*.pdf`, `*.docx`) buiten de repository. |

## Inhoud aanpassen

1. Pas `keuzehulp.html` aan. De vragen, uitleg en uitkomsten staan in het object `N` bovenaan het script, de rechtenstatements in `RS`. De ligging van de pijlen in het schema staat in `EDGES`.
2. Voer het script uit:

   ```bash
   python maak-index.py
   ```

## Lokaal bekijken

Open `index.html` in een browser. De lettertypen komen van Google Fonts. Zonder internetverbinding valt de pagina terug op systeemlettertypen.

## Publiceren op GitHub Pages

1. Push de repository naar GitHub.
2. Ga naar *Settings → Pages*.
3. Kies bij *Source* de hoofdbranch en de map `/ (root)`.

## Let op

De keuzehulp geeft richting bij de keuze, maar is geen juridisch advies voor een concreet werk. Deel 1 en de tabel met rechtenstatements gaan verder dan het officiële stroomdiagram. Laat ze nalezen door een jurist voordat de keuzehulp breed gebruikt wordt. Twijfel je over een concreet werk, overleg dan met een jurist.
