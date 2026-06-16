---
title: Firmware Migration (v2.x → v3.x)
weight: 50
tags: ["docs", "migration", "homie", "firmware"]
---

**🏊 Smart Swimming Pool: Migrate from the old Homie 3.0 format to the new MQTT Discovery format**

If you are running the **Pool Controller v2.x** (or earlier) and plan to upgrade to **v3.x**, this guide explains what changes and how to update your smart home integration.

> 💡 **New user?** If you are installing the pool controller for the first time, follow the [Getting Started](/docs/getting-started/) guide instead. This guide is only relevant if you have an existing Homie 3.0 setup.

---

## Overview

| Aspect | v2.x (Homie 3.0) | v3.x (HA Discovery) |
|--------|------------------|---------------------|
| **MQTT topic format** | `homie/<mac>/<node>/<property>` | `homeassistant/<component>/pool-controller/<id>/state` |
| **Device identifier** | MAC address (e.g., `5ccf7fb97572`) | `pool-controller` (configurable) |
| **Availability** | `homie/<mac>/$state` (`ready`/`lost`) | `homeassistant/sensor/pool-controller/availability` (`online`/`offline`) |
| **Home Assistant** | Limited support, manual config | **Native** — auto-discovery via MQTT |
| **openHAB** | Full support (native configuration) | Manual MQTT configuration required |

---

## Why the Change?

The switch from Homie 3.0 to [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) was driven by two goals:

1. **Zero-config for Home Assistant users** — HA auto-discovers all entities, no manual configuration needed
2. **Standardization** — HA Discovery is the de-facto standard for MQTT-based IoT devices, while Homie 3.0 never gained broad adoption

openHAB remains fully supported via manual MQTT configuration.

---

## Firmware Upgrade

### Step 1: Flash v3.x

