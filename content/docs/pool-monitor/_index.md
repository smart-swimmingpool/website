---
title: Pool Monitor
weight: 1
tags: ["docs", "pool-monitor", "display", "solar"]
---

# \ud83d\udda5 Pool Monitor

The **Pool Monitor** is a solar-powered wireless display that shows the current pool temperature. It's designed to be energy-efficient and completely independent of your main pool controller.

## \ud83d\udca1 Overview

The Pool Monitor provides:

- **Wireless Temperature Display**: Shows current pool water temperature
- **Solar-Powered**: Energy-efficient design for continuous operation
- **ESP8266-Based**: Low-power microcontroller with WiFi connectivity
- **E-Ink Display**: Low power consumption, visible in sunlight
- **MQTT Integration**: Subscribes to pool controller data via MQTT
- **Standalone Operation**: Works independently of the main controller

## \ud83d\udcc Key Features

- \u2705 **Solar-Powered**: Can run continuously on solar power
- \u2705 **Wireless**: No cables needed, communicates via WiFi
- \u2705 **E-Ink Display**: Clear visibility in direct sunlight
- \u2705 **Low Power**: Designed for minimal energy consumption
- \u2705 **MQTT Subscriber**: Receives data from your pool controller
- \u2705 **Standalone**: Independent of main controller operation
- \u2705 **Open Source**: MIT License, free to use and modify

## \ud83d\ud87 Quick Links

### Getting Started
- **[Pool Monitor Repository](https://github.com/smart-swimmingpool/monitor)** - Main repository with all documentation
- **[Build Guide](https://github.com/smart-swimmingpool/monitor#build-guide)** - Step-by-step construction instructions
- **[Hardware Overview](https://github.com/smart-swimmingpool/monitor#hardware)** - Component descriptions

### Hardware
- **[Wiring Diagram](https://github.com/smart-swimmingpool/monitor#wiring)** - Connection guide
- **[Bill of Materials](https://github.com/smart-swimmingpool/monitor#bill-of-materials)** - Complete parts list

### Firmware
- **[Firmware Installation](https://github.com/smart-swimmingpool/monitor#firmware)** - Flashing guide
- **[Configuration](https://github.com/smart-swimmingpool/monitor#configuration)** - Setup instructions
- **[MQTT Configuration](https://github.com/smart-swimmingpool/monitor#mqtt-configuration)** - Broker setup

## \ud83c\udf9b Hardware Requirements

| Component | Purpose | Approx. Cost |
|-----------|---------|-------------|
| ESP8266 (Wemos D1 Mini) | Main controller | 5-8 \u20ac |
| E-Ink Display (2.13") | Temperature display | 15-20 \u20ac |
| Solar Panel (6V) | Power source | 10-15 \u20ac |
| LiPo Battery (18650) | Energy storage | 5-10 \u20ac |
| Charging Circuit | Battery management | 3-5 \u20ac |
| Enclosure | Weather protection | 5-10 \u20ac |
| **Total** | | **~45-70 \u20ac** |

## \ud83d\udda5 Pin Configuration

| Function | ESP8266 Pin | Notes |
|----------|-------------|-------|
| Display SDA | D2 (GPIO4) | I2C data |
| Display SCL | D1 (GPIO5) | I2C clock |
| Display BUSY | D5 (GPIO14) | Busy signal |
| Display DC | D6 (GPIO12) | Data/Command |
| Display RST | D7 (GPIO13) | Reset |
| Display CS | D8 (GPIO15) | Chip select |
| Solar Panel | 5V | Power input |
| Battery | 3.3V | Power output |

## \ud83d\udc82 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[Visit Repository](https://github.com/smart-swimmingpool/monitor)** - Access all documentation and source code
3. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smart home integration
4. **[Grafana Dashboard](/docs/grafana-dashboard/)** - Data visualization

## \ud83d\udcdd Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[Pool Monitor Repository](https://github.com/smart-swimmingpool/monitor)**
- Open an **[Issue](https://github.com/smart-swimmingpool/monitor/issues)** for bugs or feature requests
