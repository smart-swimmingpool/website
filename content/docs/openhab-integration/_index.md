---
title: openHAB Integration
weight: 15
tags: ["docs", "openHAB", "tutorial"]
---

**🏊 Smart Swimming Pool: Integrate the Pool Controller with openHAB**

Unlike [Home Assistant](/docs/getting-started/#step-4-home-assistant-integration), which automatically discovers the pool controller via MQTT Discovery, openHAB requires **manual configuration**. This guide walks you through the process step by step.

> 💡 **Already using openHAB?**  
> The [openHAB Configuration](/docs/openhab-configuration/) page contains the complete reference files (Things, Items, Sitemap). This guide explains *how* to set them up and adapt them to your system.

---

## Prerequisites

Before you begin, make sure you have:

1. **The pool controller** flashed and running on your network (see [Getting Started](/docs/getting-started/))
2. **An MQTT broker** (e.g., [Mosquitto](https://mosquitto.org/)) — install one on the same machine as openHAB or on your network
3. **openHAB** (version 3 or 4) running and accessible via its web interface

---

## Step 1: Install the MQTT Binding

In the openHAB web interface:

1. Go to **Settings → Add-ons → Bindings**
2. Search for **"MQTT"**
3. Install the **MQTT Binding** (official binding by the openHAB project)
4. No restart is required — the binding activates immediately

---

## Step 2: Configure the MQTT Broker Thing

1. Go to **Settings → Things**
2. Click **+** (Add Thing)
3. Search for **"MQTT"** and select **MQTT Broker**
4. Configure:
   - **Host**: IP address of your MQTT broker (e.g., `192.168.1.100` or `core-mosquitto`)
   - **Port**: `1883` (default, unencrypted)
   - **Client ID**: `openHAB-pool` (must be unique on your broker)
   - **Username/Password**: Only if your broker requires authentication
5. Click **Create Thing**

The Broker thing should come **Online** within seconds. If it doesn't, check that your MQTT broker is running and reachable.

---

## Step 3: Discover the MQTT Topics

The pool controller v3.x publishes its data using [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) format. You need to find the **exact topics** your controller publishes to configure openHAB correctly.

### Option A: MQTT Explorer (Recommended)

Install [MQTT Explorer](http://mqtt-explorer.com/) on your computer:

1. Connect to your MQTT broker (host, port — same as above)
2. Browse to the `homeassistant/` prefix
3. You'll see topics organized by entity type:
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

Each entity has:
- `config` — discovery payload with metadata
- `state` — current value
- `set` — command topic (for writable entities)

### Option B: Command Line (mosquitto_sub)

If you prefer the terminal:

```bash
# Subscribe to all pool controller topics
mosquitto_sub -h <broker-ip> -t "homeassistant/#" -v

# Or filter for pool controller specifically
mosquitto_sub -h <broker-ip> -t "homeassistant/+/pool-controller/#" -v
```

> ⚠️ **Note**: Your controller's device ID may differ from `pool-controller` if you changed the **MQTT Device ID** in the pool controller's web interface. Adjust the topic prefix accordingly.

---

## Step 4: Create a Thing File

openHAB 3+ uses **`.things` files** in `$OPENHAB_CONF/things/` to define MQTT topic Things.

Create `$OPENHAB_CONF/things/pool-controller.things`:

```java
Bridge mqtt:broker:mosquitto "Mosquitto" [ host="127.0.0.1", port=1883, secure=false, clientID="openHAB-pool" ]
{
    Thing topic pool-controller "Pool Controller" @ "Outside" {
        Channels:
            // Operation Mode
            Type string : operationMode "Operation Mode"
                [ stateTopic="homeassistant/select/pool-controller/operation_mode/state",
                  commandTopic="homeassistant/select/pool-controller/operation_mode/set" ]

            // Configuration Numbers
            Type number : maxPoolTemp "Max Pool Temperature"
                [ stateTopic="homeassistant/number/pool-controller/pool_max_temp/state",
                  commandTopic="homeassistant/number/pool-controller/pool_max_temp/set" ]
            Type number : minSolarTemp "Min Solar Temperature"
                [ stateTopic="homeassistant/number/pool-controller/solar_min_temp/state",
                  commandTopic="homeassistant/number/pool-controller/solar_min_temp/set" ]
            Type number : hysteresis "Hysteresis"
                [ stateTopic="homeassistant/number/pool-controller/hysteresis/state",
                  commandTopic="homeassistant/number/pool-controller/hysteresis/set" ]
            Type number : timerStartH "Timer Start Hour"
                [ stateTopic="homeassistant/number/pool-controller/timer_start_h/state",
                  commandTopic="homeassistant/number/pool-controller/timer_start_h/set" ]
            Type number : timerStartM "Timer Start Minute"
                [ stateTopic="homeassistant/number/pool-controller/timer_start_m/state",
                  commandTopic="homeassistant/number/pool-controller/timer_start_m/set" ]
            Type number : timerEndH "Timer End Hour"
                [ stateTopic="homeassistant/number/pool-controller/timer_end_h/state",
                  commandTopic="homeassistant/number/pool-controller/timer_end_h/set" ]
            Type number : timerEndM "Timer End Minute"
                [ stateTopic="homeassistant/number/pool-controller/timer_end_m/state",
                  commandTopic="homeassistant/number/pool-controller/timer_end_m/set" ]

            // Pumps
            Type switch : poolPump "Pool Pump"
                [ stateTopic="homeassistant/switch/pool-controller/pool_pump/state",
                  commandTopic="homeassistant/switch/pool-controller/pool_pump/set" ]
            Type switch : solarPump "Solar Pump"
                [ stateTopic="homeassistant/switch/pool-controller/solar_pump/state",
                  commandTopic="homeassistant/switch/pool-controller/solar_pump/set" ]

            // Temperatures
            Type number : poolTemp "Pool Temperature"
                [ stateTopic="homeassistant/sensor/pool-controller/pool_temp/state" ]
            Type number : solarTemp "Solar Temperature"
                [ stateTopic="homeassistant/sensor/pool-controller/solar_temp/state" ]

            // System Info
            Type number : signal "WiFi Signal"
                [ stateTopic="homeassistant/sensor/pool-controller/signal/state" ]
            Type number : uptime "Uptime"
                [ stateTopic="homeassistant/sensor/pool-controller/uptime/state" ]
            Type string : fwVersion "Firmware Version"
                [ stateTopic="homeassistant/sensor/pool-controller/fw_version/state" ]
    }
}
```

> **Replace `pool-controller`** in the topic paths with your actual device ID if you changed it.

---

## Step 5: Create an Items File

Items link the MQTT channels to openHAB items that can be displayed on UIs and used in rules.

Create `$OPENHAB_CONF/items/pool-controller.items`:

```java
// Groups
Group gPool_Controller "Pool Controller" <swimmingpool>

// Operation Mode
String Pool_OpMode "Operation Mode [%s]" <settings> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:operationMode", autoupdate="true" }

// Configuration
Number Pool_MaxTemp "Max Pool Temp [%.1f °C]" <heating> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:maxPoolTemp", autoupdate="true" }
Number Pool_MinSolarTemp "Min Solar Temp [%.1f °C]" <heating> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:minSolarTemp", autoupdate="true" }
Number Pool_Hysteresis "Hysteresis [%.1f K]" <line> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:hysteresis", autoupdate="true" }

Number Pool_Timer_Start_H "Timer Start Hour [%.0f h]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerStartH", autoupdate="true" }
Number Pool_Timer_Start_M "Timer Start Min [%.0f m]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerStartM", autoupdate="true" }
Number Pool_Timer_End_H "Timer End Hour [%.0f h]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerEndH", autoupdate="true" }
Number Pool_Timer_End_M "Timer End Min [%.0f m]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:timerEndM", autoupdate="true" }

// Pumps
Switch Pool_PoolPump "Pool Pump" <pump> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:poolPump", autoupdate="false" }
Switch Pool_SolarPump "Solar Pump" <solarplant> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:solarPump", autoupdate="false" }

// Temperatures
Number Pool_PoolTemp "Pool Temperature [%.1f °C]" <temperature> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:poolTemp", autoupdate="false" }
Number Pool_SolarTemp "Solar Temperature [%.1f °C]" <temperature> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:solarTemp", autoupdate="false" }

// System
Number Pool_Signal "WiFi Signal [%.0f%%]" <network> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:signal", autoupdate="false" }
Number Pool_Uptime "Uptime [%d s]" <time> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:uptime", autoupdate="false" }
String Pool_FWVersion "Firmware [%s]" <text> (gPool_Controller)
    { channel="mqtt:topic:mosquitto:pool-controller:fwVersion", autoupdate="false" }
```

### Channel UID Format

The channel UID follows this pattern:

```
mqtt:topic:<broker-thing-id>:<thing-id>:<channel-id>
```

- `mqtt:topic` — fixed prefix for MQTT topic Things
- `mosquitto` — your broker Thing's ID (as defined in the .things file)
- `pool-controller` — your topic Thing's ID
- `poolTemp` — the channel name from the .things file

---

## Step 6: Create a Sitemap

Sitemaps define what appears on the openHAB BasicUI and mobile apps.

Create or edit `$OPENHAB_CONF/sitemaps/pool.sitemap`:

```perl
sitemap pool label="Pool Controller" {
    Frame label="Control" {
        Switch item=Pool_OpMode label="Mode" icon="settings"
            mappings=[auto="Auto", manu="Manual", boost="Boost", timer="Timer"]

        Text item=Pool_PoolPump label="Pool Pump [%s]" icon="pump"
            visibility=[Pool_OpMode==auto, Pool_OpMode==boost, Pool_OpMode==timer]
        Switch item=Pool_PoolPump label="Pool Pump" icon="pump"
            visibility=[Pool_OpMode==manu]

        Text item=Pool_SolarPump label="Solar Pump [%s]" icon="solarplant"
            visibility=[Pool_OpMode==auto, Pool_OpMode==boost, Pool_OpMode==timer]
        Switch item=Pool_SolarPump label="Solar Pump" icon="solarplant"
            visibility=[Pool_OpMode==manu]
    }

    Frame label="Temperatures" {
        Text item=Pool_PoolTemp label="Pool [%.1f °C]" icon="temperature"
            valuecolor=[>30="orange", >20="green", <=20="blue"]
        Text item=Pool_SolarTemp label="Solar [%.1f °C]" icon="temperature"
            valuecolor=[>30="orange", >20="green", <=20="blue"]
    }

    Frame label="Settings" {
        Frame label="Timer" {
            Setpoint item=Pool_Timer_Start_H label="Start Hour [%.0f]" icon="time" minValue=0 maxValue=23 step=1
            Setpoint item=Pool_Timer_Start_M label="Start Minute [%02.0f]" minValue=0 maxValue=59 step=5
            Setpoint item=Pool_Timer_End_H label="End Hour [%.0f]" icon="time" minValue=0 maxValue=23 step=1
            Setpoint item=Pool_Timer_End_M label="End Minute [%02.0f]" minValue=0 maxValue=59 step=5
        }
        Frame label="Configuration" {
            Setpoint item=Pool_MaxTemp label="Max Pool Temp [%.0f °C]" icon="heating" minValue=0 maxValue=40 step=1
            Setpoint item=Pool_MinSolarTemp label="Min Solar Temp [%.0f °C]" icon="heating" minValue=0 maxValue=100 step=1
            Setpoint item=Pool_Hysteresis label="Hysteresis [%.1f K]" icon="line" minValue=0 maxValue=10 step=0.5
        }
        Frame label="System" {
            Text item=Pool_Uptime label="Uptime"
            Text item=Pool_Signal label="WiFi Signal [%.0f %%]"
            Text item=Pool_FWVersion label="Firmware"
        }
    }
}
```

---

## Step 7: Verify Everything Works

1. **Check Things**: Go to **Settings → Things** in the openHAB UI. The `Pool Controller` Thing should show **Online**.
2. **Check Items**: Open **Settings → Items** and verify all items are present with values.
3. **Open the Sitemap**: Navigate to `http://<openhab-ip>:8080/basicui/app?sitemap=pool` or use the openHAB mobile app.

If items show as **NULL** or **Undefined**:
- Verify the MQTT topics match what your controller publishes (use MQTT Explorer to double-check)
- Ensure the broker Thing is Online
- Check `$OPENHAB_CONF/userdata/logs/openhab.log` for MQTT-related errors

---

## Configuration Files

The complete reference configuration lives in the **[openhab-config repository](https://github.com/smart-swimmingpool/openhab-config)** on GitHub:

| File | Purpose |
|------|---------|
| [`things/mqtt.things`](https://github.com/smart-swimmingpool/openhab-config/blob/main/things/mqtt.things) | MQTT Broker and Topic Things |
| [`items/2-pool.items`](https://github.com/smart-swimmingpool/openhab-config/blob/main/items/2-pool.items) | Item definitions linked to channels |
| [`sitemaps/pool.sitemap`](https://github.com/smart-swimmingpool/openhab-config/blob/main/sitemaps/pool.sitemap) | BasicUI and mobile app layout |

> **Note**: The openhab-config repository currently references **Homie 3.0** MQTT topics (for controller v2.x). If you are running controller v3.x, adapt the topics to the `homeassistant/` format shown in this guide. See the [Firmware Migration](/docs/firmware-migration/) guide for details.

---

## Troubleshooting

### Things stay OFFLINE

- **Check network connectivity**: Can your openHAB server reach the MQTT broker? (`ping <broker-ip>`)
- **Check credentials**: If your broker requires authentication, verify username/password in the Broker Thing
- **Check the logs**: Run `tail -f $OPENHAB_CONF/userdata/logs/openhab.log | grep -i mqtt` for real-time diagnostics

### Items show "—" (no value)

- The topic names in your `.things` file might not match the controller's actual topics
- Use MQTT Explorer to subscribe to `homeassistant/#` and compare
- The controller publishes numeric values as plain numbers (e.g., `25.5`) — no transformation is needed

### Commands don't reach the controller

- Verify that `commandTopic` is specified in your `.things` file for writable channels
- Check that the controller is connected to the MQTT broker (green LED on, or check the web interface)
- Test manually: `mosquitto_pub -h <broker-ip> -t "homeassistant/switch/pool-controller/pool_pump/set" -m "ON"`

### Wrong MQTT Device ID

The default device ID is `pool-controller`. If you changed it in the controller's web interface (**Configuration → MQTT → Device ID**), update all topic paths in your `.things` file to match.
