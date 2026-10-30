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

## Writing diagrams

- Use `.` and `'` for rounded corners, `-` and `|` for lines, `*` for junctions
  and `o` for terminals. See the
  [Svgbob reference](https://ivanceras.github.io/svgbob-editor/) for all shapes.
- Use spaces, not tabs, and keep lines below 100 characters.
- Add a `title` for screen readers: ` ```svgbob {title="Relay wiring"} `.

## Wiring diagram rules

- Draw a box per device with one `o` terminal per pin, and label every pin the
  way the device is labelled (`GPIO25`, `VDD`, `SDA`).
- Draw components such as resistors as a small box on the wire, entered at the
  centre column: `.--+--.` / `|4.7k |` / `'--+--'`.
- Give every device its own DATA, VDD and GND wires. A `*` junction may only join
  wires of the same net. The pull-up of a DS18B20 is the only link between DATA
  and 3V3.
- Keep the 230V side out of low-voltage drawings and link to the
  [electrical safety guide](/docs/pool-controller/electrical-safety/) instead.
- Avoid `(`, `)`, `/`, `\`, `<`, `>` and a single `-` inside labels, because
  Svgbob turns them into arcs, diagonals or arrows. Write `2 channels`, not
  `2-channel`.
- Draw one diagram per subsystem instead of one large drawing.
- Pad all rows of a box to the same length so the right border lines up.

## Hosting

The Hugo build sends each diagram once to the Kroki instance configured in
`hugo.yaml` (`params.kroki.url`, default `https://kroki.io`) and caches the
result. Visitors never contact Kroki. To keep diagram sources private, run your
own instance (`docker run -p 8000:8000 yuzutech/kroki`) and point `kroki.url`
to it. If Kroki is unreachable, the block falls back to plain text and the build
prints a warning.
