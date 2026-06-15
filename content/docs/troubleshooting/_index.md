---
title: FAQ & Troubleshooting
weight: 30
tags: ["docs", "faq", "troubleshooting"]
---

**🏊 Frequently asked questions and solutions for common problems.**

{{< safety-notice type="230v" >}}

## Relay Issues

### Relay module does not switch / pump behaves unexpectedly

**Likely cause:** Your relay module polarity does not match the firmware.

The pool controller firmware drives relays **active-low** (GPIO **LOW** = relay ON, GPIO **HIGH** = relay OFF). This matches the vast majority of common 2-channel 5V relay modules.

**Solution:**
1. **If your relay works normally:** You have a standard **active-low** module — everything is fine.
2. **If your relay is stuck ON or OFF**: Your module may be **active-high** (GPIO HIGH = relay ON).
   - Check for a jumper labeled "HIGH/LOW" on the module and set it to **LOW**.
   - If there is no jumper, you may need to replace the module with a standard active-low type (~5€).

**Quick test:** With the ESP32 powered on but NOT connected to pumps, use a multimeter to measure voltage between the relay IN pin and GND:
- When the relay should be OFF (web interface shows OFF): pin should read **~3.3V** (HIGH)
- When the relay should be ON (web interface shows ON): pin should read **~0V** (LOW)
- If the opposite happens, your module is active-high.

### Relay makes clicking noises but pump does not start

- The relay contacts may be rated for lower current than your pump draws.
- Check pump power rating: a 10A relay is sufficient for most circulation pumps. For larger pumps, use the relay to switch a contactor.

### Which relay modules are compatible?

Confirmed working modules (active-low, optocoupler isolated):
- **HW-279 / HW-316** 2-channel 5V relay module
- **SRD-05VDC-SL-C** based modules
- Most generic 2-channel 5V relay boards with optocoupler (check jumper set to **LOW**)

Avoid: modules without optocoupler isolation (single-transistor driven) — they can damage the ESP32 GPIO pins.

---

## Temperature Sensor Issues

### DS18B20 sensor not detected / reads -127°C or 85°C

**Likely cause:** Wiring problem or missing pull-up resistor.

**Diagnosis:**
- `-127°C` = sensor not found on the OneWire bus (no communication)
- `85°C` = sensor found but stuck in power-on default (parasite power issue)

**Solutions:**
1. **Check the pull-up resistor:** You MUST have a **4.7kΩ resistor** between DATA (yellow/white) and 3.3V (red). Without it, OneWire does not work.
2. **Verify wiring (esp32dev config uses separate pins):**
   - Red → 3.3V (ESP32)
   - Black → GND (ESP32)
   - Solar sensor DATA → **GPIO32** (Yellow/White)
   - Pool sensor DATA → **GPIO33** (Yellow/White)
3. **Try one sensor at a time** to isolate a faulty sensor or bad cable.
4. **Check cable length:** DS18B20 works reliably up to ~30m with a 4.7kΩ pull-up. For longer runs, use a lower value (e.g., 2.2kΩ) or shielded twisted-pair cable.
5. **Avoid parasite power mode:** The pool controller firmware uses external power mode (3 wires). Make sure both sensors have all 3 wires connected.

### Temperature readings are clearly wrong (e.g., 120°C in a 25°C pool)

- **Interference:** The sensor cable may run too close to 230V power cables. Route sensor cable at least 30cm away from mains wiring.
- **Faulty sensor:** Replace the sensor — they cost ~3€.
- **Water ingress:** If the stainless steel probe is not fully submerged or the cable end is wet, readings can be erratic. Let it dry and seal with heat shrink.

### Both sensors show the same temperature

This is expected if they are placed in water at the same temperature. To verify they are working independently:
1. Hold one sensor in your hand — the reading should rise within a few seconds.
2. Hold the other in cold water — the reading should drop.

---

## WiFi & Network Issues

### ESP32 does not appear in WiFi list after flashing

**Solution:**
1. The ESP32 starts in **AP mode** on first boot (network name: **`Pool-Controller-Setup`**).
2. If you don't see it, check the serial monitor output (115200 baud).
3. The ESP32 may have previously been configured for your home WiFi — reset to factory defaults:
   - Connect via serial monitor
   - Send `reset` command
   - Or hold the BOOT button for 10 seconds during power-on

### ESP32 connects to WiFi but is unreachable

1. Check your router's DHCP client list for the ESP32's IP address.
2. Try `ping <esp32-ip>` from your computer.
3. If the ESP32 is on a different VLAN/subnet, ensure MQTT traffic is allowed between them.
4. Try rebooting your router and the ESP32.

### WiFi connection drops frequently

- The ESP32's WiFi is sensitive to distance and interference. Keep it within 15m of your access point.
- If the access point is far, consider a WiFi repeater or a wired connection (ESP32 can use Ethernet with a LAN8720 module — not in standard firmware).

