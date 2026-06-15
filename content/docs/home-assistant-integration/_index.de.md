---
title: Home Assistant Integration
weight: 14
tags: ["docs", "home-assistant", "tutorial"]
---

**🏊 Smart Swimming Pool: Den Pool Controller mit Home Assistant integrieren**

Der Pool Controller v3.x integriert sich über **nativen [MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery)** in Home Assistant. Sobald der Controller mit Ihrem MQTT-Broker verbunden ist, registriert er automatisch alle Sensoren, Steuerungen und Konfigurationsparameter als Home-Assistant-Entities — keine manuelle Konfiguration erforderlich.

> 💡 **Sie richten den Pool Controller zum ersten Mal ein?**  
> Folgen Sie zuerst der [Erste Schritte](/docs/getting-started/)-Anleitung, die das Flashen der Firmware, die WiFi-Konfiguration und die MQTT-Einrichtung abdeckt.

---

## Voraussetzungen

Bevor der Pool Controller in Home Assistant erscheint:

1. **Home Assistant** mit konfigurierter **[MQTT-Integration](https://www.home-assistant.io/integrations/mqtt/)** (Broker-Verbindung)
2. **Pool Controller** mit dem **gleichen MQTT-Broker** verbunden (konfiguriert über die Weboberfläche: **Konfiguration → MQTT**)
3. **MQTT Discovery aktiviert** in Home Assistant (`discovery: true` in `configuration.yaml` — standardmäßig aktiviert)

---

## Funktionsweise

Beim Start und bei der MQTT-Verbindung veröffentlicht der Pool Controller **Discovery-Payloads** auf Topics wie:

```
homeassistant/sensor/pool-controller/pool-temp/config
homeassistant/switch/pool-controller/pool-pump/config
homeassistant/select/pool-controller/mode/config
...
```

Home Assistant hört standardmäßig auf `homeassistant/+/+/config` und erstellt automatisch Entities aus diesen Payloads. Alle Entities werden unter einem einzigen **Pool Controller**-Gerät gruppiert.

### Geräteinformationen

Der Controller identifiziert sich mit:

| Eigenschaft | Wert |
|-------------|------|
| **Name** | Pool Controller |
| **Hersteller** | smart-swimmingpool |
| **Modell** | Pool Controller |
| **Identifikator** | `pool_controller_<mac-suffix>` (pro Gerät eindeutig) |

---

## Vollständige Entity-Referenz

Sobald der Pool Controller verbunden ist, erstellt er folgende Entities in Home Assistant:

### 📊 Primäre Sensoren

Diese erscheinen auf der Gerätevorderseite (kein `entity_category`):

| Entity-ID | Name | Geräteklasse | Einheit |
|-----------|------|-------------|---------|
| `sensor.pool_controller_pool_temp` | Pool Temperature | `temperature` | °C |
| `sensor.pool_controller_solar_temp` | Solar Temperature | `temperature` | °C |

### 🛠️ Steuerungen (Schalter & Auswahl)

| Entity-ID | Name | Typ | Hinweis |
|-----------|------|-----|---------|
| `switch.pool_controller_pool_pump` | Pool Pump | Schalter | Nur im **Manuell**-Modus beschreibbar |
| `switch.pool_controller_solar_pump` | Solar Pump | Schalter | Nur im **Manuell**-Modus beschreibbar |
| `select.pool_controller_mode` | Operation Mode | Auswahl | Optionen: auto, manu, boost, timer |

### 🔧 Konfigurationsparameter (`entity_category: config`)

| Entity-ID | Name | Typ | Einheit | Bereich |
|-----------|------|-----|---------|--------|
| `number.pool_controller_pool_max_temp` | Max. Pool Temp | Zahl | °C | 0–40 |
| `number.pool_controller_solar_min_temp` | Min. Solar Temp | Zahl | °C | 0–100 |
| `number.pool_controller_hysteresis` | Temperature Hysteresis | Zahl | K | 0–10 |
| `number.pool_controller_temp_circ_threshold` | Circ. Temp Threshold | Zahl | °C | 0–40 |
| `number.pool_controller_temp_circ_factor` | Circ. Temp Factor | Zahl | min/°C | 0–120 |
| `number.pool_controller_temp_circ_max_runtime` | Circ. Max Runtime | Zahl | min | 60–1440 |
| `time.pool_controller_timer_start` | Timer Start | Zeit | — | HH:MM:SS |
| `time.pool_controller_timer_end` | Timer End | Zeit | — | HH:MM:SS |
| `select.pool_controller_timezone` | Timezone | Auswahl | — | (dynamische Liste) |
| `text.pool_controller_ntp_server` | NTP Server | Text | — | — |
| `update.pool_controller_firmware` | Firmware | Update | — | — |
| `climate.pool_controller_thermostat` | Pool Thermostat | Climate | °C | 0–40 |

Die **Climate**-Entity (`climate.pool_controller_thermostat`) bietet eine thermostatähnliche Steuerung:
- **HVAC-Modi**: aus, auto, heizen
- **Aktuelle Temperatur**: Pool-Wassertemperatur
- **Zieltemperatur**: entspricht der Max. Pool Temp
- **Aktion**: heizen, bereit, aus

### 🔍 Diagnose (`entity_category: diagnostic`)

| Entity-ID | Name | Geräteklasse | Einheit |
|-----------|------|-------------|---------|
| `sensor.pool_controller_controller_temp` | Controller Temperature | `temperature` | °C |
| `sensor.pool_controller_heap` | Free Heap Space | — | B |
| `sensor.pool_controller_max_alloc` | Max Alloc Block | — | B |
| `sensor.pool_controller_rssi` | WiFi Signal Strength | — | dBm |
| `sensor.pool_controller_uptime` | System Uptime | `duration` | s |
| `sensor.pool_controller_local_time` | Local Time | — | — |
| `sensor.pool_controller_effective_runtime` | Effective Runtime | `duration` | s |
| `sensor.pool_controller_solar_sensor_found` | Solar Sensor Found | — | Gefunden/Fehlt |
| `sensor.pool_controller_pool_sensor_found` | Pool Sensor Found | — | Gefunden/Fehlt |

### 🧭 Sensor-Zuordnung (Konfiguration)

| Entity-ID | Name | Typ | Zweck |
|-----------|------|-----|-------|
| `select.pool_controller_solar_sensor` | Solar Sensor | Auswahl | Bestimmten DS18B20 als Solarsensor zuweisen |
| `select.pool_controller_pool_sensor` | Pool Sensor | Auswahl | Bestimmten DS18B20 als Poolsensor zuweisen |

Diese Auswahl-Entities listen alle erkannten DS18B20-Adressen auf dem OneWire-Bus auf. Verwenden Sie sie, um einen bestimmten Sensor der Solar- oder Pool-Rolle zuzuordnen, wenn mehrere Sensoren angeschlossen sind.

> **Tipp**: Überprüfen Sie nach der Auswahl eines Sensors `sensor.pool_controller_solar_sensor_found` und `sensor.pool_controller_pool_sensor_found`, um zu bestätigen, dass der Sensor erkannt wird.

---

## Dashboard erstellen (Lovelace)

### Option A: Gerät automatisch hinzufügen

1. Gehen Sie zu **Einstellungen → Geräte & Dienste → Geräte**
2. Suchen Sie **Pool Controller** in der Geräteliste
3. Klicken Sie bei jeder gewünschten Entity auf **Zu Lovelace hinzufügen**

### Option B: Manuelle Lovelace-Konfiguration

Erstellen Sie eine Ansicht in Ihrer `ui-lovelace.yaml` oder über den Lovelace-UI-Editor:

```yaml
type: vertical-stack
cards:
  - type: entities
    title: Pool Controller
    entities:
      - entity: sensor.pool_controller_pool_temp
      - entity: sensor.pool_controller_solar_temp
      - entity: select.pool_controller_mode
      - entity: switch.pool_controller_pool_pump
      - entity: switch.pool_controller_solar_pump
      - entity: sensor.pool_controller_uptime

  - type: entities
    title: Konfiguration
    entities:
      - entity: number.pool_controller_pool_max_temp
      - entity: number.pool_controller_solar_min_temp
      - entity: number.pool_controller_hysteresis
      - entity: time.pool_controller_timer_start
      - entity: time.pool_controller_timer_end

  - type: thermostat
    entity: climate.pool_controller_thermostat

  - type: entities
    title: Diagnose
    state_color: true
    entities:
      - entity: sensor.pool_controller_rssi
      - entity: sensor.pool_controller_controller_temp
      - entity: sensor.pool_controller_effective_runtime
      - entity: sensor.pool_controller_solar_sensor_found
      - entity: sensor.pool_controller_pool_sensor_found
```

### Option C: Standard-Dashboard nutzen

Der Controller erstellt Entities in der standardmäßigen **MQTT-Gerätegruppe**. Öffnen Sie **Übersicht** → klicken Sie auf die drei Punkte → **Dashboard bearbeiten** → **Karte hinzufügen** → suchen Sie nach "Pool Controller", um einzelne Entities hinzuzufügen.

---

## Automatisierungsbeispiele

### Benachrichtigung bei Zieltemperatur

```yaml
alias: "Pool Temperatur Alarm"
triggers:
  - trigger: numeric_state
    entity_id: sensor.pool_controller_pool_temp
    above: 28
actions:
  - action: notify.mobile_app
    data:
      title: "Pool ist warm! 🏊"
      message: "Pooltemperatur: {{ states('sensor.pool_controller_pool_temp') }}°C"
```

### Heizung nachts ausschalten

```yaml
alias: "Pool Heizung Nacht Aus"
triggers:
  - trigger: time
    at: "22:00:00"
conditions:
  - condition: state
    entity_id: select.pool_controller_mode
    state: auto
actions:
  - action: select.select_option
    target:
      entity_id: select.pool_controller_mode
    data:
      option: timer
```

### Neustart bei Offline-Erkennung

```yaml
alias: "Pool Controller Offline Warnung"
triggers:
  - trigger: state
    entity_id: sensor.pool_controller_uptime
    to: unavailable
    for:
      minutes: 5
actions:
  - action: notify.mobile_app
    data:
      title: "⚠️ Pool Controller Offline"
      message: "Pool Controller seit 5 Minuten nicht erreichbar"
```

### Temperaturabhängige Solarzirkulation

Die temperaturbasierte Zirkulation nutzt die Parameter des Controllers (v3.3+):

```yaml
alias: "Solarzirkulation - Voll"
triggers:
  - trigger: time_pattern
    minutes: "/15"
conditions:
  - condition: numeric_state
    entity_id: sensor.pool_controller_solar_temp
    above: 30
  - condition: numeric_state
    entity_id: number.pool_controller_pool_max_temp
    below: "{{ states('sensor.pool_controller_pool_temp') | float }}"
actions:
  - action: switch.turn_on
    target:
      entity_id: switch.pool_controller_solar_pump
```

---

## Firmware-Updates über HA

Der Pool Controller stellt eine **Update**-Entity (`update.pool_controller_firmware`) in Home Assistant bereit:

1. Gehen Sie zu **Einstellungen → Geräte & Dienste → Geräte → Pool Controller**
2. Die **Firmware**-Entity zeigt die aktuelle vs. neueste Version
3. Klicken Sie auf **Installieren**, um ein OTA-Update auszulösen
4. Der Controller lädt das Update herunter und startet automatisch neu

> **Hinweis**: Firmware-Updates erfordern eine Internetverbindung auf dem ESP32 und mindestens 2 MB freien Flash-Speicher.

---

## Fehlerbehebung

### Pool Controller erscheint nicht in Home Assistant

1. **MQTT-Broker-Verbindung prüfen**: Ist der Controller als verbunden auf dem MQTT-Broker sichtbar? (Prüfen Sie das Topic `homeassistant/sensor/pool-controller/availability` — Payload sollte `online` sein)
2. **MQTT-Integration prüfen**: Gehen Sie zu **Einstellungen → Geräte & Dienste → Integrationen → MQTT** und bestätigen Sie die Konfiguration
3. **MQTT Discovery aktiviert**: In `configuration.yaml`:
   ```yaml
   mqtt:
     discovery: true
   ```
4. **MQTT in HA neu starten**: Gehen Sie zu **Einstellungen → System → Dienste neu starten**
5. **Controller neustarten**: ESP32 stromlos schalten oder den Neustart-Knopf in der Weboberfläche verwenden

### Entities zeigen "Nicht verfügbar"

- Der Controller ist möglicherweise offline. Prüfen Sie das oben genannte `availability`-Topic
- Es könnten veraltete retain-Nachrichten vorhanden sein. Veröffentlichen Sie eine leere Payload auf dem `/config`-Topic der Entity, um veraltete Discovery zu löschen
- Prüfen Sie `homeassistant/sensor/pool-controller/availability` — es sollte eine retained `online`-Nachricht enthalten

### Pumpenschalter lassen sich nicht umschalten

Der Pool Controller **akzeptiert Pumpenbefehle nur im Manuell-Modus**. Wenn der Controller im Auto-, Boost- oder Timer-Modus ist, werden Pumpenbefehle von Home Assistant ignoriert.

Zum Umschalten der Pumpen:
1. Setzen Sie die **Operation Mode**-Auswahl auf `manu` (Manuell)
2. Jetzt sind die Schalter-Entities beschreibbar
3. Nach der manuellen Steuerung zurück auf `auto` oder einen anderen Modus schalten

### Zahlenwerte aktualisieren sich nicht

- Der Controller akzeptiert Konfigurationsänderungen (Temperaturgrenzen, Hysterese usw.) **in jedem Modus**
- Änderungen werden im Flash-Speicher des Controllers gespeichert
- Wenn Werte zurückgesetzt werden, prüfen Sie die Weboberfläche des Controllers: **Status → Letzter Fehler**

### Sensorzuordnung zeigt keine Optionen

Die Entities `select.pool_controller_solar_sensor` und `select.pool_controller_pool_sensor` werden erst befüllt, nachdem der Controller seinen OneWire-Bus-Scan abgeschlossen hat. Dies geschieht:
- Beim Start (nachdem WiFi verbunden ist)
- Wenn Sie in der Weboberfläche auf **Neu scannen** klicken

Wenn keine DS18B20-Sensoren angeschlossen sind, zeigen diese Entities nur die Option `— Not configured —` an.
