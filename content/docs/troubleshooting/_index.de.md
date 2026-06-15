---
title: FAQ & Fehlerbehebung
weight: 30
tags: ["docs", "faq", "troubleshooting"]
---

**🏊 Häufig gestellte Fragen und Lösungen für typische Probleme.**

{{< safety-notice type="230v" >}}

## Relais-Probleme

### Relais-Modul schaltet nicht / Pumpe verhält sich unerwartet

**Wahrscheinliche Ursache:** Die Polarität des Relais-Moduls passt nicht zur Firmware.

Die Pool-Controller-Firmware steuert die Relais **Aktiv-Low** (GPIO **LOW** = Relais EIN, GPIO **HIGH** = Relais AUS). Dies entspricht der überwiegenden Mehrheit gängiger 2-Kanal-5V-Relais-Module.

**Lösung:**
1. **Wenn Ihr Relais normal funktioniert:** Sie haben ein Standard-**Aktiv-Low**-Modul — alles in Ordnung.
2. **Wenn das Relais dauerhaft ein- oder ausgeschaltet ist:** Möglicherweise ist Ihr Modul **Aktiv-High** (GPIO HIGH = Relais EIN).
   - Suchen Sie nach einem Jumper mit der Bezeichnung "HIGH/LOW" und stellen Sie ihn auf **LOW**.
   - Ohne Jumper müssen Sie das Modul möglicherweise durch ein standard Aktiv-Low-Modul ersetzen (~5€).

**Schnelltest:** Messen Sie bei eingeschaltetem ESP32 (ohne angeschlossene Pumpen!) die Spannung zwischen Relais-IN-Pin und GND:
- Bei AUS (Weboberfläche zeigt AUS): Pin sollte **~3,3V** (HIGH) anzeigen
- Bei EIN (Weboberfläche zeigt EIN): Pin sollte **~0V** (LOW) anzeigen
- Bei umgekehrtem Verhalten ist Ihr Modul Aktiv-High.

### Relais klickt, aber Pumpe startet nicht

- Die Relais-Kontakte sind möglicherweise für geringere Ströme ausgelegt als Ihre Pumpe zieht.
- Prüfen Sie die Pumpenleistung: Ein 10A-Relais ist für die meisten Umwälzpumpen ausreichend. Verwenden Sie für größere Pumpen das Relais zur Ansteuerung eines Schützes.

### Welche Relais-Module sind kompatibel?

Bestätigt funktionierende Module (Aktiv-Low, Optokopler-isoliert):
- **HW-279 / HW-316** 2-Kanal-5V-Relais-Modul
- **SRD-05VDC-SL-C** basierte Module
- Die meisten generischen 2-Kanal-5V-Relaisplatinen mit Optokopler (Jumper auf **LOW** prüfen)

Vermeiden Sie: Module ohne Optokopler-Isolation (einzeltransistor-getrieben) — diese können die ESP32-GPIO-Pins beschädigen.

---

## Temperatursensor-Probleme

### DS18B20 wird nicht erkannt / zeigt -127°C oder 85°C

**Wahrscheinliche Ursache:** Verdrahtungsproblem oder fehlender Pull-Up-Widerstand.

**Diagnose:**
- `-127°C` = Sensor nicht auf dem OneWire-Bus gefunden (keine Kommunikation)
- `85°C` = Sensor gefunden, aber im Power-On-Standard hängend (Parasite-Power-Problem)

**Lösungen:**
1. **Pull-Up-Widerstand prüfen:** Ein **4,7kΩ-Widerstand** MUSS zwischen DATA (gelb/weiß) und 3,3V (rot) liegen. Ohne diesen funktioniert OneWire nicht.
2. **Verdrahtung prüfen (esp32dev-Konfiguration verwendet getrennte Pins):**
   - Rot → 3,3V (ESP32)
   - Schwarz → GND (ESP32)
   - Solar-Sensor DATA → **GPIO32** (Gelb/Weiß)
   - Pool-Sensor DATA → **GPIO33** (Gelb/Weiß)
3. **Einen Sensor nach dem anderen testen**, um einen defekten Sensor oder ein defektes Kabel zu identifizieren.
4. **Kabellänge prüfen:** DS18B20 funktioniert zuverlässig bis ~30m mit 4,7kΩ Pull-Up. Für längere Strecken einen niedrigeren Wert (z. B. 2,2kΩ) oder geschirmte Twisted-Pair-Kabel verwenden.
5. **Parasite-Power-Modus vermeiden:** Die Firmware verwendet externen Strommodus (3 Adern). Stellen Sie sicher, dass beide Sensoren mit allen 3 Adern angeschlossen sind.

### Temperaturwerte sind offensichtlich falsch (z. B. 120°C bei 25°C Pool)

