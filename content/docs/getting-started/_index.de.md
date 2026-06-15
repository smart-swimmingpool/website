---
title: Erste Schritte
weight: 10
tags: ["docs", "getting-started", "tutorial"]
---

**🏊 Smart Swimming Pool: Heimautomatisierung für eine intelligentere Steuerung Ihres Schwimmbads**

{{< safety-notice type="230v" >}}

## Beispiel einer Anlage

In einer typischen Anlage erwärmt ein thermisches Solarsystem das Wasser und unterstützt die Raumheizung im Haus. Das erwärmte Wasser wird in einem Pufferspeicher gesammelt, der eine dritte Zirkulation für den Pool bereitstellt. Eine Pumpe an diesem Kreislauf leitet das Poolwasser durch einen Wärmetauscher:

![Beispielaufbau](schema-environment-smart-pool.png)

## Grundvoraussetzungen

- Swimmingpool mit Sandfilteranlage
- Über eine Pumpe zuschaltbarer Heizkreislauf mit Wärmetauscher
- Solarer Wärmespeicher mit zusätzlichem Heizkreislauf für den Pool

## Teileliste (Bill of Materials)

| Komponente | Preis (ca.) | Hinweise |
|-----------|-------------|----------|
| ESP32 DevKit V1 | 10–15 € | Mind. 4MB Flash, USB-Kabel inklusive |
| DS18B20 Temperatursensor (2x, wasserdicht) | 8–12 € | Edelstahlsonde, 1m Kabel |
| 2-Kanal-Relais-Modul | 5–8 € | Standard **Aktiv-Low**-Modul — siehe Hinweise |
| 4,7kΩ Widerstände (2x) | < 1 € | Pull-Up-Widerstände für OneWire-Bus |
| Breadboard + Jumper-Kabel | 3–8 € | Für Prototyp; für Dauerbetrieb Lochrasterplatine |
| USB-Netzteil (5V / 1A+) | 5–10 € | Für ESP32 + Relaismodul |
| Gehäuse (IP54+) | 5–10 € | Optional, aber empfohlen für Außeneinsatz |
| **Gesamt** | **~45–75 €** | **Ohne Pumpen / Wärmetauscher-Infrastruktur** |

> **⚠️ Relais-Modul Hinweis:** Die Firmware steuert die Relais **Aktiv-Low** (GPIO **LOW** = Relais EIN, GPIO **HIGH** = Relais AUS). Dies entspricht der überwiegenden Mehrheit günstiger 2-Kanal-5V-Relais-Module. Während des ESP32-Starts sind die GPIOs kurz im hochohmigen Zustand — die Firmware setzt sie sofort nach dem Start auf HIGH (Relais AUS). Falls Ihr Modul andersherum arbeitet (Aktiv-High), finden Sie Konfigurationsmöglichkeiten im [FAQ](/docs/troubleshooting/).

## Hardware-Aufbau

### Breadboard-Layout

![Pool Controller Breadboard](/img/pool-controller_breadboard.png)

*Der ESP32 und das Relais-Modul auf einem Breadboard — der einfachste Weg, um zu starten.*

### Schritt 1: ESP32 vorbereiten

