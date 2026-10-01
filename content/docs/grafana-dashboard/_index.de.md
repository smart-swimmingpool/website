---
title: Grafana Dashboard
weight: 1
tags: ["docs", "grafana", "visualization", "monitoring"]
---

# 📊 Grafana Dashboard

Das **Grafana Dashboard** zeigt deinen Smart Swimming Pool im zeitlichen Verlauf: Pool- und
Solartemperatur, Pumpen-Schaltzeiten, Betriebsmodus und Diagnosewerte des Controllers. Es ist
für den [Pool Controller](/docs/pool-controller/) **v5.x** gemacht und liest die Daten, die
**Home Assistant** in **InfluxDB** speichert.

![Grafana Dashboard mit Beispieldaten](https://raw.githubusercontent.com/smart-swimmingpool/grafana-dashboard/master/docs/dashboard-screenshot.png)

## 💡 Funktionsweise

```text
Pool Controller ──MQTT Discovery──▶ Home Assistant ──InfluxDB-Integration──▶ InfluxDB ──▶ Grafana
```

1. Der Pool Controller meldet seine Entitäten per Home-Assistant-MQTT-Discovery an
   (siehe [Home Assistant Integration](/docs/home-assistant-integration/)).
2. Die [InfluxDB-Integration](https://www.home-assistant.io/integrations/influxdb/) von
   Home Assistant speichert die Zustände in InfluxDB.
3. Grafana fragt diese Datenbank ab und stellt das Dashboard dar.

## ✨ Dashboard-Panels

| Bereich | Panels |
|---------|--------|
| **Temperaturen** | Anzeigen für Pool und Solar, Verlauf von Pool-, Solar- und Controller-Temperatur |
| **Pumpen & Betrieb** | Zeitleiste der Pumpen, aktueller Pumpenstatus, effektive Laufzeit, Umwälzungs-Verlängerung, Betriebsmodus (Auto, Manuell, Boost, Timer) |
| **Diagnose** | WLAN-Signal, Uptime, freier Speicher, Controller-Temperatur mit Verlauf |

## 🔧 Installation

### Voraussetzungen

- [Pool Controller](/docs/pool-controller/) v5.x, verbunden mit Home Assistant
- [InfluxDB-Integration](https://www.home-assistant.io/integrations/influxdb/) von Home Assistant
  mit Standard-Einstellungen für Measurements
- InfluxDB 1.x (oder 2.x mit InfluxQL) und Grafana 10 oder neuer

### Pool-Daten in InfluxDB speichern

Beispiel für die `configuration.yaml` von Home Assistant:

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

### Dashboard importieren

1. Lege in Grafana eine **InfluxDB**-Datenquelle (Abfragesprache **InfluxQL**) an.
2. Lade
   [`dashboard-smart-swimming-pool.json`](https://github.com/smart-swimmingpool/grafana-dashboard/blob/master/dashboard-smart-swimming-pool.json)
   herunter.
3. Öffne **Dashboards → New → Import**, lade die Datei hoch und wähle deine InfluxDB-Datenquelle.

Hast du die Pool-Controller-Entitäten in Home Assistant umbenannt, passe die Dashboard-Variablen
unter **Dashboard settings → Variables** an.

> [!NOTE]
> Du nutzt openHAB mit Pool Controller v1/v2? Das ursprüngliche Dashboard gibt es weiterhin als
> [`dashboard-smart-swimming-pool-openhab-legacy.json`](https://github.com/smart-swimmingpool/grafana-dashboard/blob/master/dashboard-smart-swimming-pool-openhab-legacy.json).

## 🚀 Nächste Schritte

1. **[Hier beginnen](/docs/start-here/)** - Wähle deinen Weg passend zu deinen Zielen
2. **[Repository besuchen](https://github.com/smart-swimmingpool/grafana-dashboard)** - Dashboard-JSON und Dokumentation
3. **[Pool Controller Setup](/docs/pool-controller/)** - Stelle sicher, dass dein Controller läuft
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Controller mit Home Assistant verbinden

## 💬 Hilfe benötigt?

- Sieh auf der Seite **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** nach
- Besuche das **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)**
- Öffne ein **[Issue](https://github.com/smart-swimmingpool/grafana-dashboard/issues)** für Fehler oder Wünsche
- Lies die **[Grafana-Dokumentation](https://grafana.com/docs/)** für Grafana-spezifische Fragen
