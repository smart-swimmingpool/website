---
title: Pool Controller
weight: 1
tags: ["docs", "pool-controller", "hardware", "firmware"]
---

# 🎛️ Pool Controller

The **Pool Controller** is the heart of the Smart Swimming Pool system. It's an ESP32-based device that provides central control logic for your pool automation.

## 💡 Overview

The Pool Controller handles:

- **Temperature Monitoring**: Reads data from DS18B20 temperature sensors (pool water and solar collector)
- **Pump Control**: Controls circulation and heating pumps via relay modules
- **Automation Logic**: Implements heating logic with hysteresis and temperature thresholds
- **Circulation Scheduling**: Automated timing for sand filter cleaning
- **MQTT Integration**: Publishes all data using Home Assistant MQTT Discovery format
- **Web Interface**: Built-in configuration UI for easy setup
- **Autonomous Operation**: Works independently without a smart home server

## ✨ Key Features

- ✅ **ESP32-based**: Powerful microcontroller with WiFi connectivity
- ✅ **MQTT Discovery**: Automatic integration with Home Assistant
- ✅ **Web UI**: Easy configuration via browser
- ✅ **Active-Low Relays**: Safe default state (relays OFF during boot)
- ✅ **Separate GPIO per Sensor**: Independent fault detection
- ✅ **Offline Operation**: Continues working without WiFi
- ✅ **Open Source**: MIT License, free to use and modify

## 🧭 Quick Links

### Getting Started

- **[Build from Zero](/docs/pool-controller/build-from-zero/)** - Complete build guide
- **[Electrical Safety](/docs/pool-controller/electrical-safety/)** - Important safety information
- **[Production Checklist](/docs/pool-controller/production-checklist/)** - Pre-deployment verification
- **[Security Checklist](/docs/pool-controller/security-checklist/)** - Security best practices

### Hardware

- **[Hardware Guide](/docs/pool-controller/hardware-guide/)** - Components, wiring and status LED
- **[ESP32 Wiring Schematic](/docs/pool-controller/esp32-complete-wiring-schematic/)** - Complete connection guide
- **[NORVI AE01-R](/docs/pool-controller/norvi-ae01-r/)** - Industrial DIN-rail variant
- **[Olimex ESP32-C6-EVB](/docs/pool-controller/olimex-esp32-c6-evb/)** - Variant with TFT display and rotary encoder
- **[Contactor Guide](/docs/pool-controller/contactor-guide/)** - Switching pumps safely
- **[Bill of Materials](/docs/bom/)** - Complete parts list

### Firmware

- **[Software Guide](/docs/pool-controller/software-guide/)** - Building and flashing the firmware
- **[User's Guide](/docs/pool-controller/users-guide/)** - Configuration via web interface
- **[MQTT Configuration](/docs/pool-controller/mqtt-configuration/)** - Broker setup and topics
- **[OTA Updates](/docs/pool-controller/ota-updates/)** - Firmware updates over the air

### Advanced

- **[Safety Model](/docs/pool-controller/safety-model/)** - Safety architecture
- **[Temperature-Based Circulation](/docs/pool-controller/temperature-based-circulation/)** - Adaptive filter runtime
- **[Troubleshooting Matrix](/docs/pool-controller/troubleshooting-matrix/)** - Common issues and solutions

## 🔧 Hardware Requirements

### Minimum Setup

| Component | Purpose | Approx. Cost |
|-----------|---------|-------------|
| ESP32 DevKit V1 | Main controller | 8-12 € |
| 2-Channel Relay Module | Pump control | 4-6 € |
| 2× DS18B20 Sensors | Temperature measurement | 6-10 € |
| 4.7kΩ Resistors (2x) | Pull-up resistors | < 1 € |
| Breadboard + Wires | Prototyping | 3-8 € |
| **Total** | | **~30 €** |

### Production Setup

| Component | Purpose | Approx. Cost |
|-----------|---------|-------------|
| NORVI AE01-R | Industrial ESP32 | 25-30 € |
| IP65 Enclosure | Weather protection | 10-15 € |
| DIN Rail Components | Professional mounting | 15-20 € |
| **Total** | | **~75 €** |

## 📌 Pin Configuration

Default pins of the **ESP32 DevKit** build (`esp32dev`). The NORVI AE01-R and Olimex ESP32-C6-EVB
builds use their own pin maps, see `src/Config.hpp` and the board pages linked above.

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

> ⚠️ **Important**: Each DS18B20 data line requires a **4.7kΩ pull-up resistor** to 3.3V.

## 🚀 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[Quick Start](/docs/quickstart/)** - Fastest way to get running (60 minutes)
3. **[Getting Started](/docs/getting-started/)** - Comprehensive build guide
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smart home integration

## 💬 Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[Pool Controller Repository](https://github.com/smart-swimmingpool/pool-controller)**
- Open an **[Issue](https://github.com/smart-swimmingpool/pool-controller/issues)** for bugs or feature requests
