---
title: Pool Controller
weight: 1
tags: ["docs", "pool-controller", "hardware", "firmware"]
---

# \ud83c\udf9b Pool Controller

Der **Pool Controller** ist das Herz des Smart Swimming Pool Systems. Es handelt sich um ein ESP32-basiertes Ger\u00e4t, das die zentrale Steuerlogik f\u00fcr Ihre Pool-Automatisierung bereitstellt.

## \ud83d\udca1 \u00dcbersicht

Der Pool Controller \u00fcbernimmt:

- **Temperatur\u00fcberwachung**: Liest Daten von DS18B20-Temperatursensoren (Poolwasser und Solarkollektor)
- **Pumpensteuerung**: Steuert Zirkulations- und Heizungspumpen \u00fcber Relaismodule
- **Automatisierungslogik**: Implementiert Heizlogik mit Hysterese und Temperaturgrenzwerten
- **Zirkulationsplanung**: Automatische Zeitschaltung f\u00fcr Sandfilterreinigung
- **MQTT-Integration**: Ver\u00f6ffentlicht alle Daten im Home Assistant MQTT Discovery Format
- **Web-Interface**: Integrierte Konfigurationsoberfl\u00e4che f\u00fcr einfache Einrichtung
- **Autonomer Betrieb**: Funktioniert unabh\u00e4ngig ohne Smarthome-Server

## \ud83d\udcc Hauptmerkmale

- \u2705 **ESP32-basiert**: Leistungsstarker Mikrocontroller mit WLAN-Anbindung
- \u2705 **MQTT Discovery**: Automatische Integration mit Home Assistant
- \u2705 **Web-UI**: Einfache Konfiguration \u00fcber Browser
- \u2705 **Active-Low-Relais**: Sichere Standardzust\u00e4nde (Relais AUS w\u00e4hrend des Boots)
- \u2705 **Separate GPIO pro Sensor**: Unabh\u00e4ngige Fehlererkennung
- \u2705 **Offline-Betrieb**: Funktioniert auch ohne WLAN weiter
- \u2705 **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## \ud83d\ud87 Schnelle Links

### Erste Schritte
- **[Von Null aufgebaut](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.de.md)** - Vollst\u00e4ndige Aufbauanleitung
- **[Elektrische Sicherheit](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/electrical-safety.de.md)** - Wichtige Sicherheitsinformationen
- **[Produktions-Checkliste](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/production-checklist.de.md)** - Vor-Inbetriebnahme-Pr\u00fcfung
- **[Sicherheits-Checkliste](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/security-checklist.de.md)** - Sicherheitsbest Practices

### Hardware
- **[Hardware \u00dcbersicht](https://github.com/smart-swimmingpool/pool-controller#hardware)** - Komponentenbeschreibungen
- **[Verdrahtungsdiagramm](https://github.com/smart-swimmingpool/pool-controller#wiring)** - Anschlussanleitung
- **[St\u00fcckliste (BOM)](/docs/bom/)** - Vollst\u00e4ndige Teileliste

### Firmware
- **[Firmware-Installation](https://github.com/smart-swimmingpool/pool-controller#firmware)** - Flash-Anleitung
- **[Konfiguration](https://github.com/smart-swimmingpool/pool-controller#configuration)** - Web-Interface-Einrichtung
- **[MQTT-Konfiguration](https://github.com/smart-swimmingpool/pool-controller#mqtt-configuration)** - Broker-Einrichtung

### Fortgeschritten
- **[Sicherheitsmodell](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/safety-model.md)** - Sicherheitsarchitektur
- **[Fehlerbehebung](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/troubleshooting.md)** - H\u00e4ufige Probleme und L\u00f6sungen
- **[API-Referenz](https://github.com/smart-swimmingpool/pool-controller#api)** - MQTT-Themen und Befehle

## \ud83c\udf9b Hardware-Anforderungen

### Minimale Einrichtung
| Komponente | Zweck | Ca. Preis |
|-----------|-------|-----------|
| ESP32 DevKit V1 | Hauptcontroller | 8-12 \u20ac |
| 2-Kanal-Relaismodul | Pumpensteuerung | 4-6 \u20ac |
| 2\u00d7 DS18B20 Sensoren | Temperaturmessung | 6-10 \u20ac |
| 4,7k\u03a9 Widerst\u00e4nde (2x) | Pull-up-Widerst\u00e4nde | < 1 \u20ac |
| Steckbrett + Kabel | Prototyping | 3-8 \u20ac |
| **Gesamt** | | **~30 \u20ac** |

### Produktionsaufbau
| Komponente | Zweck | Ca. Preis |
|-----------|-------|-----------|
| NORVI AE01-R | Industrieller ESP32 | 25-30 \u20ac |
| IP65-Geh\u00e4use | Wetterschutz | 10-15 \u20ac |
| DIN-Schiene Komponenten | Professionelle Montage | 15-20 \u20ac |
| **Gesamt** | | **~75 \u20ac** |

## \ud83d\udda5 Pin-Konfiguration

| Funktion | ESP32 Pin | Hinweise |
|----------|-----------|---------|
| Solar-Sensor (DS18B20) | GPIO32 | OneWire-Daten |
| Pool-Sensor (DS18B20) | GPIO33 | OneWire-Daten |
| Heizungspumpen-Relais | GPIO26 | Active-Low |
| Filterpumpen-Relais | GPIO25 | Active-Low |
| Relaismodul VCC | 5V (VIN) | **NICHT 3,3V!** |
| Relaismodul GND | GND | Gemeinsame Masse |
| Sensor VDD | 3,3V | Spannung f\u00fcr Sensoren |
| Sensor GND | GND | Masse f\u00fcr Sensoren |

> \u26a0\ufe0f **Wichtig**: Jede DS18B20-Datenleitung ben\u00f6tigt einen **4,7k\u03a9 Pull-up-Widerstand** zu 3,3V.

## \ud83d\udc82 N\u00e4chste Schritte

1. **[Hier beginnen](/docs/start-here/)** - W\u00e4hlen Sie Ihren Weg basierend auf Ihren Zielen
2. **[Schnellstart](/docs/quickstart/)** - Schnellster Weg zum Laufen (60 Minuten)
3. **[Erste Schritte](/docs/getting-started/)** - Umfassliche Aufbauanleitung
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smarthome-Integration

## \ud83d\udcdd Brauchen Sie Hilfe?

- Pr\u00fcfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[Pool Controller Repository](https://github.com/smart-swimmingpool/pool-controller)**
- \u00d6ffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/pool-controller/issues)** f\u00fcr Bugs oder Feature-Anfragen
