---
title: Frequently Asked Questions
weight: 28
tags: ["docs", "faq"]
---

**🏊 Smart Swimming Pool: Quick answers to common questions.**

---

## Project

### Is this project really open source?

**Yes.** The 🏊 Smart Swimming Pool is licensed under the **MIT License**. All source code, schematics, and documentation are freely available on [GitHub](https://github.com/smart-swimmingpool). You can use, modify, and distribute the project for any purpose — including commercial use.

### Does it work without internet?

**Yes.** The pool controller is fully **autonomous**. It handles circulation scheduling and heating control without any internet connection. WiFi is only needed for MQTT communication (optional) and the web interface. The controller continues working even if your router goes offline.

### Does it work without a smart home server?

**Yes.** The ESP32 runs the control logic locally. MQTT, Home Assistant, and openHAB are **optional** — they add remote control, visualization, and automation, but the controller operates perfectly without any server.

### Is there a community?

Yes. The project has a [GitHub community](https://github.com/smart-swimmingpool/smart-swimmingpool) for issues and discussions. You can also check the [Wiki](https://github.com/smart-swimmingpool/smart-swimmingpool/wiki) for community-contributed content.

---

## Features

### What can the pool controller do?

The controller automates:
- **Filter pump scheduling** — runs your sand filter system on a configurable timer
- **Solar heating control** — switches the heating circuit pump when solar energy is available
- **Temperature monitoring** — displays pool and solar collector temperatures
- **Integration** — works with Home Assistant, openHAB, and any MQTT-compatible system
- **OTA updates** — firmware can be updated over the air (v3.3+)

### Can I control the pool from my phone?

**Yes**, if you use Home Assistant or openHAB. Both provide mobile apps with dashboards and push notifications. The controller itself has a web interface accessible from any browser on your network.

### Can I use voice control (Alexa / Google Home)?

**Indirectly.** If you use Home Assistant, you can expose pool controller entities to Alexa or Google Home via the [Nabu Casa cloud](https://www.nabucasa.com/) or a local [Alexa integration](https://www.home-assistant.io/integrations/alexa/).

---

## Hardware

### What hardware do I need?

The minimum setup:
- **ESP32 DevKit V1** (~10–15€)
- **2-channel 5V relay module** (~5–8€)
- **2× DS18B20 temperature sensors** (~8–12€)
- **2× 4.7kΩ resistors + breadboard + jumper wires** (~5€)

**Total: ~35–55 €** for the controller electronics. See the [Bill of Materials](/docs/bom/) for the full list including enclosure, 230V wiring, and tools.

### Can I use this without solar heating?

**Yes.** The heating logic switches a pump based on temperature. This works with any heat source:
- Solar thermal system
- Heat pump
- Gas/oil heater with heat exchanger
- Electric heating element

Simply configure the **Min. Solar Temp** parameter to match your heat source's operating temperature.

### Can I use this with a heat pump instead of solar?

**Yes.** The controller does not care what generates the heat. It measures the temperature of the heat source (via the "solar" sensor) and switches the heating pump when the temperature is high enough. Rename the "solar sensor" to "heat pump supply" in your mind — the logic is identical.

### Which pumps can be controlled?

The relay module switches **230V / 10A max** (resistive load). For inductive loads (motors, pumps), derate to ~5A. For larger pumps, use the relay to switch a contactor that handles the pump current directly.

### Can I use a Shelly relay instead of the 2-channel module?

**Not directly.** The firmware is designed for direct GPIO-connected relays. Shelly devices are WiFi-based and would not provide the same real-time control or reliability. The project uses simple relay modules for a reason: they work even when WiFi is down.

### Is the system weatherproof?

The **ESP32 and relay module are NOT weatherproof** out of the box. For outdoor or pool house installation, use an **IP54+ enclosure** with cable glands. The DS18B20 sensors are IP68 (stainless steel probe), but the cable entry must be sealed.

### Is the pool controller CE / UL certified?

**No.** This is a hobbyist DIY project. It has not been tested or certified by any regulatory body. You build and operate it at your own risk. Always use an **RCD / FI circuit breaker** when connecting to mains power.

---

## Smart Home Integration

### Does it work with Home Assistant?

**Yes, seamlessly.** The controller uses **Home Assistant MQTT Discovery** — it automatically registers all sensors, controls, and configuration parameters as entities. No YAML configuration is needed. See the [Home Assistant Integration](/docs/home-assistant-integration/) guide.

### Does it work with openHAB?

**Yes.** The controller publishes all data via MQTT using the Homie convention (v2.x) or HA Discovery format (v3.x). openHAB can subscribe to these topics via its MQTT binding. See the [openHAB Configuration](/docs/openhab-configuration/) page.

### Does it work with Alexa, Google Home, or Apple HomeKit?

**Not directly.** The controller does not speak these protocols natively. However, if you use Home Assistant as a bridge, you can expose pool entities to Alexa, Google Home, or Apple HomeKit via the respective Home Assistant integrations.

### Can I use Grafana with this?

**Yes.** The pool controller publishes all data to MQTT. You can use [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) to ingest MQTT data into [InfluxDB](https://www.influxdata.com/) and visualize it with [Grafana](/docs/grafana-dashboard/).

---

## Configuration & Operation

### How do I set the target pool temperature?

- **Via web interface:** Open the controller's web UI → **Configuration → Heating** → set **Max. Pool Temp**
- **Via Home Assistant:** Change the `number.pool_controller_pool_max_temp` entity
- **Via MQTT:** Publish to the corresponding MQTT topic

The default range is 0–40°C.

### What is hysteresis and how do I set it?

Hysteresis prevents the pump from rapidly switching on and off when the temperature is near the setpoint. A hysteresis of **2 K** means: the pump turns on when the temperature rises 2°C above the threshold and turns off when it drops 2°C below.

**Example:** With Max. Pool Temp = 28°C and hysteresis = 2 K, the heating pump turns off at 28°C and turns back on at 26°C.

### How do I set up the filter pump schedule?

Two modes:
- **Timer mode:** Set the **Timer Start** and **Timer End** times. The filter runs continuously between these times.
- **Temperature-based mode (v3.3+):** The controller adjusts runtime based on pool temperature (uses **Circ. Temp Threshold**, **Circ. Temp Factor**, and **Circ. Max Runtime** parameters).

### Can I use the pool without the controller?

**Yes.** The controller operates in parallel with your existing pool infrastructure. If you disconnect the ESP32, the pumps simply stop switching — but your pool's manual controls (if any) remain unaffected. The relay module acts as a switch in series with your existing controls.

---

## Troubleshooting Quick Links

| Problem | Where to Look |
|---------|---------------|
| Sensor shows -127°C | [DS18B20 Troubleshooting](/docs/troubleshooting/#ds18b20-sensor-not-detected--reads--127c-or-85c) |
| Pump does not start | [Heating & Circulation Issues](/docs/troubleshooting/#heating--circulation-issues) |
| WiFi not connecting | [WiFi & Network Issues](/docs/troubleshooting/#wifi--network-issues) |
| MQTT not working | [MQTT Issues](/docs/troubleshooting/#mqtt-issues) |
| Controller won't boot | [ESP32 & Firmware Issues](/docs/troubleshooting/#esp32--firmware-issues) |
