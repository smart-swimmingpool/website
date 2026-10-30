---
title: Publikationen
weight: 62
tags: ["docs", "publication"]
---

Auch verfügbar als [Blog-Beiträge]({{< relref path="/blog" lang="de" >}}) auf dieser Seite.

- [Projekt Smart Swimmingpool](https://www.az-delivery.de/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/projekt-smart-swimmingpool-einleitung), _Oktober 2018_

  Vierteilige Blog-Reihe zur Version 1 des Smart Pool Controllers.

  📄 [Hier auf der Seite lesen]({{< relref "/blog/projekt-smart-swimmingpool-einleitung" >}})

  - [Smarte Steuerung für den Swimmingpool (1/4)]({{< relref "/blog/smarte-steuerung-1-4" >}})
  - [Der Pool-Controller (2/4)]({{< relref "/blog/pool-controller-2-4" >}})
  - [Swimmingpool und OpenHAB (3/4)]({{< relref "/blog/swimmingpool-openhab-3-4" >}})
  - [Der smarte Pool (4/4)]({{< relref "/blog/der-smarte-pool-4-4" >}})

- [Project Smart Swimming Pool](https://medium.com/diy-my-smart-home/project-smart-swimmingpool-4c40eb6741f6), _Dezember 2018_

  Englischer Blogpost über Version 1 des Smart Swimming Pool.

  📄 [Hier auf der Seite lesen]({{< relref path="/blog/smart-swimming-pool-project" lang="en" >}})

## Projektgeschichte

🏊 Smart Swimming Pool basiert auf einem [früheren Projekt](https://github.com/stritti/smart-swimming-pool), das noch nicht modular aufgebaut war und die gesamte Steuerlogik als openHAB-Regeln implementierte.

Die erste Version war im **Sommer 2018** im Einsatz und zeigte einige Schwächen:

- Die Steuerung der Pumpen über 433-MHz-Steckdosenschalter war unzuverlässig — ohne Rückmeldung war der tatsächliche Status unbekannt
- Die Schaltlogik lebte in openHAB-Regeln, was bei unzuverlässigem WLAN zu Problemen führte
- MQTT-Nachrichten verwendeten ein proprietäres Format

Aus diesen Erfahrungen entstand die überarbeitete Version des 🏊 Smart Swimming Pools: modular, widerstandsfähig und auf Standards basierend.
