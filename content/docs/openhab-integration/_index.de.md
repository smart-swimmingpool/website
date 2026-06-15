---
title: openHAB Integration
weight: 15
tags: ["docs", "openHAB", "tutorial"]
---

**🏊 Smart Swimming Pool: Den Pool Controller mit openHAB integrieren**

Im Gegensatz zu [Home Assistant](/docs/getting-started/#step-4-home-assistant-integration), das den Pool Controller automatisch per MQTT Discovery erkennt, erfordert openHAB eine **manuelle Konfiguration**. Diese Anleitung führt Sie Schritt für Schritt durch den Prozess.

> 💡 **Sie nutzen bereits openHAB?**  
> Die [openHAB Konfiguration](/docs/openhab-configuration/) enthält die vollständigen Referenzdateien (Things, Items, Sitemap). Diese Anleitung erklärt, *wie* Sie diese einrichten und an Ihr System anpassen.

---

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Folgendes vorhanden ist:

1. **Der Pool Controller** ist geflasht und läuft in Ihrem Netzwerk (siehe [Erste Schritte](/docs/getting-started/))
2. **Ein MQTT-Broker** (z. B. [Mosquitto](https://mosquitto.org/)) — installieren Sie ihn auf dem gleichen Rechner wie openHAB oder in Ihrem Netzwerk
3. **openHAB** (Version 3 oder 4) läuft und ist über die Weboberfläche erreichbar

---

## Schritt 1: MQTT Binding installieren

In der openHAB-Weboberfläche:

1. Gehen Sie zu **Einstellungen → Add-ons → Bindings**
2. Suchen Sie nach **"MQTT"**
3. Installieren Sie das **MQTT Binding** (offizielles Binding des openHAB-Projekts)
4. Kein Neustart erforderlich — das Binding ist sofort aktiv

---

## Schritt 2: MQTT Broker Thing konfigurieren

1. Gehen Sie zu **Einstellungen → Things**
2. Klicken Sie auf **+** (Thing hinzufügen)
3. Suchen Sie nach **"MQTT"** und wählen Sie **MQTT Broker**
4. Konfigurieren Sie:
   - **Host**: IP-Adresse Ihres MQTT-Brokers (z. B. `192.168.1.100` oder `core-mosquitto`)
   - **Port**: `1883` (Standard, unverschlüsselt)
   - **Client ID**: `openHAB-pool` (muss auf Ihrem Broker eindeutig sein)
   - **Benutzername/Passwort**: Nur wenn Ihr Broker eine Authentifizierung erfordert
5. Klicken Sie auf **Thing erstellen**

Das Broker Thing sollte innerhalb von Sekunden **Online** sein. Falls nicht, überprüfen Sie, ob Ihr MQTT-Broker läuft und erreichbar ist.

---

## Schritt 3: MQTT-Topics ermitteln

Der Pool Controller v3.x veröffentlicht seine Daten im [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery)-Format. Sie müssen die **genauen Topics** Ihres Controllers ermitteln, um openHAB korrekt zu konfigurieren.

### Option A: MQTT Explorer (Empfohlen)

Installieren Sie [MQTT Explorer](http://mqtt-explorer.com/) auf Ihrem Computer:

1. Verbinden Sie sich mit Ihrem MQTT-Broker (Host, Port — wie oben)
2. Navigieren Sie zum Präfix `homeassistant/`
3. Sie sehen die Topics nach Entitätstyp organisiert:
   ```
   homeassistant/
   ├── sensor/
   │   └── pool-controller/
   │       ├── pool_temp/
   │       ├── solar_temp/
   │       └── availability/
   ├── switch/
   │   └── pool-controller/
   │       ├── pool_pump/
   │       └── solar_pump/
   ├── select/
   │   └── pool-controller/
   │       └── operation_mode/
   └── number/
       └── pool-controller/
           ├── pool_max_temp/
           ├── solar_min_temp/
           ├── hysteresis/
           ├── timer_start_h/
           ├── timer_start_m/
           ├── timer_end_h/
           └── timer_end_m/
   ```

Jede Entität hat:
- `config` — Discovery-Payload mit Metadaten
- `state` — aktueller Wert
- `set` — Befehlstopic (für beschreibbare Entitäten)

### Option B: Kommandozeile (mosquitto_sub)

Wenn Sie die Kommandozeile bevorzugen:

```bash
# Alle Pool-Controller-Topics abonnieren
mosquitto_sub -h <broker-ip> -t "homeassistant/#" -v

# Oder nur nach dem Pool Controller filtern
mosquitto_sub -h <broker-ip> -t "homeassistant/+/pool-controller/#" -v
```

> ⚠️ **Hinweis**: Die Geräte-ID Ihres Controllers kann von `pool-controller` abweichen, wenn Sie die **MQTT-Geräte-ID** in der Weboberfläche des Pool Controllers geändert haben. Passen Sie das Topic-Präfix entsprechend an.

---

## Schritt 4: Thing-Datei erstellen

openHAB 3+ verwendet **`.things`-Dateien** in `$OPENHAB_CONF/things/`, um MQTT-Topic-Things zu definieren.

Erstellen Sie `$OPENHAB_CONF/things/pool-controller.things`:

```java
Bridge mqtt:broker:mosquitto "Mosquitto" [ host="127.0.0.1", port=1883, secure=false, clientID="openHAB-pool" ]
{
    Thing topic pool-controller "Pool Controller" @ "Außenbereich" {
        Channels:
            // Betriebsmodus
            Type string : operationMode "Betriebsmodus"
                [ stateTopic="homeassistant/select/pool-controller/operation_mode/state",
                  commandTopic="homeassistant/select/pool-controller/operation_mode/set" ]

            // Konfigurationszahlen
            Type number : maxPoolTemp "Max. Pooltemperatur"
                [ stateTopic="homeassistant/number/pool-controller/pool_max_temp/state",
                  commandTopic="homeassistant/number/pool-controller/pool_max_temp/set" ]
            Type number : minSolarTemp "Min. Solartemperatur"
                [ stateTopic="homeassistant/number/pool-controller/solar_min_temp/state",
                  commandTopic="homeassistant/number/pool-controller/solar_min_temp/set" ]
            Type number : hysteresis "Hysterese"
                [ stateTopic="homeassistant/number/pool-controller/hysteresis/state",
                  commandTopic="homeassistant/number/pool-controller/hysteresis/set" ]
            Type number : timerStartH "Timer Start Stunde"
                [ stateTopic="homeassistant/number/pool-controller/timer_start_h/state",
                  commandTopic="homeassistant/number/pool-controller/timer_start_h/set" ]
            Type number : timerStartM "Timer Start Minute"
                [ stateTopic="homeassistant/number/pool-controller/timer_start_m/state",
                  commandTopic="homeassistant/number/pool-controller/timer_start_m/set" ]
            Type number : timerEndH "Timer Ende Stunde"
                [ stateTopic="homeassistant/number/pool-controller/timer_end_h/state",
                  commandTopic="homeassistant/number/pool-controller/timer_end_h/set" ]
            Type number : timerEndM "Timer Ende Minute"
                [ stateTopic="homeassistant/number/pool-controller/timer_end_m/state",
                  commandTopic="homeassistant/number/pool-controller/timer_end_m/set" ]

            // Pumpen
            Type switch : poolPump "Poolpumpe"
                [ stateTopic="homeassistant/switch/pool-controller/pool_pump/state",
                  commandTopic="homeassistant/switch/pool-controller/pool_pump/set" ]
            Type switch : solarPump "Solarpumpe"
                [ stateTopic="homeassistant/switch/pool-controller/solar_pump/state",
                  commandTopic="homeassistant/switch/pool-controller/solar_pump/set" ]

            // Temperaturen
            Type number : poolTemp "Pooltemperatur"
                [ stateTopic="homeassistant/sensor/pool-controller/pool_temp/state" ]
            Type number : solarTemp "Solartemperatur"
                [ stateTopic="homeassistant/sensor/pool-controller/solar_temp/state" ]

            // Systeminfo
            Type number : signal "WiFi-Signal"
                [ stateTopic="homeassistant/sensor/pool-controller/signal/state" ]
            Type number : uptime "Betriebszeit"
                [ stateTopic="homeassistant/sensor/pool-controller/uptime/state" ]
            Type string : fwVersion "Firmware-Version"
                [ stateTopic="homeassistant/sensor/pool-controller/fw_version/state" ]
    }
}
```

> **Ersetzen Sie `pool-controller`** in den Topic-Pfaden durch Ihre tatsächliche Geräte-ID, falls Sie diese geändert haben.

---

## Schritt 5: Items-Datei erstellen

Items verknüpfen die MQTT-Kanäle mit openHAB-Items, die in Benutzeroberflächen angezeigt und in Regeln verwendet werden können.

Erstellen Sie `$OPENHAB_CONF/items/pool-controller.items`:

```java
// Gruppen
Group gPool_Controller "Pool Controller" <swimmingpool>

// Betriebsmodus
String Pool_OpMode "Betriebsmodus [%s]" <settings> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:operationMode", autoupdate="true" }

// Konfiguration
Number Pool_MaxTemp "Max. Pooltemp. [%.1f °C]" <heating> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:maxPoolTemp", autoupdate="true" }
Number Pool_MinSolarTemp "Min. Solartemp. [%.1f °C]" <heating> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:minSolarTemp", autoupdate="true" }
Number Pool_Hysteresis "Hysterese [%.1f K]" <line> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:hysteresis", autoupdate="true" }

Number Pool_Timer_Start_H "Timer Start Std. [%.0f h]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerStartH", autoupdate="true" }
Number Pool_Timer_Start_M "Timer Start Min. [%.0f m]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerStartM", autoupdate="true" }
Number Pool_Timer_End_H "Timer Ende Std. [%.0f h]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerEndH", autoupdate="true" }
Number Pool_Timer_End_M "Timer Ende Min. [%.0f m]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerEndM", autoupdate="true" }

// Pumpen
Switch Pool_PoolPump "Poolpumpe" <pump> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:poolPump", autoupdate="false" }
Switch Pool_SolarPump "Solarpumpe" <solarplant> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:solarPump", autoupdate="false" }

// Temperaturen
Number Pool_PoolTemp "Pooltemperatur [%.1f °C]" <temperature> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:poolTemp", autoupdate="false" }
Number Pool_SolarTemp "Solartemperatur [%.1f °C]" <temperature> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:solarTemp", autoupdate="false" }

// System
Number Pool_Signal "WiFi-Signal [%.0f%%]" <network> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:signal", autoupdate="false" }
Number Pool_Uptime "Betriebszeit [%d s]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:uptime", autoupdate="false" }
String Pool_FWVersion "Firmware [%s]" <text> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:fwVersion", autoupdate="false" }
```

### Channel-UID-Format

Die Channel-UID folgt diesem Muster:

```
mqtt:topic:<Broker-Thing-ID>:<Thing-ID>:<Channel-ID>
```

- `mqtt:topic` — festes Präfix für MQTT-Topic-Things
- `mosquitto` — die ID Ihres Broker-Things (wie in der .things-Datei definiert)
- `pool-controller` — die ID Ihres Topic-Things
- `poolTemp` — der Channel-Name aus der .things-Datei

---

## Schritt 6: Sitemap erstellen

Sitemaps definieren, was in der openHAB BasicUI und den mobilen Apps angezeigt wird.

Erstellen oder bearbeiten Sie `$OPENHAB_CONF/sitemaps/pool.sitemap`:

```perl
sitemap pool label="Pool Controller" {
    Frame label="Steuerung" {
        Switch item=Pool_OpMode label="Modus" icon="settings"
            mappings=[auto="Auto", manu="Manuell", boost="Boost", timer="Timer"]

        Text item=Pool_PoolPump label="Poolpumpe [%s]" icon="pump"
            visibility=[Pool_OpMode==auto, Pool_OpMode==boost, Pool_OpMode==timer]
        Switch item=Pool_PoolPump label="Poolpumpe" icon="pump"
            visibility=[Pool_OpMode==manu]

        Text item=Pool_SolarPump label="Solarpumpe [%s]" icon="solarplant"
            visibility=[Pool_OpMode==auto, Pool_OpMode==boost, Pool_OpMode==timer]
        Switch item=Pool_SolarPump label="Solarpumpe" icon="solarplant"
            visibility=[Pool_OpMode==manu]
    }

    Frame label="Temperaturen" {
        Text item=Pool_PoolTemp label="Pool [%.1f °C]" icon="temperature"
            valuecolor=[>30="orange", >20="green", <=20="blue"]
        Text item=Pool_SolarTemp label="Solar [%.1f °C]" icon="temperature"
            valuecolor=[>30="orange", >20="green", <=20="blue"]
    }

    Frame label="Einstellungen" {
        Frame label="Timer" {
            Setpoint item=Pool_Timer_Start_H label="Start Std. [%.0f]" icon="time" minValue=0 maxValue=23 step=1
            Setpoint item=Pool_Timer_Start_M label="Start Min. [%02.0f]" minValue=0 maxValue=59 step=5
            Setpoint item=Pool_Timer_End_H label="Ende Std. [%.0f]" icon="time" minValue=0 maxValue=23 step=1
            Setpoint item=Pool_Timer_End_M label="Ende Min. [%02.0f]" minValue=0 maxValue=59 step=5
        }
        Frame label="Konfiguration" {
            Setpoint item=Pool_MaxTemp label="Max. Pooltemp. [%.0f °C]" icon="heating" minValue=0 maxValue=40 step=1
            Setpoint item=Pool_MinSolarTemp label="Min. Solartemp. [%.0f °C]" icon="heating" minValue=0 maxValue=100 step=1
            Setpoint item=Pool_Hysteresis label="Hysterese [%.1f K]" icon="line" minValue=0 maxValue=10 step=0.5
        }
        Frame label="System" {
            Text item=Pool_Uptime label="Betriebszeit"
            Text item=Pool_Signal label="WiFi-Signal [%.0f %%]"
            Text item=Pool_FWVersion label="Firmware"
        }
    }
}
```

---

## Schritt 7: Funktion prüfen

1. **Things prüfen**: Gehen Sie zu **Einstellungen → Things** in der openHAB-Oberfläche. Das `Pool Controller` Thing sollte **Online** anzeigen.
2. **Items prüfen**: Öffnen Sie **Einstellungen → Items** und verifizieren Sie, dass alle Items vorhanden sind und Werte anzeigen.
3. **Sitemap öffnen**: Navigieren Sie zu `http://<openhab-ip>:8080/basicui/app?sitemap=pool` oder nutzen Sie die openHAB-App.

Wenn Items **NULL** oder **Nicht definiert** anzeigen:
- Prüfen Sie, ob die MQTT-Topics mit den tatsächlichen Topics Ihres Controllers übereinstimmen (MQTT Explorer hilft beim Vergleichen)
- Stellen Sie sicher, dass das Broker Thing Online ist
- Überprüfen Sie `$OPENHAB_CONF/userdata/logs/openhab.log` auf MQTT-bezogene Fehler

---

## Konfigurationsdateien

Die vollständige Referenzkonfiguration liegt im **[openhab-config Repository](https://github.com/smart-swimmingpool/openhab-config)** auf GitHub:

| Datei | Zweck |
|-------|-------|
| [`things/mqtt.things`](https://github.com/smart-swimmingpool/openhab-config/blob/main/things/mqtt.things) | MQTT-Broker und Topic-Things |
| [`items/2-pool.items`](https://github.com/smart-swimmingpool/openhab-config/blob/main/items/2-pool.items) | Item-Definitionen verknüpft mit Channels |
| [`sitemaps/pool.sitemap`](https://github.com/smart-swimmingpool/openhab-config/blob/main/sitemaps/pool.sitemap) | BasicUI- und App-Layout |

> **Hinweis**: Das openhab-config Repository verwendet derzeit **Homie 3.0** MQTT-Topics (für Controller v2.x). Wenn Sie Controller v3.x betreiben, passen Sie die Topics an das in dieser Anleitung gezeigte `homeassistant/`-Format an. Siehe dazu die [Firmware-Migration](/docs/firmware-migration/).

---

## Fehlerbehebung

### Things bleiben OFFLINE

- **Netzwerkverbindung prüfen**: Kann Ihr openHAB-Server den MQTT-Broker erreichen? (`ping <broker-ip>`)
- **Zugangsdaten prüfen**: Wenn Ihr Broker eine Authentifizierung erfordert, verifizieren Sie Benutzername/Passwort im Broker-Thing
- **Logs prüfen**: Führen Sie `tail -f $OPENHAB_CONF/userdata/logs/openhab.log | grep -i mqtt` für Echtzeit-Diagnose aus

### Items zeigen "—" (kein Wert)

- Die Topic-Namen in Ihrer `.things`-Datei stimmen möglicherweise nicht mit den tatsächlichen Topics des Controllers überein
- Nutzen Sie MQTT Explorer, um `homeassistant/#` zu abonnieren und zu vergleichen
- Der Controller sendet Zahlenwerte als einfache Zahlen (z. B. `25.5`) — keine Transformation erforderlich

### Befehle erreichen den Controller nicht

- Stellen Sie sicher, dass `commandTopic` in Ihrer `.things`-Datei für beschreibbare Channels angegeben ist
- Prüfen Sie, ob der Controller mit dem MQTT-Broker verbunden ist (grüne LED oder Weboberfläche prüfen)
- Testen Sie manuell: `mosquitto_pub -h <broker-ip> -t "homeassistant/switch/pool-controller/pool_pump/set" -m "ON"`

### Falsche MQTT-Geräte-ID

Die Standard-Geräte-ID ist `pool-controller`. Wenn Sie sie in der Weboberfläche des Controllers geändert haben (**Konfiguration → MQTT → Geräte-ID**), aktualisieren Sie alle Topic-Pfade in Ihrer `.things`-Datei entsprechend.
