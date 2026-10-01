---
title: Pool Monitor
weight: 1
tags: ["docs", "pool-monitor", "display", "solar"]
---

# 🌡️ Pool Monitor

Der **Pool Monitor** ist ein solarbetriebenes, kabelloses Display, das die aktuelle Pooltemperatur anzeigt. Es ist so konzipiert, dass es energieeffizient ist und vollständig unabhängig von Ihrem Haupt-Pool-Controller funktioniert.

## 💡 Übersicht

Der Pool Monitor bietet:

- **Kabellose Temperaturanzeige**: Zeigt die aktuelle Poolwassertemperatur an
- **Solarbetrieben**: Energieeffizientes Design für kontinuierlichen Betrieb
- **ESP8266-basiert**: Mikrocontroller mit niedrigem Stromverbrauch und WLAN-Anbindung
- **E-Ink-Display**: Geringer Stromverbrauch, bei Sonneneinstrahlung gut lesbar
- **MQTT-Integration**: Empfängt Daten vom Pool-Controller über MQTT
- **Standalone-Betrieb**: Funktioniert unabhängig vom Hauptcontroller

## ✨ Hauptmerkmale

- ✅ **Solarbetrieben**: Kann kontinuierlich mit Solarstrom betrieben werden
- ✅ **Kabellos**: Keine Kabel benötigt, kommuniziert über WLAN
- ✅ **E-Ink-Display**: Klare Sichtbarkeit bei direktem Sonnenlicht
- ✅ **Niedriger Stromverbrauch**: Für minimalen Energieverbrauch ausgelegt
- ✅ **MQTT-Abonnent**: Empfängt Daten von Ihrem Pool-Controller
- ✅ **Standalone**: Unabhängig vom Hauptcontroller-Betrieb
- ✅ **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## 🧭 Schnelle Links

### Erste Schritte

- **[Pool Monitor Repository](https://github.com/smart-swimmingpool/monitor)** - Haupt-Repository mit aller Dokumentation
- **[Aufbauanleitung](https://github.com/smart-swimmingpool/monitor#build-guide)** - Schritt-für-Schritt-Bauanleitung
- **[Hardware Übersicht](https://github.com/smart-swimmingpool/monitor#hardware)** - Komponentenbeschreibungen

### Hardware

- **[Verdrahtungsdiagramm](https://github.com/smart-swimmingpool/monitor#wiring)** - Anschlussanleitung
- **[Stückliste](https://github.com/smart-swimmingpool/monitor#bill-of-materials)** - Vollständige Teileliste

### Firmware

- **[Firmware-Installation](https://github.com/smart-swimmingpool/monitor#firmware)** - Flash-Anleitung
- **[Konfiguration](https://github.com/smart-swimmingpool/monitor#configuration)** - Einrichtungshinweise
- **[MQTT-Konfiguration](https://github.com/smart-swimmingpool/monitor#mqtt-configuration)** - Broker-Einrichtung

## 🔧 Hardware-Anforderungen

| Komponente | Zweck | Ca. Preis |
|-----------|-------|-----------|
| ESP8266 (Wemos D1 Mini) | Hauptcontroller | 5-8 € |
| E-Ink-Display (2,13") | Temperaturanzeige | 15-20 € |
| Solarmodul (6V) | Stromquelle | 10-15 € |
| LiPo-Akku (18650) | Energiespeicher | 5-10 € |
| Ladeschaltung | Akku-Management | 3-5 € |
| Gehäuse | Wetterschutz | 5-10 € |
| **Gesamt** | | **~45-70 €** |

## 📌 Pin-Konfiguration

| Funktion | ESP8266 Pin | Hinweise |
|----------|-------------|---------|
| Display SDA | D2 (GPIO4) | I2C-Daten |
| Display SCL | D1 (GPIO5) | I2C-Takt |
| Display BUSY | D5 (GPIO14) | Beschäftigt-Signal |
| Display DC | D6 (GPIO12) | Daten/Befehl |
| Display RST | D7 (GPIO13) | Reset |
| Display CS | D8 (GPIO15) | Chip-Auswahl |
| Solarmodul | 5V | Stromeingang |
| Akku | 3,3V | Stromausgang |

## 🚀 Nächste Schritte

1. **[Hier beginnen](/docs/start-here/)** - Wählen Sie Ihren Weg basierend auf Ihren Zielen
2. **[Repository besuchen](https://github.com/smart-swimmingpool/monitor)** - Zugriff auf alle Dokumentationen und Quellcode
3. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smarthome-Integration
4. **[Grafana Dashboard](/docs/grafana-dashboard/)** - Datenvisualisierung

## 💬 Brauchen Sie Hilfe?

- Prüfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[Pool Monitor Repository](https://github.com/smart-swimmingpool/monitor)**
- Öffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/monitor/issues)** für Bugs oder Feature-Anfragen
