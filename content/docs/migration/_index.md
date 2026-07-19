---
title: Upgrade & Migration
weight: 25
tags: ["docs", "migration", "upgrade", "releases"]
---

**🏊 Smart Swimming Pool: How to update the pool controller firmware between major versions.**

This page documents breaking changes, new parameters, and migration steps between releases. Always read the relevant section **before** updating.

---

## Quick Reference

| From → To | Type | Breaking Changes | Migration Required |
|-----------|------|:----------------:|:------------------:|
| v2.x → v3.2 | Major rewrite | ✅ MQTT protocol, Homie → HA Discovery | Config reset, re-flash |
| v3.2 → v3.3 | Minor update | None | Optional (config preserved) |

---

## v2.x → v3.2 (Major Update)

Released: May 2026

This update is a **major rewrite** of the firmware. The entire MQTT protocol changed from **Homie convention** to **Home Assistant MQTT Discovery**.

### Breaking Changes

| Area | v2.x | v3.2+ | Impact |
|------|------|-------|--------|
| **MQTT Protocol** | Homie convention | Home Assistant MQTT Discovery | All MQTT topics changed. Smart home integrations must be reconfigured |
| **Device ID** | Custom | `pool_controller_<mac>` | Home Assistant creates a new device — delete the old one |
| **Firmware target** | ESP8266 supported | ESP32 only | ESP8266 users cannot upgrade; must migrate hardware |
| **Configuration** | Webserver-based | Web UI on LittleFS | Settings not compatible; must be reconfigured |
| **Web interface** | Basic HTML forms | Full SPA on LittleFS | Requires `uploadfs` step after flashing |

### Migration Steps

1. **Back up your settings** — Take screenshots of your v2.x configuration (MQTT broker, temperature limits, timer settings)
2. **Flash the new firmware** via USB (PlatformIO, `esp32dev` environment)
3. **Upload the filesystem image** (`pio run -e esp32dev -t uploadfs`)
4. **Reconfigure everything** via the new web interface (WiFi, MQTT, temperature limits)
5. **Reconfigure Home Assistant:** The new controller appears as a new device (`Pool Controller`). Add entities to your dashboard. Delete the old v2.x device from HA
6. **Reconfigure automation:** MQTT topics have changed — update any custom automations that referenced Homie topics
7. **Verify** that all sensors report correct values and pumps respond

### What Changed for the Better

| v2.x Limitation | v3.2+ Solution |
|-----------------|----------------|
| Homie topics required custom HA configuration | Automatic MQTT Discovery — no YAML needed |
| ESP8266 had limited flash and RAM | ESP32 with 4MB flash, ample RAM |
| Web UI was bare-bones | Full configuration UI on LittleFS |
| No OTA updates | OTA from GitHub releases (added in v3.3) |

---

## v3.2 → v3.3 (Minor Update)

Released: June 2026

### New Features

| Feature | Description |
|---------|-------------|
| **OTA Updates** | Firmware can now be updated via Home Assistant or the web interface. The controller checks GitHub releases automatically |
| **NTP Configuration** | Configure NTP server and timezone via web UI or MQTT — no more compile-time timezone |
| **Local Time Display** | Controller shows current local time in diagnostics |
| **Timer entities** | Timer start/end changed from separate hour+minute numbers to single `time` entities (HH:MM format) |
| **Web UI restructured** | Settings tabs reorganized; HA entity categories updated |
| **Config backup** | NVS configuration is backed up; MQTT errors are reported |
| **LittleFS mount fix** | Web portal now correctly mounts LittleFS on startup |

### Breaking Changes

**None.** The v3.3 update is fully backward-compatible with v3.2 configurations.

### Migration Steps

1. **Option A — OTA from Home Assistant:**
   - Go to **Settings → Devices & Services → Devices → Pool Controller**
   - The **Firmware** update entity (`update.pool_controller_firmware`) shows the new version
   - Click **Install** — the controller downloads and applies the update
   - Wait for the controller to reboot

2. **Option B — OTA from web interface:**
   - Open the controller web interface
   - Go to **System → Firmware Update**
   - Click **Check for Updates** and follow the prompts

3. **Option C — USB flash (fallback):**
   - Connect the ESP32 via USB
   - Flash firmware + filesystem as usual
   - All settings are preserved (stored in NVS partition)

### Post-Update Checks

- [ ] Web interface reachable at the same IP address
- [ ] All temperature sensors report correct values
- [ ] MQTT connection established
- [ ] Home Assistant shows all entities as available
- [ ] Timer entities now show as single HH:MM controls

### New Configuration Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ntp_server` | Text | `pool.ntp.org` | NTP server for time synchronization |
| `timezone` | Select | `UTC` | IANA timezone (e.g., `Europe/Berlin`) |

These are configured via:
- Web interface: **Configuration → System**
- Home Assistant: `text.pool_controller_ntp_server`, `select.pool_controller_timezone`

---

## Rollback

If an update causes issues, you can roll back to the previous version:

### v3.3 → v3.2

**Settings may not be compatible** — v3.3 introduced new parameters (NTP, timezone) that v3.2 does not recognize. v3.2 will ignore unknown parameters, so downgrade is generally safe.

1. Flash the v3.2 firmware via USB:
   ```bash
   git checkout v3.2.0
   pio run -e esp32dev -t upload
   ```
2. Upload the v3.2 filesystem image:
   ```bash
   pio run -e esp32dev -t uploadfs
   ```
3. Reboot and verify everything works

### v3.2 → v2.x

**Full reconfiguration required.** See the v2.x → v3.2 migration steps above — the same incompatibilities apply in reverse.

---

## Version History

| Version | Date | Highlights |
|---------|------|-----------|
| **v3.3.0** | 2026-06-22 | OTA updates, NTP config, local time display, timer entities, web UI restructure |
| **v3.2.0** | 2026-05-22 | HA MQTT Discovery, ESP32-only, new web UI, WPS onboarding |
| **v2.x** | 2020–2025 | Homie convention, ESP8266+ESP32, openHAB-centric |

See the [GitHub Releases](https://github.com/smart-swimmingpool/pool-controller/releases) for the full changelog of each version.
