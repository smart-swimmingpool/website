---
title: Home Assistant Integration
weight: 14
tags: ["docs", "home-assistant", "tutorial"]
---

**🏊 Smart Swimming Pool: Integrate the Pool Controller with Home Assistant**

The Pool Controller v3.x integrates with Home Assistant through **native [MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery)**. When connected to your MQTT broker, the controller automatically registers all its sensors, controls, and configuration parameters as Home Assistant entities — no manual configuration required.

> 💡 **First time setting up the pool controller?**  
> Follow the [Getting Started](/docs/getting-started/) guide first, which covers flashing the firmware, WiFi configuration, and MQTT setup.

---

## Prerequisites

Before the pool controller can appear in Home Assistant:

1. **Home Assistant** with the **[MQTT integration](https://www.home-assistant.io/integrations/mqtt/)** configured (broker connection)
2. **Pool Controller** connected to the **same MQTT broker** (configured via its web interface: **Configuration → MQTT**)
3. **MQTT Discovery enabled** in Home Assistant (`discovery: true` in `configuration.yaml` — enabled by default)

---

## How It Works

On startup and when MQTT connects, the pool controller publishes **discovery payloads** to topics like:

```
homeassistant/sensor/pool-controller/pool-temp/config
homeassistant/switch/pool-controller/pool-pump/config
homeassistant/select/pool-controller/mode/config
...
```

Home Assistant listens on `homeassistant/+/+/config` by default, automatically creating entities from these payloads. All entities are grouped under a single **Pool Controller** device.

### Device Info

The controller identifies itself with:

| Property | Value |
|----------|-------|
| **Name** | Pool Controller |
| **Manufacturer** | smart-swimmingpool |
| **Model** | Pool Controller |
| **Identifiers** | `pool_controller_<mac-suffix>` (unique per device) |

---

## Complete Entity Reference

When the pool controller connects, it creates the following entities in Home Assistant:

### 📊 Primary Sensors

These appear on the device's front page (no `entity_category`):

| Entity ID | Name | Device Class | Unit |
|-----------|------|-------------|------|
| `sensor.pool_controller_pool_temp` | Pool Temperature | `temperature` | °C |
| `sensor.pool_controller_solar_temp` | Solar Temperature | `temperature` | °C |

### 🛠️ Controls (Switches & Select)

| Entity ID | Name | Type | Notes |
|-----------|------|------|-------|
| `switch.pool_controller_pool_pump` | Pool Pump | Switch | Writable only in **Manual** mode |
| `switch.pool_controller_solar_pump` | Solar Pump | Switch | Writable only in **Manual** mode |
| `select.pool_controller_mode` | Operation Mode | Select | Options: auto, manu, boost, timer |

### 🔧 Configuration Parameters (`entity_category: config`)

| Entity ID | Name | Type | Unit | Range |
|-----------|------|------|------|-------|
| `number.pool_controller_pool_max_temp` | Max. Pool Temp | Number | °C | 0–40 |
| `number.pool_controller_solar_min_temp` | Min. Solar Temp | Number | °C | 0–100 |
| `number.pool_controller_hysteresis` | Temperature Hysteresis | Number | K | 0–10 |
| `number.pool_controller_temp_circ_threshold` | Circ. Temp Threshold | Number | °C | 0–40 |
| `number.pool_controller_temp_circ_factor` | Circ. Temp Factor | Number | min/°C | 0–120 |
| `number.pool_controller_temp_circ_max_runtime` | Circ. Max Runtime | Number | min | 60–1440 |
| `time.pool_controller_timer_start` | Timer Start | Time | — | HH:MM:SS |
| `time.pool_controller_timer_end` | Timer End | Time | — | HH:MM:SS |
| `select.pool_controller_timezone` | Timezone | Select | — | (dynamic list) |
| `text.pool_controller_ntp_server` | NTP Server | Text | — | — |
| `update.pool_controller_firmware` | Firmware | Update | — | — |
| `climate.pool_controller_thermostat` | Pool Thermostat | Climate | °C | 0–40 |

The **Climate** entity (`climate.pool_controller_thermostat`) provides a thermostat-style control:
- **HVAC modes**: off, auto, heat
- **Current temperature**: pool water temperature
- **Target temperature**: maps to Max. Pool Temp
- **Action**: heating, idle, off

### 🔍 Diagnostics (`entity_category: diagnostic`)

| Entity ID | Name | Device Class | Unit |
|-----------|------|-------------|------|
| `sensor.pool_controller_controller_temp` | Controller Temperature | `temperature` | °C |
| `sensor.pool_controller_heap` | Free Heap Space | — | B |
| `sensor.pool_controller_max_alloc` | Max Alloc Block | — | B |
| `sensor.pool_controller_rssi` | WiFi Signal Strength | — | dBm |
| `sensor.pool_controller_uptime` | System Uptime | `duration` | s |
| `sensor.pool_controller_local_time` | Local Time | — | — |
| `sensor.pool_controller_effective_runtime` | Effective Runtime | `duration` | s |
| `sensor.pool_controller_solar_sensor_found` | Solar Sensor Found | — | Found/Missing |
| `sensor.pool_controller_pool_sensor_found` | Pool Sensor Found | — | Found/Missing |

### 🧭 Sensor Mapping (Configuration)

| Entity ID | Name | Type | Purpose |
|-----------|------|------|---------|
| `select.pool_controller_solar_sensor` | Solar Sensor | Select | Assign a specific DS18B20 as solar sensor |
| `select.pool_controller_pool_sensor` | Pool Sensor | Select | Assign a specific DS18B20 as pool sensor |

These select entities list all detected DS18B20 addresses on the OneWire bus. Use them to pin a specific sensor to the solar or pool role when multiple sensors are connected.

> **Tip**: After selecting a sensor, check `sensor.pool_controller_solar_sensor_found` and `sensor.pool_controller_pool_sensor_found` to confirm the sensor is detected.

---

## Creating a Dashboard (Lovelace)

### Option A: Add Device Automatically

1. Go to **Settings → Devices & Services → Devices**
2. Find **Pool Controller** in the device list
3. Click **Add to Lovelace** on each entity you want to display

### Option B: Manual Lovelace Configuration

Create a view in your `ui-lovelace.yaml` or via the Lovelace UI editor:

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
    title: Configuration
    entities:
      - entity: number.pool_controller_pool_max_temp
      - entity: number.pool_controller_solar_min_temp
      - entity: number.pool_controller_hysteresis
      - entity: time.pool_controller_timer_start
      - entity: time.pool_controller_timer_end

  - type: thermostat
    entity: climate.pool_controller_thermostat

  - type: entities
    title: Diagnostics
    state_color: true
    entities:
      - entity: sensor.pool_controller_rssi
      - entity: sensor.pool_controller_controller_temp
      - entity: sensor.pool_controller_effective_runtime
      - entity: sensor.pool_controller_solar_sensor_found
      - entity: sensor.pool_controller_pool_sensor_found
```

### Option C: Use the Default Dashboard

The controller creates entities in the default **MQTT device** group. Open **Overview** → click the three dots → **Edit dashboard** → **Add card** → search for "Pool Controller" to add entities individually.

---

## Automation Examples

### Notify When Pool Reaches Target Temperature

```yaml
alias: "Pool Temperature Alert"
triggers:
  - trigger: numeric_state
    entity_id: sensor.pool_controller_pool_temp
    above: 28
actions:
  - action: notify.mobile_app
    data:
      title: "Pool is warm! 🏊"
      message: "Pool temperature is {{ states('sensor.pool_controller_pool_temp') }}°C"
```

### Turn Off Heating at Night

```yaml
alias: "Pool Heating Night Off"
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

### Restart Controller if Offline

```yaml
alias: "Pool Controller Offline Alert"
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
      message: "Pool controller has been unreachable for 5 minutes"
```

### Energy-Based Solar Circulation

Using the temperature-based circulation parameters (requires controller v3.3+):

```yaml
alias: "Solar Circulation - Full"
triggers:
  - trigger: time_pattern
    minutes: "/15"
conditions:
  - condition: numeric_state
    entity_id: sensor.pool_controller_solar_temp
    above: 30
  - condition: template
    value_template: "{{ states('sensor.pool_controller_pool_temp') | float < states('number.pool_controller_pool_max_temp') | float }}"
actions:
  - action: switch.turn_on
    target:
      entity_id: switch.pool_controller_solar_pump
```

---

## Firmware Updates via HA

The pool controller exposes an **Update** entity (`update.pool_controller_firmware`) in Home Assistant:

1. Go to **Settings → Devices & Services → Devices → Pool Controller**
2. The **Firmware** entity shows the current vs. latest version
3. Click **Install** to trigger an OTA update
4. The controller downloads the update and reboots automatically

> **Note**: Firmware updates require an internet connection on the ESP32 and at least 2MB of free flash space.

---

## Troubleshooting

### Pool Controller device doesn't appear in Home Assistant

1. **Check MQTT broker connection**: Does the controller show as connected on the MQTT broker? (Check `homeassistant/sensor/pool-controller/availability` topic — payload should be `online`)
2. **Verify MQTT integration**: Go to **Settings → Devices & Services → Integrations → MQTT** and confirm it's configured
3. **Check MQTT Discovery is enabled**: In `configuration.yaml`:
   ```yaml
   mqtt:
     discovery: true
   ```
4. **Restart MQTT** in Home Assistant: Go to **Settings → System → Restart Services**
5. **Reboot the controller**: Power-cycle the ESP32 or use the web interface's reboot button

### Entities show as "Unavailable"

- The controller may be offline. Check the `availability` topic mentioned above
- Messages might be retained from a previous instance. Publish an empty payload to the entity's `/config` topic to clear stale discovery
- Check `homeassistant/sensor/pool-controller/availability` — it should carry a retained `online` message

### Pump switches don't toggle

The pool controller **only accepts pump commands in Manual mode**. If the controller is in Auto, Boost, or Timer mode, pump commands from Home Assistant are ignored.

To toggle pumps:
1. Set **Operation Mode** select to `manu` (Manual)
2. Now the switch entities are writable
3. After manual control, switch back to `auto` or another mode to resume automated operation

### Numbers don't update when changed

- The controller accepts configuration changes (temperature limits, hysteresis, etc.) **in any mode**
- Changes are persisted to the controller's flash memory
- If values revert, check the controller's web interface: **Status → Last Error**

### Sensor mapping switches don't show options

The `select.pool_controller_solar_sensor` and `select.pool_controller_pool_sensor` entities only populate after the controller has completed its OneWire bus scan. This happens:
- On startup (after WiFi connects)
- When you press **Rescan** from the web interface

If no DS18B20 sensors are connected, these entities will only show the `— Not configured —` option.
