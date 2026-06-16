---
title: Inbetriebnahme-Checkliste
weight: 11
tags: ["docs", "checklist", "safety", "commissioning"]
---

**🏊 Smart Swimming Pool: Schritt-für-Schritt-Checkliste für die erste Inbetriebnahme.**

Verwenden Sie diese Checkliste **bevor** Sie Pumpen an die Netzspannung anschließen. Haken Sie jeden Punkt ab, um einen sicheren und erfolgreichen ersten Start zu gewährleisten.

{{< safety-notice type="230v" >}}

---

## 1. Hardware-Aufbau

### 1.1 Controller-Elektronik

- [ ] ESP32 fest auf Breadboard oder Lochrasterplatine
- [ ] Relais-Modul angeschlossen: **VCC → 5V** (nicht 3,3V!), **GND → GND**
- [ ] Relais IN1 (GPIO26) vorbereitet für **Heizkreispumpe**
- [ ] Relais IN2 (GPIO25) vorbereitet für **Filter-/Umwälzpumpe**
- [ ] DS18B20 Solar-Sensor: **DATA → GPIO32**, **VDD → 3,3V**, **GND → GND**
- [ ] DS18B20 Pool-Sensor: **DATA → GPIO33**, **VDD → 3,3V**, **GND → GND**
- [ ] **4,7kΩ Pull-Up-Widerstand** zwischen jeder DATA-Leitung und 3,3V (insgesamt 2 Widerstände)
- [ ] Keine Kurzschlüsse zwischen benachbarten Pins auf dem Breadboard

### 1.2 Spannungsversorgung

- [ ] USB-Netzteil: **5V / 1A minimum** (Qualitätsmarke, kein Discounter-Handy-Ladegerät)
- [ ] USB-Kabel ist ein **Datenkabel** (kein reines Ladekabel)
- [ ] Netzteil steht **trocken** oder in IP-geschütztem Gehäuse

### 1.3 Gehäuse (falls verwendet)

- [ ] Gehäuse ist **IP54 oder besser** für Außen-/Gartenhaus-Installation
- [ ] PG-Verschraubungen für alle Kabeleinführungen installiert
- [ ] Belüftungsöffnungen, falls das Gehäuse Wärme staut
- [ ] Zugentlastung für alle Kabel am Gehäuseeingang

---

## 2. 230V / Netzspannungsseite

> ⚠️ **Lebensgefahr!** Arbeiten an 230V-Stromkreisen dürfen nur von qualifiziertem Fachpersonal durchgeführt werden. Beachten Sie die geltenden Elektrovorschriften.

- [ ] **FI-Schutzschalter (RCD)** in der Zuleitung installiert (vorgeschrieben!)
- [ ] **Leitungsschutzschalter (LS)** mit passender Auslösecharakteristik für jede Pumpe
- [ ] Kabelquerschnitt ausreichend für die Stromaufnahme der Pumpen
- [ ] Alle Verbindungen in einem **Verteilerkasten** oder einer Abzweigdose
- [ ] **Pumpen sind NOCH NICHT an die Relaisausgänge angeschlossen** — zuerst ohne 230V testen
- [ ] Falls vorhanden: 230V-Verdrahtung vor Pumpenanschluss mit Spannungsprüfer prüfen

---

## 3. Firmware & Erster Start

- [ ] PlatformIO-Projekt geöffnet, Umgebung auf **esp32dev** eingestellt
- [ ] Firmware erfolgreich hochgeladen: `pio run -e esp32dev -t upload`
- [ ] Dateisystem-Image hochgeladen: `pio run -e esp32dev -t uploadfs`
- [ ] Serielle Monitor-Ausgabe bei **115200 Baud**
- [ ] ESP32 startet im AP-Modus:
  ```
  [INFO] Pool Controller v3.x.x starting...
  [INFO] WiFi: Starting in AP mode
  [INFO] AP: 'Pool-Controller-Setup'. IP: 192.168.4.1
  ```

### 3.1 Wenn der Start fehlschlägt

| Symptom | Wahrscheinliche Ursache | Prüfung |
|---------|------------------------|---------|
| Keine Ausgabe im seriellen Monitor | Falsche Baudrate oder USB-Kabel | Monitor auf 115200 Baud; Daten-USB-Kabel versuchen |
| Dauerhafter Neustart | Netzteil zu schwach | 5V/1A+ Qualitätsnetzteil verwenden |
| `ets` Boot-Meldung, dann Neustart | Flash-Einstellungen falsch | DIO-Modus, 4MB Flash-Größe sicherstellen |
| "Failed to connect to ESP32" | Falscher COM-Port oder BOOT nicht gedrückt | BOOT-Taste während des Flash-Vorgangs halten |

