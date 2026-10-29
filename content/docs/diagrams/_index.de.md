---
title: Diagramme mit Svgbob
weight: 90
tags: ["docs", "contributing", "diagrams"]
---

Schaltpläne und andere technische Zeichnungen werden als ASCII-Art in einem
Codeblock mit der Sprache `svgbob` geschrieben. Beim Build erzeugt die Website
daraus über [Kroki](https://kroki.io/) mit
[Svgbob](https://github.com/ivanceras/svgbob) ein SVG. Die Diagramme folgen dem
hellen und dunklen Theme, und der Quelltext bleibt auf GitHub als Text lesbar.

## Beispiel: Verdrahtung von Sensor und Relais

```svgbob
 .---------------------.        .--------------------.
 |        ESP32        |        |     Relaismodul    |
 |                     |        |    2 Kanal, 5V     |
 |           GPIO25 o--+--------+--o IN1             |
 |           GPIO26 o--+--------+--o IN2             |
 |               5V o--+--------+--o VCC             |
 |              GND o--+--------+--o GND             |
 |                     |        '--------------------'
 |                     |
 |                     |             .--------------------.
 |                     |             |   DS18B20 Solar    |
 |           GPIO32 o--+----*--------+--o DATA            |
 |                     |    |        |                    |
 |                     | .--+--.     |                    |
 |                     | |4.7k |     |                    |
 |                     | '--+--'     |                    |
 |                     |    |        |                    |
 |              3V3 o--+----*--------+--o VDD             |
 |                     |             |                    |
 |              GND o--+-------------+--o GND             |
 '---------------------'             '--------------------'
```

## Diagramme schreiben

- `.` und `'` für runde Ecken, `-` und `|` für Linien, `*` für Verbindungspunkte
  und `o` für Anschlüsse. Alle Formen stehen in der
  [Svgbob-Referenz](https://ivanceras.github.io/svgbob-editor/).
- Nur Leerzeichen, keine Tabs, und Zeilen unter 100 Zeichen.
- Mit `title` für Screenreader: ` ```svgbob {title="Relais-Verdrahtung"} `.

## Hosting

Der Hugo-Build sendet jedes Diagramm einmal an die in `hugo.yaml`
(`params.kroki.url`, Standard `https://kroki.io`) eingestellte Kroki-Instanz und
cacht das Ergebnis. Besucher kontaktieren Kroki nie. Wer die Diagrammquellen
nicht nach außen geben will, betreibt eine eigene Instanz
(`docker run -p 8000:8000 yuzutech/kroki`) und trägt sie bei `kroki.url` ein.
Ist Kroki nicht erreichbar, wird der Block als Text angezeigt und der Build gibt
eine Warnung aus.
