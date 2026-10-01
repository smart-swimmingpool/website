---
title: Water Quality Monitor
weight: 1
tags: ["docs", "water-quality", "pH", "chlorine", "esp8266"]
---

# 🧪 Water Quality Monitor

Der **Water Quality Monitor** ist ein geplantes Modul, das die chemische Wasserqualität deines
Pools misst — **pH-Wert**, **Chlor** und **Wassertemperatur** — und die Werte per MQTT an dein
Smarthome-System sendet.

> [!WARNING]
> **Status: in Entwicklung.** Das Modul befindet sich in der Planungs- und frühen Prototyp-Phase.
> Eine fertige Firmware gibt es noch nicht. Beiträge sind herzlich willkommen!

## 💡 Geplante Messgrößen

| Parameter | Bereich | Bedeutung |
|-----------|---------|-----------|
| **pH-Wert** | 0–14 | Beeinflusst die Wirksamkeit von Chlor und den Badekomfort |
| **Chlor** | 0–10 ppm | Wichtigstes Desinfektionsmittel gegen Bakterien und Algen |
| **Temperatur** | 0–60 °C | Beeinflusst chemische Reaktionen und Komfort |

## 🧩 Einbindung ins Smart-Swimming-Pool-System

- Veröffentlicht Messwerte per **MQTT**, wie der [Pool Controller](/docs/pool-controller/)
- Werte lassen sich speichern und visualisieren, z. B. mit dem [Grafana Dashboard](/docs/grafana-dashboard/)
- Nutzbar in [Home Assistant](/docs/home-assistant-integration/) und [openHAB](/docs/openhab-integration/)

## 🧭 Dokumentation

- **[Hardware-Anleitung](/docs/water-quality-monitor/hardware-guide/)** - Sensoroptionen, Schaltungsideen und Stückliste (englisch)
- **[Repository](https://github.com/smart-swimmingpool/water-quality-monitor)** - Quellcode und aktueller Stand

## 🤝 Mitmachen

- pH- und Chlorsensoren mit ESP8266/ESP32-Boards testen
- Schaltung, Platine oder ein wasserdichtes Gehäuse entwerfen
- Sensorauslesung, Kalibrierung und MQTT-Versand implementieren
- Praxistests durchführen und mit Teststreifen/Testkits vergleichen

Öffne ein **[Issue](https://github.com/smart-swimmingpool/water-quality-monitor/issues)**, um Ideen
zu diskutieren oder deinen Beitrag abzustimmen.
