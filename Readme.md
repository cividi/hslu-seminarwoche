# HSLU Seminarwoche 2021

- Ziel: https://sandbox.gemeindescan.ch/de/IRMV1/T7Y16K/
- Datengrundlage: OpenStreetMap Export [data/lucerne-supermarkets.csv](data/lucerne-supermarkets.csv)

![](img/supermarkets-lucerne.png)

## Tools
- Tabellenverarbeitung (z.b. Excel, Numbers, Libre Sheets, ...)
- Online GeoJSON Editor: [geojson.io](https://geojson.io) – [Mit rohem CSV](https://geojson.io/#id=github:cividi/hslu-seminarwoche/blob/main/data/lucerne-supermarkets.geojson)
- Data Package Creator: [datapackage-ui.cividi.vercel.app](https://create.cividi.ch) – [Vorbereitetes datapackage.json Template](data/datapackage.json)
- Gemeindescan Sandbox Workspace: [sandbox.gemeindescan.ch](https://sandbox.gemeindescan.ch/de/IRMV1/T7Y16K/)

## Schritte im Detail

### Daten vorbereiten
1. Dieses Repo über grünen Code > Download ZIP herunterladen
1. [data/lucerne-supermarkets.csv](data/lucerne-supermarkets.csv) in Excel öffen (via Daten > aus Text laden)
    - Encoding / File Format: Unicode / UTF-8
    - Delimeter/Trennzeichen: Komma
1. Als .xlsx speichern zum späteren weiterbearbeiten
1. [Spalten](#ergänzte-spalten) `title`, `description`, `marker-color`, ... händisch oder per Excel Formeln ergänzen
    - `title`: `=D2` oder jede andere Spalte, ggf. mittels `CONCAT` zusammengefügt (siehe `description`), D3 = Spalte D in der gleichen Zeile, hier Zeile 2
    - `marker-color`: `=IF(M2="yes","#00AF00",IF(M2="no","#DC0000","#B6B6B6"))`, M2: Spalte M in Zeile 2
    - `wheelchair_label`: `=IF(M2="yes","ja",IF(M2="no","nein","unbekannt"))`
    - `description`: `=CONCAT("Rollstuhlzugänglich: ",N2)`
1. Datei > Speichern als: Als CSV speichern

### CSV nach GeoJSON konvertieren
1. Auf geojson.io über Open > File exportiertes CSV laden
1. Über Save > As GeoJSON exportieren

### Snapshot erstellen
1. create.cividi.ch aufrufen
1. Über `Upload`, das Snapshot Template [`data/datapackage.json`](data/datapackage.json) aufrufen
1. `Add Resource` wählen
1. Bei der neuen Ressource auf `Load` klicken und das vorher von geojson.io heruntergeladene `.geojson` auswählen
1. Über `Download` den fertigen snapshot (Data Package) herunterladen

### Snapshot publizieren
1. [Sandbox Workspace öffnen](https://sandbox.gemeindescan.ch/de/IRMV1/T7Y16K/)
1. Unten links einloggen
1. Über + einen Snapshot hinzufügen
1. Titel, Thema und Gemeinde einfüllen
1. von create.cividi.ch heruntergeladenen Snapshot als JSON Datei auswählen
1. `Speichern` klicken

## Weiterführende Links/Hintergünde
- Geo Tools:
    - [Overpass Turbo](https://overpass-turbo.eu) – OpenStreetMap Query-Interface & Export – [Supermarktabfrage](https://overpass-turbo.eu/s/13se)
    - [OpenStreetMap](https://openstreetmap.org) – "Wikipedia" der Karten
    - Schweizer Landeskarte [map.geo.admin.ch](https://map.geo.admin.ch)
    - [QGIS](https://qgis.org) – freies, open-source GIS
- Frictionless Data
    - [Frictionless Data](https://frictionlessdata.io)
    - [Official Data Package Creator](https://create.frictionlessdata.io)
    - [Spatial Data Package](https://github.com/cividi/spatial-data-package-spec)
    - [Gemeindescan Platform](https://github.com/cividi/spatial-data-package-platform)