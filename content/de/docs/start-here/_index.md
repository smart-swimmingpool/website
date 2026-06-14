---
title: Hier starten
weight: 1
---

👋 Willkommen beim **Smart Swimming Pool**-Projekt! Diese Seite hilft dir,
den richtigen Einstieg zu finden — je nachdem, was du bauen möchtest.

---

## Wähle deinen Pfad

### 🔰 Ich möchte den einfachstmöglichen Aufbau

**Ziel**: Pool-Umwälzung mit minimalem Kosten- und Arbeitsaufwand automatisieren.

- **Steckbrett oder Lochrasterplatine** mit ESP32 DevKit V1
- 2-Kanal-Relaismodul zur Pumpensteuerung
- 2× DS18B20 Temperatursensoren
- Vorgefertigte Firmware flashen
- Steuerung über Home Assistant

**Hier starten**: [Pool-Controller — Von Null aufgebaut](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.de.md)

| Komponente | Ca. Preis |
|-----------|-----------|
| ESP32 DevKit V1 | 8–12 € |
| 2-Kanal-Relaismodul | 4–6 € |
| 2× DS18B20 Sensoren | 6–10 € |
| Steckbrett + Kabel | 5 € |
| **Gesamt** | **~30 €** |

---

### 🏊 Ich habe einen Standard-Pool mit Sandfilter und Solarheizung

**Ziel**: Vollautomation mit Zeitplan-Umwälzung und Solarheizungsregelung.

- Die [Von Null aufgebaut](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.de.md)-Anleitung befolgen
- **IP65-Gehäuse** für Wetterschutz verwenden
- Ordnungsgemäße **Netzspannungs-Verdrahtung** mit Sicherung und FI-Schutz
- **Home Assistant**-Integration für Dashboard und Automatisierung
- **MQTT** für zuverlässige Kommunikation

**Erforderliche Lektüre**:
- [Elektrische Sicherheit](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/electrical-safety.de.md)
- [Produktions-Checkliste](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/production-checklist.de.md)
- [Sicherheits-Checkliste](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/security-checklist.de.md)

---

### 🏭 Ich baue eine produktionsreife Installation

**Ziel**: Industriegerechter, 24/7 zuverlässiger Pool-Controller mit voller
Sicherheit.

- **NORVI AE01-R** oder eigene Platine für höchste Zuverlässigkeit
- **IP66+-Gehäuse** mit Kabelverschraubungen
- **Hutschienenmontage**
- Ordnungsgemäße **Überstromabsicherung** und **Erdung**
- **Flash-Verschlüsselung** aktiviert
- **IoT-VLAN** mit Firewall-Regeln
- Regelmäßiger **Wartungsplan**

**Erforderliche Lektüre**:
- [Von Null aufgebaut](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.de.md)
- [Elektrische Sicherheit](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/electrical-safety.de.md)
- [Sicherheitsmodell](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/safety-model.de.md)
- [Produktions-Checkliste](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/production-checklist.de.md)
- [Sicherheits-Checkliste](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/security-checklist.de.md)
- [Fehlerbehebung](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/troubleshooting.de.md)

---

## Architektur-Übersicht

