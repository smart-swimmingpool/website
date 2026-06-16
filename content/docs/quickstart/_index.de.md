---
title: Schnellstart
weight: 8
tags: ["docs", "getting-started", "quickstart", "tutorial"]
---

**🏊 Smart Swimming Pool: Vom Karton bis zum laufenden Pool in 60 Minuten.**

Dies ist der Express-Pfad — minimale Theorie, maximale Aktion. Führen Sie jeden Schritt genau aus, und Sie haben innerhalb einer Stunde einen funktionierenden Pool-Controller.

> 📖 Ausführliche Erklärungen im [Erste Schritte](/docs/getting-started/)-Handbuch.

---

## Was Sie brauchen

- ESP32 DevKit V1 + USB-Kabel (Datenkabel!)
- 2-Kanal 5V Relais-Modul (Aktiv-Low)
- 2× DS18B20 Temperatursensoren (wasserdicht)
- 2× 4,7kΩ Widerstände
- Breadboard + Jumper-Kabel
- 5V USB-Netzteil (1A+)
- Computer mit VS Code + PlatformIO
- MQTT-Broker im Netzwerk (optional für ersten Test)

**Alle Teile: ~45–75 €** — siehe [Stückliste (BOM)](/docs/bom/).

---

## Schritt 1: Verkabeln (5 Minuten)

### Breadboard-Aufbau

```
┌─────────────────────────────────────────┐
│  ESP32 DevKit                           │
│  ┌──────────────────────────────────────┤
│  │ USB    GND  5V  GPIO32  GPIO33  ... │
│  └──────────────────────────────────────┤
│           │    │    │       │           │
│           │    │    ├──4,7kΩ─┤ 3,3V    │
│           │    │    │       │           │
│  ─────────┤    │    │       │           │
│  DS18B20 #1   │    │   DS18B20 #2       │
│  (Solar)      │    │   (Pool)           │
└─────────────────────────────────────────┘
```

**Verbindungen:**

| Von | Nach | Farbe |
|-----|------|-------|
| ESP32 3,3V | DS18B20 #1 VDD (rot) | Rot |
| ESP32 3,3V | DS18B20 #2 VDD (rot) | Rot |
| ESP32 GND | DS18B20 #1 GND (schwarz) | Schwarz |
| ESP32 GND | DS18B20 #2 GND (schwarz) | Schwarz |
| ESP32 GPIO32 | DS18B20 #1 DATA (gelb) | Gelb |
| ESP32 GPIO33 | DS18B20 #2 DATA (gelb) | Gelb |
| GPIO32 → 3,3V | 4,7kΩ Pull-Up | — |
| GPIO33 → 3,3V | 4,7kΩ Pull-Up | — |
| ESP32 5V (VIN) | Relais-Modul VCC | Rot |
| ESP32 GND | Relais-Modul GND | Schwarz |
| ESP32 GPIO26 | Relais IN1 (Heizpumpe) | Blau |
| ESP32 GPIO25 | Relais IN2 (Filterpumpe) | Grün |

> ⚠️ **Doppelprüfung:** Relais VCC geht an **5V** (ESP32 VIN), NICHT an 3,3V.

---

## Schritt 2: Firmware flashen (10 Minuten)

1. VS Code mit PlatformIO-Erweiterung öffnen
2. Pool-Controller klonen und öffnen:
   ```bash
   git clone https://github.com/smart-swimmingpool/pool-controller.git
   cd pool-controller
   code .
   ```
3. ESP32 per USB verbinden
4. **Firmware hochladen:** PlatformIO-Fußleiste → **→ (Upload and Monitor)** neben `esp32dev`
5. **Dateisystem hochladen:** PlatformIO-Tab → `esp32dev` → **Platform → Upload Filesystem Image**
6. Auf Abschluss beider Uploads warten

**Erwartete Ausgabe (115200 Baud):**
```
[INFO] Pool Controller v3.x.x starting...
[INFO] WiFi: Starting in AP mode
[INFO] AP: 'Pool-Controller-Setup'. IP: 192.168.4.1
[INFO] OneWire: Found 2 DS18B20 sensor(s)
```

---

## Schritt 3: WLAN konfigurieren (3 Minuten)

1. Mit WLAN **`Pool-Controller-Setup`** verbinden (offen, kein Passwort)
2. Browser öffnen → **http://192.168.4.1**
3. WLAN-Name und Passwort des Heimnetzes eingeben
4. **Save** klicken — ESP32 startet neu und verbindet sich mit dem Heimnetz

---

## Schritt 4: MQTT verbinden (3 Minuten)

