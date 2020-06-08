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

**🏊 Smart Swimming Pool: Pool Automatisierung zur smarten Steuerung des Swimmingpools**

Dieses Projekt ist in verschiedene Module aufgeteilt:

- [Pool Controller]({{< ref "../pool-controller/_index.de.md" >}})
- [OpenHab Konfiguration]({{< ref "../openhab-configuration/_index.de.md" >}})

Zudem gibt es ein [Wiki](https://github.com/smart-swimmingpool/smart-swimmingpool/wiki).

## Beispiel einer Anlage

In meiner Anlage habe ich ein thermisches Solarsystem zur Warmwasserbereitung und zur Unterstützung der Raumheizung im Haus. Das erwärmte Wasser wird in einem Puffer gesammelt, der eine dritte Zirkulation für meinen Pool hat.
An diese dritte Zirkulation ist eine Pumpe angeschlossen, die über einen Wärmetauscher das Wasser des Pools erwärmt:

{{< figure library="true" src="schema-environment-smart-pool.png" title="Beispielaufbau" lightbox="true" >}}
