---
title: openHAB Konfiguration
weight: 1
tags: ["docs", "openhab", "configuration", "smarthome"]
---

# \ud83c\udfed openHAB Konfiguration

Die **openHAB Konfiguration** bietet vollst\u00e4ndige Konfigurationsdateien f\u00fcr die Integration Ihres Smart Swimming Pools mit dem openHAB Smarthome-Server.

## \ud83d\udca1 \u00dcbersicht

Dieses Modul enth\u00e4lt:

- **Sitemap**: Benutzeroberfl\u00e4che zur Steuerung Ihres Pools \u00fcber openHAB-Apps
- **Items**: Alle Datenpunkte und Steuerungen f\u00fcr Ihr Poolsystem
- **Regeln**: Automatisierungslogik f\u00fcr die Poolsteuerung
- **Transformationen**: Datenformatierung und Einheitenumrechnungen
- **Persistenz**: Konfiguration f\u00fcr historische Datenspeicherung

## \ud83d\udcc Hauptmerkmale

- \u2705 **Vollst\u00e4ndige Sitemap**: Mobilefreundliche Oberfl\u00e4che zur Poolsteuerung
- \u2705 **MQTT-Binding**: Integration mit Ihrem Pool-Controller \u00fcber MQTT
- \u2705 **Automatisierungsregeln**: Fortgeschrittene Automatisierungslogik
- \u2705 **Historische Daten**: Persistenzkonfiguration f\u00fcr Diagramme und Trends
- \u2705 **Mehrsprachig**: Unterst\u00fctzung f\u00fcr verschiedene Sprachen
- \u2705 **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## \ud83d\ud87 Schnelle Links

### Erste Schritte
- **[openHAB Konfiguration Repository](https://github.com/smart-swimmingpool/openhab-config)** - Haupt-Repository mit allen Konfigurationsdateien
- **[openHAB Integrationsanleitung](/docs/openhab-integration/)** - Schritt-f\u00fcr-Schritt-Integrationsanleitung
- **[Installation](https://github.com/smart-swimmingpool/openhab-config#installation)** - Setup-Anleitung

### Konfigurationsdateien
- **[Sitemap](https://github.com/smart-swimmingpool/openhab-config/blob/main/sitemaps/pool.sitemap)** - Benutzeroberfl\u00e4chendefinition
- **[Items](https://github.com/smart-swimmingpool/openhab-config/blob/main/items/pool.items)** - Datenpunkte und Steuerungen
- **[Regeln](https://github.com/smart-swimmingpool/openhab-config/blob/main/rules/pool.rules)** - Automatisierungslogik
- **[Transformationen](https://github.com/smart-swimmingpool/openhab-config/tree/main/transform)** - Datenformatierung
- **[Persistenz](https://github.com/smart-swimmingpool/openhab-config/blob/main/persistence/rrd4j.persist)** - Historische Datenspeicherung

## \ud83c\udf9b Sitemap-Vorschau

Die Sitemap bietet eine mobilefreundliche Oberfl\u00e4che mit:

- **Dashboard**: \u00dcbersicht \u00fcber alle Pool-Status und Steuerungen
- **Temperaturen**: Aktuelle Pool- und Solartemperaturen
- **Pumpensteuerung**: Manuelle und automatische Pumpensteuerung
- **Heizung**: Heizkreislaufsteuerung und Einstellungen
- **Zeitpl\u00e4ne**: Zirkulations- und Heizungszeitpl\u00e4ne
- **Verlauf**: Historische Daten und Diagramme
- **Einstellungen**: Konfiguration und Systemeinstellungen

## \ud83d\udda5 Items \u00dcbersicht

Die Items-Datei enth\u00e4lt:

| Kategorie | Items | Beschreibung |
|----------|-------|--------------|
| **Temperaturen** | PoolTemp, SolarTemp | Aktuelle Temperaturen von den Sensoren |
| **Pumpen** | FilterPumpe, Heizungspumpe | Pumpenstatus und Steuerung |
| **Heizung** | HeizungAktiviert, MaxPoolTemp | Heizungssteuerungsparameter |
| **Zeitpl\u00e4ne** | Zirkulationszeitplan | Zeitschaltungseinstellungen |
| **System** | Systemstatus, Betriebszeit | Systemgesundheit und Status |

## \ud83d\udc82 N\u00e4chste Schritte

1. **[Hier beginnen](/docs/start-here/)** - W\u00e4hlen Sie Ihren Weg basierend auf Ihren Zielen
2. **[openHAB Integrationsanleitung](/docs/openhab-integration/)** - Schritt-f\u00fcr-Schritt-Integrationsanleitung
3. **[Repository besuchen](https://github.com/smart-swimmingpool/openhab-config)** - Zugriff auf alle Konfigurationsdateien
4. **[Pool Controller Setup](/docs/pool-controller/)** - Stellen Sie sicher, dass Ihr Controller l\u00e4uft

## \ud83d\udcdd Brauchen Sie Hilfe?

- Pr\u00fcfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[openHAB Konfiguration Repository](https://github.com/smart-swimmingpool/openhab-config)**
- \u00d6ffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/openhab-config/issues)** f\u00fcr Bugs oder Feature-Anfragen
- Konsultieren Sie die **[openHAB-Dokumentation](https://www.openhab.org/docs/)** f\u00fcr openHAB-spezifische Fragen
