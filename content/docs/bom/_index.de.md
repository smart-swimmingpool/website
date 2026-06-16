---
title: Stückliste (BOM)
weight: 9
tags: ["docs", "bom", "hardware", "shopping-list"]
---

**🏊 Smart Swimming Pool: Vollständige Einkaufsliste mit Teilenummern, Preisen und Bezugstipps.**

Diese Stückliste (Bill of Materials / BOM) deckt alle Komponenten ab, die für den Bau des Pool-Controllers benötigt werden — inklusive Elektrik, Sensorik, Gehäuse und Werkzeug. Preisangaben sind Schätzwerte Stand 2026.

---

## 1. Controller-Elektronik

Diese Teile bilden den Kern des Pool-Controllers. Alle Komponenten sind Standard-Maker/Hobbyist-Artikel.

| # | Bauteil | Menge | Ca. Preis | Details | Beispiel-Quelle |
|---|---------|:-----:|:---------:|---------|-----------------|
| 1 | **ESP32 DevKit V1** (CP2102) | 1 | 10–15 € | 4MB Flash, CP2102 USB-Serial | Amazon, AZ-Delivery |
| 2 | **2-Kanal 5V Relais-Modul** | 1 | 5–8 € | Aktiv-Low, Optokopler-isoliert, HW-279/HW-316 | Amazon, eBay |
| 3 | **DS18B20 Temperatursensor** (wasserdicht) | 2 | 4–6 €/Stk | Edelstahlsonde, 1m Kabel, 3-adrig | Amazon, Reichelt |
| 4 | **4,7kΩ Widerstand** (¼W, ±5%) | 2 | 0,10 €/Stk | Metallschicht oder Kohleschicht | Reichelt, Pollin |
| 5 | **Breadboard** (830 Kontakte) | 1 | 3–5 € | Für Prototyping | Amazon, Reichelt |
| 6 | **Jumper-Kabel** (M-M, M-F) | 20+ | 3–5 € | Verschiedene Farben/Längen | Amazon |
| 7 | **USB-Netzteil** (5V, 1A+) | 1 | 5–10 € | Qualitätsmarke (Anker, Samsung, Apple) | Fachhandel |
| 8 | **USB-A auf Micro-USB Kabel** | 1 | 3–5 € | **Datenkabel** (kein reines Ladekabel) | Amazon |

| | **Zwischensumme (nur Controller)** | | **~35–55 €** | |
| | (Bestehende BOM = 45–75 € inkl. Gehäuse) | | | |

---

## 2. Gehäuse & Mechanik

Schützt die Elektronik vor Feuchtigkeit und mechanischen Beschädigungen.

| # | Bauteil | Menge | Ca. Preis | Details | Beispiel-Quelle |
|---|---------|:-----:|:---------:|---------|-----------------|
| 9 | **Hutschienengehäuse** (ABS, IP54+) | 1 | 8–15 € | Z.B. Fibox 4-Module, 100×75×105mm | Reichelt, Conrad |
| 10 | **Hutschiene** (35mm, 15cm) | 1 | 2–4 € | Gelochte Stahlschiene zur Montage | Reichelt |
| 11 | **PG7 Kabelverschraubung** (5–7mm Kabel) | 4–6 | 1–2 €/Stk | Für Sensorkabel und USB-Eingang | Amazon, Reichelt |
| 12 | **PG11 Kabelverschraubung** (8–10mm Kabel) | 1–2 | 1–2 €/Stk | Für Netzkabel-Eingang (falls 230V im Gehäuse) | Amazon, Reichelt |
| 13 | **Hutschienen-Halter** für ESP32 | 1 | 3–5 € | 3D-gedruckt optional; Kabelbinder gehen auch | Thingiverse |
| 14 | **Kabelbinder** (100mm, Sortiment) | 10+ | 2–3 € | Kabelmanagement im Gehäuse | Baumarkt |
| 15 | **Kabelbinder-Grundplatten** (klebend) | 5+ | 3–4 € | Auf Gehäuseinnenfläche kleben | Amazon |

| | **Zwischensumme (Gehäuse)** | | **~25–45 €** | |
| | *Nicht nötig bei reiner Breadboard-Nutzung im Innenbereich* | | | |

---

## 3. Elektroinstallation (230V)

