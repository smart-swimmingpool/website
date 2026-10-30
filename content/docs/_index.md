---
title: Documentation
weight: 1
---

{{< safety-notice type="230v" >}}

# 🏊 Smart Swimming Pool Documentation

Everything you need to build, connect and maintain your smart pool automation. The pages are grouped in the order you will probably need them — the same grouping you see in the sidebar.

The core is the **Pool Controller**, an ESP32-based device that:

- ✅ Automates circulation time for cleaning the water
- ✅ Heats with solar energy and switches an additional heating circuit pump
- ✅ Works independently of a specific smart home server, and keeps running without WiFi
- ✅ Integrates with Home Assistant via MQTT Discovery (openHAB via manual MQTT configuration)
- ✅ Can be operated from a smartphone or the built-in web interface

---

## 🧭 Find Your Way

| Step | What you want to do | Pages |
|------|---------------------|-------|
| **1 · Start** | Decide how to build and get a first working setup | [Start Here](/docs/start-here/) · [Quick Start](/docs/quickstart/) · [Build Guide](/docs/getting-started/) |
| **2 · Plan & Build** | Understand the system, buy parts, commission safely | [Architecture](/docs/architecture/) · [Bill of Materials](/docs/bom/) · [Commissioning Checklist](/docs/checklist/) |
| **3 · Components** | Learn about each module of the system | [Pool Controller](/docs/components/pool-controller/) · [Pool Monitor](/docs/components/pool-monitor/) · [Grafana Dashboard](/docs/components/grafana-dashboard/) · [Water Quality Monitor](/docs/components/water-quality-monitor/) |
| **4 · Smart Home Integration** | Connect the controller to your smart home | [Home Assistant](/docs/integrations/home-assistant/) · [openHAB](/docs/integrations/openhab/) · [openHAB Configuration](/docs/integrations/openhab-configuration/) |
| **5 · Operation & Support** | Something is unclear, broken or needs an update | [FAQ](/docs/faq/) · [Troubleshooting](/docs/troubleshooting/) · [Upgrade & Migration](/docs/migration/) |
| **6 · Project** | Background, contributing, media | [Diagrams with Svgbob](/docs/diagrams/) · [Publications](/docs/publications/) · [Gallery](/docs/gallery/) |

**New here?** Read [Start Here](/docs/start-here/), then follow either the [Quick Start](/docs/quickstart/) (60 minutes, breadboard) or the detailed [Build Guide](/docs/getting-started/). Run the [Commissioning Checklist](/docs/checklist/) before connecting any pump to mains voltage.

---

## 🗂️ Repositories

Module details (purpose, difficulty, cost) are in [Components](/docs/components/) and [Smart Home Integration](/docs/integrations/). The controller cost covers the electronics only; the [Bill of Materials](/docs/bom/) lists enclosure, mains wiring and tools as well.

| Repository | Purpose | Language |
|-----------|---------|----------|
| [pool-controller](https://github.com/smart-swimmingpool/pool-controller) | ESP32 firmware, web UI, hardware docs | C++ (PlatformIO) |
| [monitor](https://github.com/smart-swimmingpool/monitor) | Solar-powered temperature display | C++ |
| [grafana-dashboard](https://github.com/smart-swimmingpool/grafana-dashboard) | Grafana dashboard JSON | JSON |
| [water-quality-monitor](https://github.com/smart-swimmingpool/water-quality-monitor) | pH and chlorine monitor (in development) | — |
| [openhab-config](https://github.com/smart-swimmingpool/openhab-config) | openHAB configuration (legacy) | openHAB DSL |
| [website](https://github.com/smart-swimmingpool/website) | Project website (Hugo) | Markdown, Hugo |

---

## 💬 Need Help?

Look up the symptom in [Troubleshooting](/docs/troubleshooting/), check the [FAQ](/docs/faq/), or open an [issue](https://github.com/smart-swimmingpool/pool-controller/issues). All project repositories are on [GitHub](https://github.com/smart-swimmingpool).
