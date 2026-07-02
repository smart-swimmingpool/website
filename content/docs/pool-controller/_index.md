---
title: Pool Controller
weight: 1
tags: ["docs", "pool-controller", "hardware", "firmware"]
---

# \ud83c\udf9b Pool Controller

The **Pool Controller** is the heart of the Smart Swimming Pool system. It's an ESP32-based device that provides central control logic for your pool automation.

## \ud83d\udca1 Overview

The Pool Controller handles:

- **Temperature Monitoring**: Reads data from DS18B20 temperature sensors (pool water and solar collector)
- **Pump Control**: Controls circulation and heating pumps via relay modules
- **Automation Logic**: Implements heating logic with hysteresis and temperature thresholds
- **Circulation Scheduling**: Automated timing for sand filter cleaning
- **MQTT Integration**: Publishes all data using Home Assistant MQTT Discovery format
- **Web Interface**: Built-in configuration UI for easy setup
- **Autonomous Operation**: Works independently without a smart home server

## \ud83d\udcc Key Features

- \u2705 **ESP32-based**: Powerful microcontroller with WiFi connectivity
- \u2705 **MQTT Discovery**: Automatic integration with Home Assistant
- \u2705 **Web UI**: Easy configuration via browser
- \u2705 **Active-Low Relays**: Safe default state (relays OFF during boot)
- \u2705 **Separate GPIO per Sensor**: Independent fault detection
- \u2705 **Offline Operation**: Continues working without WiFi
- \u2705 **Open Source**: MIT License, free to use and modify

## \ud83d\ud87 Quick Links

### Getting Started
- **[Build from Zero](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.md)** - Complete build guide
- **[Electrical Safety](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/electrical-safety.md)** - Important safety information
- **[Production Checklist](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/production-checklist.md)** - Pre-deployment verification
- **[Security Checklist](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/security-checklist.md)** - Security best practices

### Hardware
- **[Hardware Overview](https://github.com/smart-swimmingpool/pool-controller#hardware)** - Component descriptions
- **[Wiring Diagram](https://github.com/smart-swimmingpool/pool-controller#wiring)** - Connection guide
- **[Bill of Materials](/docs/bom/)** - Complete parts list

### Firmware
- **[Firmware Installation](https://github.com/smart-swimmingpool/pool-controller#firmware)** - Flashing guide
- **[Configuration](https://github.com/smart-swimmingpool/pool-controller#configuration)** - Web interface setup
- **[MQTT Configuration](https://github.com/smart-swimmingpool/pool-controller#mqtt-configuration)** - Broker setup

### Advanced
- **[Safety Model](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/safety-model.md)** - Safety architecture
- **[Troubleshooting](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/troubleshooting.md)** - Common issues and solutions
- **[API Reference](https://github.com/smart-swimmingpool/pool-controller#api)** - MQTT topics and commands

## \ud83c\udf9b Hardware Requirements

### Minimum Setup
| Component | Purpose | Approx. Cost |
|-----------|---------|-------------|
| ESP32 DevKit V1 | Main controller | 8-12 \u20ac |
| 2-Channel Relay Module | Pump control | 4-6 \u20ac |
| 2\u00d7 DS18B20 Sensors | Temperature measurement | 6-10 \u20ac |
| 4.7k\u03a9 Resistors (2x) | Pull-up resistors | < 1 \u20ac |
| Breadboard + Wires | Prototyping | 3-8 \u20ac |
| **Total** | | **~30 \u20ac** |

### Production Setup
| Component | Purpose | Approx. Cost |
|-----------|---------|-------------|
| NORVI AE01-R | Industrial ESP32 | 25-30 \u20ac |
| IP65 Enclosure | Weather protection | 10-15 \u20ac |
| DIN Rail Components | Professional mounting | 15-20 \u20ac |
| **Total** | | **~75 \u20ac** |

## \ud83d\udda5 Pin Configuration

| Function | ESP32 Pin | Notes |
|----------|-----------|-------|
| Solar Sensor (DS18B20) | GPIO32 | OneWire data |
| Pool Sensor (DS18B20) | GPIO33 | OneWire data |
| Heating Pump Relay | GPIO26 | Active-low |
| Filter Pump Relay | GPIO25 | Active-low |
| Relay Module VCC | 5V (VIN) | **NOT 3.3V!** |
| Relay Module GND | GND | Common ground |
| Sensor VDD | 3.3V | Power for sensors |
| Sensor GND | GND | Ground for sensors |

> \u26a0\ufe0f **Important**: Each DS18B20 data line requires a **4.7k\u03a9 pull-up resistor** to 3.3V.

## \ud83d\udc82 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[Quick Start](/docs/quickstart/)** - Fastest way to get running (60 minutes)
3. **[Getting Started](/docs/getting-started/)** - Comprehensive build guide
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smart home integration

## \ud83d\udcdd Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[Pool Controller Repository](https://github.com/smart-swimmingpool/pool-controller)**
- Open an **[Issue](https://github.com/smart-swimmingpool/pool-controller/issues)** for bugs or feature requests
