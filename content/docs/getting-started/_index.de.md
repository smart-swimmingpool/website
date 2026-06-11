---
title: Getting Started
weight: 10
tags: ["docs", "getting-started", "tutorial"]
---

**🏊 Smart Swimming Pool: Heimautomatisierung für eine intelligentere Steuerung Ihres Schwimmbads**

## Beispiel einer Anlage

In einer typischen Anlage erwärmt ein thermisches Solarsystem das Wasser und unterstützt die Raumheizung im Haus. Das erwärmte Wasser wird in einem Pufferspeicher gesammelt, der eine dritte Zirkulation für den Pool bereitstellt. Eine Pumpe an diesem Kreislauf leitet das Poolwasser durch einen Wärmetauscher:

![Beispielaufbau](schema-environment-smart-pool.png)

## Grundvoraussetzungen

- Swimmingpool mit Sandfilteranlage
- Über eine Pumpe zuschaltbarer Heizkreislauf mit Wärmetauscher
- Solarer Wärmespeicher mit zusätzlichem Heizkreislauf für den Pool

## Vorbereitungen

Sofern ein Heizkreislauf mit Wärmetauscher vorbereitet ist, kann mit der Umsetzung der smarten Steuerung des Pools begonnen werden.

Herz des Systems ist der [Pool Controller](https://github.com/smart-swimmingpool/pool-controller). Dieser übernimmt:

- Steuerung der Zirkulationszeit für die Sandfilterreinigung
- Zuschalten des Heizkreislaufs zur Erwärmung des Poolwassers
- Melden von Status und Temperaturen für die Integration in Smart-Home-Server

Der [Pool Controller](https://github.com/smart-swimmingpool/pool-controller) nutzt [Home Assistant MQTT Discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) für nahtlose Smarthome-Integration. Mit der hier vorgestellten Konfiguration kann der Pool-Controller schnell eingerichtet und von jeder Home Assistant-kompatiblen App gesteuert werden.

### Home Assistant Dashboard

Der Pool Controller registriert via MQTT Discovery automatisch alle Sensoren und Steuerelemente in Home Assistant. Nachfolgend ein Beispiel des Dashboards und der zugehörigen Konfigurationseinträge:

![Home Assistant Dashboard](/img/ha-pool-dashboard.jpg)

*Pool-Controller-Entitäten im Home Assistant Dashboard*

![Home Assistant Device Eintrag](/img/ha-pool-device.jpg)

*MQTT Discovery-Geräteeintrag mit allen Sensoren und Steuerungen*

![Home Assistant Konfiguration](/img/ha-pool-config.jpg)

*Konfigurationseinträge für den Pool Controller in Home Assistant*

## Historie

🏊 Smart Swimming Pool basiert auf einem [früheren Projekt](https://github.com/stritti/smart-swimming-pool), das noch nicht modular aufgebaut war und die gesamte Steuerlogik als openHAB-Regeln implementierte.

Die erste Version war im **Sommer 2018** im Einsatz und zeigte einige Schwächen:

- Die Steuerung der Pumpen über 433-MHz-Steckdosenschalter war unzuverlässig — ohne Rückmeldung war der tatsächliche Status unbekannt
- Die Schaltlogik lebte in openHAB-Regeln, was bei unzuverlässigem WLAN zu Problemen führte
- MQTT-Nachrichten verwendeten ein proprietäres Format

Aus diesen Erfahrungen entstand die überarbeitete Version des 🏊 Smart Swimming Pools: modular, widerstandsfähig und auf Standards basierend.
