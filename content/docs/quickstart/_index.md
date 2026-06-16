---
title: Quick Start
weight: 8
tags: ["docs", "getting-started", "quickstart", "tutorial"]
---

**🏊 Smart Swimming Pool: From box to a working pool in 60 minutes.**

This is the express path — minimal theory, maximum action. Follow each step exactly, and you will have a working pool controller within an hour.

> 📖 For detailed explanations and background, see the [Getting Started guide](/docs/getting-started/).

---

## What You Need

- ESP32 DevKit V1 + USB cable (data cable!)
- 2-channel 5V relay module (active-low)
- 2× DS18B20 temperature sensors (waterproof)
- 2× 4.7kΩ resistors
- Breadboard + jumper wires
- 5V USB power supply (1A+)
- Computer with VS Code + PlatformIO installed
- MQTT broker running on your network (optional for first test)

**All parts: ~45–75 €** — see [Bill of Materials](/docs/bom/) for details.

---

## Step 1: Wire It Up (5 minutes)

### Breadboard Layout

```
┌─────────────────────────────────────────┐
│  ESP32 DevKit                           │
│  ┌──────────────────────────────────────┤
│  │ USB    GND  5V  GPIO32  GPIO33  ... │
│  └──────────────────────────────────────┤
│           │    │    │       │           │
│           │    │    ├──4.7kΩ─┤ 3.3V     │
│           │    │    │       │           │
│  ─────────┤    │    │       │           │
│  DS18B20 #1   │    │   DS18B20 #2       │
│  (Solar)      │    │   (Pool)           │
└─────────────────────────────────────────┘
```

**Connections:**

| From | To | Wire |
|------|-----|------|
| ESP32 3.3V | DS18B20 #1 VDD (red) | Red |
| ESP32 3.3V | DS18B20 #2 VDD (red) | Red |
| ESP32 GND | DS18B20 #1 GND (black) | Black |
| ESP32 GND | DS18B20 #2 GND (black) | Black |
| ESP32 GPIO32 | DS18B20 #1 DATA (yellow) | Yellow |
| ESP32 GPIO33 | DS18B20 #2 DATA (yellow) | Yellow |
| GPIO32 → 3.3V | 4.7kΩ pull-up resistor | — |
| GPIO33 → 3.3V | 4.7kΩ pull-up resistor | — |
| ESP32 5V (VIN) | Relay module VCC | Red |
| ESP32 GND | Relay module GND | Black |
| ESP32 GPIO26 | Relay IN1 (heating pump) | Blue |
| ESP32 GPIO25 | Relay IN2 (filter pump) | Green |

> ⚠️ **Double-check:** Relay VCC goes to **5V** (ESP32 VIN pin), NOT to 3.3V.

---

## Step 2: Flash the Firmware (10 minutes)

1. Open VS Code with the PlatformIO extension installed
2. Clone and open the pool-controller:
   ```bash
   git clone https://github.com/smart-swimmingpool/pool-controller.git
   cd pool-controller
   code .
   ```
3. Connect the ESP32 via USB
4. **Upload firmware:** In the PlatformIO footer bar, click the **→ (Upload and Monitor)** button next to `esp32dev`
5. **Upload filesystem:** PlatformIO tab → `esp32dev` → **Platform → Upload Filesystem Image**
6. Wait for both uploads to complete

**Expected serial output (115200 baud):**
```
[INFO] Pool Controller v3.x.x starting...
[INFO] WiFi: Starting in AP mode
[INFO] AP: 'Pool-Controller-Setup'. IP: 192.168.4.1
[INFO] OneWire: Found 2 DS18B20 sensor(s)
```

---

## Step 3: Configure WiFi (3 minutes)

1. Connect your phone/laptop to the WiFi network **`Pool-Controller-Setup`** (open, no password)
2. Open browser → **http://192.168.4.1**
3. Enter your home WiFi SSID and password
4. Click **Save** — the ESP32 reboots and connects to your network

---

