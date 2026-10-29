---
title: Start Here
weight: 11
---

👋 Welcome to the **Smart Swimming Pool** project! This page helps you find
the right path based on what you want to build.

---

## Choose Your Path

### 🔰 I want the simplest possible setup

**Goal**: Automate pool circulation with minimal cost and effort.

- Use a **breadboard or protoboard** with ESP32 DevKit V1
- 2-channel relay module for pump control
- 2× DS18B20 temperature sensors
- Flash the pre-built firmware
- Control via Home Assistant

**Start here**: [Pool Controller — Build from Zero](/docs/pool-controller/build-from-zero/)

| Component | Approx. Cost |
|-----------|-------------|
| ESP32 DevKit V1 | 8–12 € |
| 2-ch relay module | 4–6 € |
| 2× DS18B20 sensors | 6–10 € |
| Breadboard + wires | 5 € |
| Resistors, power supply, misc. | see BOM |
| **Total** | **~35–55 €** (see [Bill of Materials](/docs/bom/)) |

---

### 🏊 I have a standard pool with sand filter and solar heating

**Goal**: Full automation with circulation scheduling and solar heating.

- Follow the [Build from Zero](/docs/pool-controller/build-from-zero/) guide
- Use an **IP65 enclosure** for weather protection
- Proper **mains wiring** with fuse and RCD protection
- **Home Assistant** integration for dashboard and automation
- **MQTT** for reliable communication

**Required reading**:
- [Electrical Safety](/docs/pool-controller/electrical-safety/)
- [Production Checklist](/docs/pool-controller/production-checklist/)
- [Security Checklist](/docs/pool-controller/security-checklist/)

---

### 🏭 I'm building a production-ready installation

**Goal**: Industrial-grade, 24/7 reliable pool controller with full safety.

- Use the **NORVI AE01-R** or custom PCB for reliability
- **IP66+** enclosure with cable glands
- **DIN-rail** mounted components
- Proper **overcurrent protection** and **grounding**
- **Flash encryption** enabled
- **IoT VLAN** with firewall rules
- Regular **maintenance schedule**

**Required reading**:
- [Build from Zero](/docs/pool-controller/build-from-zero/)
- [Electrical Safety](/docs/pool-controller/electrical-safety/)
- [Safety Model](/docs/pool-controller/safety-model/)
- [Production Checklist](/docs/pool-controller/production-checklist/)
- [Security Checklist](/docs/pool-controller/security-checklist/)
- [Troubleshooting](/docs/troubleshooting/)

---

## How It Fits Together

Sensors and relays attach to the ESP32 pool controller, which talks MQTT to your smart home (Home Assistant, openHAB). The pin assignment, wiring diagram and data flow are documented once, in **[Architecture](/docs/architecture/)** — so they cannot drift apart.

---

## Repository Overview

| Repository | Purpose | Language |
|-----------|---------|----------|
| [pool-controller](https://github.com/smart-swimmingpool/pool-controller) | ESP32 firmware, web UI, hardware docs | C++ (PlatformIO) |
| [website](https://github.com/smart-swimmingpool/website) | Project website (Hugo) | Markdown, Hugo |
| [openhab-config](https://github.com/smart-swimmingpool/openhab-config) | openHAB configuration (legacy) | openHAB DSL |
| [monitor](https://github.com/smart-swimmingpool/monitor) | Solar-powered temperature display | C++ |
| [grafana-dashboard](https://github.com/smart-swimmingpool/grafana-dashboard) | Grafana dashboard JSON | JSON |

---

## Questions?

Common questions (Do I need Home Assistant? What if I have no solar heating? Do I need an electrician?) are answered in the **[FAQ](/docs/faq/)**. If something does not work, see **[Troubleshooting](/docs/troubleshooting/)**.

---

## Next Steps

1. Pick a path above and follow the [Quick Start](/docs/quickstart/) or the detailed [Build Guide](/docs/getting-started/)
2. Order the parts from the [Bill of Materials](/docs/bom/)
3. Build and test on a breadboard, then run the [Commissioning Checklist](/docs/checklist/)
4. Install in an enclosure
5. Integrate with [Home Assistant](/docs/home-assistant-integration/) or [openHAB](/docs/openhab-integration/)
6. Enjoy your smart pool!

---

## Project History

🏊 Smart Swimming Pool originated from an [earlier project](https://github.com/stritti/smart-swimming-pool) that was not yet modular and had all control logic implemented as openHAB rules.

The first version ran in **Summer 2018** and revealed several weaknesses:

- Controlling pumps via 433 MHz socket switches was unreliable — no feedback meant the actual state was unknown
- Switching logic lived in openHAB rules, causing problems when WiFi was unreliable
- MQTT messages used a proprietary format

Based on these lessons, the revised 🏊 Smart Swimming Pool was built: modular, resilient, and standards-based.