Für den sicheren Anschluss der Relais an die Pumpen.

| # | Bauteil | Menge | Ca. Preis | Details | Hinweise |
|---|---------|:-----:|:---------:|---------|----------|
| 16 | **FI-Schutzschalter (RCD)** (30mA) | 1 | 20–35 € | 2-polig, 25A, 30mA Bemessungsfehlerstrom | **Vorgeschrieben** für 230V |
| 17 | **Leitungsschutzschalter (MCB)** (B10A oder B16A) | 1–2 | 5–10 €/Stk | Überstromschutz pro Pumpenstromkreis | Pro Pumpenkreis |
| 18 | **Dreiadriges Netzkabel** (NYM-J 3×1,5mm²) | 5–10m | 2–3 €/m | Für 230V-Verdrahtung zwischen Relais und Pumpen | Baumarkt |
| 19 | **Flexibles Steuerkabel** (LiYY 3×0,75mm²) | 2–3m | 1–2 €/m | Für Relais→Pumpe-Verbindung im Gehäuse | Reichelt |
| 20 | **Aderendhülsen** (0,75mm² und 1,5mm²) | 20+ | 3–5 € | Für feindrähtige Leiter an Schraubklemmen | Reichelt, Amazon |
| 21 | **Aderendhülsen-Crimper** | 1 | 8–15 € | Zum Verpressen der Hülsen | Reichelt, Amazon |
| 22 | **Hutschienen-Reihenklemmen** (2,5mm², grau) | 4–6 | 1–2 €/Stk | Zur Verdrahtungsverteilung im Gehäuse | Reichelt, Wago |
| 23 | **Hutschienen-Schutzklemme** (grün-gelb) | 2 | 2–3 €/Stk | Für PE-/Erdungsanschluss | Reichelt |
| 24 | **Endwinkel** für Reihenklemmen | 2 | 1 €/Stk | Fixieren der Klemmen auf der Hutschiene | Reichelt |
| 25 | **Aderkennzeichnungsringe** (nummeriert) | 1 Satz | 3–5 € | Zur Kabelfindung bei Wartung | Reichelt |
| 26 | **Zugentlastung** für Netzkabel | 2 | 2–4 €/Stk | Verhindert Zugbelastung der Klemmen | Baumarkt |

| | **Zwischensumme (Elektrik)** | | **~60–110 €** | |
| | *Vieles ist ggf. bereits im Verteilerkasten vorhanden* | | | |

---

## 4. Temperatursensor-Montage

Zusätzliches Material zur Montage der DS18B20-Sensoren an Rohren.

| # | Bauteil | Menge | Ca. Preis | Details | Hinweise |
|---|---------|:-----:|:---------:|---------|----------|
| 27 | **DS18B20 Edelstahlsonde** (9mm × 30mm) | 2 | 4–6 €/Stk | Bessere Qualität als Generic — nach "Sanitary" suchen | Reichelt, Amazon |
| 28 | **Sensor-Verlängerungskabel** (4-adrig, geschirmt) | 5–15m | 2–3 €/m | Zur Verlängerung; **geschirmte Twisted-Pair** bevorzugt | Reichelt |
| 29 | **Schrumpfschlauch** (Sortiment, 3:1) | 1 Satz | 3–5 € | Zum Abdichten von Kabelverbindungen | Amazon |
| 30 | **Kabelschellen** (für Rohrmontage) | 10+ | 2–3 € | Sensorkabel entlang Rohrleitungen fixieren | Baumarkt |
| 31 | **Wärmeleitpaste** (CPU-Paste) | 1 Tube | 3–5 € | Verbessert Wärmeübergang zwischen Sonde und Rohr | Reichelt |
| 32 | **Kabelverbindungsdose** (IP44+) | 1 | 3–5 € | Für Sensor-Verlängerungsverbindungen | Baumarkt |

| | **Zwischensumme (Sensormontage)** | | **~25–45 €** | |
| | *Stark abhängig von benötigten Kabellängen* | | | |

---

## 5. Werkzeug & Verbrauchsmaterial

Wichtige Werkzeuge für den Zusammenbau — nicht in den Controller-Kosten enthalten.

