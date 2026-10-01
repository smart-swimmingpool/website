---
title: openHAB Konfiguration
weight: 1
tags: ["docs", "openhab", "configuration", "smarthome"]
---

# 🏠 openHAB Konfiguration

Die **openHAB Konfiguration** bietet vollständige Konfigurationsdateien für die Integration Ihres Smart Swimming Pools mit dem openHAB Smarthome-Server.

## 💡 Übersicht

Dieses Modul enthält:

- **Sitemap**: Benutzeroberfläche zur Steuerung Ihres Pools über openHAB-Apps
- **Items**: Alle Datenpunkte und Steuerungen für Ihr Poolsystem
- **Regeln**: Automatisierungslogik für die Poolsteuerung
- **Transformationen**: Datenformatierung und Einheitenumrechnungen
- **Persistenz**: Konfiguration für historische Datenspeicherung

## ✨ Hauptmerkmale

- ✅ **Vollständige Sitemap**: Mobilefreundliche Oberfläche zur Poolsteuerung
- ✅ **MQTT-Binding**: Integration mit Ihrem Pool-Controller über MQTT
- ✅ **Automatisierungsregeln**: Fortgeschrittene Automatisierungslogik
- ✅ **Historische Daten**: Persistenzkonfiguration für Diagramme und Trends
- ✅ **Mehrsprachig**: Unterstützung für verschiedene Sprachen
- ✅ **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## 🧭 Schnelle Links

### Erste Schritte

- **[openHAB Konfiguration Repository](https://github.com/smart-swimmingpool/openhab-config)** - Haupt-Repository mit allen Konfigurationsdateien
- **[openHAB Integrationsanleitung](/docs/openhab-integration/)** - Schritt-für-Schritt-Integrationsanleitung
- **[Installation](https://github.com/smart-swimmingpool/openhab-config#installation)** - Setup-Anleitung

### Konfigurationsdateien

- **[Sitemap](https://github.com/smart-swimmingpool/openhab-config/blob/master/sitemaps/pool.sitemap)** - Benutzeroberflächendefinition
- **[Items](https://github.com/smart-swimmingpool/openhab-config/blob/master/items/2-pool.items)** - Datenpunkte und Steuerungen
- **[Regeln](https://github.com/smart-swimmingpool/openhab-config/blob/master/rules/pool.rules)** - Automatisierungslogik
- **[Transformationen](https://github.com/smart-swimmingpool/openhab-config/tree/master/transform)** - Datenformatierung
- **[Persistenz](https://github.com/smart-swimmingpool/openhab-config/blob/master/persistence/rrd4j.persist)** - Historische Datenspeicherung

## 🖼️ Sitemap-Vorschau

Die Sitemap bietet eine mobilefreundliche Oberfläche mit:

- **Dashboard**: Übersicht über alle Pool-Status und Steuerungen
- **Temperaturen**: Aktuelle Pool- und Solartemperaturen
- **Pumpensteuerung**: Manuelle und automatische Pumpensteuerung
- **Heizung**: Heizkreislaufsteuerung und Einstellungen
- **Zeitpläne**: Zirkulations- und Heizungszeitpläne
- **Verlauf**: Historische Daten und Diagramme
- **Einstellungen**: Konfiguration und Systemeinstellungen

## 📋 Items Übersicht

Die Items-Datei enthält:

| Kategorie | Items | Beschreibung |
|----------|-------|--------------|
| **Temperaturen** | PoolTemp, SolarTemp | Aktuelle Temperaturen von den Sensoren |
| **Pumpen** | FilterPumpe, Heizungspumpe | Pumpenstatus und Steuerung |
| **Heizung** | HeizungAktiviert, MaxPoolTemp | Heizungssteuerungsparameter |
| **Zeitpläne** | Zirkulationszeitplan | Zeitschaltungseinstellungen |
| **System** | Systemstatus, Betriebszeit | Systemgesundheit und Status |

## 🚀 Nächste Schritte

1. **[Hier beginnen](/docs/start-here/)** - Wählen Sie Ihren Weg basierend auf Ihren Zielen
2. **[openHAB Integrationsanleitung](/docs/openhab-integration/)** - Schritt-für-Schritt-Integrationsanleitung
3. **[Repository besuchen](https://github.com/smart-swimmingpool/openhab-config)** - Zugriff auf alle Konfigurationsdateien
4. **[Pool Controller Setup](/docs/pool-controller/)** - Stellen Sie sicher, dass Ihr Controller läuft

## 💬 Brauchen Sie Hilfe?

- Prüfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[openHAB Konfiguration Repository](https://github.com/smart-swimmingpool/openhab-config)**
- Öffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/openhab-config/issues)** für Bugs oder Feature-Anfragen
- Konsultieren Sie die **[openHAB-Dokumentation](https://www.openhab.org/docs/)** für openHAB-spezifische Fragen