Follow the standard flashing procedure in the [Getting Started](/docs/getting-started/#firmware-installation) guide:

```bash
# In VS Code with PlatformIO:
# 1. Upload the firmware
# 2. Upload the filesystem image (LittleFS/web interface)
```

> ⚠️ **Important**: After flashing v3.x, the web interface is **fully rewritten**. Settings from the old web UI are **not** carried over. You must reconfigure WiFi and MQTT via the setup AP (`Pool-Controller-Setup`).

### Step 2: Reconfigure WiFi and MQTT

1. After flashing, the ESP32 starts in AP mode (`Pool-Controller-Setup`)
2. Connect to it and configure your WiFi at `http://192.168.4.1`
3. After reboot, configure MQTT via **Configuration → MQTT**

### Step 3: Reapply Configuration Parameters

After migration, reconfigure these parameters in the web interface (or via Home Assistant):

- Max. Pool Temperature
- Min. Solar Temperature
- Hysteresis
- Timer Start / End
- Sensor addresses (DS18B20)

---

## Migration by Smart Home Platform

### Home Assistant Users

**You're done after Step 2.** The v3.x firmware auto-discovers via MQTT.

1. Go to **Settings → Devices & Services**
2. The **Pool Controller** device should appear automatically
3. See the [Home Assistant Integration Guide](/docs/home-assistant-integration/) for the complete entity reference

> **Note**: If you had manually configured MQTT sensors in Home Assistant for the Homie topics, those will show as **unavailable** after the upgrade. Remove them manually — the auto-discovered entities replace them.

### openHAB Users

openHAB requires **manual MQTT configuration**. The [openHAB Integration Guide](/docs/openhab-integration/) shows the complete setup.

#### What needs to change

| File | Change |
|------|--------|
| `things/mqtt.things` | All topic paths: `homie/<mac>/...` → `homeassistant/...` |
| `items/2-pool.items` | Channel bindings: update topic references |
| `sitemaps/pool.sitemap` | Usually no change (item names stay the same) |

#### Topic mapping reference

| v2.x Homie Topic | v3.x HA Discovery Topic |
|-------------------|------------------------|
| `homie/<mac>/operation-mode/mode` | `homeassistant/select/pool-controller/mode/state` |
| `homie/<mac>/operation-mode/mode/set` | `homeassistant/select/pool-controller/mode/set` |
| `homie/<mac>/operation-mode/pool-max-temp` | `homeassistant/number/pool-controller/pool-max-temp/state` |
| `homie/<mac>/operation-mode/pool-max-temp/set` | `homeassistant/number/pool-controller/pool-max-temp/set` |
| `homie/<mac>/operation-mode/solar-min-temp` | `homeassistant/number/pool-controller/solar-min-temp/state` |
| `homie/<mac>/operation-mode/solar-min-temp/set` | `homeassistant/number/pool-controller/solar-min-temp/set` |
| `homie/<mac>/operation-mode/hysteresis` | `homeassistant/number/pool-controller/hysteresis/state` |
| `homie/<mac>/operation-mode/hysteresis/set` | `homeassistant/number/pool-controller/hysteresis/set` |
| `homie/<mac>/pool-pump/switch` | `homeassistant/switch/pool-controller/pool-pump/state` |
| `homie/<mac>/pool-pump/switch/set` | `homeassistant/switch/pool-controller/pool-pump/set` |
| `homie/<mac>/solar-pump/switch` | `homeassistant/switch/pool-controller/solar-pump/state` |
| `homie/<mac>/solar-pump/switch/set` | `homeassistant/switch/pool-controller/solar-pump/set` |
| `homie/<mac>/pool-temp/temperature` | `homeassistant/sensor/pool-controller/pool-temp/state` |
| `homie/<mac>/solar-temp/temperature` | `homeassistant/sensor/pool-controller/solar-temp/state` |

#### Key changes in values

| Aspect | v2.x (Homie) | v3.x (HA Discovery) |
|--------|-------------|---------------------|
| Pump ON value | `true` | `ON` |
| Pump OFF value | `false` | `OFF` |
| Availability online | `ready` | `online` |
| Availability offline | `lost` | `offline` |

---

## Breaking Changes

### 1. Timer entities restructured

**v2.x**: 4 separate `number` entities for timer start/end (hours + minutes each)

```
homie/<mac>/operation-mode/timer-start-h
homie/<mac>/operation-mode/timer-start-min
homie/<mac>/operation-mode/timer-end-h
homie/<mac>/operation-mode/timer-end-min
```

**v3.x**: 2 `time` entities with `HH:MM:SS` format

```
homeassistant/time/pool-controller/timer-start
homeassistant/time/pool-controller/timer-end
```

The old entities are automatically removed from Home Assistant when v3.x starts (empty retained payloads are published to their config topics).

### 2. Timezone entity changed

**v2.x**: `number` entity with timezone index (e.g., `0`, `1`, ...)

**v3.x**: `select` entity with human-readable timezone labels (e.g., `Europe/Berlin`, `America/New_York`)

### 3. Temperature-based circulation (new in v3.3+)

v3.3 added three new configuration parameters for temperature-controlled circulation:

- `temp-circ-threshold` — minimum temperature difference to trigger circulation
- `temp-circ-factor` — runtime multiplier per degree above threshold
- `temp-circ-max-runtime` — maximum circulation runtime

These did not exist in v2.x and have no Homie equivalent.

### 4. Device identifier is now configurable

In v2.x, the device ID was **always** the MAC address (`5ccf7fb97572`). In v3.x, the default device ID is `pool-controller`, but you can **change it** in **Configuration → MQTT → Device ID** in the web interface.

If you change it, update all topic paths accordingly.

### 5. No Homie-compatibility mode

The v3.x firmware **only** supports Home Assistant MQTT Discovery. There is no Homie 3.0 backward-compatibility mode. If you need Homie for custom integrations, stay on v2.x.

---

## Rollback

If you need to revert to v2.x:

1. Flash the v2.x firmware using PlatformIO
2. Reconfigure WiFi and MQTT (v2.x also uses the setup AP)
3. The old Homie topics become active again
4. openHAB or Home Assistant will reconnect automatically

> **Note**: The v3.x flash erases the LittleFS filesystem partition. v2.x may store configuration differently. Expect to reconfigure all settings after downgrading.

---

## Older Firmware Versions

| Version | MQTT Format | Status |
|---------|-------------|--------|
| **1.x** | Proprietary JSON | No longer supported |
| **2.x** | Homie 3.0 | Legacy — update recommended |
| **3.x** | HA Discovery | Current — recommended for all users |
