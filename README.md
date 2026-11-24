# Mag het op Collectie Nederland?

Klikbare keuzehulp bij de vraag: *mag ik dit werk op CollectieNederland.nl tonen?*

De keuzehulp volgt het stroomdiagram van de RCE en de toelichting uit het rapport ‘Auteursrecht x CollectieNederland’, de Q&A bij dat rapport, de Begrippenlijst auteursrecht en aanverwante rechten, en de Erfgoedwet en de Regeling beheer rijkscollectie en subsidiëring museale instellingen (Rbr). Daarna krijg je een uitkomst met de reden, de vervolgstappen en eventuele signalen over het rechtenveld.

## Opbouw

De keuzehulp heeft twee delen.

**Deel 1 · Welke rechten**: dit is een aanvulling op het stroomdiagram, op basis van hetzelfde rapport.

1. Wat staat er in het rechtenveld? Publiek domein, CC0 of een CC-licentie, In Copyright, of niet beoordeeld/leeg.
2. Is het werk zelf nog beschermd? Het peiljaar rekent de pagina zelf uit: 70 jaar na het sterfjaar van de maker.
3. Is het werk publiek domein? Dan volgt de vraag of de afbeelding een plat werk laat zien of een 3D-object. Bij een 3D-object kan de foto eigen rechten van de fotograaf hebben.
4. Staat er een CC-licentie? Dan volgt de vraag of de rechthebbende die zelf heeft gegeven.

**Deel 2 · Stroomdiagram RCE**: het stroomdiagram, met één toegevoegde keuze in de eerste vraag: embedden met eigen thumbnails. Volgens de Q&A zijn eigen thumbnails het grootste risico, dus daarvoor vraagt de keuzehulp naar toestemming.

1. Hoe ga je het werk tonen: embedden of framen, embedden met eigen thumbnails, of zelf hosten?
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

Bij elke uitkomst staan het risico voor RCE, de juridische grondslag en wat je daarna doet. Klopt het rechtenveld volgens je antwoorden niet, dan staat er ook een **signaal voor het rechtenveld**. Een voorbeeld: het veld zegt publiek domein, maar het werk is nog beschermd. De grondslag is de toelichting bij art. 2.2 Rbr: bij rijkscollecties horen auteurs- en gebruiksrechten bij de registratie. Met **Kopieer advies** neem je de route, de uitkomst en de signalen als tekst over, bijvoorbeeld voor een mail of ticket.

## Rechtenstatements vertaald

Onder het schema staat een tabel met alle waarden uit de RCE-thesaurus [Rechtenstatus en gebruiksrechten](https://data.cultureelerfgoed.nl/rights.html), met hun Nederlandse labels. Net als de thesaurus scheidt de tabel de **rechtenstatus** (de twaalf rights statements van RightsStatements.org plus Publiek domein) van het **gebruiksrecht** (CC0 en de CC-licenties, alleen als er een rechthebbende is). Waarden die Europeana niet accepteert, zijn gemarkeerd. Per waarde zie je wat die betekent, of die toestemming geeft en waar je in de keuzehulp terechtkomt. Elke code linkt naar de officiële uitleg; met **Start** begin je direct met die waarde.

De signalen voor het rechtenveld noemen de juiste waarde met de URI uit de thesaurus.

## Bestanden

| Bestand | Doel |
| --- | --- |
| `keuzehulp.html` | Bron van de keuzehulp. Hieruit wordt ook het Claude-artifact op claude.ai gepubliceerd; dat voegt zelf het HTML-skelet toe. |
| `index.html` | De keuzehulp voor GitHub Pages, gemaakt door `maak-index.py`. Pas dit bestand niet met de hand aan. |
| `beeldroutes.html` | Bron van de overlegpagina ‘Hoe komt het beeld op Collectie Nederland?’: embedden, framen, thumbnails en hosten naast elkaar, met het NDE-datasetregister en de freeze. |
| `beeldroutes/index.html` | De overlegpagina voor GitHub Pages, gemaakt door `maak-index.py`. Pas dit bestand niet met de hand aan. |
| `maak-index.py` | Zet het HTML-skelet om de bronbestanden heen en schrijft de Pages-versies. De pagina's linken naar elkaar via hun claude.ai-adres; het script maakt daar op GitHub Pages lokale links van (`ARTIFACTS`). |
| `.gitignore` | Houdt de originele brondocumenten (`*.pdf`, `*.docx`) buiten de repository. |

## Inhoud aanpassen

1. Pas het bronbestand aan, nooit de Pages-versie.
   - In `keuzehulp.html` staan de vragen, uitleg en uitkomsten in het object `N` bovenaan het script, de rechtenstatements in `RS` en de ligging van de pijlen in het schema in `EDGES`.
   - In `beeldroutes.html` staan de vier routes in `ROUTES` onderaan de pagina; de rest is gewone HTML.
2. Voer het script uit; het werkt beide Pages-versies bij:

   ```bash
   python maak-index.py
   ```

## Lokaal bekijken

Open `index.html` of `beeldroutes/index.html` in een browser. Op GitHub Pages staat de overlegpagina onder `/beeldroutes/`. De lettertypen komen van Google Fonts. Zonder internetverbinding valt de pagina terug op systeemlettertypen.

## Publiceren op GitHub Pages

1. Push de repository naar GitHub.
2. Ga naar *Settings → Pages*.
3. Kies bij *Source* de hoofdbranch en de map `/ (root)`.

## Let op

De keuzehulp geeft richting bij de keuze, maar is geen juridisch advies voor een concreet werk. Deel 1, de keuze voor eigen thumbnails en de tabel met rechtenstatements gaan verder dan het officiële stroomdiagram. Laat ze nalezen door een jurist voordat de keuzehulp breed gebruikt wordt. Twijfel je over een concreet werk, overleg dan met een jurist.
