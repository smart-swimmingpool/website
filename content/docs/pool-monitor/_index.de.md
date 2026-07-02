---
title: Pool Monitor
weight: 1
tags: ["docs", "pool-monitor", "display", "solar"]
---

# \ud83d\udda5 Pool Monitor

Der **Pool Monitor** ist ein solarbetriebenes, kabelloses Display, das die aktuelle Pooltemperatur anzeigt. Es ist so konzipiert, dass es energieeffizient ist und vollst\u00e4ndig unabh\u00e4ngig von Ihrem Haupt-Pool-Controller funktioniert.

## \ud83d\udca1 \u00dcbersicht

Der Pool Monitor bietet:

- **Kabellose Temperaturanzeige**: Zeigt die aktuelle Poolwassertemperatur an
- **Solarbetrieben**: Energieeffizientes Design f\u00fcr kontinuierlichen Betrieb
- **ESP8266-basiert**: Mikrocontroller mit niedrigem Stromverbrauch und WLAN-Anbindung
- **E-Ink-Display**: Geringer Stromverbrauch, bei Sonneneinstrahlung gut lesbar
- **MQTT-Integration**: Empf\u00e4ngt Daten vom Pool-Controller \u00fcber MQTT
- **Standalone-Betrieb**: Funktioniert unabh\u00e4ngig vom Hauptcontroller

## \ud83d\udcc Hauptmerkmale

- \u2705 **Solarbetrieben**: Kann kontinuierlich mit Solarstrom betrieben werden
- \u2705 **Kabellos**: Keine Kabel ben\u00f6tigt, kommuniziert \u00fcber WLAN
- \u2705 **E-Ink-Display**: Klare Sichtbarkeit bei direktem Sonnenlicht
- \u2705 **Niedriger Stromverbrauch**: F\u00fcr minimalen Energieverbrauch ausgelegt
- \u2705 **MQTT-Abonnent**: Empf\u00e4ngt Daten von Ihrem Pool-Controller
- \u2705 **Standalone**: Unabh\u00e4ngig vom Hauptcontroller-Betrieb
- \u2705 **Open Source**: MIT-Lizenz, frei zu verwenden und zu modifizieren

## \ud83d\ud87 Schnelle Links

### Erste Schritte
- **[Pool Monitor Repository](https://github.com/smart-swimmingpool/monitor)** - Haupt-Repository mit aller Dokumentation
- **[Aufbauanleitung](https://github.com/smart-swimmingpool/monitor#build-guide)** - Schritt-f\u00fcr-Schritt-Bauanleitung
- **[Hardware \u00dcbersicht](https://github.com/smart-swimmingpool/monitor#hardware)** - Komponentenbeschreibungen

### Hardware
- **[Verdrahtungsdiagramm](https://github.com/smart-swimmingpool/monitor#wiring)** - Anschlussanleitung
- **[St\u00fcckliste](https://github.com/smart-swimmingpool/monitor#bill-of-materials)** - Vollst\u00e4ndige Teileliste

### Firmware
- **[Firmware-Installation](https://github.com/smart-swimmingpool/monitor#firmware)** - Flash-Anleitung
- **[Konfiguration](https://github.com/smart-swimmingpool/monitor#configuration)** - Einrichtungshinweise
- **[MQTT-Konfiguration](https://github.com/smart-swimmingpool/monitor#mqtt-configuration)** - Broker-Einrichtung

## \ud83c\udf9b Hardware-Anforderungen

| Komponente | Zweck | Ca. Preis |
|-----------|-------|-----------|
| ESP8266 (Wemos D1 Mini) | Hauptcontroller | 5-8 \u20ac |
| E-Ink-Display (2,13") | Temperaturanzeige | 15-20 \u20ac |
| Solarmodul (6V) | Stromquelle | 10-15 \u20ac |
| LiPo-Akku (18650) | Energiespeicher | 5-10 \u20ac |
| Ladeschaltung | Akku-Management | 3-5 \u20ac |
| Geh\u00e4use | Wetterschutz | 5-10 \u20ac |
| **Gesamt** | | **~45-70 \u20ac** |

## \ud83d\udda5 Pin-Konfiguration

| Funktion | ESP8266 Pin | Hinweise |
|----------|-------------|---------|
| Display SDA | D2 (GPIO4) | I2C-Daten |
| Display SCL | D1 (GPIO5) | I2C-Takt |
| Display BUSY | D5 (GPIO14) | Besch\u00e4ftigt-Signal |
| Display DC | D6 (GPIO12) | Daten/Befehl |
| Display RST | D7 (GPIO13) | Reset |
| Display CS | D8 (GPIO15) | Chip-Auswahl |
| Solarmodul | 5V | Stromeingang |
| Akku | 3,3V | Stromausgang |

## \ud83d\udc82 N\u00e4chste Schritte

1. **[Hier beginnen](/docs/start-here/)** - W\u00e4hlen Sie Ihren Weg basierend auf Ihren Zielen
2. **[Repository besuchen](https://github.com/smart-swimmingpool/monitor)** - Zugriff auf alle Dokumentationen und Quellcode
3. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Smarthome-Integration
4. **[Grafana Dashboard](/docs/grafana-dashboard/)** - Datenvisualisierung

## \ud83d\udcdd Brauchen Sie Hilfe?

- Pr\u00fcfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie das **[Pool Monitor Repository](https://github.com/smart-swimmingpool/monitor)**
- \u00d6ffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/monitor/issues)** f\u00fcr Bugs oder Feature-Anfragen
