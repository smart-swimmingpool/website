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
| **3 · Komponenten** | Die einzelnen Module kennenlernen | [Pool Controller](/docs/components/pool-controller/) · [Pool Monitor](/docs/components/pool-monitor/) · [Grafana Dashboard](/docs/components/grafana-dashboard/) · [Water Quality Monitor](/docs/components/water-quality-monitor/) |
| **4 · Smart-Home-Integration** | Den Controller mit dem Smart Home verbinden | [Home Assistant](/docs/integrations/home-assistant/) · [openHAB](/docs/integrations/openhab/) · [openHAB Konfiguration](/docs/integrations/openhab-configuration/) |
| **5 · Betrieb & Support** | Etwas ist unklar, defekt oder muss aktualisiert werden | [FAQ](/docs/faq/) · [Fehlerbehebung](/docs/troubleshooting/) · [Upgrade & Migration](/docs/migration/) |
| **6 · Projekt** | Hintergrund, Mitmachen, Medien | [Diagramme mit Svgbob](/docs/diagrams/) · [Publikationen](/docs/publications/) · [Galerie](/docs/gallery/) |

**Neu hier?** Lesen Sie [Hier starten](/docs/start-here/) und folgen Sie dann entweder dem [Schnellstart](/docs/quickstart/) (60 Minuten, Steckbrett) oder der ausführlichen [Bauanleitung](/docs/getting-started/). Arbeiten Sie die [Inbetriebnahme-Checkliste](/docs/checklist/) ab, bevor Sie eine Pumpe an die Netzspannung anschließt.

---

## 🗂️ Repositories

Details zu den Modulen (Zweck, Schwierigkeit, Kosten) stehen unter [Komponenten](/docs/components/) und [Smart-Home-Integration](/docs/integrations/). Die Kosten des Controllers gelten nur für die Elektronik; die [Stückliste](/docs/bom/) enthält zusätzlich Gehäuse, Netzverkabelung und Werkzeug.

| Repository | Zweck | Sprache |
|-----------|-------|---------|
| [pool-controller](https://github.com/smart-swimmingpool/pool-controller) | ESP32-Firmware, Web-UI, Hardware-Doku | C++ (PlatformIO) |
| [monitor](https://github.com/smart-swimmingpool/monitor) | Solarbetriebene Temperaturanzeige | C++ |
| [grafana-dashboard](https://github.com/smart-swimmingpool/grafana-dashboard) | Grafana-Dashboard-JSON | JSON |
| [water-quality-monitor](https://github.com/smart-swimmingpool/water-quality-monitor) | pH- und Chlor-Monitor (in Entwicklung) | — |
| [openhab-config](https://github.com/smart-swimmingpool/openhab-config) | openHAB-Konfiguration (Legacy) | openHAB DSL |
| [website](https://github.com/smart-swimmingpool/website) | Projekt-Website (Hugo) | Markdown, Hugo |

---

## 💬 Brauchen Sie Hilfe?

Schlagen Sie das Symptom in der [Fehlerbehebung](/docs/troubleshooting/) nach, lesen Sie die [FAQ](/docs/faq/) oder öffnen Sie ein [Issue](https://github.com/smart-swimmingpool/pool-controller/issues). Alle Projekt-Repositories finden Sie auf [GitHub](https://github.com/smart-swimmingpool).