```
┌──────────────────────────────────────────────────────────────┐
│                      Pool-Umgebung                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐ │
│  │ Pool-    │  │ Solar-   │  │ Sand-    │  │ Wärme-       │ │
│  │ pumpe    │  │ pumpe    │  │ filter   │  │ tauscher     │ │
│  └────┬─────┘  └────┬─────┘  └──────────┘  └──────┬───────┘ │
│       │              │                              │         │
└───────┼──────────────┼──────────────────────────────┼─────────┘
        │              │                              │
        ▼              ▼                              ▼
┌──────────────────────────────────────────────────────────────┐
│                   Pool-Controller (ESP32)                     │
│  ┌────────────┐  ┌────────────┐  ┌──────────────────────┐   │
│  │ DS18B20    │  │ DS18B20    │  │ 2-Kanal-Relais       │   │
│  │ Pool-Temp  │  │ Solar-Temp │  │ GPIO18 → Poolpumpe   │   │
│  │ GPIO16     │  │ GPIO15     │  │ GPIO19 → Solarpumpe  │   │
│  └────────────┘  └────────────┘  └──────────────────────┘   │
│                          │                                    │
│                    ┌─────┴──────┐                              │
│                    │  WiFi STA  │                              │
│                    │  MQTT Pub  │                              │
│                    │  Web-UI    │                              │
│                    └─────┬──────┘                              │
└──────────────────────────┼────────────────────────────────────┘
                           │ MQTT
                           ▼
┌──────────────────────────────────────────────────────────────┐
│                   Smart-Home-Server                            │
│  ┌────────────────────┐  ┌────────────────────────────────┐  │
│  │ Home Assistant     │  │ MQTT-Broker (Mosquitto)        │  │
│  │ • MQTT Discovery   │  │ • pool-controller/# Topics     │  │
│  │ • Lovelace UI      │  │ • Auth aktiviert               │  │
│  │ • Automatisierungen│  │ • Nur lokal                    │  │
│  └────────────────────┘  └────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

---

## Repository-Übersicht

| Repository | Zweck | Sprache |
|-----------|-------|---------|
| [pool-controller](https://github.com/smart-swimmingpool/pool-controller) | ESP32-Firmware, Web-UI, Hardware-Doku | C++ (PlatformIO) |
| [website](https://github.com/smart-swimmingpool/website) | Projekt-Website (Hugo) | Markdown, Hugo |
| [openhab-config](https://github.com/smart-swimmingpool/openhab-config) | openHAB-Konfiguration (Legacy) | openHAB DSL |
| [monitor](https://github.com/smart-swimmingpool/monitor) | Solarbetriebene Temperaturanzeige | C++ |
| [grafana-dashboard](https://github.com/smart-swimmingpool/grafana-dashboard) | Grafana-Dashboard-JSON | JSON |

---

## FAQ

### Brauche ich Home Assistant?

Nein. Der Controller hat ein integriertes Web-Interface zur direkten Steuerung.
Home Assistant bietet ein schöneres Dashboard und Automatisierungsmöglichkeiten,
ist aber nicht erforderlich.

### Kann ich openHAB verwenden?

Ja. openHAB wird über MQTT unterstützt. Siehe das
[openHAB-Config-Repository](https://github.com/smart-swimmingpool/openhab-config).
Hinweis: Home Assistant Discovery ist heute der primäre Integrationspfad —
openHAB erfordert manuelle MQTT-Konfiguration.

### Was, wenn ich keine Solarheizung habe?

Kein Problem. Die Solarpumpen-Funktionen können ungenutzt bleiben. Der
Controller funktioniert einwandfrei nur mit der Pool-Umwälzung.

### Kann ich das mit jeder Poolpumpe verwenden?

Ja, solange die Pumpe über ein Relais (Netzspannung) ein- und ausgeschaltet
werden kann. Die meisten Sandfilterpumpen unterstützen dies. Beachte den
Schaltplan deiner Pumpe.

### Wie lang dürfen die DS18B20-Sensorkabel sein?

Bis zu 10 Meter mit 4,7 kΩ Pull-up. Für längere Strecken einen niedrigeren
Pull-up-Wert (z. B. 2,2 kΩ) oder einen dedizierten OneWire-Treiber verwenden.

### Muss ich Elektriker sein?

Die grundlegende Verdrahtung (Relais zu Pumpen) erfordert Arbeiten mit 230V AC.
Wenn du dich mit Netzspannung nicht wohlfühlst, beauftrage eine
qualifizierte Elektrofachkraft.

### Kann ich den Controller ohne WLAN betreiben?

Der Controller benötigt WLAN für die MQTT-Kommunikation, arbeitet aber mit
der zuletzt bekannten Konfiguration weiter, wenn das WLAN ausfällt. Eine
zukünftige Version wird den standalone-Betrieb mit Display und Tasten
unterstützen.

---

## Nächste Schritte

1. Die [Von Null aufgebaut](https://github.com/smart-swimmingpool/pool-controller/blob/main/docs/build-from-zero.de.md)-Anleitung lesen
2. Teile aus der Stückliste bestellen
3. Auf dem Steckbrett aufbauen und testen
4. Im Gehäuse installieren
5. In Home Assistant integrieren
6. Deinen smarten Pool genießen!
