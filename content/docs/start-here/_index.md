---
title: Start Here
weight: 1
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

**Start here**: [Pool Controller — Build from Zero](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.md)

| Component | Approx. Cost |
|-----------|-------------|
| ESP32 DevKit V1 | 8–12 € |
| 2-ch relay module | 4–6 € |
| 2× DS18B20 sensors | 6–10 € |
| Breadboard + wires | 5 € |
| **Total** | **~30 €** |

---

### 🏊 I have a standard pool with sand filter and solar heating

**Goal**: Full automation with circulation scheduling and solar heating.

- Follow the [Build from Zero](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.md) guide
- Use an **IP65 enclosure** for weather protection
- Proper **mains wiring** with fuse and RCD protection
- **Home Assistant** integration for dashboard and automation
- **MQTT** for reliable communication

**Required reading**:
- [Electrical Safety](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/electrical-safety.md)
- [Production Checklist](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/production-checklist.md)
- [Security Checklist](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/security-checklist.md)

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
- [Build from Zero](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.md)
- [Electrical Safety](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/electrical-safety.md)
- [Safety Model](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/safety-model.md)
- [Production Checklist](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/production-checklist.md)
- [Security Checklist](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/security-checklist.md)
- [Troubleshooting](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/troubleshooting.md)

---

## Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│                     Pool Environment                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐ │
│  │ Pool     │  │ Solar    │  │ Sand     │  │ Heat         │ │
│  │ Pump     │  │ Pump     │  │ Filter   │  │ Exchanger    │ │
│  └────┬─────┘  └────┬─────┘  └──────────┘  └──────┬───────┘ │
│       │              │                              │         │
└───────┼──────────────┼──────────────────────────────┼─────────┘
        │              │                              │
        ▼              ▼                              ▼
┌──────────────────────────────────────────────────────────────┐
│                   Pool Controller (ESP32)                     │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────┐   │
│  │ DS18B20    │  │ DS18B20    │  │ 2-Ch Relay Module    │   │
│  │ Pool Temp  │  │ Solar Temp │  │ GPIO18 → Pool Pump   │   │
│  │ GPIO16     │  │ GPIO15     │  │ GPIO19 → Solar Pump  │   │
│  └────────────┘  └────────────┘  └──────────────────────┘   │
│                          │                                    │
│                    ┌─────┴──────┐                              │
│                    │  WiFi STA  │                              │
│                    │  MQTT Pub  │                              │
│                    │  Web UI    │                              │
│                    └─────┬──────┘                              │
└──────────────────────────┼────────────────────────────────────┘
                           │ MQTT
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                    Smart Home Server                          │
│  ┌────────────────────┐  ┌────────────────────────────────┐  │
│  │ Home Assistant     │  │ MQTT Broker (Mosquitto)        │  │
│  │ • MQTT Discovery   │  │ • pool-controller/# topics     │  │
│  │ • Lovelace UI      │  │ • Auth enabled                 │  │
│  │ • Automations      │  │ • Local only                   │  │
│  └────────────────────┘  └────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

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

## FAQ

### Do I need Home Assistant?

No. The controller has a built-in web interface for direct management.
Home Assistant provides a nicer dashboard and automation capabilities,
but is not required.

### Can I use openHAB instead?

Yes. openHAB is supported via MQTT. See the
[openHAB configuration](https://github.com/smart-swimmingpool/openhab-config)
repository. Note that Home Assistant Discovery is now the primary integration
path — openHAB requires manual MQTT configuration.

### What if I don't have solar heating?

No problem. The solar pump functions can be left unused. The controller
works perfectly with just pool circulation.

### Can I use this with any pool pump?

Yes, as long as the pump can be switched on/off via a relay (mains voltage).
Most sand filter pumps support this. Check your pump's wiring diagram.

### What is the maximum cable length for DS18B20 sensors?

Up to 10 meters with 4.7 kΩ pull-up. For longer runs, use a lower value
pull-up (e.g., 2.2 kΩ) or a dedicated OneWire driver.

### Do I need to be an electrician?

Basic wiring (relays to pumps) requires working with 230V AC. If you're
not comfortable with mains voltage, hire a qualified electrician.

### Can I use the controller without WiFi?

The controller needs WiFi for MQTT communication, but it continues running
with its last known configuration if WiFi is lost. A future version will
support standalone operation with a display and buttons.

---

## Next Steps

1. Read the [Build from Zero](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.md) guide
2. Order the parts from the bill of materials
3. Build and test on a breadboard
4. Install in an enclosure
5. Integrate with Home Assistant
6. Enjoy your smart pool!
