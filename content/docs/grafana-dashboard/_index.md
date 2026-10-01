---
title: Grafana Dashboard
weight: 1
tags: ["docs", "grafana", "visualization", "monitoring"]
---

# 📊 Grafana Dashboard

The **Grafana Dashboard** visualizes your Smart Swimming Pool over time: pool and solar
temperatures, pump switching times, the operation mode and controller diagnostics. It is
made for the [Pool Controller](/docs/pool-controller/) **v5.x** and reads the data that
**Home Assistant** stores in **InfluxDB**.

![Grafana Dashboard with example data](https://raw.githubusercontent.com/smart-swimmingpool/grafana-dashboard/master/docs/dashboard-screenshot.png)

## 💡 How It Works

```text
Pool Controller ──MQTT discovery──▶ Home Assistant ──InfluxDB integration──▶ InfluxDB ──▶ Grafana
```

1. The Pool Controller publishes its entities via Home Assistant MQTT discovery
    (see [Home Assistant Integration](/docs/home-assistant-integration/)).
2. The [InfluxDB integration](https://www.home-assistant.io/integrations/influxdb/) of
    Home Assistant stores the entity states in InfluxDB.
3. Grafana queries this database and renders the dashboard.

## ✨ Dashboard Panels

| Section | Panels |
|---------|--------|
| **Temperatures** | Pool and solar gauges, history of pool, solar and controller temperature |
| **Pumps & Operation** | Pump state timeline, current pump state, effective runtime, circulation extension, operation mode (auto, manual, boost, timer) |
| **Diagnostics** | WiFi signal, uptime, free heap, controller temperature with history |

## 🔧 Installation

### Prerequisites

- [Pool Controller](/docs/pool-controller/) v5.x connected to Home Assistant
- Home Assistant [InfluxDB integration](https://www.home-assistant.io/integrations/influxdb/)
  with default measurement settings
- InfluxDB 1.x (or 2.x with InfluxQL) and Grafana 10 or newer

### Store the pool data in InfluxDB

Example for Home Assistant's `configuration.yaml`:

```yaml
influxdb:
  host: influxdb.local
  database: home_assistant
  include:
    entity_globs:
      - sensor.pool_controller_*
      - switch.pool_controller_*
      - select.pool_controller_*
```

### Import the dashboard

1. Add an **InfluxDB** data source (query language **InfluxQL**) in Grafana.
2. Download
    [`dashboard-smart-swimming-pool.json`](https://github.com/smart-swimmingpool/grafana-dashboard/blob/master/dashboard-smart-swimming-pool.json).
3. Open **Dashboards → New → Import**, upload the file and select your InfluxDB data source.

If you renamed the Pool Controller entities in Home Assistant, adjust the dashboard
variables under **Dashboard settings → Variables**.

> [!NOTE]
> Using openHAB with Pool Controller v1/v2? The original dashboard is still available as
> [`dashboard-smart-swimming-pool-openhab-legacy.json`](https://github.com/smart-swimmingpool/grafana-dashboard/blob/master/dashboard-smart-swimming-pool-openhab-legacy.json).

## 🚀 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[Visit Repository](https://github.com/smart-swimmingpool/grafana-dashboard)** - Dashboard JSON and documentation
3. **[Pool Controller Setup](/docs/pool-controller/)** - Ensure your controller is running
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Connect the controller to Home Assistant

## 💬 Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)**
- Open an **[Issue](https://github.com/smart-swimmingpool/grafana-dashboard/issues)** for bugs or feature requests
- Consult the **[Grafana Documentation](https://grafana.com/docs/)** for Grafana-specific questions
