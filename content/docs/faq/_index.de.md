---
title: Häufig gestellte Fragen (FAQ)
weight: 28
tags: ["docs", "faq"]
---

**🏊 Smart Swimming Pool: Kurze Antworten auf häufige Fragen.**

---

## Projekt

### Ist dieses Projekt wirklich Open Source?

**Ja.** Der 🏊 Smart Swimming Pool ist unter der **MIT-Lizenz** veröffentlicht. Der gesamte Quellcode, Schaltpläne und die Dokumentation sind frei auf [GitHub](https://github.com/smart-swimmingpool) verfügbar. Sie können das Projekt für jeden Zweck nutzen, modifizieren und verteilen — auch kommerziell.

### Funktioniert es ohne Internet?

**Ja.** Der Pool-Controller ist vollständig **autark**. Er übernimmt Zirkulationssteuerung und Heizungsregelung ohne Internetverbindung. WLAN wird nur für MQTT-Kommunikation (optional) und die Weboberfläche benötigt. Der Controller arbeitet auch bei Router-Ausfall weiter.

### Funktioniert es ohne Smart-Home-Server?

**Ja.** Die Steuerlogik läuft lokal auf dem ESP32. MQTT, Home Assistant und openHAB sind **optional** — sie erweitern um Fernsteuerung und Visualisierung, aber der Controller arbeitet auch ohne Server einwandfrei.

### Gibt es eine Community?

Ja. Das Projekt hat eine [GitHub-Community](https://github.com/smart-swimmingpool/smart-swimmingpool) für Issues und Diskussionen. Auch das [Wiki](https://github.com/smart-swimmingpool/smart-swimmingpool/wiki) enthält Community-Inhalte.

---

## Funktionen

### Was kann der Pool-Controller?

Der Controller automatisiert:
- **Filterpumpen-Steuerung** — Sandfilteranlage nach Timer oder Temperatur
- **Solarheizungs-Steuerung** — Heizkreispumpe bei verfügbarer Solarenergie
- **Temperaturüberwachung** — Pool- und Kollektortemperatur
- **Integration** — Home Assistant, openHAB und jedes MQTT-System
- **OTA-Updates** — Firmware-Updates über WLAN (ab v3.3)

### Kann ich den Pool vom Handy steuern?

**Ja**, mit Home Assistant oder openHAB. Beide bieten Apps mit Dashboard und Push-Benachrichtigungen. Der Controller selbst hat eine Weboberfläche für den Zugriff aus dem Heimnetz.

### Kann ich Sprachsteuerung nutzen (Alexa / Google Home)?

**Indirekt.** Mit Home Assistant als Brücke können Sie Pool-Entities an Alexa oder Google Home anbinden (via [Nabu Casa](https://www.nabucasa.com/) oder lokaler [Alexa-Integration](https://www.home-assistant.io/integrations/alexa/)).

---

## Hardware

### Welche Hardware wird mindestens benötigt?

- **ESP32 DevKit V1** (~10–15€)
- **2-Kanal 5V Relais-Modul** (~5–8€)
- **2× DS18B20 Temperatursensoren** (~8–12€)
- **2× 4,7kΩ Widerstände + Breadboard + Jumper** (~5€)

**Gesamt: ~35–55 €** für die Controller-Elektronik. Die vollständige [Stückliste (BOM)](/docs/bom/) enthält auch Gehäuse, 230V-Installation und Werkzeug.

### Kann ich das ohne Solarheizung nutzen?

**Ja.** Die Heizlogik schaltet eine Pumpe temperaturgesteuert. Das funktioniert mit jeder Wärmequelle:
- Solarthermie
- Wärmepumpe
- Gas-/Ölheizung mit Wärmetauscher
- Elektro-Heizelement

Stellen Sie den Parameter **Min. Solar Temp** einfach auf die Betriebstemperatur Ihrer Wärmequelle ein.

### Kann ich das mit einer Wärmepumpe statt Solar nutzen?

**Ja.** Der Controller misst die Temperatur der Wärmequelle (über den „Solar"-Sensor) und schaltet die Heizpumpe bei ausreichender Temperatur. Der „Solar"-Sensor kann auch „Wärmepumpen-Vorlauf" heißen — die Logik ist identisch.

### Welche Pumpen können gesteuert werden?

Das Relais-Modul schaltet **230V / 10A max** (ohmsche Last). Bei induktiven Lasten (Motoren/Pumpen) mit ~5A bemessen. Für größere Pumpen das Relais zur Ansteuerung eines Schützes verwenden.

### Kann ich ein Shelly-Relais statt des 2-Kanal-Moduls verwenden?

**Nicht direkt.** Die Firmware ist für direkt per GPIO angesteuerte Relais ausgelegt. Shelly-Geräte sind WiFi-basiert und bieten nicht die gleiche Echtzeitsteuerung oder Zuverlässigkeit. Das Projekt verwendet einfache Relais-Module bewusst: sie funktionieren auch ohne WLAN.

### Ist das System wetterfest?

**ESP32 und Relais-Modul sind NICHT wetterfest** im Auslieferungszustand. Für Außen-Installation ein **IP54+-Gehäuse** mit Kabelverschraubungen verwenden. Die DS18B20-Sensoren sind IP68 (Edelstahlsonde), aber die Kabeleinführung muss abgedichtet sein.

### Ist der Pool-Controller CE-/UL-zertifiziert?

**Nein.** Dies ist ein Hobby-DIY-Projekt. Es wurde von keiner Aufsichtsbehörde geprüft oder zertifiziert. Sie bauen und betreiben es auf eigene Gefahr. Verwenden Sie immer einen **FI-Schutzschalter (RCD)** beim Anschluss an die Netzspannung.

---

## Smart-Home-Integration

### Funktioniert es mit Home Assistant?

**Ja, nahtlos.** Der Controller nutzt **Home Assistant MQTT Discovery** — alle Sensoren, Steuerungen und Parameter erscheinen automatisch als Entities. Keine YAML-Konfiguration nötig. Siehe [Home Assistant Integration](/docs/home-assistant-integration/).

### Funktioniert es mit openHAB?

**Ja.** Der Controller veröffentlicht alle Daten per MQTT im HA Discovery-Format (v3.x) oder der Homie-Convention (v2.x). openHAB kann diese Topics via MQTT-Binding abonnieren. Siehe [openHAB Konfiguration](/docs/openhab-configuration/).

### Funktioniert es mit Alexa, Google Home oder Apple HomeKit?

**Nicht direkt.** Der Controller spricht diese Protokolle nicht nativ. Mit Home Assistant als Brücke können Pool-Entities aber an Alexa, Google Home oder Apple HomeKit angebunden werden.

### Kann ich Grafana nutzen?

**Ja.** Der Controller veröffentlicht alle Daten per MQTT. Mit [Telegraf](https://www.influxdata.com/time-series-platform/telegraf/) können MQTT-Daten in [InfluxDB](https://www.influxdata.com/) gespeichert und mit [Grafana](/docs/grafana-dashboard/) visualisiert werden.

---

## Konfiguration & Betrieb

### Wie stelle ich die Zieltemperatur ein?

- **Weboberfläche:** Controller-UI → **Configuration → Heating** → **Max. Pool Temp**
- **Home Assistant:** Entity `number.pool_controller_pool_max_temp` ändern
- **MQTT:** Passendes Topic veröffentlichen

Der Standardbereich ist 0–40°C.

### Was ist Hysterese und wie stelle ich sie ein?

Hysterese verhindert schnelles Ein-/Ausschalten der Pumpe nahe der Solltemperatur. Eine Hysterese von **2 K** bedeutet: die Pumpe schaltet 2°C über dem Schwellwert ein und 2°C darunter aus.

**Beispiel:** Bei Max. Pool Temp = 28°C und Hysterese = 2 K schaltet die Heizpumpe bei 28°C aus und bei 26°C wieder ein.

### Wie stelle ich den Filterpumpen-Zeitplan ein?

Zwei Modi:
- **Timer-Modus:** **Timer Start** und **Timer End** einstellen. Die Filterpumpe läuft durchgehend zwischen diesen Zeiten.
- **Temperaturbasierter Modus (v3.3+):** Die Laufzeit wird anhand der Pooltemperatur angepasst (Parameter **Circ. Temp Threshold**, **Circ. Temp Factor**, **Circ. Max Runtime**).

### Kann ich den Pool ohne Controller betreiben?

**Ja.** Der Controller arbeitet parallel zur vorhandenen Pool-Infrastruktur. Bei Trennung des ESP32 schalten die Pumpen einfach nicht — die manuelle Steuerung (falls vorhanden) bleibt unbeeinflusst.

---

## Troubleshooting-Schnelllinks

| Problem | Wo prüfen? |
|---------|------------|
| Sensor zeigt -127°C | [DS18B20 Fehlerbehebung](/docs/troubleshooting/#ds18b20-wird-nicht-erkannt--zeigt--127c-oder-85c) |
| Pumpe startet nicht | [Heizungs- & Zirkulationsprobleme](/docs/troubleshooting/#heizungs--zirkulationsprobleme) |
| WLAN verbindet nicht | [WLAN- & Netzwerk-Probleme](/docs/troubleshooting/#wlan--netzwerk-probleme) |
| MQTT funktioniert nicht | [MQTT-Probleme](/docs/troubleshooting/#mqtt-probleme) |
| Controller startet nicht | [ESP32- & Firmware-Probleme](/docs/troubleshooting/#esp32--firmware-probleme) |