- **Störungen:** Das Sensorkabel verläuft möglicherweise zu nah an 230V-Kabeln. Verlegen Sie das Sensorkabel mindestens 30cm entfernt von Netzleitung.
- **Defekter Sensor:** Sensor ersetzen — kosten ~3€.
- **Feuchtigkeit:** Wenn die Edelstahlsonde nicht vollständig eingetaucht ist oder das Kabelende nass ist, können die Werte unplausibel sein. Trocknen lassen und mit Schrumpfschlauch abdichten.

### Beide Sensoren zeigen dieselbe Temperatur

Das ist normal, wenn sie im Wasser auf gleicher Temperatur liegen. Zur Überprüfung:
1. Nehmen Sie einen Sensor in die Hand — der Wert sollte innerhalb weniger Sekunden steigen.
2. Halten Sie den anderen in kaltes Wasser — der Wert sollte fallen.

---

## WLAN- & Netzwerk-Probleme

### ESP32 erscheint nicht in der WLAN-Liste nach dem Flashen

**Lösung:**
1. Der ESP32 startet beim ersten Boot im **AP-Modus** (Netzwerkname: **`Pool-Controller-Setup`**).
2. Wenn Sie ihn nicht sehen, prüfen Sie die serielle Monitor-Ausgabe (115200 Baud).
3. Der ESP32 wurde möglicherweise bereits für Ihr Heim-WLAN konfiguriert — zurücksetzen auf Werkseinstellungen:
   - Per seriellem Monitor verbinden
   - Befehl `reset` senden
   - Oder BOOT-Taste für 10 Sekunden beim Einschalten gedrückt halten

### ESP32 verbindet sich mit WLAN, ist aber nicht erreichbar

1. Prüfen Sie die DHCP-Client-Liste Ihres Routers auf die IP-Adresse des ESP32.
2. Versuchen Sie `ping <esp32-ip>` von Ihrem Computer.
3. Wenn der ESP32 in einem anderen VLAN/Subnetz ist, stellen Sie sicher, dass MQTT-Traffic erlaubt ist.
4. Starten Sie Router und ESP32 neu.

### WLAN-Verbindung bricht häufig ab

- Die WLAN-Reichweite des ESP32 ist begrenzt. Halten Sie ihn innerhalb von 15m Ihres Access Points.
- Bei weiter Entfernung: WLAN-Repeater oder kabelgebundene Verbindung (ESP32 kann mit LAN8720-Modul Ethernet nutzen – nicht im Standard-Firmware-Umfang).

---

## MQTT-Probleme

### Controller erscheint nicht in Home Assistant

**Voraussetzungen:**
1. Home Assistant muss die **MQTT-Integration** konfiguriert haben (Einstellungen → Geräte & Dienste → Integration hinzufügen → MQTT).
2. Der Pool Controller muss mit **demselben MQTT-Broker** verbunden sein.

**Fehlersuche:**
1. Öffnen Sie die Weboberfläche des Pool Controllers → **Konfiguration → MQTT**.
2. Überprüfen Sie Broker-Adresse, Port (Standard: 1883) und Zugangsdaten.
3. Klicken Sie auf **Verbindung testen** — Sie sollten "Verbunden" oder eine Fehlermeldung sehen.
4. Prüfen Sie die Home Assistant-Logs: Suchen Sie nach `MQTT` oder `pool`.
5. Testen Sie MQTT manuell:
   ```bash
   mosquitto_pub -h <broker-ip> -t "test" -m "hallo"
   mosquitto_sub -h <broker-ip> -t "#" -v  # sollte pool-Themen zeigen
   ```

### MQTT-Nachrichten werden gesendet, aber Home Assistant zeigt "unbekannte" Entitäten

- Der Controller verwendet **Home Assistant MQTT Discovery** (automatische Entity-Erstellung).
- Wenn Entitäten "unbekannt" anzeigen, erreicht das Discovery-Thema möglicherweise HA nicht.
- Prüfen Sie, ob das MQTT-Präfix in Ihrer Home Assistant MQTT-Integration mit dem des Controllers übereinstimmt (Standard ist `homeassistant`).

### MQTT verbindet nicht / Verbindung abgelehnt

- Stellen Sie sicher, dass der MQTT-Broker läuft: `systemctl status mosquitto` (Linux) oder prüfen Sie den Home Assistant Add-on-Status.
- Prüfen Sie die Firewall-Regeln: Port 1883 (TCP) muss zwischen ESP32 und Broker offen sein.
- Bei Authentifizierung: Benutzername und Passwort in der MQTT-Konfiguration des Controllers prüfen.

---

## ESP32- & Firmware-Probleme

### ESP32 startet nicht / startet ständig neu

