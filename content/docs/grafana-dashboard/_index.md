---
title: Grafana Dashboard
weight: 1
tags: ["docs", "grafana", "visualization", "monitoring"]
---

# 📊 Grafana Dashboard

The **Grafana Dashboard** visualizes the temperatures and pump switching times of your
Smart Swimming Pool over time. It is a ready-to-import dashboard JSON that reads the data
your smart home server persists in **InfluxDB**.

## 💡 How It Works

```text
Pool Controller ──MQTT──▶ openHAB / Home Assistant ──persistence──▶ InfluxDB ──▶ Grafana
```

1. The [Pool Controller](/docs/pool-controller/) publishes temperatures and pump states via MQTT.
2. Your smart home server (e.g. the [openHAB Configuration](/docs/openhab-configuration/))
   stores the item states in an InfluxDB database.
3. Grafana reads this database and renders the dashboard.

## ✨ Dashboard Panels

The dashboard (`dashboard-smart-swimming-pool.json`) contains these panels:

| Panel | Type | Data (InfluxDB measurement) |
|-------|------|-----------------------------|
| **Temperaturen** | Time series | Pool, solar and air temperature |
| **Pool** | Gauge | `Pool_Controller_PoolTemp_Temperature` |
| **Solar** | Gauge | `Pool_Controller_SolarTemp_Temperature` |
| **Luft** (air) | Gauge | `localCurrentTemperature` |
| **Schaltzeiten** (switching times) | Time series | `Pool_Controller_PoolPump_Switch`, `Pool_Controller_SolarPump_Switch` |

The default time range is the last 30 minutes with an auto refresh every minute.

## 🔧 Installation

### Prerequisites

- A running [Pool Controller](/docs/pool-controller/) publishing data via MQTT
- A smart home server persisting the pool items to InfluxDB
  (see [openHAB Integration](/docs/openhab-integration/))
- [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) with an
  [InfluxDB data source](https://grafana.com/docs/grafana/latest/datasources/influxdb/)

### Import the Dashboard

1. Download
   [`dashboard-smart-swimming-pool.json`](https://github.com/smart-swimmingpool/grafana-dashboard/blob/master/dashboard-smart-swimming-pool.json).
2. In Grafana open **Dashboards → New → Import** and upload the file.
3. Select your InfluxDB data source (the dashboard was created with a data source named
   `openhab_home`).
4. If your items are named differently, adjust the measurements in the panel queries.

## 🚀 Next Steps

1. **[Start Here](/docs/start-here/)** - Choose your path based on your goals
2. **[Visit Repository](https://github.com/smart-swimmingpool/grafana-dashboard)** - Dashboard JSON and documentation
3. **[Pool Controller Setup](/docs/pool-controller/)** - Ensure your controller is running
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Alternative visualization option

## 💬 Need Help?

- Check the **[FAQ & Troubleshooting](/docs/troubleshooting/)** page
- Visit the **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)**
- Open an **[Issue](https://github.com/smart-swimmingpool/grafana-dashboard/issues)** for bugs or feature requests
- Consult the **[Grafana Documentation](https://grafana.com/docs/)** for Grafana-specific questions
