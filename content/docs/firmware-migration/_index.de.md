---
title: Firmware-Migration (v2.x → v3.x)
weight: 50
tags: ["docs", "migration", "homie", "firmware"]
---

**🏊 Smart Swimming Pool: Migration vom alten Homie 3.0-Format zum neuen MQTT-Discovery-Format**

Wenn Sie den **Pool Controller v2.x** (oder älter) betreiben und auf **v3.x** upgraden möchten, erklärt dieser Leitfaden, was sich ändert und wie Sie Ihre Smart-Home-Integration aktualisieren müssen.

> 💡 **Neuling?** Wenn Sie den Pool Controller zum ersten Mal installieren, folgen Sie stattdessen der [Erste Schritte](/docs/getting-started/)-Anleitung. Diese Anleitung ist nur relevant, wenn Sie bereits ein Homie 3.0-Setup haben.

---

## Übersicht

| Aspekt | v2.x (Homie 3.0) | v3.x (HA Discovery) |
|--------|------------------|---------------------|
| **MQTT-Topic-Format** | `homie/<mac>/<node>/<property>` | `homeassistant/<component>/pool-controller/<id>/state` |
| **Geräte-ID** | MAC-Adresse (z.B. `5ccf7fb97572`) | `pool-controller` (konfigurierbar) |
| **Verfügbarkeit** | `homie/<mac>/$state` (`ready`/`lost`) | `homeassistant/sensor/pool-controller/availability` (`online`/`offline`) |
| **Home Assistant** | Eingeschränkt, manuelle Konfiguration | **Nativ** — automatische Erkennung via MQTT |
| **openHAB** | Volle Unterstützung (native Konfiguration) | Manuelle MQTT-Konfiguration erforderlich |

---

## Warum die Änderung?

Der Wechsel von Homie 3.0 zu [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) hatte zwei Ziele:

1. **Null-Konfiguration für Home Assistant-Nutzer** — HA erkennt alle Entitäten automatisch, keine manuelle Konfiguration nötig
2. **Standardisierung** — HA Discovery ist der De-facto-Standard für MQTT-basierte IoT-Geräte, während Homie 3.0 nie breite Akzeptanz fand

openHAB wird weiterhin vollständig über manuelle MQTT-Konfiguration unterstützt.

---

## Firmware-Upgrade

### Schritt 1: v3.x flashen

