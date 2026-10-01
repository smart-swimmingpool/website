---
title: Pool Controller
weight: 1
tags: ["docs", "pool-controller", "hardware", "firmware"]
---

# 🎛️ Pool Controller

Der **Pool Controller** ist das Herz des Smart Swimming Pool Systems. Es handelt sich um ein ESP32-basiertes Gerät, das die zentrale Steuerlogik für Ihre Pool-Automatisierung bereitstellt.

## 💡 Übersicht

Der Pool Controller übernimmt:

- **Temperaturüberwachung**: Liest Daten von DS18B20-Temperatursensoren (Poolwasser und Solarkollektor)
- **Pumpensteuerung**: Steuert Zirkulations- und Heizungspumpen über Relaismodule
- **Automatisierungslogik**: Implementiert Heizlogik mit Hysterese und Temperaturgrenzwerten
- **Zirkulationsplanung**: Automatische Zeitschaltung für Sandfilterreinigung
- **MQTT-Integration**: Veröffentlicht alle Daten im Home Assistant MQTT Discovery Format
- **Web-Interface**: Integrierte Konfigurationsoberfläche für einfache Einrichtung
- **Autonomer Betrieb**: Funktioniert unabhängig ohne Smarthome-Server

## ✨ Hauptmerkmale

- ✅ **ESP32-basiert**: Leistungsstarker Mikrocontroller mit WLAN-Anbindung
- ✅ **MQTT Discovery**: Automatische Integration mit Home Assistant
- ✅ **Web-UI**: Einfache Konfiguration über Browser
- ✅ **Active-Low-Relais**: Sichere Standardzustände (Relais AUS während des Boots)
- ✅ **Separate GPIO pro Sensor**: Unabhängige Fehlererkennung
- ✅ **Offline-Betrieb**: Funktioniert auch ohne WLAN weiter
- ✅ **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## 🧭 Schnelle Links

### Erste Schritte

- **[Aufbau von Grund auf](/docs/pool-controller/build-from-zero/)** - Vollständige Aufbauanleitung
- **[Elektrische Sicherheit](/docs/pool-controller/electrical-safety/)** - Wichtige Sicherheitsinformationen
- **[Produktions-Checkliste](/docs/pool-controller/production-checklist/)** - Prüfung vor der Inbetriebnahme
- **[Sicherheits-Checkliste](/docs/pool-controller/security-checklist/)** - Empfehlungen zur IT-Sicherheit

### Hardware

- **[Hardware-Anleitung](/docs/pool-controller/hardware-guide/)** - Komponenten, Verdrahtung und Status-LED
- **[ESP32-Verdrahtungsplan](/docs/pool-controller/esp32-complete-wiring-schematic/)** - Vollständige Anschlussanleitung
- **[NORVI AE01-R](/docs/pool-controller/norvi-ae01-r/)** - Industrielle Hutschienen-Variante
- **[Olimex ESP32-C6-EVB](/docs/pool-controller/olimex-esp32-c6-evb/)** - Variante mit TFT-Display und Drehgeber (englisch)
- **[Schütz-Anleitung](/docs/pool-controller/contactor-guide/)** - Pumpen sicher schalten
- **[Stückliste (BOM)](/docs/bom/)** - Vollständige Teileliste

### Firmware

- **[Software-Anleitung](/docs/pool-controller/software-guide/)** - Firmware bauen und flashen
- **[Benutzerhandbuch](/docs/pool-controller/users-guide/)** - Konfiguration über das Web-Interface
- **[MQTT-Konfiguration](/docs/pool-controller/mqtt-configuration/)** - Broker-Einrichtung und Topics
- **[OTA-Updates](/docs/pool-controller/ota-updates/)** - Firmware-Updates über WLAN

### Fortgeschritten

- **[Sicherheitsmodell](/docs/pool-controller/safety-model/)** - Sicherheitsarchitektur
- **[Temperaturbasierte Umwälzung](/docs/pool-controller/temperature-based-circulation/)** - Adaptive Filterlaufzeit
- **[Fehlerbehebungs-Matrix](/docs/pool-controller/troubleshooting-matrix/)** - Häufige Probleme und Lösungen

## 🔧 Hardware-Anforderungen

### Minimale Einrichtung

| Komponente | Zweck | Ca. Preis |
|-----------|-------|-----------|
| ESP32 DevKit V1 | Hauptcontroller | 8-12 € |
| 2-Kanal-Relaismodul | Pumpensteuerung | 4-6 € |
| 2× DS18B20 Sensoren | Temperaturmessung | 6-10 € |
| 4,7kΩ Widerstände (2x) | Pull-up-Widerstände | < 1 € |
| Steckbrett + Kabel | Prototyping | 3-8 € |
| **Gesamt** | | **~30 €** |

### Produktionsaufbau

| Komponente | Zweck | Ca. Preis |
|-----------|-------|-----------|
| NORVI AE01-R | Industrieller ESP32 | 25-30 € |
| IP65-Gehäuse | Wetterschutz | 10-15 € |
| DIN-Schiene Komponenten | Professionelle Montage | 15-20 € |
| **Gesamt** | | **~75 €** |

## 📌 Pin-Konfiguration

Standard-Pins des **ESP32-DevKit**-Builds (`esp32dev`). Die Builds für NORVI AE01-R und Olimex ESP32-C6-EVB
nutzen eigene Pinbelegungen, siehe `src/Config.hpp` und die oben verlinkten Board-Seiten.

| Funktion | ESP32 Pin | Hinweise |
|----------|-----------|---------|
| Solar-Sensor (DS18B20) | GPIO32 | OneWire-Daten |
| Pool-Sensor (DS18B20) | GPIO33 | OneWire-Daten |
| Heizungspumpen-Relais | GPIO26 | Active-Low |
| Filterpumpen-Relais | GPIO25 | Active-Low |
| Relaismodul VCC | 5V (VIN) | **NICHT 3,3V!** |
| Relaismodul GND | GND | Gemeinsame Masse |
| Sensor VDD | 3,3V | Spannung für Sensoren |
| Sensor GND | GND | Masse für Sensoren |

> ⚠️ **Wichtig**: Jede DS18B20-Datenleitung benötigt einen **4,7kΩ Pull-up-Widerstand** zu 3,3V.

## 🚀 Nächste Schritte

1. **[Hier beginnen](/docs/start-here/)** - Wählen Sie Ihren Weg basierend auf Ihren Zielen
2. **[Schnellstart](/docs/quickstart/)** - Schnellster Weg zum Laufen (60 Minuten)
3. **[Erste Schritte](/docs/getting-started/)** - Umfassliche Aufbauanleitung
4. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smarthome-Integration

## 💬 Brauchen Sie Hilfe?

- Prüfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[Pool Controller Repository](https://github.com/smart-swimmingpool/pool-controller)**
- Öffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/pool-controller/issues)** für Bugs oder Feature-Anfragen
