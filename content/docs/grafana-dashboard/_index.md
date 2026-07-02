---
title: Grafana Dashboard
weight: 1
tags: ["docs", "grafana", "visualization", "monitoring"]
---

# \ud83d\udcc Grafana Dashboard

The **Grafana Dashboard** provides beautiful visualization of your pool data, allowing you to track temperature trends, system status, and historical data over time.

## \ud83d\udca1 Overview

The Grafana Dashboard offers:

- **Temperature Visualization**: Track pool and solar temperatures over time
- **Historical Data**: View trends and patterns in your pool data
- **System Monitoring**: Monitor pump status, uptime, and other metrics
- **Customizable**: Adapt the dashboard to your specific needs
- **Real-Time Updates**: Live data from your pool controller via MQTT
- **Alerting**: Set up notifications for specific conditions

## \ud83d\udcc Key Features

- \u2705 **Temperature Charts**: Beautiful graphs showing temperature trends
- \u2705 **Pump Status**: Visual indication of pump operation times
- \u2705 **System Health**: Monitor controller uptime and connectivity
- \u2705 **Custom Panels**: Add or modify panels to suit your needs
- \u2705 **Time Range Selection**: View data from hours to months
- \u2705 **Export/Import**: Share your dashboard configuration with others
- \u2705 **Open Source**: MIT License, free to use and modify

## \ud83d\ud87 Quick Links

### Getting Started
- **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)** - Main repository with dashboard JSON
- **[Installation Guide](https://github.com/smart-swimmingpool/grafana-dashboard#installation)** - Step-by-step setup instructions
- **[Configuration](https://github.com/smart-swimmingpool/grafana-dashboard#configuration)** - Dashboard setup and customization

### Prerequisites
- **[Grafana Installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)** - Install Grafana on your system
- **[InfluxDB Setup](https://www.influxdata.com/time-series-platform/influxdb/)** - Time series database for storing pool data
- **[MQTT to InfluxDB](https://github.com/smart-swimmingpool/grafana-dashboard#mqtt-to-influxdb)** - Bridge MQTT data to InfluxDB

### Dashboard Setup
- **[Import Dashboard](https://github.com/smart-swimmingpool/grafana-dashboard#import-dashboard)** - Import the pre-configured dashboard
- **[Data Sources](https://github.com/smart-swimmingpool/grafana-dashboard#data-sources)** - Configure data sources in Grafana
- **[Customization](https://github.com/smart-swimmingpool/grafana-dashboard#customization)** - Adapt the dashboard to your needs

## \ud83c\udf9b Screenshot

![Grafana Dashboard](/img/grafana-dashboard.png)

*The Smart Swimming Pool Grafana Dashboard showing temperature trends and system status*

## \ud83d\udda5 Dashboard Panels

The default dashboard includes:

| Panel | Description | Data Source |
|-------|-------------|-------------|
| **Pool Temperature** | Current and historical pool water temperature | MQTT/InfluxDB |
| **Solar Temperature** | Current and historical solar collector temperature | MQTT/InfluxDB |
| **Temperature Difference** | Difference between solar and pool temperature | Calculated |
| **Pump Status** | Current state and operation times of both pumps | MQTT/InfluxDB |
| **System Uptime** | Controller uptime and connectivity status | MQTT/InfluxDB |
| **Heating Efficiency** | Heating performance metrics | Calculated |
| **Daily Statistics** | Daily temperature ranges and pump operation | MQTT/InfluxDB |

## \ud83d\udc82 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[Visit Repository](https://github.com/smart-swimmingpool/grafana-dashboard)** - Access dashboard JSON and documentation
3. **[Pool Controller Setup](/docs/pool-controller/)** - Ensure your controller is running
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Alternative visualization option

## \ud83d\udcdd Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)**
- Open an **[Issue](https://github.com/smart-swimmingpool/grafana-dashboard/issues)** for bugs or feature requests
- Consult the **[Grafana Documentation](https://grafana.com/docs/)** for Grafana-specific questions
