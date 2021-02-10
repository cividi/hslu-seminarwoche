# HSLU Seminarwoche 2021

Ziel: https://sandbox.gemeindescan.ch/de/IRMV1/T7Y16K/

![](img/supermarkets-lucerne.png)

## Tools
- Datengrundlage: OpenStreetMap Export [data/lucerne-supermarkets.csv](data/lucerne-supermarkets.csv)
- Tabellenverarbeitung (z.b. Excel, Numbers, Libre Sheets, ...)
- Online GeoJSON Editor: [geojson.io](https://geojson.io) – [Mit rohem CSV](https://geojson.io/#id=github:cividi/hslu-seminarwoche/blob/main/data/lucerne-supermarkets.csv)
- Data Package Creator: [datapackage-ui.cividi.vercel.app](https://datapackage-ui.cividi.vercel.app) – [Vorbereitetes datapackage.json](data/datapackage.json)
- Gemeindescan Sandbox: [sandbox.gemeindescan.ch](https://sandbox.gemeindescan.ch)

## Ergänzte Spalten

- `title`: `=D3` oder jede andere Spalte, ggf. mittels `CONCAT` zusammengefügt
- `wheelchair_label`: `=IF(M2="yes","ja",IF(M2="no","nein","unbekannt"))`
- `description`: `=CONCAT("Rollstuhlzugänglich: ",N2)`
- `marker-color`: `=IF(M2="yes","#00AF00",IF(M2="no","#DC0000","#B6B6B6"))`

## Weiterführende Links/Hintergünde
- GIS Tools:
    - [QGIS](https://qgis.org) – freies, open-source GIS
    - [OpenStreeMap](https://openstreetmap.org) – "Wikipedia" der Karten
    - [Overpass Turbo](https://overpass-turbo.eu) – OpenStreetMap Query-Interface & Export – [Supermarktabfrage](https://overpass-turbo.eu/s/13se)
- Frictionless Data
    - [Frictionless Data](https://frictionlessdata.io)
    - [Spatial Data Package](https://github.com/cividi/spatial-data-package-spec)
    - [Gemeindescan Platform](https://github.com/cividi/spatial-data-package-platform)