---

## 4. Temperatursensoren

- [ ] Serielle Monitor-Ausgabe zeigt erkannte DS18B20-Sensoren:
  ```
  [INFO] OneWire: Found 2 DS18B20 sensor(s)
  [INFO] DS18B20[0]: 28-xxxxxxxxxxxx (Solar sensor on GPIO32)
  [INFO] DS18B20[1]: 28-yyyyyyyyyyyy (Pool sensor on GPIO33)
  ```
- [ ] Beide Sensoren zeigen plausible Temperaturen (nicht `-127°C` oder `85°C`)
- [ ] Einen Sensor erwärmen (Hand drauf) — Wert steigt innerhalb weniger Sekunden
- [ ] Wenn nur 1 Sensor gefunden: Verkabelung, Pull-Up-Widerstand prüfen oder Sensor einzeln testen

### 4.1 Temperatursensor-Schnellprüfung

| Anzeige | Bedeutung | Maßnahme |
|---------|-----------|----------|
| `-127°C` | Sensor nicht auf dem Bus gefunden | DATA-Leitung, Pull-Up, GPIO-Pin prüfen |
| `85°C` | Sensor im Power-On-Standard | Parasite-Power prüfen; alle 3 Adern müssen angeschlossen sein |
| Sprunghafte Werte | Elektrische Störungen | Sensorkabel >30cm von 230V-Leitungen verlegen |
| Beide Sensoren identisch | Normal bei gleicher Wassertemperatur | Mit Hand-Wärmetest überprüfen (siehe oben) |

---

## 5. WLAN & Netzwerk

- [ ] Mit WLAN-Netzwerk `Pool-Controller-Setup` verbunden
- [ ] Weboberfläche erreichbar unter **http://192.168.4.1**
- [ ] Heim-WLAN in der Weboberfläche konfiguriert → **Connection**
- [ ] ESP32 neu gestartet und mit Heimnetz verbunden
- [ ] Neue IP-Adresse notiert (Router-DHCP oder serielle Monitor-Ausgabe)
- [ ] Weboberfläche erreichbar unter **http://<neue-ip>/**
- [ ] ESP32 per Ping erreichbar: `ping <neue-ip>`

---

## 6. MQTT-Verbindung

### Voraussetzungen

- [ ] MQTT-Broker (Mosquitto) installiert und läuft
- [ ] Broker vom Netzwerk des ESP32 aus erreichbar (gleiches Subnetz oder Firewall-Regel für Port 1883)
- [ ] Bei Authentifizierung: Benutzername/Passwort notiert

### Konfiguration

- [ ] Weboberfläche → **Configuration → MQTT**:
  - [ ] Broker-Adresse eingetragen
  - [ ] Port korrekt (Standard: `1883`)
  - [ ] Zugangsdaten eingetragen (falls erforderlich)
- [ ] **Test Connection** klicken — Ergebnis zeigt **"Connected"**
- [ ] **Save** klicken — Controller startet MQTT-Verbindung neu

### Überprüfung

- [ ) Alle Topics auf dem Broker abonnieren:
  ```bash
  mosquitto_sub -h <broker-ip> -t "#" -v
  ```
- [ ] Pool-Controller-Topics erscheinen (Prefix `homeassistant/` oder `homie/`)
- [ ] Sensorwerte aktualisieren sich regelmäßig
- [ ] Wenn Topics fehlen: `homeassistant`-Prefix in der HA-Konfiguration prüfen

---

## 7. Funktionstest (Ohne 230V)

Bevor Sie Pumpen anschließen, testen Sie, ob der Controller die Relais schalten kann.

- [ ] **Multimeter bereit**, auf Gleichspannungsmessung eingestellt
- [ ] Spannung zwischen Relais-IN1-Pin und GND messen:
  - Weboberfläche zeigt Relais **AUS** → IN1 zeigt **~3,3V (HIGH)**
  - Weboberfläche zeigt Relais **EIN** → IN1 zeigt **~0V (LOW)**
- [ ] Wiederholung für Relais IN2 — gleiches Verhalten
- [ ] Bei umgekehrten Spannungen: Relais-Modul ist **Aktiv-High** — Jumper suchen (HIGH/LOW) oder Modul ersetzen

### Relais-Test nach GPIO

