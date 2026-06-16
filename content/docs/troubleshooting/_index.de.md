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

## Heizungs- & Zirkulationsprobleme

### Solarpumpe startet nie / Pool heizt nicht auf

**Prüfen Sie in dieser Reihenfolge:**

1. **Solartemperatur > Pooltemperatur?** Die Heizlogik aktiviert nur, wenn der Solarkollektor wärmer ist als das Poolwasser. Liest der Solar-Sensor niedrigere Werte als der Pool-Sensor, erfolgt keine Heizung — das ist bei Bewölkung oder nachts korrekt.

2. **Hysterese zu hoch eingestellt?** Die Standard-Hysterese beträgt 2 K. Bei >5 K benötigt der Controller eine große Temperaturdifferenz zum Einschalten. Versuchen Sie 1–2 K.

3. **Min. Solar Temp zu hoch?** Wenn der Parameter **Min. Solar Temp** über der tatsächlichen Kollektortemperatur liegt, wird der Heizkreis blockiert. Zum Test auf 20–25°C senken.

4. **Sensoren vertauscht?** Wenn Solar- und Pool-Sensor an den falschen GPIO-Pins angeschlossen sind, liest der Controller die falschen Temperaturen. Prüfen Sie:
   - GPIO32 = Solarkollektor (sollte bei Sonne wärmer sein)
   - GPIO33 = Poolwasser (sollte näher an Umgebungstemperatur sein)
   - **Status**-Seite in der Weboberfläche zum Vergleich der Werte

5. **Heizkreis deaktiviert?** In der Weboberfläche **Configuration → Heating** prüfen, ob der Heizkreis **aktiviert** ist.

6. **Motorventil geschlossen?** Falls ein Motorventil im Heizkreis verbaut ist, prüfen ob es geöffnet ist (separates Relais oder manuell).

### Pumpe schaltet im Auto-Modus nicht

Der Pool-Controller aktiviert Pumpen im Automatik-Modus nur unter bestimmten Bedingungen:

- **Filterpumpe:** Läuft nach Zeitplan (Timer oder temperaturbasiert). Läuft nur innerhalb des eingestellten Zeitfensters.
- **Heizpumpe:** Nur wenn Solartemperatur > Pooltemperatur + Hysterese, UND Pooltemperatur < max. Pooltemperatur.

**Logik prüfen:**
1. **Operation Mode** auf **`manu`** (Manuell) in der Weboberfläche **Control**-Seite
2. Jede Pumpe manuell ein- und ausschalten — bestätigt, dass Relais und Verkabelung funktionieren
3. Zurück auf **`auto`** schalten und beobachten: ggf. wartet der Controller nur auf Bedingungen

### Eine Pumpe funktioniert, die andere nicht

- Verkabelung der betroffenen Pumpe auf der 230V-Seite prüfen (LS, FI, Schütz)
- Relais-Kanäle in der Weboberfläche tauschen (folgt die Pumpe dem getauschten Kanal, liegt das Problem auf der 230V-Seite; wenn nicht, ist der Relais-Kanal defekt)
- Spannung an den Relais-Ausgangsklemmen beim Schalten messen

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

### Temperaturwerte schwanken / springen unregelmäßig

**Wahrscheinliche Ursache:** Elektrische Störungen oder lockerer Kontakt auf der DATA-Leitung.

**Lösungen:**
1. **DATA-Verbindung prüfen:** Ein loses Jumper-Kabel auf dem Breadboard kann intermittierenden Kontakt verursachen. Kabel fest in das Breadboard drücken.
2. **Sensorkabel von 230V fernhalten:** Mindestens **30 cm** Abstand zu Netzleitungen. Parallele Verlegung über längere Strecken verstärkt Störungen.
3. **Geschirmtes Kabel verwenden:** Bei Verlängerungen >5 m **geschirmte Twisted-Pair-Kabel** (z.B. LiYCY 2×0,25mm²) nutzen. Schirm nur auf ESP32-Seite an GND anschließen.
4. **Pull-Up-Widerstand prüfen:** Widerstand zwischen DATA und 3,3V messen — sollte ~4,7 kΩ betragen.
5. **Wasser in der Verbindungsdose?:** Bei Verlängerungskabeln kann die Verbindungsdose Kondenswasser enthalten. Öffnen, trocknen und mit Schrumpfschlauch oder Silikon abdichten.

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

