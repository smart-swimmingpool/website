---
title: Commissioning Checklist
weight: 11
tags: ["docs", "checklist", "safety", "commissioning"]
---

**🏊 Smart Swimming Pool: Step-by-step checklist for first-time setup and commissioning.**

Use this checklist **before** connecting pumps to mains voltage. Tick off each item to ensure a safe and successful first run.

{{< safety-notice type="230v" >}}

---

## 1. Hardware Assembly

### 1.1 Controller Electronics

- [ ] ESP32 firmly seated on breadboard or perfboard
- [ ] Relay module connected: **VCC → 5V** (not 3.3V!), **GND → GND**
- [ ] Relay IN1 (GPIO26) prepared for **heating circuit pump**
- [ ] Relay IN2 (GPIO25) prepared for **filter/circulation pump**
- [ ] DS18B20 solar sensor: **DATA → GPIO32**, **VDD → 3.3V**, **GND → GND**
- [ ] DS18B20 pool sensor: **DATA → GPIO33**, **VDD → 3.3V**, **GND → GND**
- [ ] **4.7kΩ pull-up resistor** between each DATA pin and 3.3V (2 resistors total)
- [ ] No shorts between adjacent pins on the breadboard

### 1.2 Power Supply

- [ ] USB power supply: **5V / 1A minimum** (quality brand, not a phone charger from a discount store)
- [ ] USB cable is a **data cable** (not charge-only)
- [ ] Power supply is in a **dry location** or IP-rated enclosure

### 1.3 Enclosure (if used)

- [ ] Enclosure is **IP54 or better** for outdoor / pool house installation
- [ ] Cable glands (PG fittings) installed for all cable entries
- [ ] Ventilation openings if enclosure traps heat
- [ ] Strain relief on all cables entering the enclosure

---

## 2. 230V / Mains Side

> ⚠️ **Danger to life!** Work on 230V circuits must only be performed by qualified personnel. Observe all applicable electrical codes.

- [ ] **RCD / FI circuit breaker** installed in the supply line (mandatory!)
- [ ] **Circuit breaker** (MCB) with appropriate rating for each pump
- [ ] Cable cross-section adequate for pump current draw
- [ ] All connections in a **junction box** or distribution board
- [ ] **Pumps are NOT connected to the relay outputs yet** — test without 230V first
- [ ] If available: use a mains tester to verify the 230V wiring before connecting pumps

---

## 3. Firmware & First Boot

- [ ] PlatformIO project opened, environment set to **esp32dev**
- [ ] Firmware uploaded successfully: `pio run -e esp32dev -t upload`
- [ ] Filesystem image uploaded: `pio run -e esp32dev -t uploadfs`
- [ ] Serial monitor shows boot log at **115200 baud**
- [ ] ESP32 starts in AP mode:
  ```
  [INFO] Pool Controller v3.x.x starting...
  [INFO] WiFi: Starting in AP mode
  [INFO] AP: 'Pool-Controller-Setup'. IP: 192.168.4.1
  ```

### 3.1 If Boot Fails

| Symptom | Likely Cause | Check |
|---------|-------------|-------|
| No output on serial monitor | Wrong baud rate or USB cable | Set monitor to 115200 baud; try a data USB cable |
| Continuous reboot loop | Power supply too weak | Use 5V/1A+, quality brand |
| `ets` boot message then restart | Flash settings wrong | Ensure DIO mode, 4MB flash size |
| "Failed to connect to ESP32" | Wrong COM port or BOOT not held | Hold BOOT during flash start |

---

## 4. Temperature Sensors

- [ ] After boot, serial monitor shows detected DS18B20 sensors:
  ```
  [INFO] OneWire: Found 2 DS18B20 sensor(s)
  [INFO] DS18B20[0]: 28-xxxxxxxxxxxx (Solar sensor on GPIO32)
  [INFO] DS18B20[1]: 28-yyyyyyyyyyyy (Pool sensor on GPIO33)
  ```
- [ ] Both sensors read plausible temperatures (not `-127°C` or `85°C`)
- [ ] Warm one sensor by holding it — reading rises within seconds
- [ ] If only 1 sensor found: check wiring, pull-up resistor, or try the sensor alone

### 4.1 Temperature Sensor Quick Check

| Reading | Meaning | Action |
|---------|---------|--------|
| `-127°C` | Sensor not found on bus | Check DATA wire, pull-up resistor, GPIO pin |
| `85°C` | Sensor stuck at power-on default | Check for parasite power; all 3 wires must be connected |
| Erratic / jumping values | Electrical interference | Keep sensor cable >30cm away from 230V wiring |
| Both sensors identical | Normal if in same water | Verify with hand warmth test (see above) |

---

## 5. WiFi & Network

- [ ] Connected to `Pool-Controller-Setup` WiFi network
- [ ] Web interface reachable at **http://192.168.4.1**
- [ ] Home WiFi configured in web interface → **Connection** section
- [ ] ESP32 rebooted and connected to home network
- [ ] New IP address noted (from router DHCP or serial monitor)
- [ ] Web interface reachable at **http://<new-ip>/**
- [ ] ESP32 pingable from your computer: `ping <new-ip>`