Folgen Sie der Standard-Flash-Prozedur in der [Erste Schritte](/docs/getting-started/#firmware-installation)-Anleitung:

```bash
# In VS Code mit PlatformIO:
# 1. Firmware hochladen
# 2. Dateisystem-Image (LittleFS/Webinterface) hochladen
```

> ⚠️ **Wichtig**: Nach dem Flashen von v3.x ist das Webinterface **komplett neu geschrieben**. Einstellungen aus dem alten Web-UI werden **nicht übernommen**. Sie müssen WiFi und MQTT über den Setup-AP (`Pool-Controller-Setup`) neu konfigurieren.

### Schritt 2: WiFi und MQTT neu konfigurieren

1. Nach dem Flashen startet der ESP32 im AP-Modus (`Pool-Controller-Setup`)
2. Verbinden Sie sich damit und konfigurieren Sie Ihr WLAN unter `http://192.168.4.1`
3. Nach dem Neustart konfigurieren Sie MQTT über **Konfiguration → MQTT**

### Schritt 3: Konfigurationsparameter erneut einstellen

Nach der Migration konfigurieren Sie diese Parameter im Webinterface (oder über Home Assistant) neu:

- Maximale Pooltemperatur
- Minimale Solartemperatur
- Hysterese
- Timer Start / Ende
- Sensor-Adressen (DS18B20)

---

## Migration nach Smart-Home-Plattform

### Home Assistant-Nutzer

**Sie sind nach Schritt 2 fertig.** Die v3.x-Firmware erkennt sich automatisch über MQTT Discovery.

1. Gehen Sie zu **Einstellungen → Geräte & Dienste**
2. Das Gerät **Pool Controller** sollte automatisch erscheinen
3. Siehe [Home Assistant Integrations-Guide](/docs/home-assistant-integration/) für die vollständige Entity-Referenz

> **Hinweis**: Wenn Sie manuell MQTT-Sensoren in Home Assistant für die Homie-Topics konfiguriert hatten, werden diese nach dem Upgrade als **nicht verfügbar** angezeigt. Entfernen Sie sie manuell — die automatisch erkannten Entitäten ersetzen sie.

### openHAB-Nutzer

openHAB erfordert **manuelle MQTT-Konfiguration**. Der [openHAB Integrations-Guide](/docs/openhab-integration/) zeigt die vollständige Einrichtung.

#### Was sich ändern muss

| Datei | Änderung |
|-------|----------|
| `things/mqtt.things` | Alle Topic-Pfade: `homie/<mac>/...` → `homeassistant/...` |
| `items/2-pool.items` | Channel-Bindungen: Topic-Referenzen aktualisieren |
| `sitemaps/pool.sitemap` | Meist keine Änderung (Item-Namen bleiben gleich) |

#### Topic-Mapping-Referenz

| v2.x Homie-Topic | v3.x HA-Discovery-Topic |
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

#### Wichtige Werte-Änderungen

| Aspekt | v2.x (Homie) | v3.x (HA Discovery) |
|--------|-------------|---------------------|
| Pumpe EIN | `true` | `ON` |
| Pumpe AUS | `false` | `OFF` |
| Verfügbarkeit online | `ready` | `online` |
| Verfügbarkeit offline | `lost` | `offline` |

---

## Breaking Changes

### 1. Timer-Entities umstrukturiert

**v2.x**: 4 separate `number`-Entities für Timer-Start/Ende (Stunden + Minuten einzeln)

```
homie/<mac>/operation-mode/timer-start-h
homie/<mac>/operation-mode/timer-start-min
homie/<mac>/operation-mode/timer-end-h
homie/<mac>/operation-mode/timer-end-min
```

**v3.x**: 2 `time`-Entities im `HH:MM:SS`-Format

```
homeassistant/time/pool-controller/timer-start
homeassistant/time/pool-controller/timer-end
```

Die alten Entitäten werden automatisch aus Home Assistant entfernt, wenn v3.x startet (leere retained-Payloads werden auf ihre Config-Topics veröffentlicht).

### 2. Timezone-Entity geändert

**v2.x**: `number`-Entity mit Zeitzonen-Index (z.B. `0`, `1`, ...)

**v3.x**: `select`-Entity mit lesbaren Zeitzonen-Labels (z.B. `Europe/Berlin`, `America/New_York`)

### 3. Temperaturbasierte Zirkulation (neu in v3.3+)

v3.3 fügte drei neue Konfigurationsparameter für temperaturgesteuerte Zirkulation hinzu:

- `temp-circ-threshold` — minimale Temperaturdifferenz für Zirkulation
- `temp-circ-factor` — Laufzeit-Multiplikator pro Grad über Schwelle
- `temp-circ-max-runtime` — maximale Zirkulationslaufzeit

Diese gab es in v2.x nicht und haben kein Homie-Äquivalent.

### 4. Geräte-ID ist jetzt konfigurierbar

In v2.x war die Geräte-ID **immer** die MAC-Adresse (`5ccf7fb97572`). In v3.x ist die Standard-ID `pool-controller`, aber Sie können sie im Webinterface unter **Konfiguration → MQTT → Geräte-ID** **ändern**.

Wenn Sie sie ändern, aktualisieren Sie alle Topic-Pfade entsprechend.

### 5. Kein Homie-Kompatibilitätsmodus

Die v3.x-Firmware **unterstützt nur** Home Assistant MQTT Discovery. Es gibt keinen Rückwärtskompatibilitätsmodus für Homie 3.0. Wenn Sie Homie für benutzerdefinierte Integrationen benötigen, bleiben Sie bei v2.x.

---

## Rollback

Falls Sie zu v2.x zurückkehren müssen:

1. Flashen Sie die v2.x-Firmware mit PlatformIO
2. Konfigurieren Sie WiFi und MQTT neu (v2.x verwendet ebenfalls den Setup-AP)
3. Die alten Homie-Topics werden wieder aktiv
4. openHAB oder Home Assistant verbinden sich automatisch neu

> **Hinweis**: Das Flashen von v3.x löscht die LittleFS-Dateisystempartition. v2.x speichert die Konfiguration möglicherweise anders. Planen Sie ein, nach dem Downgrade alle Einstellungen neu zu konfigurieren.

---

## Ältere Firmware-Versionen

| Version | MQTT-Format | Status |
|---------|-------------|--------|
| **1.x** | Proprietäres JSON | Nicht mehr unterstützt |
| **2.x** | Homie 3.0 | Legacy — Update empfohlen |
| **3.x** | HA Discovery | Aktuell — für alle Nutzer empfohlen |
