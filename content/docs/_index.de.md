---
title: Dokumentation
weight: 1
---

{{< safety-notice type="230v" >}}

# 🏊 Smart Swimming Pool Dokumentation

Alles, was Sie brauchen, um Ihre smarte Pool-Automatisierung zu bauen, anzubinden und zu warten. Die Seiten sind in der Reihenfolge gruppiert, in der Sie sie voraussichtlich brauchen — genau wie in der Seitenleiste.

Kern des Systems ist der **Pool Controller**, ein ESP32-basiertes Gerät, das:

- ✅ die Umwälzzeit zur Reinigung des Wassers automatisiert
- ✅ per Solarenergie heizt und eine zusätzliche Heizkreispumpe schaltet
- ✅ unabhängig von einem bestimmten Smart-Home-Server arbeitet und auch ohne WLAN weiterläuft
- ✅ per MQTT Discovery in Home Assistant eingebunden wird (openHAB über manuelle MQTT-Konfiguration)
- ✅ per Smartphone oder über die eingebaute Weboberfläche bedient werden kann

---

## 🧭 Orientierung

| Schritt | Was Sie vorhaben | Seiten |
|---------|----------------|--------|
| **1 · Start** | Bauweise wählen und ein erstes lauffähiges System aufbauen | [Hier starten](/docs/start-here/) · [Schnellstart](/docs/quickstart/) · [Bauanleitung](/docs/getting-started/) |
| **2 · Planen & Bauen** | System verstehen, Teile kaufen, sicher in Betrieb nehmen | [Architektur](/docs/architecture/) · [Stückliste](/docs/bom/) · [Inbetriebnahme-Checkliste](/docs/checklist/) |
| **3 · Komponenten** | Die einzelnen Module kennenlernen | [Pool Controller](/docs/pool-controller/) · [Pool Monitor](/docs/pool-monitor/) · [Grafana Dashboard](/docs/grafana-dashboard/) · [Water Quality Monitor](/docs/water-quality-monitor/) |
| **4 · Smart-Home-Integration** | Den Controller mit dem Smart Home verbinden | [Home Assistant](/docs/home-assistant-integration/) · [openHAB](/docs/openhab-integration/) · [openHAB Konfiguration](/docs/openhab-configuration/) |
| **5 · Betrieb & Support** | Etwas ist unklar, defekt oder muss aktualisiert werden | [FAQ](/docs/faq/) · [Fehlerbehebung](/docs/troubleshooting/) · [Upgrade & Migration](/docs/migration/) |
| **6 · Projekt** | Hintergrund, Mitmachen, Medien | [Diagramme mit Svgbob](/docs/diagrams/) · [Publikationen](/docs/publications/) · [Galerie](/docs/gallery/) |

**Neu hier?** Lesen Sie [Hier starten](/docs/start-here/) und folgen Sie dann entweder dem [Schnellstart](/docs/quickstart/) (60 Minuten, Steckbrett) oder der ausführlichen [Bauanleitung](/docs/getting-started/). Arbeiten Sie die [Inbetriebnahme-Checkliste](/docs/checklist/) ab, bevor Sie eine Pumpe an die Netzspannung anschließt.

---

## 📦 Module im Überblick

| Modul | Zweck | Schwierigkeit | Kosten |
|-------|-------|---------------|--------|
| **[Pool Controller](/docs/pool-controller/)** | Hauptsteuerlogik (erforderlich) | ⭐⭐ | ~35–55 € |
| **[Home Assistant Integration](/docs/home-assistant-integration/)** | Smart-Home-Dashboard | ⭐ | Kostenlos |
| **[openHAB Integration](/docs/openhab-integration/)** | Alternatives Smart Home | ⭐⭐ | Kostenlos |
| **[Pool Monitor](/docs/pool-monitor/)** | Kabelloses Temperaturdisplay | ⭐⭐ | ~20–40 € |
| **[Grafana Dashboard](/docs/grafana-dashboard/)** | Datenvisualisierung | ⭐ | Kostenlos |
| **[Water Quality Monitor](/docs/water-quality-monitor/)** | pH, Chlor und Temperatur (in Entwicklung) | ⭐⭐⭐ | offen |

Die Kosten des Controllers gelten nur für die Elektronik; die [Stückliste](/docs/bom/) enthält zusätzlich Gehäuse, Netzverkabelung und Werkzeug.

---

## 💬 Brauchen Sie Hilfe?

Schlagen Sie das Symptom in der [Fehlerbehebung](/docs/troubleshooting/) nach, lesen Sie die [FAQ](/docs/faq/) oder öffnen Sie ein [Issue](https://github.com/smart-swimmingpool/pool-controller/issues). Alle Projekt-Repositories finden Sie auf [GitHub](https://github.com/smart-swimmingpool).
