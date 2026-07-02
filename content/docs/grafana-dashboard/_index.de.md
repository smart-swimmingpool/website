---
title: Grafana Dashboard
weight: 1
tags: ["docs", "grafana", "visualization", "monitoring"]
---

# \ud83d\udcc Grafana Dashboard

Das **Grafana Dashboard** bietet eine sch\u00f6ne Visualisierung Ihrer Pool-Daten und erm\u00f6glicht es Ihnen, Temperaturtrends, Systemstatus und historische Daten \u00fcber die Zeit zu verfolgen.

## \ud83d\udca1 \u00dcbersicht

Das Grafana Dashboard bietet:

- **Temperaturvisualisierung**: Verfolgen Sie Pool- und Solartemperaturen \u00fcber die Zeit
- **Historische Daten**: Zeigen Sie Trends und Muster in Ihren Pool-Daten an
- **System\u00fcberwachung**: \u00dcberwachen Sie Pumpenstatus, Betriebszeit und andere Metriken
- **Anpassbar**: Passen Sie das Dashboard an Ihre spezifischen Bed\u00fcrfnisse an
- **Echtzeit-Updates**: Live-Daten von Ihrem Pool-Controller \u00fcber MQTT
- **Benachrichtigungen**: Richten Sie Warnungen f\u00fcr bestimmte Bedingungen ein

## \ud83d\udcc Hauptmerkmale

- \u2705 **Temperaturdiagramme**: Sch\u00f6ne Grafiken, die Temperaturtrends zeigen
- \u2705 **Pumpenstatus**: Visuelle Anzeige der Pumpenbetriebszeiten
- \u2705 **Systemgesundheit**: \u00dcberwachen Sie Controller-Betriebszeit und Verbindung
- \u2705 **Benutzerdefinierte Panels**: F\u00fcgen Sie Panels hinzu oder passen Sie sie an
- \u2705 **Zeitbereichsauswahl**: Zeigen Sie Daten von Stunden bis Monaten an
- \u2705 **Export/Import**: Teilen Sie Ihre Dashboard-Konfiguration mit anderen
- \u2705 **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## \ud83d\ud87 Schnelle Links

### Erste Schritte
- **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)** - Haupt-Repository mit Dashboard-JSON
- **[Installationsanleitung](https://github.com/smart-swimmingpool/grafana-dashboard#installation)** - Schritt-f\u00fcr-Schritt-Setup-Anleitung
- **[Konfiguration](https://github.com/smart-swimmingpool/grafana-dashboard#configuration)** - Dashboard-Setup und Anpassung

### Voraussetzungen
- **[Grafana-Installation](https://grafana.com/docs/grafana/latest/setup-grafana/installation/)** - Installieren Sie Grafana auf Ihrem System
- **[InfluxDB-Setup](https://www.influxdata.com/time-series-platform/influxdb/)** - Zeitreihendatenbank zum Speichern von Pool-Daten
- **[MQTT zu InfluxDB](https://github.com/smart-swimmingpool/grafana-dashboard#mqtt-to-influxdb)** - Br\u00fccke MQTT-Daten zu InfluxDB

### Dashboard-Setup
- **[Dashboard importieren](https://github.com/smart-swimmingpool/grafana-dashboard#import-dashboard)** - Importieren Sie das vorkonfigurierte Dashboard
- **[Datenquellen](https://github.com/smart-swimmingpool/grafana-dashboard#data-sources)** - Konfigurieren Sie Datenquellen in Grafana
- **[Anpassung](https://github.com/smart-swimmingpool/grafana-dashboard#customization)** - Passen Sie das Dashboard an Ihre Bed\u00fcrfnisse an

## \ud83c\udf9b Screenshot

![Grafana Dashboard](/img/grafana-dashboard.png)

*Das Smart Swimming Pool Grafana Dashboard zeigt Temperaturtrends und Systemstatus*

## \ud83d\udda5 Dashboard-Panels

Das Standard-Dashboard enth\u00e4lt:

| Panel | Beschreibung | Datenquelle |
|-------|--------------|-------------|
| **Pool-Temperatur** | Aktuelle und historische Poolwassertemperatur | MQTT/InfluxDB |
| **Solar-Temperatur** | Aktuelle und historische Solarkollektortemperatur | MQTT/InfluxDB |
| **Temperaturdifferenz** | Differenz zwischen Solar- und Pool-Temperatur | Berechnet |
| **Pumpenstatus** | Aktueller Zustand und Betriebszeiten beider Pumpen | MQTT/InfluxDB |
| **System-Betriebszeit** | Controller-Betriebszeit und Verbindungsstatus | MQTT/InfluxDB |
| **Heizungseffizienz** | Heizungsleistungsmetriken | Berechnet |
| **Tagesstatistiken** | T\u00e4gliche Temperaturbereiche und Pumpenbetrieb | MQTT/InfluxDB |

## \ud83d\udc82 N\u00e4chste Schritte

1. **[Hier beginnen](/docs/start-here/)** - W\u00e4hlen Sie Ihren Weg basierend auf Ihren Zielen
2. **[Repository besuchen](https://github.com/smart-swimmingpool/grafana-dashboard)** - Zugriff auf Dashboard-JSON und Dokumentation
3. **[Pool Controller Setup](/docs/pool-controller/)** - Stellen Sie sicher, dass Ihr Controller l\u00e4uft
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Alternative Visualisierungsoption

## \ud83d\udcdd Brauchen Sie Hilfe?

- Pr\u00fcfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[Grafana Dashboard Repository](https://github.com/smart-swimmingpool/grafana-dashboard)**
- \u00d6ffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/grafana-dashboard/issues)** f\u00fcr Bugs oder Feature-Anfragen
- Konsultieren Sie die **[Grafana-Dokumentation](https://grafana.com/docs/)** f\u00fcr Grafana-spezifische Fragen
