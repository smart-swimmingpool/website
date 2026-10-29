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
| **3 · Components** | Learn about each module of the system | [Pool Controller](/docs/pool-controller/) · [Pool Monitor](/docs/pool-monitor/) · [Grafana Dashboard](/docs/grafana-dashboard/) · [Water Quality Monitor](/docs/water-quality-monitor/) |
| **4 · Smart Home Integration** | Connect the controller to your smart home | [Home Assistant](/docs/home-assistant-integration/) · [openHAB](/docs/openhab-integration/) · [openHAB Configuration](/docs/openhab-configuration/) |
| **5 · Operation & Support** | Something is unclear, broken or needs an update | [FAQ](/docs/faq/) · [Troubleshooting](/docs/troubleshooting/) · [Upgrade & Migration](/docs/migration/) |
| **6 · Project** | Background, contributing, media | [Diagrams with Svgbob](/docs/diagrams/) · [Publications](/docs/publications/) · [Gallery](/docs/gallery/) |

**New here?** Read [Start Here](/docs/start-here/), then follow either the [Quick Start](/docs/quickstart/) (60 minutes, breadboard) or the detailed [Build Guide](/docs/getting-started/). Run the [Commissioning Checklist](/docs/checklist/) before connecting any pump to mains voltage.

---

## 📦 Modules at a Glance

| Module | Purpose | Difficulty | Cost |
|--------|---------|------------|------|
| **[Pool Controller](/docs/pool-controller/)** | Main control logic (required) | ⭐⭐ | ~35–55 € |
| **[Home Assistant Integration](/docs/home-assistant-integration/)** | Smart home dashboard | ⭐ | Free |
| **[openHAB Integration](/docs/openhab-integration/)** | Alternative smart home | ⭐⭐ | Free |
| **[Pool Monitor](/docs/pool-monitor/)** | Wireless temperature display | ⭐⭐ | ~20–40 € |
| **[Grafana Dashboard](/docs/grafana-dashboard/)** | Data visualization | ⭐ | Free |
| **[Water Quality Monitor](/docs/water-quality-monitor/)** | pH, chlorine and temperature (in development) | ⭐⭐⭐ | tbd |

Costs for the controller are for the electronics only; the [Bill of Materials](/docs/bom/) lists enclosure, mains wiring and tools as well.

---

## 💬 Need Help?

Look up the symptom in [Troubleshooting](/docs/troubleshooting/), check the [FAQ](/docs/faq/), or open an [issue](https://github.com/smart-swimmingpool/pool-controller/issues). All project repositories are on [GitHub](https://github.com/smart-swimmingpool).
