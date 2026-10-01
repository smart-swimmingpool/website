---
title: Water Quality Monitor
weight: 1
tags: ["docs", "water-quality", "pH", "chlorine", "esp8266"]
---

# 🧪 Water Quality Monitor

The **Water Quality Monitor** is a planned module to measure the chemical quality of your
pool water — **pH**, **chlorine** and **water temperature** — and publish the values via MQTT
to your smart home system.

> [!WARNING]
> **Status: in development.** The module is in the planning and early prototyping phase.
> There is no released firmware yet. Contributions are very welcome!

## 💡 Planned Measurements

| Parameter | Range | Why it matters |
|-----------|-------|----------------|
| **pH** | 0–14 | Affects chlorine effectiveness and swimmer comfort |
| **Chlorine** | 0–10 ppm | Primary sanitizer against bacteria and algae |
| **Temperature** | 0–60 °C | Influences chemical reactions and comfort |

## 🧩 Fit in the Smart Swimming Pool System

- Publishes measurements via **MQTT**, like the [Pool Controller](/docs/pool-controller/)
- Values can be stored and visualized, e.g. with the [Grafana Dashboard](/docs/grafana-dashboard/)
- Usable from [Home Assistant](/docs/home-assistant-integration/) and [openHAB](/docs/openhab-integration/)

## 🧭 Documentation

- **[Hardware Guide](/docs/water-quality-monitor/hardware-guide/)** - Sensor options, circuit ideas and parts list
- **[Repository](https://github.com/smart-swimmingpool/water-quality-monitor)** - Source code and current status

## 🤝 How You Can Help

- Test pH and chlorine sensors with ESP8266/ESP32 boards
- Design the circuit, a PCB or a waterproof enclosure
- Implement sensor reading, calibration and MQTT publishing
- Share field test results and compare readings with test kits

Open an **[Issue](https://github.com/smart-swimmingpool/water-quality-monitor/issues)** to discuss
ideas or to coordinate your contribution.
