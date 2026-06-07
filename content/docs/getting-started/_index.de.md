---
title: Getting Started
linktitle: Getting Started
description: Getting Stated für den Smart Swimming Pool - Heimautomation für eine intelligentere Steuerung Ihres Swimmingpools
summary: Getting Stated für den Smart Swimming Pool - Heimautomation für eine intelligentere Steuerung Ihres Swimmingpools
type: docs
date: "2020-05-28"
publishdate: "2020-05-28"
lastmod: "2020-06-02"
featured: true
menu:
  docs:
    parent: Dokumente
    name: Getting Started
    weight: 10
toc: true
tags: ["docs", "getting-started", "tutorial"]
---

**🏊 Smart Swimming Pool: Heimautomatisierung für eine intelligentere Steuerung Ihres Schwimmbads**

## Beispiel einer Anlage

In meiner Anlage habe ich ein thermisches Solarsystem zur Warmwasserbereitung
und zur Unterstützung der Raumheizung im Haus. Das erwärmte Wasser wird in
einem Puffer gesammelt, der eine dritte Zirkulation für meinen Pool hat.

An diese dritte Zirkulation ist eine Pumpe angeschlossen, die über einen
Wärmetauscher das Wasser des Pools erwärmt:

{{< figure library="true" src="schema-environment-smart-pool.png" title="Beispielaufbau" lightbox="true" >}}

## Grundvoraussetzungen

- Swimmingpool mit Sandfilteranlage
- Über eine Pumpe zuschaltbarer Heizkreislauf mit Wärmetauscher
- Solarer Wärmespeicher mit zusätzlichem Heizkreislauf für den Pool

## Vorbereitungen

Sofern ein Heizkreislauf über einen Wärmetauscher vorbereitet ist, kann mit der Umsetzung der smarten Steuerung des Pools begonnen werden.

Herz des Systems ist der [Pool Controller](https://github.com/smart-swimmingpool/pool-controller). Dieser übernimmt die zentrale Steuerung von:

- Zirkulationszeitraum für die Reinigung mittels Sandfilteranlage
- Zuschalten des Heizkreislaufs für Erwärmung des Poolwassers
- Melden der Zustände und aktuellen Temperaturen für die Integration in Smart Home Server Lösungen

Der [Pool Controller](https://github.com/smart-swimmingpool/pool-controller) unterstützt zur Kommunikation mit anderen Smart Home Systemen das auf MQTT basierende Protokoll [Homie](https://homieiot.github.io/) und bietet somit eine einfache Integration beispielsweise in [openHAB](https://github.com/smart-swimmingpool/openhab-config). Mittels der vorgestellten Konfiguration für den openHAB-Server kann so schnell und einfach die Steuerung und Konfiguration des Pool Controllers vorgenommen werden.

## Historie

🏊 Smart Swimming Pools basiert auf dem
[ersten Projekt](https://github.com/stritti/smart-swimming-pool) das noch
nicht modular aufgebaut war und die Steuerlogik innerhalb von openHAB-Regeln
implementiert hatte.

Diese Version war im __Sommer 2018__ im Einsatz und zeigte ein paar Schwächen:

- Die Steuerung der Pumpen über 433MHz-Steckdosenschalter war nicht zuverlässig, da es keine
  Schaltbestätigung gab und der Status so unbekannt war.
- Die Schaltlogik war als Regeln auf dem openHAB-Server implementiert. Das führte zu Problemen,
  wenn das WLAN nicht zuverlässig funktioniert.
- Die MQTT-Nachrichten hatten ein proprietäres Nachrichtenformat.

Aus der Erfahrung des Sommers 2018 entstand dann diese überarbeitete Version
des 🏊 Smart Swimming Pools: modular, widerstandsfähig, auf Standards setzend.
