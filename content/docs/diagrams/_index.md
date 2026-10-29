---
title: Diagrams with Svgbob
weight: 90
tags: ["docs", "contributing", "diagrams"]
---

Wiring diagrams and other technical drawings are written as plain ASCII art in a
fenced code block with the language `svgbob`. At build time the site turns them
into SVG through [Kroki](https://kroki.io/) using
[Svgbob](https://github.com/ivanceras/svgbob). The diagrams follow the light and
dark theme, and the source stays readable as text on GitHub.

## Example: sensor and relay wiring

```svgbob
 .---------------------.        .--------------------.
 |        ESP32        |        |    Relay module    |
 |                     |        |   2 channels, 5V   |
 |           GPIO25 o--+--------+--o IN1             |
 |           GPIO26 o--+--------+--o IN2             |
 |               5V o--+--------+--o VCC             |
 |              GND o--+--------+--o GND             |
 |                     |        '--------------------'
 |           GPIO32 o--+----*-----------.
 |                     |    |           |
 |              3V3 o--+----+--[ 4.7k ]-'
 |                     |    |
 |              GND o--+----+----.
 '---------------------'    |    |
                          DATA  GND
                       DS18B20 Solar
```

## Writing diagrams

- Use `.` and `'` for rounded corners, `-` and `|` for lines, `*` for junctions
  and `o` for terminals. See the
  [Svgbob reference](https://ivanceras.github.io/svgbob-editor/) for all shapes.
- Use spaces, not tabs, and keep lines below 100 characters.
- Add a `title` for screen readers: ` ```svgbob {title="Relay wiring"} `.

## Hosting

The Hugo build sends each diagram once to the Kroki instance configured in
`hugo.yaml` (`params.kroki.url`, default `https://kroki.io`) and caches the
result. Visitors never contact Kroki. To keep diagram sources private, run your
own instance (`docker run -p 8000:8000 yuzutech/kroki`) and point `kroki.url`
to it. If Kroki is unreachable, the block falls back to plain text and the build
prints a warning.