| GPIO | Erwartet AUS | Erwartet EIN | Steuert |
|------|-------------|-------------|---------|
| GPIO26 (IN1) | ~3,3V (HIGH) | ~0V (LOW) | Heizpumpe (noch nicht angeschlossen) |
| GPIO25 (IN2) | ~3,3V (HIGH) | ~0V (LOW) | Filterpumpe (noch nicht angeschlossen) |

---

## 8. Home Assistant Integration (Optional)

- [ ] MQTT-Integration in Home Assistant konfiguriert (Einstellungen → Geräte & Dienste → MQTT)
- [ ] Discovery aktiviert: `discovery: true` in der HA `configuration.yaml`
- [ ] Pool Controller erscheint als Gerät unter **Einstellungen → Geräte & Dienste → Geräte**
- [ ] Alle Entities sichtbar und melden Werte:
  - `sensor.pool_controller_pool_temp` — Pooltemperatur
  - `sensor.pool_controller_solar_temp` — Solartemperatur
  - `select.pool_controller_mode` — Betriebsmodus
  - `switch.pool_controller_pool_pump` — Pumpensteuerung
  - `switch.pool_controller_solar_pump` — Solarpumpensteuerung
- [ ] **Betriebsmodus** kann via HA geändert werden (auf `manu` und zurück auf `auto` schalten)

---

## 9. Erster echter Test (Mit Pumpen)

Erst fortfahren, wenn alle vorherigen Schritte bestanden sind.

- [ ] **ESP32 vom USB-Netz trennen**
- [ ] Relaisausgänge mit den Pumpen-Schützen oder direkt mit den Pumpen verdrahten (230V-Seite)
- [ ] Doppelprüfung: Relais COM (Common) und NO (Normally Open) korrekt angeschlossen
- [ ] ESP32 wieder an USB-Netz anschließen
- [ ] Betriebsmodus auf **Manuell (`manu`)** via Weboberfläche stellen
- [ ] **Heizpumpe** via Weboberfläche EIN schalten — Pumpe läuft
- [ ] **Heizpumpe** AUS schalten — Pumpe stoppt
- [ ] **Filterpumpe** EIN schalten — Pumpe läuft
- [ ] **Filterpumpe** AUS schalten — Pumpe stoppt
- [ ] Wenn Pumpe nicht startet: 230V-Verkabelung, Leitungsschutz, FI prüfen
- [ ] Wenn Pumpe nicht stoppt: Relais-Kontakte könnten verschweißt sein — sofort 230V trennen

---

## 10. Automatik-Test

- [ ] Betriebsmodus auf **Auto** stellen
- [ ] Prüfen, ob der Controller die Pumpen gemäß Heizlogik schaltet
- [ ] Solartemperatur > Pooltemperatur + Hysterese → Heizpumpe sollte EIN schalten
- [ ] Pooltemperatur erreicht max. eingestellte Temperatur → Heizpumpe sollte AUS schalten
- [ ] Filter-/Umwälzpumpe läuft gemäß Zeitplan (Timer oder temperaturbasiert)

---

## 11. Abschlussprüfung

- [ ] Temperaturdifferenz zwischen Solar- und Pool-Sensor plausibel
- [ ] Controller bleibt 24+ Stunden stabil ohne unerwartete Neustarts
- [ ] WLAN-Verbindung bleibt stabil (RSSI in Diagnose prüfen)
- [ ] MQTT-Verbindung bleibt bestehen (Verfügbarkeits-Topic: sollte `online` zeigen)
- [ ] Home Assistant (falls verwendet) zeigt korrekte und aktuelle Werte

---

## Kurzreferenz

Druckbare Kurzfassung für den Einsatz vor Ort:

```
☐ ESP32: 5V USB-Strom, Datenkabel
☐ Relais VCC → 5V, GND → GND
☐ Relais IN1 → GPIO26 (Heizung)
☐ Relais IN2 → GPIO25 (Filter)
☐ DS18B20 #1: GPIO32 + 4,7kΩ Pull-Up
☐ DS18B20 #2: GPIO33 + 4,7kΩ Pull-Up
☐ FI-Schutzschalter auf 230V-Seite
☐ Firmware + Dateisystem geflasht
☐ WLAN konfiguriert, Web-UI erreichbar
☐ MQTT-Testverbindung erfolgreich
☐ Relais-Spannungen korrekt (3,3V AUS / 0V EIN)
☐ Manueller Pumpentest (ohne 230V Automatik)
```