**Serielle Monitor-Ausgabe:**
```
ets Jun  8 2016 00:22:57
rst:0xc (SW_CPU_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
```

**Lösungen:**
1. **Stromversorgung prüfen:** ESP32 benötigt eine stabile 5V-Versorgung. USB-Ports an Computern oder günstige Handynetzteile liefern oft nicht genug Strom (>500mA). Verwenden Sie ein qualitativ hochwertiges 5V/1A+ Netzteil.
2. **Falsche Flash-Einstellungen:** In Arduino IDE oder PlatformIO sicherstellen:
   - Flash Mode: **DIO** (nicht QIO)
   - Flash Size: **4MB** (oder entsprechend Ihrem Board)
   - Partition Scheme: **Default 4MB with spiffs**
3. **Schlechtes USB-Kabel:** Manche Kabel sind reine Ladekabel (keine Datenleitungen). Verwenden Sie ein bekannt gutes Datenkabel.
4. Wenn das Booten mit USB am Computer funktioniert, aber nicht mit einem separaten Netzteil, ist das Netzteil wahrscheinlich zu schwach.

### "A fatal error occurred: Failed to connect to ESP32" beim Flashen

1. Halten Sie die **BOOT**-Taste am ESP32, klicken Sie in der IDE auf **Upload**, lassen Sie BOOT los, sobald das Flashen beginnt.
2. Prüfen Sie, ob der richtige COM-Port ausgewählt ist.
3. Versuchen Sie ein anderes USB-Kabel (Datenkabel, kein reines Ladekabel).
4. Bei CP210x-basierten Boards: Treiber installieren/neu installieren.

### Serieller Monitor zeigt Zeichensalat

- Falsche Baudrate — stellen Sie sie auf **115200** ein.
- Falsche Spannung — ESP32 arbeitet mit 3,3V. Wenn Sie ihn an einen Arduino Uno angeschlossen haben, könnte die serielle Schnittstelle beschädigt sein.

---

## Allgemein & Hardware

### Das System hat mehr als 100€ gekostet — ist das normal?

Die Schätzung von **~45–75€** umfasst **nur die Controller-Elektronik** (ESP32, Sensoren, Relais, Breadboard, Gehäuse). Nicht enthalten sind:
- Poolpumpe und Filtersystem
- Heizkreispumpe
- Wärmetauscher-Installation
- Verdrahtungsmaterial (Kabel, Steckverbinder, Sicherungen)

Wenn diese Komponenten hinzukommen, können die Gesamtkosten deutlich höher sein.

### Kann ich das ohne Smart-Home-Server nutzen?

**Ja.** Der Pool Controller ist vollständig autark:
- Er übernimmt Zirkulationssteuerung und Heizungsregelung **ohne** externen Server.
- Die Weboberfläche erlaubt grundlegende Konfiguration und manuelle Steuerung.
- MQTT-Integration und Home Assistant sind optional — sie erweitern um Fernsteuerung, Automatisierung und Visualisierung.

### Wie wetterfest ist das System?

Der Pool Controller selbst ist **nicht wetterfest** im Auslieferungszustand. Sie benötigen:

| Standort | Schutz |
|----------|--------|
| Inneninstallation (bevorzugt) | Kein besonderer Schutz nötig |
| Außen / Gartenhaus | **IP54+**-Gehäuse, Kabelverschraubungen für alle Eingänge |
| Sensoren (DS18B20) | Edelstahlsonde ist IP68 — Kabeleinführung muss abgedichtet sein |
| Netzteil | Muss trocken stehen oder in IP-geschütztem Gehäuse |

### Kann ich das mit einer Wärmepumpe statt Solarheizung nutzen?

Ja. Die Heizungslogik des Pool Controllers schaltet eine Pumpe bei Heizbedarf. Das funktioniert mit jeder Wärmequelle:
- Solarthermie-Anlage
- Wärmepumpe
- Gas-/Ölheizung mit Wärmetauscher
- Elektro-Heizelement (über Relais/Schütz)

### Welche Pumpen können gesteuert werden?

Das Relais-Modul schaltet 230V/10A max (ohmsche Last). Bei induktiven Lasten (Motoren, Pumpen) mit ~5A. Verwenden Sie für größere Pumpen das Relais zur Ansteuerung eines Schützes.

### Ist dieses Projekt CE-/UL-zertifiziert?

**Nein.** Dies ist ein Hobby-DIY-Projekt. Es wurde von keiner Aufsichtsbehörde geprüft oder zertifiziert. Sie bauen und betreiben es auf eigene Gefahr. Verwenden Sie immer einen **RCD (FI-Schutzschalter)** beim Anschluss an die Netzspannung.

{{< safety-notice type="230v" >}}