### Pumpenschalter reagieren nicht auf Home Assistant

**Wahrscheinliche Ursache:** Der Controller akzeptiert Pumpenbefehle per MQTT nur im **Manuell**-Modus.

**Lösungen:**
1. **Operation Mode** auf **`manu`** in Home Assistant stellen (`select.pool_controller_mode`)
2. Die Pumpenschalter sollten jetzt schreibbar sein
3. Nach manueller Steuerung zurück auf `auto` für automatischen Betrieb

Wenn die Schalter auch im `manu`-Modus nicht reagieren:
1. MQTT-**Verfügbarkeits-Topic** prüfen: `homeassistant/sensor/pool-controller/availability` sollte `online` anzeigen
2. Stale-Discovery löschen: Leeres Payload an das `/config`-Topic der Entity senden
3. Controller über die Weboberfläche neu starten

---

## Controller & Automatisierungsprobleme

### Controller schaltet Pumpen nicht, obwohl Bedingungen erfüllt sind

**Prüfen Sie:**

1. **Ist der Betriebsmodus auf `auto`?** Im Modus `manu` (Manuell) automatisiert der Controller nicht. Im Modus `timer` läuft nur der Timer-Zeitplan. Nur `auto` nutzt die vollständige Heizlogik.
2. **Status-Seite prüfen:** Die Weboberfläche **Status** zeigt den aktuellen Zustand aller Sensoren und die Entscheidungslogik des Controllers. Wenn der Controller Bedingungen als nicht erfüllt ansieht, ist der Grund hier sichtbar.
3. **MQTT-Befehl anhängig?** Wenn Sie kürzlich eine Pumpe via Home Assistant geschaltet haben, überschreibt ein MQTT-Befehl ggf. den Automatik-Zustand. Pumpe AUS und zurück auf AUTO schalten oder Controller neu starten.
4. **Firmware-Fehler?** GitHub Issues für Ihre Firmware-Version prüfen.

### Modus-Wahl lässt sich nicht ändern / springt zurück

- Der Controller speichert den Modus im Flash-Speicher. Wenn der Modus nach Sekunden zurückspringt, kann das Schreiben fehlschlagen.
- Controller neu starten und erneut versuchen.
- Bei anhaltendem Problem: Firmware neu flashen (Konfiguration bleibt in den meisten Fällen erhalten).

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

### Controller nach Firmware-Update nicht erreichbar

**Wahrscheinliche Ursache:** Das Update hat die WLAN-Konfiguration zurückgesetzt oder die IP-Adresse geändert.

**Lösungen:**
1. **WLAN-Zugangsdaten zurückgesetzt.** Nach manchen Updates fällt der Controller in den AP-Modus zurück (`Pool-Controller-Setup`). Mit diesem Netzwerk verbinden und WLAN über die Weboberfläche unter `http://192.168.4.1` neu konfigurieren.
2. **IP-Adresse geändert.** DHCP-Client-Liste des Routers nach einer neuen IP durchsuchen. Der Controller kann nach dem Flashen eine andere MAC-Adresse haben, wenn die NVS-Partition gelöscht wurde.
3. **OTA-Update fehlgeschlagen.** War das OTA-Update unterbrochen oder die neue Firmware defekt, kann der Controller in einer Boot-Schleife hängen. Wiederherstellung erfordert **serielles (USB-) Flashen**:
   - ESP32 per USB verbinden
   - BOOT-Taste gedrückt halten
   - Firmware via PlatformIO wie gewohnt flashen
4. **Partitionslayout geändert.** Bei geändertem Partitionsschema kann das Dateisystem (Weboberfläche) fehlen oder beschädigt sein. Dateisystem-Image erneut hochladen:
   ```bash
   pio run -e esp32dev -t uploadfs
   ```
5. **Vorbeugung:** Vor OTA-Update sicherstellen, dass der ESP32 in WLAN-Reichweite ist und eine stabile Stromversorgung hat. Update nicht unterbrechen.

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
