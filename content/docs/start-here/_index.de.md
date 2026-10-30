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

**Hier starten**: [Pool-Controller — Von Null aufgebaut](/docs/components/pool-controller/build-from-zero/)

**Kosten:** ca. **35–55 €** für die Controller-Elektronik — Teile, Gehäuse und Netzverkabelung stehen in der [Stückliste](/docs/bom/).

---

### 🏊 Ich habe einen Standard-Pool mit Sandfilter und Solarheizung

**Ziel**: Vollautomation mit Zeitplan-Umwälzung und Solarheizungsregelung.

- Die [Von Null aufgebaut](/docs/components/pool-controller/build-from-zero/)-Anleitung befolgen
- **IP65-Gehäuse** für Wetterschutz verwenden
- Ordnungsgemäße **Netzspannungs-Verdrahtung** mit Sicherung und FI-Schutz
- **Home Assistant**-Integration für Dashboard und Automatisierung
- **MQTT** für zuverlässige Kommunikation

**Erforderliche Lektüre**:
- [Elektrische Sicherheit](/docs/components/pool-controller/electrical-safety/)
- [Produktions-Checkliste](/docs/components/pool-controller/production-checklist/)
- [Sicherheits-Checkliste](/docs/components/pool-controller/security-checklist/)

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
- [Von Null aufgebaut](/docs/components/pool-controller/build-from-zero/)
- [Elektrische Sicherheit](/docs/components/pool-controller/electrical-safety/)
- [Sicherheitsmodell](/docs/components/pool-controller/safety-model/)
- [Produktions-Checkliste](/docs/components/pool-controller/production-checklist/)
- [Sicherheits-Checkliste](/docs/components/pool-controller/security-checklist/)
- [Fehlerbehebung](/docs/troubleshooting/)

---

## So hängt alles zusammen

Sensoren und Relais hängen am ESP32-Pool-Controller, der per MQTT mit Ihrem Smart Home (Home Assistant, openHAB) spricht. Pinbelegung, Schaltplan und Datenfluss sind einmalig in der **[Architektur](/docs/architecture/)** dokumentiert — damit nichts auseinanderläuft.

---

## Fragen?

Häufige Fragen (Brauche ich Home Assistant? Was, wenn ich keine Solarheizung habe? Brauche ich einen Elektriker?) beantwortet die **[FAQ](/docs/faq/)**. Wenn etwas nicht funktioniert, hilft die **[Fehlerbehebung](/docs/troubleshooting/)**.

---

## Nächste Schritte

Wählen Sie einen Pfad, folgen Sie dem [Schnellstart](/docs/quickstart/) oder der [Bauanleitung](/docs/getting-started/), bestellen Sie die Teile laut [Stückliste](/docs/bom/), testen Sie auf dem Steckbrett, arbeiten Sie die [Inbetriebnahme-Checkliste](/docs/checklist/) ab, bauen Sie alles ins Gehäuse und binden Sie [Home Assistant](/docs/integrations/home-assistant/) oder [openHAB](/docs/integrations/openhab/) ein. Alle Repositories und Seiten im Überblick finden Sie in der [Dokumentation](/docs/).

Hintergrund zur Entstehung des Projekts: [Projektgeschichte](/docs/publications/#projektgeschichte).
