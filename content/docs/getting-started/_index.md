---
title: Getting Started
linktitle: Getting Started
description: Getting Stated on Smart Swimming Pool - Home automation for smarter Control of your Swimming Pool
type: docs  # Do not modify.
date: "2020-05-28"
publishdate: "2020-05-28"
lastmod: "2020-05-28"
featured: true
menu:
  docs:
    parent: Documents
    name: Getting Started
    weight: 10
tags: ["docs", "getting-started", "tutorial"]
toc: true
---

**🏊 Smart Swimming Pool: Home automation for smarter Control of your Swimming Pool**

## Example Environment

In my setting I have a thermal solar system for heating water and for
support of heating environment within the house. the heated water is
collected within a buffer which has a third circulation for my pool.
Attached to this third circulation a pump is attached to heat via heat
exchanger the water of the pool:

{{< figure library="true" src="schema-environment-smart-pool.png"
    title="Example Environment" lightbox="true" >}}

## Basic Requirements

- Swimming pool with sand filter system
- Heating circuit with heat exchanger that can be switched on via a pump
- Solar heat storage tank with additional heating circuit for the pool

## Preparations

If a heating circuit is prepared via a heat exchanger, the implementation of the smart control of the pool can be started.

The heart of the system is the [Pool Controller]({{{< ref "../pool-controller" >}}). This is responsible for the central control of:

- Circulation period for cleaning by means of a sand filter system
- Switching on the heating circuit for warming up the pool water
- Reporting of statuses and current temperatures for integration into Smart Home Server solutions

The [pool controller]({{{{{< ref "../pool-controller" >}}) supports the MQTT based protocol [Homie](https://homieiot.github.io/) for communication with other smart home systems and thus offers easy integration into [openHAB]({{{{{< ref "../openhab-configuration" >}}). Using the configuration for the openHAB-Server presented here, the pool controller can be quickly and easily controlled and configured.

## History

🏊 Smart Swimming Pool is based on the
[first project](https://github.com/stritti/smart-swimming-pool)
which was not yet modular and had implemented the control logic
within openHAB rules.

The first version was in use in __Summer 2018__ and showed some weaknesses:

- Controlling the pumps via 433 MHz socket switches was not reliable,
  because there were no confirmation and the status was unknown.
- The switching logic was implemented in rules on the openHAB server.
  This led to problems, if the WiFi does not work reliably.
- The MQTT messages had a proprietary message format.

From the experience of the summer of 2018 resulted this revised
version of the 🏊 Smart Swimming Pool: modular, resiliant using standards.