1. Schließen Sie den ESP32 per USB an Ihren Computer an.
2. Prüfen Sie, ob er als serielle Schnittstelle erkannt wird (`/dev/ttyUSB0` unter Linux, `COM3` unter Windows).
3. Installieren Sie ggf. **CP210x**- oder **CH340**-Treiber ([CP210x Treiber](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers), [CH340 Treiber](https://www.wch.cn/download/CH341SER_EXE.html)).

### Schritt 2: Temperatursensoren anschließen

Die DS18B20-Sensoren verwenden das **OneWire-Protokoll**. Verbinden Sie sie wie folgt:

Die Firmware (esp32dev-Umgebung) weist **jedem Sensor einen eigenen GPIO-Pin** zu:

| Sensor | ESP32 Pin | Kabel (typisch) |
|--------|-----------|----------------|
| Solar-Kollektor (DS18B20 #1) | **GPIO32** | VDD=Rot, GND=Schwarz, DATA=Gelb/Weiß |
| Poolwasser (DS18B20 #2) | **GPIO33** | VDD=Rot, GND=Schwarz, DATA=Gelb/Weiß |

> **Wichtig:** Schließen Sie einen **4,7kΩ-Widerstand** zwischen **jeder** DATA-Leitung und 3.3V an (Pull-Up). OneWire benötigt einen separaten Pull-Up pro GPIO-Pin. Für zwei Sensoren auf getrennten GPIOs benötigen Sie **zwei 4,7kΩ-Widerstände**.

### Schritt 3: Relais-Modul anschließen

| ESP32 Pin | Relais-Modul | Hinweise |
|-----------|-------------|----------|
| GPIO26 | IN1 | Heizkreispumpe |
| GPIO25 | IN2 | Umwälzpumpe / Filter |
| 5V (VIN) | VCC | **5V** nicht 3.3V! |
| GND | GND | Gemeinsame Masse mit ESP32 |

> **⚠️ Stromversorgung:** Das Relais-Modul benötigt **5V** Spannung (nutzen Sie den VIN-Pin des ESP32 bei USB-Stromversorgung). Nicht vom 3.3V-Pin versorgen. Verbinden Sie ESP32 GND mit Relais GND (gemeinsame Masse).

### Schritt 4: Abschließende Prüfung

Bevor Sie Pumpen oder Netzspannung anschließen:
1. Überprüfen Sie alle Verbindungen anhand des Schaltplans.
2. Vergewissern Sie sich, dass das Relais-Modul korrekt arbeitet: Bei eingeschaltetem ESP32 (noch ohne Pumpensteuerung) messen Sie die GPIO-Pins mit einem Multimeter — sie sollten HIGH sein (Relais AUS). Nach dem Schalten eines Relais über die Weboberfläche sollte der zugehörige GPIO auf LOW gehen (Relais EIN).
3. Spiele Sie zuerst die Firmware auf (siehe unten) und testen Sie mit dem Webinterface **ohne** angeschlossene Pumpen.
4. Immer noch keine 230V? Erste erfolgreiche Firmware-Tests abwarten.

## Firmware-Installation

### PlatformIO (Empfohlen)

> ⚠️ **Wichtig:** Der Pool-Controller ist ein PlatformIO-Projekt. Es gibt **keine** Arduino-IDE-kompatible `.ino`-Datei. PlatformIO ist die einzige unterstützte Build-Methode.

1. Installieren Sie [Visual Studio Code](https://code.visualstudio.com/) und die [PlatformIO-Erweiterung](https://platformio.org/install/ide?install=vscode).
2. Repository klonen:
   ```bash
   git clone https://github.com/smart-swimmingpool/pool-controller.git
   cd pool-controller
   ```
3. Öffnen Sie den Ordner in VS Code — PlatformIO erkennt das Projekt automatisch.
4. **Die richtige Umgebung wählen:** Das Projekt hat als Voreinstellung die Umgebung für den NORVI AE01-R Industrie-Controller. Für ein Standard-ESP32-DevKit wechseln Sie zur `esp32dev`-Umgebung:
   - Klicken Sie auf das **PlatformIO-Logo** (⚡-Symbol) in der VS-Code-Fußzeile
   - Gehen Sie zu **Project Tasks → esp32dev**
   - Oder nutzen Sie den Umgebungswechsler unten im VS-Code-Fenster
5. Verbinden Sie den ESP32 per USB.
6. **Schritt A — Firmware flashen:** Klicken Sie auf den **→ (Upload and Monitor)**-Button neben `esp32dev` in der PlatformIO-Fußzeile. Die Firmware wird kompiliert und geflasht.
7. **Schritt B — Dateisystem hochladen (Weboberfläche):** Die Weboberfläche wird in einer separaten LittleFS-Partition gespeichert und muss nach der Firmware hochgeladen werden:
   - Öffnen Sie in VS Code den PlatformIO-Reiter → **esp32dev → Platform → Upload Filesystem Image**
   - Oder per Terminal:
     ```bash
     pio run -e esp32dev -t uploadfs
     ```
   - Ohne diesen Schritt zeigt die Weboberfläche eine **Fehlerseite** statt der Konfigurationsseite.

### Nach dem Flashen prüfen

Öffnen Sie den seriellen Monitor (115200 Baud). Sie sollten sehen:

```
[INFO] Pool Controller v3.3.0 starting...
[INFO] WiFi: Starting in AP mode
[INFO] AP: 'Pool-Controller-Setup'. IP: 192.168.4.1
```

Der ESP32 startet standardmäßig im **Access Point (AP) Modus**.

## Erste Inbetriebnahme & Konfiguration

### Schritt 1: Mit ESP32 verbinden

1. Suchen Sie nach WLAN-Netzwerken — Sie sehen **`Pool-Controller-Setup`** (offenes Netzwerk, kein Passwort).
2. Verbinden Sie sich von Ihrem Smartphone oder Laptop.
3. Öffnen Sie einen Browser und gehen Sie zu **http://192.168.4.1**

### Schritt 2: WLAN konfigurieren

1. Die Weboberfläche zeigt eine Konfigurationsseite.
2. Geben Sie Ihren WLAN-Namen (SSID) und Ihr Passwort ein.
3. Klicken Sie auf **Speichern** — der ESP32 startet neu und verbindet sich mit Ihrem Netzwerk.

### Schritt 3: MQTT einrichten

1. Finden Sie die IP-Adresse des ESP32 (Router oder serieller Monitor).
2. Öffnen Sie `http://<esp32-ip>/` im Browser.
3. Gehen Sie zu **Konfiguration → MQTT**.
4. Geben Sie die Adresse Ihres MQTT-Brokers ein (z. B. `192.168.1.100` oder `core-mosquitto`).
5. Bei Authentifizierung Benutzername/Passwort eingeben.
6. Klicken Sie auf **Speichern** — der Controller verbindet sich neu mit MQTT.

> **Kein MQTT-Broker?** Installieren Sie [Mosquitto](https://mosquitto.org/download/) auf einem Rechner im Netzwerk oder nutzen Sie das Mosquitto-Add-On in Home Assistant.

### Schritt 4: Home Assistant Integration

Wenn Sie Home Assistant mit MQTT verwenden:

1. Der Controller sendet automatisch MQTT Discovery-Nachrichten.
2. In Home Assistant gehen Sie zu **Einstellungen → Geräte & Dienste**.
3. Klicken Sie auf **Integration hinzufügen → MQTT** (falls nicht schon konfiguriert).
4. Der Pool Controller sollte automatisch als neues Gerät erscheinen.
5. Alle Sensoren, Steuerungen und Konfigurationsparameter erscheinen als Entities — keine manuelle Einrichtung nötig.

> ▶️ **Ausführliche Anleitung**: Siehe [Home Assistant Integrations-Guide](/docs/home-assistant-integration/) für die vollständige Entity-Referenz, Dashboard-Einrichtung, Automatisierungsbeispiele und Fehlerbehebung.

### Schritt 5: Pumpen anschließen

Erst jetzt — nach erfolgreichem Test — die Pumpen anschließen:
1. **Trennen** Sie den ESP32 von der USB-Stromversorgung.
2. Verdrahten Sie die Relaisausgänge mit Ihren Pumpenschützen/Ventilen.
3. Verwenden Sie geeignete Kabelquerschnitte für 230V.
4. Schließen Sie die Netzspannung über einen **RCD (FI-Schutzschalter)** an.
5. Versorgen Sie den ESP32 wieder über sein USB-Netzteil (elektrisch getrennt von 230V).

{{< safety-notice type="230v" >}}

## Modulare Systemübersicht

Die Erste-Schritte-Anleitung konzentriert sich auf den **Pool Controller** als zentrales Modul. Das System hat zusätzliche optionale Module:

| Modul | Zweck | Wann hinzufügen |
|-------|-------|-----------------|
| **Pool Controller** (diese Anleitung) | Hauptsteuerung: Pumpen, Heizung, Zirkulation | Erforderlich — hier starten |
| **Home Assistant** | Nativer MQTT Discovery | Automatisch — keine Einrichtung nötig |
| **Pool Monitor** | Solarbetriebene Temperaturanzeige | Nachdem der Controller läuft |
| **Grafana Dashboard** | Datenvisualisierung und -verlauf | Wenn Sie historische Diagramme möchten |
| **openHAB Konfiguration** | Integration mit openHAB | Wenn Sie openHAB statt Home Assistant nutzen |
| **Smart Analyzer** *(geplant)* | Wasserqualitätsüberwachung | Noch nicht verfügbar |

## Wie geht es weiter?

Sobald Ihr Pool Controller läuft:
- Entdecken Sie den **[Home Assistant Integrations-Guide](/docs/home-assistant-integration/)** für die vollständige Entity-Referenz, Dashboard-Einrichtung und Automatisierungsbeispiele
- Richten Sie das **[Grafana Dashboard](/docs/grafana-dashboard/)** für Temperaturverläufe ein
- Fügen Sie den **[Pool Monitor](/docs/pool-monitor/)** für ein eigenes Display hinzu
- Besuchen Sie das **[FAQ](/docs/troubleshooting/)** bei Problemen
- Folgen Sie der **[openHAB Integrations-Anleitung](/docs/openhab-integration/)**, um openHAB Schritt für Schritt einzurichten
- Nutzen Sie die **[openHAB Konfiguration](/docs/openhab-configuration/)** als Referenz für die vollständigen Konfigurationsdateien

## Vorbereitungen

Sofern ein Heizkreislauf mit Wärmetauscher vorbereitet ist, kann mit der Umsetzung der smarten Steuerung des Pools begonnen werden.

Herz des Systems ist der [Pool Controller](https://github.com/smart-swimmingpool/pool-controller). Dieser übernimmt:

- Steuerung der Zirkulationszeit für die Sandfilterreinigung
- Zuschalten des Heizkreislaufs zur Erwärmung des Poolwassers
- Melden von Status und Temperaturen für die Integration in Smart-Home-Server

Der [Pool Controller](https://github.com/smart-swimmingpool/pool-controller) nutzt [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) für nahtlose Smarthome-Integration. Mit der hier vorgestellten Konfiguration kann der Pool-Controller schnell eingerichtet und von jeder Home Assistant-kompatiblen App gesteuert werden.

### Home Assistant Dashboard

Der Pool Controller registriert via MQTT Discovery automatisch alle Sensoren und Steuerelemente in Home Assistant. Nachfolgend ein Beispiel des Dashboards und der zugehörigen Konfigurationseinträge:

![Home Assistant Dashboard](/img/ha-pool-dashboard.jpg)

*Pool-Controller-Entitäten im Home Assistant Dashboard*

![Home Assistant Device Eintrag](/img/ha-pool-device.jpg)

*MQTT Discovery-Geräteeintrag mit allen Sensoren und Steuerungen*

![Home Assistant Konfiguration](/img/ha-pool-config.jpg)

*Konfigurationseinträge für den Pool Controller in Home Assistant*

## Historie

🏊 Smart Swimming Pool basiert auf einem [früheren Projekt](https://github.com/stritti/smart-swimming-pool), das noch nicht modular aufgebaut war und die gesamte Steuerlogik als openHAB-Regeln implementierte.

Die erste Version war im **Sommer 2018** im Einsatz und zeigte einige Schwächen:

- Die Steuerung der Pumpen über 433-MHz-Steckdosenschalter war unzuverlässig — ohne Rückmeldung war der tatsächliche Status unbekannt
- Die Schaltlogik lebte in openHAB-Regeln, was bei unzuverlässigem WLAN zu Problemen führte
- MQTT-Nachrichten verwendeten ein proprietäres Format

Aus diesen Erfahrungen entstand die überarbeitete Version des 🏊 Smart Swimming Pools: modular, widerstandsfähig und auf Standards basierend.
