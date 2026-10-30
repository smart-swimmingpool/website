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

**Start here**: [Pool Controller — Build from Zero](/docs/components/pool-controller/build-from-zero/)

**Cost:** about **35–55 €** for the controller electronics — see the [Bill of Materials](/docs/bom/) for parts, enclosure and mains wiring.

---

### 🏊 I have a standard pool with sand filter and solar heating

**Goal**: Full automation with circulation scheduling and solar heating.

- Follow the [Build from Zero](/docs/components/pool-controller/build-from-zero/) guide
- Use an **IP65 enclosure** for weather protection
- Proper **mains wiring** with fuse and RCD protection
- **Home Assistant** integration for dashboard and automation
- **MQTT** for reliable communication

**Required reading**:
- [Electrical Safety](/docs/components/pool-controller/electrical-safety/)
- [Production Checklist](/docs/components/pool-controller/production-checklist/)
- [Security Checklist](/docs/components/pool-controller/security-checklist/)

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
- [Build from Zero](/docs/components/pool-controller/build-from-zero/)
- [Electrical Safety](/docs/components/pool-controller/electrical-safety/)
- [Safety Model](/docs/components/pool-controller/safety-model/)
- [Production Checklist](/docs/components/pool-controller/production-checklist/)
- [Security Checklist](/docs/components/pool-controller/security-checklist/)
- [Troubleshooting](/docs/troubleshooting/)

---

## How It Fits Together

Sensors and relays attach to the ESP32 pool controller, which talks MQTT to your smart home (Home Assistant, openHAB). The pin assignment, wiring diagram and data flow are documented once, in **[Architecture](/docs/architecture/)** — so they cannot drift apart.

---

## Questions?

Common questions (Do I need Home Assistant? What if I have no solar heating? Do I need an electrician?) are answered in the **[FAQ](/docs/faq/)**. If something does not work, see **[Troubleshooting](/docs/troubleshooting/)**.

---

## Next Steps

Pick a path, follow the [Quick Start](/docs/quickstart/) or the [Build Guide](/docs/getting-started/), order the parts from the [Bill of Materials](/docs/bom/), test on a breadboard, run the [Commissioning Checklist](/docs/checklist/), install everything in an enclosure and connect [Home Assistant](/docs/integrations/home-assistant/) or [openHAB](/docs/integrations/openhab/). The full overview of all repositories and pages is in the [documentation](/docs/).

Background on how the project started: [Project History](/docs/publications/#project-history).
