---
title: Hier starten
weight: 11
---

👋 Willkommen beim **Smart Swimming Pool**-Projekt! Diese Seite hilft Ihnen,
den richtigen Einstieg zu finden — je nachdem, was Sie bauen möchten.

---

## Wählen Sie Ihren Pfad

### 🔰 Ich möchte den einfachstmöglichen Aufbau

**Ziel**: Pool-Umwälzung mit minimalem Kosten- und Arbeitsaufwand automatisieren.

- **Steckbrett oder Lochrasterplatine** mit ESP32 DevKit V1
- 2-Kanal-Relaismodul zur Pumpensteuerung
- 2× DS18B20 Temperatursensoren
- Vorgefertigte Firmware flashen
- Steuerung über Home Assistant

**Hier starten**: [Pool-Controller — Von Null aufgebaut](/docs/pool-controller/build-from-zero/)

| Komponente | Ca. Preis |
|-----------|-----------|
| ESP32 DevKit V1 | 8–12 € |
| 2-Kanal-Relaismodul | 4–6 € |
| 2× DS18B20 Sensoren | 6–10 € |
| Steckbrett + Kabel | 5 € |
| Widerstände, Netzteil, Kleinteile | siehe Stückliste |
| **Gesamt** | **~35–55 €** (siehe [Stückliste](/docs/bom/)) |

---

### 🏊 Ich habe einen Standard-Pool mit Sandfilter und Solarheizung

**Ziel**: Vollautomation mit Zeitplan-Umwälzung und Solarheizungsregelung.

- Die [Von Null aufgebaut](/docs/pool-controller/build-from-zero/)-Anleitung befolgen
- **IP65-Gehäuse** für Wetterschutz verwenden
- Ordnungsgemäße **Netzspannungs-Verdrahtung** mit Sicherung und FI-Schutz
- **Home Assistant**-Integration für Dashboard und Automatisierung
- **MQTT** für zuverlässige Kommunikation

**Erforderliche Lektüre**:
- [Elektrische Sicherheit](/docs/pool-controller/electrical-safety/)
- [Produktions-Checkliste](/docs/pool-controller/production-checklist/)
- [Sicherheits-Checkliste](/docs/pool-controller/security-checklist/)

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
- [Von Null aufgebaut](/docs/pool-controller/build-from-zero/)
- [Elektrische Sicherheit](/docs/pool-controller/electrical-safety/)
- [Sicherheitsmodell](/docs/pool-controller/safety-model/)
- [Produktions-Checkliste](/docs/pool-controller/production-checklist/)
- [Sicherheits-Checkliste](/docs/pool-controller/security-checklist/)
- [Fehlerbehebung](/docs/troubleshooting/)

---

## So hängt alles zusammen

Sensoren und Relais hängen am ESP32-Pool-Controller, der per MQTT mit Ihrem Smart Home (Home Assistant, openHAB) spricht. Pinbelegung, Schaltplan und Datenfluss sind einmalig in der **[Architektur](/docs/architecture/)** dokumentiert — damit nichts auseinanderläuft.

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

## Fragen?

Häufige Fragen (Brauche ich Home Assistant? Was, wenn ich keine Solarheizung habe? Brauche ich einen Elektriker?) beantwortet die **[FAQ](/docs/faq/)**. Wenn etwas nicht funktioniert, hilft die **[Fehlerbehebung](/docs/troubleshooting/)**.

---

## Nächste Schritte

1. Wählen Sie oben einen Pfad und folgen Sie dem [Schnellstart](/docs/quickstart/) oder der ausführlichen [Bauanleitung](/docs/getting-started/)
2. Bestellen Sie die Teile laut [Stückliste](/docs/bom/)
3. Bauen Sie auf dem Steckbrett auf, testen Sie und arbeiten Sie die [Inbetriebnahme-Checkliste](/docs/checklist/) ab
4. Installieren Sie alles im Gehäuse
5. Binden Sie [Home Assistant](/docs/home-assistant-integration/) oder [openHAB](/docs/openhab-integration/) ein
6. Genießen Sie Ihren smarten Pool!

---

## Projektgeschichte

🏊 Smart Swimming Pool basiert auf einem [früheren Projekt](https://github.com/stritti/smart-swimming-pool), das noch nicht modular aufgebaut war und die gesamte Steuerlogik als openHAB-Regeln implementierte.

Die erste Version war im **Sommer 2018** im Einsatz und zeigte einige Schwächen:

- Die Steuerung der Pumpen über 433-MHz-Steckdosenschalter war unzuverlässig — ohne Rückmeldung war der tatsächliche Status unbekannt
- Die Schaltlogik lebte in openHAB-Regeln, was bei unzuverlässigem WLAN zu Problemen führte
- MQTT-Nachrichten verwendeten ein proprietäres Format

Aus diesen Erfahrungen entstand die überarbeitete Version des 🏊 Smart Swimming Pools: modular, widerstandsfähig und auf Standards basierend.
