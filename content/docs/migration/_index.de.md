---
title: Upgrade & Migration
weight: 25
tags: ["docs", "migration", "upgrade", "releases"]
---

**🏊 Smart Swimming Pool: Wie Sie die Firmware des Pool-Controllers zwischen Hauptversionen aktualisieren.**

Diese Seite dokumentiert Breaking Changes, neue Parameter und Migrationsschritte zwischen Releases. Lesen Sie den entsprechenden Abschnitt **vor** dem Update.

---

## Kurzreferenz

| Von → Nach | Typ | Breaking Changes | Migration nötig |
|-----------|------|:----------------:|:---------------:|
| v2.x → v3.2 | Großes Rewrite | ✅ MQTT-Protokoll, Homie → HA Discovery | Reset, neu flashen |
| v3.2 → v3.3 | Kleines Update | Keine | Optional (Config bleibt) |

---

## v2.x → v3.2 (Großes Update)

Veröffentlicht: Mai 2026

Dieses Update ist ein **komplettes Rewrite** der Firmware. Das gesamte MQTT-Protokoll wechselte von der **Homie-Convention** zu **Home Assistant MQTT Discovery**.

### Breaking Changes

| Bereich | v2.x | v3.2+ | Auswirkung |
|---------|------|-------|------------|
| **MQTT-Protokoll** | Homie-Convention | Home Assistant MQTT Discovery | Alle MQTT-Topics geändert. Smarthome-Integrationen müssen neu konfiguriert werden |
| **Geräte-ID** | Benutzerdefiniert | `pool_controller_<mac>` | Home Assistant erzeugt neues Gerät — altes löschen |
| **Firmware-Ziel** | ESP8266 unterstützt | Nur ESP32 | ESP8266-Nutzer können nicht updaten; Hardware-Wechsel nötig |
| **Konfiguration** | Webserver-basiert | Web-UI auf LittleFS | Einstellungen nicht kompatibel; Neukonfiguration nötig |
| **Weboberfläche** | Einfache HTML-Formulare | Vollständige SPA auf LittleFS | Erfordert `uploadfs`-Schritt nach dem Flashen |

### Migrationsschritte

1. **Einstellungen sichern** — Screenshots der v2.x-Konfiguration machen (MQTT-Broker, Temperaturgrenzen, Timer)
2. **Neue Firmware flashen** via USB (PlatformIO, Umgebung `esp32dev`)
3. **Dateisystem-Image hochladen** (`pio run -e esp32dev -t uploadfs`)
4. **Alles neu konfigurieren** via Weboberfläche (WLAN, MQTT, Temperaturgrenzen)
5. **Home Assistant neu konfigurieren:** Neuer Controller erscheint als neues Gerät. Entities zum Dashboard hinzufügen. Altes v2.x-Gerät in HA löschen
6. **Automationen anpassen:** MQTT-Topics haben sich geändert — alle Homie-basierten Automatisierungen aktualisieren
7. **Überprüfen:** Alle Sensoren melden korrekte Werte, Pumpen reagieren

### Was sich verbessert hat

| v2.x-Einschränkung | v3.2+-Lösung |
|--------------------|-------------|
| Homie-Topics erforderten manuelle HA-Konfiguration | Automatischer MQTT Discovery — kein YAML nötig |
| ESP8266 mit wenig Flash und RAM | ESP32 mit 4MB Flash, reichlich RAM |
| Web-UI war minimalistisch | Vollständige Konfigurations-UI auf LittleFS |
| Keine OTA-Updates | OTA von GitHub Releases (ab v3.3) |

---

## v3.2 → v3.3 (Kleines Update)

Veröffentlicht: Juni 2026

### Neue Funktionen

