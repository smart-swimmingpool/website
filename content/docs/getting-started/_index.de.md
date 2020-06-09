---
linktitle: Getting Started
summary: Getting Stated on Smart Swimming Pool
weight: 1

# page metadata.
title: Getting Started
date: "2020-05-28"
lastmod: "2020-06-02"
draft: false
toc: true
type: docs
featured: true

tags: ["docs", "getting-started", "tutorial"]

menu:
  docs:
    parent: Dokumente
    name: Getting Started
    weight: 10
---

## Beispiel einer Anlage

In meiner Anlage habe ich ein thermisches Solarsystem zur Warmwasserbereitung
und zur Unterstützung der Raumheizung im Haus. Das erwärmte Wasser wird in
einem Puffer gesammelt, der eine dritte Zirkulation für meinen Pool hat.

An diese dritte Zirkulation ist eine Pumpe angeschlossen, die über einen
Wärmetauscher das Wasser des Pools erwärmt:

{{< figure library="true" src="schema-environment-smart-pool.png" title="Beispielaufbau" lightbox="true" >}}

## Historie

Die Version 2 des 🏊 Smart Swimming Pools basiert auf dem
[ersten Projekt](https://github.com/stritti/smart-swimming-pool) das noch
nicht modular aufgebaut war und die Steuerlogik innerhalb von openHAB-Regeln
implementiert hatte.

Diese Version war im __Sommer 2018__ im Einsatz und zeigte ein paar Schwächen:

- Die Steuerung der Pumpen über 433MHz-Steckdosenschalter war nicht zuverlässig, da es keine
  Schaltbestätigung gab und der Status so unbekannt war.
- Die Schaltlogik war als Regeln auf dem openHAB-Server implementiert. Das führte zu Problemen,
  wenn das WLAN nicht zuverlässig funktioniert.
- Die MQTT-Nachrichten hatten ein proprietäres Nachrichtenformat.

Aus der Erfahrung des Sommers 2018 entstand dann diese zweite Version
des 🏊 Smart Swimming Pools.
