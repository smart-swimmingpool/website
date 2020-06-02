---
linktitle: Pool Controller
summary: Control your Smart Swimming Pool smart
weight: 2

# page metadata.
title: Pool Controller
date: "2020-05-28"
lastmod: "2020-06-02"
draft: false
toc: true
type: docs
featured: true

tags: ["docs", "controller", "tutorial"]

menu:
  docs:
    parent: Dokumente
    name: Pool Controller
    weight: 10
---
**🏊 The Homie 3.0 compatible Smart Swimmingpool Controller 🎛️**

Manage your swmming pool on the smart way to enjoy it in confortable and cheap (less than 100€) way.

## Main Features

- [x] Manage water timed circulation for cleaning
- [x] Manage water heating by additional pump for solar circuit
- [x] [Homie 3.0](https://homieiot.github.io/) compatible MQTT messaging
- [x] Independent of specific smarthome servers
  - [x] [openHAB](https://www.openhab.org) since Version 2.4 using MQTT Homie
  - [x] [Home Assistant](home-assistant.io) using MQTT Homie
- [x] Timesync via NTP (europe.pool.ntp.org)
- [x] Logging-Information via Homie-Node

## Planned Features

- [ ] Configurable NTP Server (currently hardcoded: europe.pool.ntp.org)
- [ ] be more smart: self learning for improved pool pump timed circulation for cleaning and heating
- [ ] two separate circulation cycles
- [ ] store configuration changes persistent on conroller
- [ ] temperature based cleaning circulation time (colder == shorter, hotter == longer)
- [ ] Improved sketch to work completly without WiFi connection
      - Homie should run without WiFi connection
      - enhance sketch using display and buttons to setup environment.
- see also the [issue list](https://github.com/smart-swimmingpool/pool-controller/issues)

## Guides

- [Software Guide](https://smart-swimmingpool.github.io/pool-controller/software-guide.html)
- [Hardware Guide](https://smart-swimmingpool.github.io/pool-controller/hardware-guide.html)
- [Users Guide](https://smart-swimmingpool.github.io/pool-controller/users-guide.html)


[![works with MQTT Homie](https://homieiot.github.io/img/works-with-homie.svg "works with MQTT Homie")](https://homieiot.github.io/)