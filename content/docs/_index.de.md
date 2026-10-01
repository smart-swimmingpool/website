---
title: Dokumentation
weight: 1
---

{{< safety-notice type="230v" >}}

# 🏊 Smart Swimming Pool Dokumentation

Willkommen zur umfassenden Dokumentation des Smart Swimming Pool Projekts. Hier finden Sie alles, was Sie benötigen, um Ihr intelligentes Pool-Automatisierungssystem aufzubauen, zu konfigurieren und zu warten.

## 🧭 Schnelle Navigation

### 👋 Neu bei Smart Swimming Pool?

Beginnen Sie hier, um das Projekt zu verstehen und Ihren Weg zu wählen:

- **[Hier beginnen](/docs/start-here/)** - Wählen Sie Ihren Weg basierend auf Ihren Zielen und Ihrem Kenntnisstand
- **[Schnellstart](/docs/quickstart/)** - Von der Box zum funktionierenden Pool in 60 Minuten
- **[Erste Schritte](/docs/getting-started/)** - Detaillierte Schritt-für-Schritt-Anleitung

### 🧩 Kernkomponenten

- **[Pool Controller](/docs/pool-controller/)** - Das Herz des Systems: ESP32-basierte zentrale Steuerlogik
- **[Home Assistant Integration](/docs/home-assistant-integration/)** - Automatische MQTT Discovery für nahtlose Integration
- **[openHAB Integration](/docs/openhab-integration/)** - Schritt-für-Schritt-Anleitung für openHAB-Benutzer
- **[Pool Monitor](/docs/pool-monitor/)** - Solarbetriebenes, kabelloses Temperaturdisplay
- **[Grafana Dashboard](/docs/grafana-dashboard/)** - Visualisieren Sie Ihre Pool-Daten mit schönen Diagrammen
- **[Water Quality Monitor](/docs/water-quality-monitor/)** - Messung von pH-Wert und Chlor (in Entwicklung)

### 🗺️ Systemdesign & Planung

- **[Architektur](/docs/architecture/)** - Systemübersicht und Datenfluss
- **[Stückliste (BOM)](/docs/bom/)** - Vollständige Einkaufsliste mit Preisen und Bezugsquellen
- **[Inbetriebnahme-Checkliste](/docs/checklist/)** - Prüfliste vor dem ersten Einschalten

### ⚠️ Fehlerbehebung & Support

- **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** - Häufige Probleme und Lösungen
- **[Migrationsanleitung](/docs/migration/)** - Upgrade zwischen Firmware-Versionen
- **[Firmware-Migration](/docs/firmware-migration/)** - Migration von älteren Versionen

---

## 📋 Projektübersicht

Das **Smart Swimming Pool** Projekt ist ein modulares, Open-Source-System zur Automatisierung Ihres Swimmingpools. Das Kernmodul ist der **Pool Controller**, ein ESP32-basiertes Gerät, das:

- ✅ Die Zirkulationszeit zur Wasserreinigung automatisiert
- ✅ Die Heizung mit Solarenergie steuert
- ✅ Die Wassererwärmung über eine zusätzliche Pumpe für den Heizkreislauf verwaltet
- ✅ Unabhängig von bestimmten Smarthome-Servern funktioniert
- ✅ Sich nahtlos mit Home Assistant über MQTT Discovery integriert
- ✅ Auch ohne dauerhafte WLAN-Verbindung funktioniert
- ✅ Über Smartphone oder Hardware-Tasten bedient werden kann
- ✅ Modular und erweiterbar ist

---

## 💡 Wie diese Dokumentation organisiert ist

### Für Anfänger

Wenn Sie neu im Projekt sind, folgen Sie diesem Pfad:

1. **[Hier beginnen](/docs/start-here/)** - Verstehen Sie die verschiedenen Wege, die Sie einschlagen können
2. **[Schnellstart](/docs/quickstart/)** oder **[Erste Schritte](/docs/getting-started/)** - Bauen Sie Ihren ersten Controller
3. **[Architektur](/docs/architecture/)** - Verstehen Sie, wie alles zusammenarbeitet

### Für Fortgeschrittene

Wenn Sie bereits mit den Grundlagen vertraut sind:

1. **[Pool Controller](/docs/pool-controller/)** - Vertiefung in den Hauptcontroller
2. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Fortgeschrittenes Dashboard und Automatisierung
3. **[openHAB Integration](/docs/openhab-integration/)** - Alternative Smarthome-Integration
4. **[Fehlerbehebung](/docs/troubleshooting/)** - Lösen Sie komplexe Probleme

### Referenzmaterialien

- **[Stückliste (BOM)](/docs/bom/)** - Vollständige Teileliste
- **[Checkliste](/docs/checklist/)** - Sicherheits- und Inbetriebnahme-Checkliste
- **[FAQ](/docs/faq/)** - Häufig gestellte Fragen

---

## 📦 Modulübersicht

| Modul | Zweck | Schwierigkeitsgrad | Kosten |
|-------|-------|------------------|--------|
| **[Pool Controller](/docs/pool-controller/)** | Hauptsteuerlogik | ⭐⭐ | ~30-75 € |
| **[Home Assistant Integration](/docs/home-assistant-integration/)** | Smarthome-Dashboard | ⭐ | Kostenlos |
| **[Pool Monitor](/docs/pool-monitor/)** | Kabelloses Temperaturdisplay | ⭐⭐ | ~20-40 € |
| **[Grafana Dashboard](/docs/grafana-dashboard/)** | Datenvisualisierung | ⭐ | Kostenlos |
| **[openHAB Integration](/docs/openhab-integration/)** | Alternative Smarthome | ⭐⭐ | Kostenlos |
| **[Water Quality Monitor](/docs/water-quality-monitor/)** | pH, Chlor und Temperatur (in Entwicklung) | ⭐⭐⭐ | offen |

---

## 💬 Brauchen Sie Hilfe?

- Prüfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Lesen Sie die **[FAQ](/docs/faq/)**
- Öffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/pool-controller/issues)** für Fragen, Bugs oder Feature-Anfragen
- Alle **[Projekt-Repositories](https://github.com/smart-swimmingpool)** auf GitHub ansehen

---

## 🚀 Nächste Schritte

Bereit loszulegen? Wählen Sie Ihren Weg:

- **[Hier beginnen](/docs/start-here/)** - Finden Sie den richtigen Weg für Ihre Bedürfnisse
- **[Schnellstart](/docs/quickstart/)** - Schnellster Weg zum Laufen
- **[Erste Schritte](/docs/getting-started/)** - Umfassliche Aufbauanleitung
