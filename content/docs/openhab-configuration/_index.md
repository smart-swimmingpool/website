---
title: openHAB Configuration
weight: 1
tags: ["docs", "openhab", "configuration", "smarthome"]
---

# \ud83c\udfed openHAB Configuration

The **openHAB Configuration** provides complete configuration files for integrating your Smart Swimming Pool with openHAB smart home server.

## \ud83d\udca1 Overview

This module includes:

- **Sitemap**: User interface for controlling your pool from openHAB apps
- **Items**: All the data points and controls for your pool system
- **Rules**: Automation logic for pool control
- **Transformations**: Data formatting and unit conversions
- **Persistence**: Historical data storage configuration

## \ud83d\udcc Key Features

- \u2705 **Complete Sitemap**: Mobile-friendly interface for pool control
- \u2705 **MQTT Binding**: Integration with your pool controller via MQTT
- \u2705 **Automation Rules**: Advanced automation logic
- \u2705 **Historical Data**: Persistence configuration for charts and trends
- \u2705 **Multi-Language**: Support for different languages
- \u2705 **Open Source**: MIT License, free to use and modify

## \ud83d\ud87 Quick Links

### Getting Started
- **[openHAB Configuration Repository](https://github.com/smart-swimmingpool/openhab-config)** - Main repository with all configuration files
- **[openHAB Integration Guide](/docs/openhab-integration/)** - Step-by-step integration guide
- **[Installation](https://github.com/smart-swimmingpool/openhab-config#installation)** - Setup instructions

### Configuration Files
- **[Sitemap](https://github.com/smart-swimmingpool/openhab-config/blob/main/sitemaps/pool.sitemap)** - User interface definition
- **[Items](https://github.com/smart-swimmingpool/openhab-config/blob/main/items/pool-controller.items)** - Data points and controls
- **[Rules](https://github.com/smart-swimmingpool/openhab-config/blob/main/rules/pool-automation.rules)** - Automation logic
- **[Transformations](https://github.com/smart-swimmingpool/openhab-config/tree/main/transform)** - Data formatting
- **[Persistence](https://github.com/smart-swimmingpool/openhab-config/blob/main/persistence/rrd4j.persist)** - Historical data storage

## \ud83c\udf9b Sitemap Preview

The sitemap provides a mobile-friendly interface with:

- **Dashboard**: Overview of all pool status and controls
- **Temperatures**: Current pool and solar temperatures
- **Pump Control**: Manual and automatic pump control
- **Heating**: Heating circuit control and settings
- **Schedules**: Circulation and heating schedules
- **History**: Historical data and charts
- **Settings**: Configuration and system settings

## \ud83d\udda5 Items Overview

The items file includes:

| Category | Items | Description |
|----------|-------|-------------|
| **Temperatures** | PoolTemp, SolarTemp | Current temperatures from sensors |
| **Pumps** | FilterPump, HeatingPump | Pump status and control |
| **Heating** | HeatingEnabled, MaxPoolTemp | Heating control parameters |
| **Schedules** | CirculationSchedule | Circulation timing settings |
| **System** | SystemStatus, Uptime | System health and status |

## \ud83d\udc82 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[openHAB Integration Guide](/docs/openhab-integration/)** - Step-by-step integration instructions
3. **[Visit Repository](https://github.com/smart-swimmingpool/openhab-config)** - Access all configuration files
4. **[Pool Controller Setup](/docs/pool-controller/)** - Ensure your controller is running

## \ud83d\udcdd Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[openHAB Configuration Repository](https://github.com/smart-swimmingpool/openhab-config)**
- Open an **[Issue](https://github.com/smart-swimmingpool/openhab-config/issues)** for bugs or feature requests
- Consult the **[openHAB Documentation](https://www.openhab.org/docs/)** for openHAB-specific questions