| Funktion | Beschreibung |
|----------|-------------|
| **OTA-Updates** | Firmware kann via Home Assistant oder Weboberfläche aktualisiert werden. Controller prüft automatisch auf neue GitHub-Releases |
| **NTP-Konfiguration** | NTP-Server und Zeitzone via Web-UI oder MQTT konfigurierbar — keine Compile-Zeit-Zeitzone mehr nötig |
| **Lokale Zeit** | Controller zeigt aktuelle Ortszeit in der Diagnose an |
| **Timer-Entities** | Timer-Start/-Ende von separaten Stunden+Minuten auf einzelne `time`-Entities umgestellt (HH:MM-Format) |
| **Web-UI umstrukturiert** | Einstellungs-Tabs neu organisiert, HA-Entity-Kategorien aktualisiert |
| **Config-Backup** | NVS-Konfiguration wird gesichert; MQTT-Fehler werden gemeldet |
| **LittleFS-Mount-Fix** | Webportal mountet LittleFS jetzt korrekt beim Start |

### Breaking Changes

**Keine.** v3.3 ist vollständig abwärtskompatibel mit v3.2-Konfigurationen.

### Migrationsschritte

1. **Option A — OTA via Home Assistant:**
   - **Einstellungen → Geräte & Dienste → Geräte → Pool Controller**
   - Die **Firmware**-Update-Entity (`update.pool_controller_firmware`) zeigt die neue Version
   - **Installieren** klicken — Controller lädt das Update herunter und wendet es an
   - Auf Neustart warten

2. **Option B — OTA via Weboberfläche:**
   - Controller-Webinterface öffnen
   - **System → Firmware Update**
   - **Nach Updates suchen** klicken

3. **Option C — USB-Flash (Fallback):**
   - ESP32 per USB verbinden
   - Firmware + Dateisystem wie gewohnt flashen
   - Alle Einstellungen bleiben erhalten (NVS-Partition)

### Post-Update-Prüfungen

- [ ] Weboberfläche unter gleicher IP erreichbar
- [ ] Alle Temperatursensoren zeigen korrekte Werte
- [ ] MQTT-Verbindung hergestellt
- [ ] Home Assistant zeigt alle Entities als verfügbar
- [ ] Timer-Entities jetzt als einzelne HH:MM-Regler

### Neue Konfigurationsparameter

| Parameter | Typ | Standard | Beschreibung |
|-----------|-----|----------|-------------|
| `ntp_server` | Text | `pool.ntp.org` | NTP-Server für Zeitsynchronisation |
| `timezone` | Select | `UTC` | IANA-Zeitzone (z.B. `Europe/Berlin`) |

Konfiguration via:
- Weboberfläche: **Configuration → System**
- Home Assistant: `text.pool_controller_ntp_server`, `select.pool_controller_timezone`

---

## Rollback

Falls ein Update Probleme verursacht, kann auf die vorherige Version zurückgesetzt werden:

### v3.3 → v3.2

**Einstellungen sind möglicherweise nicht kompatibel** — v3.3 führte neue Parameter (NTP, Zeitzone) ein, die v3.2 nicht kennt. v3.2 ignoriert unbekannte Parameter, daher ist ein Downgrade in der Regel sicher.

1. v3.2-Firmware via USB flashen:
   ```bash
   git checkout v3.2.0
   pio run -e esp32dev -t upload
   ```
2. v3.2-Dateisystem-Image hochladen:
   ```bash
   pio run -e esp32dev -t uploadfs
   ```
3. Neu starten und Funktion prüfen

### v3.2 → v2.x

**Vollständige Neukonfiguration erforderlich.** Siehe v2.x → v3.2-Migrationsschritte oben.

---

## Versionsgeschichte

| Version | Datum | Highlights |
|---------|-------|-----------|
| **v3.3.0** | 2026-06-06 | OTA-Updates, NTP-Konfiguration, lokale Zeit, Timer-Entities, Web-UI-Neustrukturierung |
| **v3.2.0** | 2026-05-22 | HA MQTT Discovery, nur ESP32, neue Web-UI, WPS-Onboarding |
| **v2.x** | 2020–2025 | Homie-Convention, ESP8266+ESP32, openHAB-zentriert |

Vollständiges Changelog auf [GitHub Releases](https://github.com/smart-swimmingpool/pool-controller/releases).
