---
title: Grafana Dashboard
weight: 1
tags: ["docs", "grafana", "visualization", "monitoring"]
---

# 📊 Grafana Dashboard

Das **Grafana Dashboard** visualisiert die Temperaturen und Pumpen-Schaltzeiten deines
Smart Swimming Pools im zeitlichen Verlauf. Es ist ein fertiges Dashboard-JSON, das die
Daten liest, die dein Smarthome-Server in **InfluxDB** speichert.

## 💡 Funktionsweise

```text
Pool Controller ──MQTT──▶ openHAB / Home Assistant ──Persistenz──▶ InfluxDB ──▶ Grafana
```

1. Der [Pool Controller](/docs/pool-controller/) veröffentlicht Temperaturen und Pumpenzustände per MQTT.
2. Dein Smarthome-Server (z. B. mit der [openHAB Konfiguration](/docs/openhab-configuration/))
   speichert die Item-Zustände in einer InfluxDB-Datenbank.
3. Grafana liest diese Datenbank und stellt das Dashboard dar.

## ✨ Dashboard-Panels

Das Dashboard (`dashboard-smart-swimming-pool.json`) enthält folgende Panels:

| Panel | Typ | Daten (InfluxDB-Measurement) |
|-------|-----|------------------------------|
| **Temperaturen** | Zeitverlauf | Pool-, Solar- und Lufttemperatur |
| **Pool** | Anzeige (Gauge) | `Pool_Controller_PoolTemp_Temperature` |
| **Solar** | Anzeige (Gauge) | `Pool_Controller_SolarTemp_Temperature` |
| **Luft** | Anzeige (Gauge) | `localCurrentTemperature` |
| **Schaltzeiten** | Zeitverlauf | `Pool_Controller_PoolPump_Switch`, `Pool_Controller_SolarPump_Switch` |

Standardmäßig werden die letzten 30 Minuten angezeigt, aktualisiert wird jede Minute.

## 🔧 Installation

### Voraussetzungen

- Ein laufender [Pool Controller](/docs/pool-controller/), der Daten per MQTT veröffentlicht
- Ein Smarthome-Server, der die Pool-Items in InfluxDB speichert
  (siehe [openHAB Integration](/docs/openhab-integration/))
- [Grafana](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) mit einer
  [InfluxDB-Datenquelle](https://grafana.com/docs/grafana/latest/datasources/influxdb/)

### Dashboard importieren

1. Lade
   [`dashboard-smart-swimming-pool.json`](https://github.com/smart-swimmingpool/grafana-dashboard/blob/master/dashboard-smart-swimming-pool.json)
   herunter.
2. Öffne in Grafana **Dashboards → New → Import** und lade die Datei hoch.
3. Wähle deine InfluxDB-Datenquelle aus (das Dashboard wurde mit einer Datenquelle namens
   `openhab_home` erstellt).
4. Heißen deine Items anders, passe die Measurements in den Panel-Abfragen an.

## 🚀 Nächste Schritte

1. **[Hier beginnen](/docs/start-here/)** - Wähle deinen Weg passend zu deinen Zielen
2. **[Repository besuchen](https://github.com/smart-swimmingpool/grafana-dashboard)** - Dashboard-JSON und Dokumentation
3. **[Pool Controller Setup](/docs/pool-controller/)** - Stelle sicher, dass dein Controller läuft
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Alternative Visualisierung

## 💬 Hilfe benötigt?

- Sieh auf der Seite **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** nach
- Besuche das **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)**
- Öffne ein **[Issue](https://github.com/smart-swimmingpool/grafana-dashboard/issues)** für Fehler oder Wünsche
- Lies die **[Grafana-Dokumentation](https://grafana.com/docs/)** für Grafana-spezifische Fragen
