---
title: Dokumentation
weight: 1
---

{{< safety-notice type="230v" >}}

# \ud83c\udfca Smart Swimming Pool Dokumentation

Willkommen zur umfassenden Dokumentation des Smart Swimming Pool Projekts. Hier finden Sie alles, was Sie ben\u00f6tigen, um Ihr intelligentes Pool-Automatisierungssystem aufzubauen, zu konfigurieren und zu warten.

## \ud83d\ud87 Schnelle Navigation

### \ud83d\udc68 Neu bei Smart Swimming Pool?
Beginnen Sie hier, um das Projekt zu verstehen und Ihren Weg zu w\u00e4hlen:

- **[Hier beginnen](/docs/start-here/)** - W\u00e4hlen Sie Ihren Weg basierend auf Ihren Zielen und Ihrem Kenntnisstand
- **[Schnellstart](/docs/quickstart/)** - Von der Box zum funktionierenden Pool in 60 Minuten
- **[Erste Schritte](/docs/getting-started/)** - Detaillierte Schritt-f\u00fcr-Schritt-Anleitung

### \ud83c\udf9b Kernkomponenten

- **[Pool Controller](/docs/pool-controller/)** - Das Herz des Systems: ESP32-basierte zentrale Steuerlogik
- **[Home Assistant Integration](/docs/home-assistant-integration/)** - Automatische MQTT Discovery f\u00fcr nahtlose Integration
- **[openHAB Integration](/docs/openhab-integration/)** - Schritt-f\u00fcr-Schritt-Anleitung f\u00fcr openHAB-Benutzer
- **[Pool Monitor](/docs/pool-monitor/)** - Solarbetriebenes, kabelloses Temperaturdisplay
- **[Grafana Dashboard](/docs/grafana-dashboard/)** - Visualisieren Sie Ihre Pool-Daten mit sch\u00f6nen Diagrammen

### \ud83d\udda5 Systemdesign & Planung

- **[Architektur](/docs/architecture/)** - System\u00fcbersicht und Datenfluss
- **[St\u00fcckliste (BOM)](/docs/bom/)** - Vollst\u00e4ndige Einkaufsliste mit Preisen und Bezugsquellen
- **[Inbetriebnahme-Checkliste](/docs/checklist/)** - Pr\u00fcfliste vor dem ersten Einschalten

### \u26a0\ufe0f Fehlerbehebung & Support

- **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** - H\u00e4ufige Probleme und L\u00f6sungen
- **[Migrationsanleitung](/docs/migration/)** - Upgrade zwischen Firmware-Versionen
- **[Firmware-Migration](/docs/firmware-migration/)** - Migration von \u00e4lteren Versionen

---

## \ud83d\udcc Projekt\u00fcbersicht

Das **Smart Swimming Pool** Projekt ist ein modulares, Open-Source-System zur Automatisierung Ihres Swimmingpools. Das Kernmodul ist der **Pool Controller**, ein ESP32-basiertes Ger\u00e4t, das:

- \u2705 Die Zirkulationszeit zur Wasserreinigung automatisiert
- \u2705 Die Heizung mit Solarenergie steuert
- \u2705 Die Wassererw\u00e4rmung \u00fcber eine zus\u00e4tzliche Pumpe f\u00fcr den Heizkreislauf verwaltet
- \u2705 Unabh\u00e4ngig von bestimmten Smarthome-Servern funktioniert
- \u2705 Sich nahtlos mit Home Assistant \u00fcber MQTT Discovery integriert
- \u2705 Auch ohne dauerhafte WLAN-Verbindung funktioniert
- \u2705 \u00dcber Smartphone oder Hardware-Tasten bedient werden kann
- \u2705 Modular und erweiterbar ist

---

## \ud83d\udca1 Wie diese Dokumentation organisiert ist

### F\u00fcr Anf\u00e4nger
Wenn Sie neu im Projekt sind, folgen Sie diesem Pfad:

1. **[Hier beginnen](/docs/start-here/)** - Verstehen Sie die verschiedenen Wege, die Sie einschlagen k\u00f6nnen
2. **[Schnellstart](/docs/quickstart/)** oder **[Erste Schritte](/docs/getting-started/)** - Bauen Sie Ihren ersten Controller
3. **[Architektur](/docs/architecture/)** - Verstehen Sie, wie alles zusammenarbeitet

### F\u00fcr Fortgeschrittene
Wenn Sie bereits mit den Grundlagen vertraut sind:

1. **[Pool Controller](/docs/pool-controller/)** - Vertiefung in den Hauptcontroller
2. **[Home Assistant Integration](/docs/home-assistant-integration/)** - Fortgeschrittenes Dashboard und Automatisierung
3. **[openHAB Integration](/docs/openhab-integration/)** - Alternative Smarthome-Integration
4. **[Fehlerbehebung](/docs/troubleshooting/)** - L\u00f6sen Sie komplexe Probleme

### Referenzmaterialien
- **[St\u00fcckliste (BOM)](/docs/bom/)** - Vollst\u00e4ndige Teileliste
- **[Checkliste](/docs/checklist/)** - Sicherheits- und Inbetriebnahme-Checkliste
- **[FAQ](/docs/faq/)** - H\u00e4ufig gestellte Fragen

---

## \ud83d\udc82 Modul\u00fcbersicht

| Modul | Zweck | Schwierigkeitsgrad | Kosten |
|-------|-------|------------------|--------|
| **[Pool Controller](/docs/pool-controller/)** | Hauptsteuerlogik | \ud83d\udca1\ud83d\udca1 | ~30-75 \u20ac |
| **[Home Assistant Integration](/docs/home-assistant-integration/)** | Smarthome-Dashboard | \ud83d\udca1 | Kostenlos |
| **[Pool Monitor](/docs/pool-monitor/)** | Kabelloses Temperaturdisplay | \ud83d\udca1\ud83d\udca1 | ~20-40 \u20ac |
| **[Grafana Dashboard](/docs/grafana-dashboard/)** | Datenvisualisierung | \ud83d\udca1 | Kostenlos |
| **[openHAB Integration](/docs/openhab-integration/)** | Alternative Smarthome | \ud83d\udca1\ud83d\udca1 | Kostenlos |

---

## \ud83d\udcdd Brauchen Sie Hilfe?

- Pr\u00fcfen Sie die **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** Seite
- Besuchen Sie unsere **[GitHub Diskussionen](https://github.com/smart-swimmingpool/smart-swimmingpool/discussions)**
- Lesen Sie das **[Community Wiki](https://github.com/smart-swimmingpool/smart-swimmingpool/wiki)**
- \u00d6ffnen Sie ein **[Issue](https://github.com/smart-swimmingpool/smart-swimmingpool/issues)** f\u00fcr Bugs oder Feature-Anfragen

---

## \ud83c\udf88 N\u00e4chste Schritte

Bereit loszulegen? W\u00e4hlen Sie Ihren Weg:

- **[Hier beginnen](/docs/start-here/)** - Finden Sie den richtigen Weg f\u00fcr Ihre Bed\u00fcrfnisse
- **[Schnellstart](/docs/quickstart/)** - Schnellster Weg zum Laufen
- **[Erste Schritte](/docs/getting-started/)** - Umfassliche Aufbauanleitung