---

## MQTT Issues

### Controller does not appear in Home Assistant

**Prerequisites:**
1. Home Assistant must have the **MQTT integration** configured (Settings → Devices & Services → Add Integration → MQTT).
2. The pool controller must be connected to the **same MQTT broker**.

**Troubleshooting:**
1. Open the pool controller web interface → **Configuration → MQTT**.
2. Verify broker address, port (default: 1883), and credentials.
3. Click **Test Connection** — you should see "Connected" or an error message.
4. Check the Home Assistant logs: look for `MQTT` or `pool` entries.
5. Try publishing a message manually to verify MQTT works:
   ```bash
   mosquitto_pub -h <broker-ip> -t "test" -m "hello"
   mosquitto_sub -h <broker-ip> -t "#" -v  # should show pool topics
   ```

### MQTT messages are published but Home Assistant shows "unknown" entities

- The controller uses **Home Assistant MQTT Discovery** (automatic entity creation).
- If entities show as "unknown", the discovery topic may not be reaching HA.
- Check that the MQTT prefix in your Home Assistant MQTT integration matches the controller's prefix (default is `homeassistant`).

### MQTT not connecting / connection refused

- Ensure the MQTT broker is running: `systemctl status mosquitto` (Linux) or check the Home Assistant add-on status.
- Check firewall rules: port 1883 (TCP) must be open between ESP32 and broker.
- If using authentication, verify username and password in the controller's MQTT configuration.

---

## ESP32 & Firmware Issues

### ESP32 does not boot / continuously reboots

**Serial monitor shows:**
```
ets Jun  8 2016 00:22:57
rst:0xc (SW_CPU_RESET),boot:0x13 (SPI_FAST_FLASH_BOOT)
```

**Solutions:**
1. **Check power:** ESP32 needs a stable 5V supply. USB ports on some computers or cheap phone chargers may not deliver enough current (>500mA). Use a quality 5V/1A+ power supply.
2. **Wrong flash settings:** In Arduino IDE or PlatformIO, ensure:
   - Flash Mode: **DIO** (not QIO)
   - Flash Size: **4MB** (or whatever your board has)
   - Partition Scheme: **Default 4MB with spiffs**
3. **Bad USB cable:** Some cables are charge-only (no data lines). Use a known-good data cable.
4. If booting works with the USB connected to a computer but not from a standalone power supply, the power supply is likely insufficient.

### "A fatal error occurred: Failed to connect to ESP32" when flashing

1. Hold the **BOOT** button on the ESP32, click **Upload** in the IDE, release BOOT when flashing starts.
2. Check the correct COM port is selected.
3. Try a different USB cable (data, not charge-only).
4. If using a CP210x-based board, install/reinstall the driver.

### Serial monitor shows garbled text

- Wrong baud rate — set it to **115200**.
- Wrong voltage — ESP32 runs at 3.3V. If you connected it to an Arduino Uno, you may have damaged the serial interface.

---

## General & Hardware

### The system cost more than 100€ — is that normal?

The **~45–75€** estimate covers the **controller electronics only** (ESP32, sensors, relay, breadboard, enclosure). It does **not** include:
- Pool pump and filter system
- Heating circuit pump
- Heat exchanger installation
- Wiring materials (cables, connectors, circuit breakers)

If you need to add these, the total project cost can be significantly higher.

### Can I use this without a smart home server?

**Yes.** The pool controller is fully autonomous:
- It handles circulation scheduling and heating control **without** any server.
- The web interface allows basic configuration and manual control.
- MQTT integration and Home Assistant are optional — they add remote control, automation, and visualization.

### How weatherproof is the system?

The pool controller itself is **not weatherproof** out of the box. You need:

| Location | Protection |
|----------|-----------|
| Indoor installation (preferred) | No special protection needed |
| Outdoor / pool house | **IP54+** enclosure, cable glands for all entries |
| Sensors (DS18B20) | Stainless steel probe is IP68 — cable entry must be sealed |
| Power supply | Must be in a dry location or in an IP-rated enclosure |

### Can I use this with a heat pump instead of solar heating?

Yes. The pool controller's heating logic switches a pump when heating is needed. This works with any heat source:
- Solar thermal system
- Heat pump
- Gas/oil heater with heat exchanger
- Electric heating element (via relay / contactor)

### Which pumps can be controlled?

The relay module switches 230V/10A max (resistive load). For inductive loads (motors, pumps), derate to ~5A. For larger pumps, use the relay to switch a contactor that handles the pump current.

### Is this project CE / UL certified?

**No.** This is a hobbyist DIY project. It is not tested or certified by any regulatory body. You build and operate it at your own risk. Always use an RCD (residual-current device / FI-Schutzschalter) when connecting to mains power.

{{< safety-notice type="230v" >}}