---

## 6. MQTT Connection

### Prerequisites

- [ ] MQTT broker (Mosquitto) is installed and running
- [ ] Broker is reachable from the ESP32's network (same subnet or firewall rule for port 1883)
- [ ] If using authentication: username/password noted

### Configuration

- [ ] Web interface → **Configuration → MQTT**:
  - [ ] Broker address entered
  - [ ] Port correct (default: `1883`)
  - [ ] Credentials entered (if required)
- [ ] Click **Test Connection** — result shows **"Connected"**
- [ ] Click **Save** — controller restarts MQTT connection

### Verification

- [ ] Subscribe to all topics on the broker:
  ```bash
  mosquitto_sub -h <broker-ip> -t "#" -v
  ```
- [ ] Pool controller topics appear (prefixed with `homeassistant/` or `homie/`)
- [ ] Sensor values update periodically
- [ ] If topics are missing: check `homeassistant` prefix in HA configuration

---

## 7. Functional Test (Without 230V)

Before connecting any pump, test that the controller can switch the relays.

- [ ] **Multimeter ready**, set to DC voltage mode
- [ ] Measure between relay IN1 pin and GND:
  - Web interface shows relay **OFF** → IN1 reads **~3.3V (HIGH)**
  - Web interface shows relay **ON** → IN1 reads **~0V (LOW)**
- [ ] Repeat for relay IN2 — same behavior
- [ ] If voltages are reversed: your relay module is **active-high** — check for a HIGH/LOW jumper or replace the module

### Relay Test by GPIO

| GPIO | Expected OFF | Expected ON | Controls |
|------|-------------|-------------|----------|
| GPIO26 (IN1) | ~3.3V (HIGH) | ~0V (LOW) | Heating pump (not yet connected) |
| GPIO25 (IN2) | ~3.3V (HIGH) | ~0V (LOW) | Filter pump (not yet connected) |

---

## 8. Home Assistant Integration (Optional)

- [ ] MQTT integration configured in Home Assistant (Settings → Devices & Services → MQTT)
- [ ] Discovery enabled: `discovery: true` in HA `configuration.yaml`
- [ ] Pool Controller appears as a device in **Settings → Devices & Services → Devices**
- [ ] All entities visible and reporting values:
  - `sensor.pool_controller_pool_temp` — pool temperature
  - `sensor.pool_controller_solar_temp` — solar temperature
  - `select.pool_controller_mode` — operation mode
  - `switch.pool_controller_pool_pump` — pump control
  - `switch.pool_controller_solar_pump` — solar pump control
- [ ] **Operation Mode** can be changed via HA (try switching to `manu` and back to `auto`)

---

## 9. First Real Test (With Pumps)

Only proceed when all previous steps pass.

- [ ] **Disconnect** ESP32 from USB power
- [ ] Wire relay outputs to pump contactors or directly to pumps (230V side)
- [ ] Double-check: relay common (COM) and normally open (NO) wired correctly
- [ ] Reconnect ESP32 to USB power
- [ ] Set operation mode to **Manual (`manu`)** via web interface
- [ ] Toggle **Heating Pump** ON via web interface — pump starts
- [ ] Toggle **Heating Pump** OFF — pump stops
- [ ] Toggle **Filter Pump** ON — pump starts
- [ ] Toggle **Filter Pump** OFF — pump stops
- [ ] If pump does not start: check 230V wiring, circuit breaker, RCD
- [ ] If pump starts but does not stop: relay contacts may be welded — disconnect 230V immediately

---

## 10. Automation Test

- [ ] Set operation mode to **Auto**
- [ ] Verify the controller switches pumps according to its heating logic
- [ ] Solar temperature > Pool temperature + hysteresis → heating pump should turn ON
- [ ] Pool temperature reaches max. set temperature → heating pump should turn OFF
- [ ] Filter/circulation pump runs according to its schedule (timer or temperature-based)

---

## 11. Final Verification

- [ ] Temperature difference between solar and pool sensor is plausible
- [ ] Controller remains stable for 24+ hours without unexpected reboots
- [ ] WiFi connection stays stable (check RSSI in diagnostics)
- [ ] MQTT connection persists (check availability topic: should read `online`)
- [ ] Home Assistant (if used) shows correct and current values

---

## Quick Reference Card

Print this abbreviated checklist for quick on-site reference:

```
☐ ESP32: 5V USB power, data cable
☐ Relay VCC → 5V, GND → GND
☐ Relay IN1 → GPIO26 (heating)
☐ Relay IN2 → GPIO25 (filter)
☐ DS18B20 #1: GPIO32 + 4.7kΩ pull-up
☐ DS18B20 #2: GPIO33 + 4.7kΩ pull-up
☐ RCD / FI installed on 230V side
☐ Firmware + Filesystem uploaded
☐ WiFi configured, web UI reachable
☐ MQTT test connection successful
☐ Relay voltages correct (3.3V OFF / 0V ON)
☐ Manual pump test (without 230V automa
```