1. IP-Adresse des ESP32 im Router ermitteln (oder serielle Monitor-Ausgabe)
2. **http://<esp32-ip>/** im Browser öffnen
3. **Configuration → MQTT**
4. MQTT-Broker-Adresse eintragen (z.B. `192.168.1.100` oder `core-mosquitto`)
5. Bei Authentifizierung: Benutzername/Passwort eintragen
6. **Test Connection** — sollte "Connected" anzeigen
7. **Save** klicken

**Kein Broker?** [Mosquitto](https://mosquitto.org/download/) installieren oder das Mosquitto-Add-on in Home Assistant nutzen.

---

## Schritt 5: Sensoren prüfen (3 Minuten)

Weboberfläche **Status**-Seite prüfen:

| Sensor | Erwartet |
|--------|----------|
| **Pooltemperatur** | Plausible Raum-/Wassertemperatur (nicht -127°C) |
| **Solartemperatur** | Plausible Raum-/Wassertemperatur (nicht -127°C) |
| **Solar Sensor Found** | ✅ Ja |
| **Pool Sensor Found** | ✅ Ja |

**Anzeige -127°C?** Pull-Up-Widerstand und Datenleitung prüfen.

---

## Schritt 6: Relais testen (5 Minuten, OHNE 230V)

1. Webinterface **Control** → **Operation Mode** auf **`manu`** (Manuell)
2. Multimeter auf Gleichspannung einstellen
3. **Heating Pump** EIN schalten:
   - GPIO26 (Relais IN1) sollte **~0V (LOW)** anzeigen
4. EIN → AUS:
   - GPIO26 sollte wieder **~3,3V (HIGH)** anzeigen
5. Wiederholung für **Filter Pump** an GPIO25

**Spannungen vertauscht?** Relais ist Aktiv-High → Jumper (HIGH/LOW) am Modul suchen oder Modul ersetzen.

---

## Schritt 7: Pumpen anschließen (10 Minuten)

> ⚠️ **230V Netzspannung — Lebensgefahr.** Alle Sicherheitsvorkehrungen beachten.

1. **ESP32 vom USB trennen**
2. Relaisausgänge mit Pumpen-Schützen oder direkt mit Pumpen verdrahten
3. **FI-Schutzschalter** auf der 230V-Seite sicherstellen
4. ESP32 wieder an USB anschließen
5. **Operation Mode** auf **`manu`** (Manuell)
6. **Heating Pump** EIN — Pumpe läuft
7. AUS — Pumpe stoppt
8. Wiederholung für **Filter Pump**

---

## Schritt 8: Automatik aktivieren (2 Minuten)

1. **Operation Mode** auf **`auto`**
2. **Max. Pool Temp** auf Zieltemperatur (z.B. 28°C)
3. **Min. Solar Temp** (z.B. 35°C)
4. **Hysterese** (z.B. 2 K)

Der Controller arbeitet jetzt vollautomatisch.

---

## Schritt 9: Home Assistant verbinden (5 Minuten)

Falls Home Assistant genutzt wird:

1. **Einstellungen → Geräte & Dienste → Integration hinzufügen → MQTT**
2. `discovery: true` sicherstellen (Standard)
3. **Pool Controller** erscheint automatisch als neues Gerät
4. Entities zum Lovelace-Dashboard hinzufügen

Siehe [Home Assistant Integration](/docs/home-assistant-integration/) für Dashboard-Einrichtung und Automationsbeispiele.

---

## Fertig! 🎉

Ihr Pool-Controller ist betriebsbereit. Nächste Schritte:

- **[Grafana Dashboard](/docs/grafana-dashboard/)** für Temperaturverlauf einrichten
- **[Pool Monitor](/docs/pool-monitor/)** für kabelloses Display hinzufügen
- **[Inbetriebnahme-Checkliste](/docs/checklist/)** für ausführlichere Prüfung durchgehen
- **[FAQ & Fehlerbehebung](/docs/troubleshooting/)** bei Problemen

---

## Kurzreferenz: Pin-Belegung

| Komponente | ESP32 Pin |
|-----------|-----------|
| DS18B20 Solar (DATA) | GPIO32 |
| DS18B20 Pool (DATA) | GPIO33 |
| 4,7kΩ Pull-Up (pro Sensor) | DATA → 3,3V |
| Relais IN1 (Heizpumpe) | GPIO26 |
| Relais IN2 (Filterpumpe) | GPIO25 |
| Relais VCC | 5V (VIN) |
| Relais GND | GND |
| DS18B20 VDD | 3,3V |
| DS18B20 GND | GND |