## Step 4: Connect to MQTT (3 minutes)

1. Find the ESP32's IP address on your router (or from the serial monitor)
2. Open **http://<esp32-ip>/** in your browser
3. Go to **Configuration → MQTT**
4. Enter your MQTT broker address (e.g., `192.168.1.100` or `core-mosquitto`)
5. If using authentication, enter username/password
6. Click **Test Connection** — it should say "Connected"
7. Click **Save**

**No broker yet?** Install [Mosquitto](https://mosquitto.org/download/) on any machine on your network, or use the Mosquitto add-on in Home Assistant.

---

## Step 5: Verify Sensors (3 minutes)

Check the web interface **Status** page:

| Sensor | Expected |
|--------|----------|
| **Pool Temperature** | Plausible room/water temperature (not -127°C) |
| **Solar Temperature** | Plausible room/water temperature (not -127°C) |
| **Solar Sensor Found** | ✅ Yes |
| **Pool Sensor Found** | ✅ Yes |

**Reading -127°C?** Check the pull-up resistor and data wire connections.

---

## Step 6: Test Relays (5 minutes, NO 230V)

1. On the web interface **Control** page, set **Operation Mode** to **`manu`** (Manual)
2. Grab a multimeter, set to DC voltage
3. Toggle **Heating Pump** ON:
   - GPIO26 (Relay IN1) should read **~0V (LOW)**
4. Toggle ON → OFF:
   - GPIO26 should go back to **~3.3V (HIGH)**
5. Repeat for **Filter Pump** on GPIO25

**Voltages reversed?** Your relay is active-high → check for a HIGH/LOW jumper on the module, or replace it.

---

## Step 7: Connect Pumps (10 minutes)

> ⚠️ **230V mains voltage — risk of death.** Observe all safety precautions.

1. **Disconnect** ESP32 from USB power
2. Wire relay outputs to pump contactors or directly to pumps
3. Ensure **RCD/FI circuit breaker** is installed on the 230V side
4. Reconnect ESP32 to USB power
5. Set **Operation Mode** to **`manu`** (Manual)
6. Toggle **Heating Pump** ON — pump should start
7. Toggle OFF — pump should stop
8. Repeat for **Filter Pump**

---

## Step 8: Enable Automation (2 minutes)

1. Set **Operation Mode** to **`auto`**
2. Set **Max. Pool Temp** to your target (e.g., 28°C)
3. Set **Min. Solar Temp** (e.g., 35°C)
4. Set **Hysteresis** (e.g., 2 K)

The controller now handles everything automatically.

---

## Step 9: Connect to Home Assistant (5 minutes)

If you use Home Assistant:

1. Go to **Settings → Devices & Services → Add Integration → MQTT**
2. Ensure `discovery: true` is set (default)
3. The **Pool Controller** should appear as a new device automatically
4. Add entities to your Lovelace dashboard

See the [Home Assistant Integration Guide](/docs/home-assistant-integration/) for the complete dashboard setup and automation examples.

---

## You're Done! 🎉

Your pool controller is now fully operational. Next steps:

- Set up the **[Grafana Dashboard](/docs/grafana-dashboard/)** for temperature history
- Add the **[Pool Monitor](/docs/pool-monitor/)** for a wireless display
- Follow the **[Commissioning Checklist](/docs/checklist/)** for a more thorough verification
- Read the **[FAQ & Troubleshooting](/docs/troubleshooting/)** if something isn't working

---

## Quick Reference: Pin Map

| Component | ESP32 Pin |
|-----------|-----------|
| DS18B20 Solar (DATA) | GPIO32 |
| DS18B20 Pool (DATA) | GPIO33 |
| 4.7kΩ pull-up (each) | DATA → 3.3V |
| Relay IN1 (heating pump) | GPIO26 |
| Relay IN2 (filter pump) | GPIO25 |
| Relay VCC | 5V (VIN) |
| Relay GND | GND |
| DS18B20 VDD | 3.3V |
| DS18B20 GND | GND |