| # | Werkzeug | Ca. Preis | Erforderlich? | Hinweise |
|---|----------|:---------:|:-----------:|----------|
| 33 | **Digital-Multimeter** | 15–30 € | ✅ **Ja** | Muss Gleichspannung, Durchgang, Widerstand messen |
| 34 | **Abisolierzange** (automatisch) | 8–15 € | ✅ **Ja** | Zum Abisolieren von 0,75–2,5mm² Leitungen |
| 35 | **Schraubendreher-Satz** (Schlitz + Kreuz) | 5–10 € | ✅ Ja | Für Reihenklemmen und Hutschienen-Komponenten |
| 36 | **Lötkolben** (30W+) | 15–25 € | ⬜ Optional | Nur bei Sensor-Verlängerungen mit Löten |
| 37 | **Heißluftföhn** | 15–30 € | ⬜ Optional | Für Schrumpfschlauch |
| 38 | **Durchgangsprüfer** | 5–10 € | ⬜ Optional | Zur Überprüfung der Verdrahtung |

| | **Zwischensumme (Werkzeug)** | | **~60–100 €** | |
| | *Teilweise bereits im eigenen Werkstattbestand* | | | |

---

## Bestellreihenfolge

Wenn Sie alles auf einmal bestellen möchten, hier die Priorität:

1. **Must-have (ESP32, Relais, Sensoren, Widerstände, Breadboard, Netzteil)** — ~35 €
   → Reicht zum Flashen der Firmware und Testen der Sensoren
2. **Gehäuse + Verschraubungen + Hutschiene** — ~25 €
   → Für den dauerhaften Einbau
3. **Elektrik (FI, LS, Kabel, Klemmen)** — ~60 €
   → Nur falls der Verteilerkasten erweitert werden muss
4. **Sensor-Montage (Kabel, Schrumpfschlauch)** — ~25 €
   → Nur bei entfernten Sensor-Standorten

Sie können mit **Must-have-Teilen** (Kategorie 1) starten und später erweitern.

---

## Bezugstipps

| Artikel | Tipp |
|---------|------|
| **ESP32** | Bei AZ-Delivery (Deutschland) kaufen — bekannte Qualität, schneller Versand. "ESP32 WROOM" von No-Name-Verkäufern meiden. |
| **DS18B20** | Nach "DS18B20 sanitary sensor" suchen — bessere Abdichtung. Günstige (<2€) fallen oft nach 1–2 Saisons aus. |
| **Relais-Modul** | Auf **Optokopler-isoliert** und **Aktiv-Low** achten. HW-279 ist das zuverlässigste Modell. |
| **FI-Schutzschalter** | Von Hager, ABB, Schneider oder Siemens kaufen. No-Name-Sicherheitsschalter meiden. |
| **Kabel** | NYM-J für feste Installation, LiYY für flexible Innenverdrahtung. |
| **Widerstände** | 4,7kΩ, ¼W, ±5% — kosten 10 Cent. 10 Stück kaufen, Reserve haben. |

---

## Preiszusammenfassung

| Kategorie | Hauptkomponenten | Preisrahmen |
|-----------|-----------------|-------------|
| Controller-Elektronik | ESP32, Relais, Sensoren, Breadboard, Netzteil | **35–55 €** |
| Gehäuse & Mechanik | Gehäuse, Verschraubungen, Hutschiene, Befestigung | **25–45 €** |
| Elektrik (230V) | FI, LS, Kabel, Klemmen, Aderendhülsen | **60–110 €** |
| Sensor-Montage | Verlängerungskabel, Schrumpfschlauch, Verbindungsdose | **25–45 €** |
| Werkzeug | Multimeter, Abisolierzange, Schraubendreher | **60–100 €** |
| **Gesamt (nur Controller)** | Kategorien 1–2 | **60–100 €** |
| **Gesamt (komplette Installation)** | Kategorien 1–4 | **145–255 €** |
| **Inkl. Werkzeug** | Kategorien 1–5 | **205–355 €** |

> 💡 Die bestehende "Erste Schritte"-BOM schätzt **45–75 €** für die **Controller-Elektronik + Gehäuse** (Kategorien 1+2). Die erweiterte BOM oben ergänzt die **Elektroinstallation (230V)** und das **Sensor-Montagematerial**, die für eine reale Pool-Installation notwendig sind.
