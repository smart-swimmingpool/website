---
title: Getting Started
linktitle: Getting Started
description: Getting Stated on Smart Swimming Pool
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

**🏊 Smart Swimming Pool: Pool automation for Smarter Control of your Swimming Pool**

## Example Environment

In my setting I have a thermal solar system for heating water and for
support of heating environment within the house. the heated water is
collected within a buffer which has a third circulation for my pool.
Attached to this third circulation a pump is attached to heat via heat
exchanger the water of the pool:

{{< figure library="true" src="schema-environment-smart-pool.png"
    title="Example Environment" lightbox="true" >}}

## History

Version 2 of the 🏊 Smart Swimming Pool is based on the
[first project](https://github.com/stritti/smart-swimming-pool)
which is not yet modular and had implemented the control logic
within openHAB rules.

This version was in use in __Summer 2018__ and showed some weaknesses:

- Controlling the pumps via 433MHz socket switches was not reliable,
  because there were no confirmation and the status was so unknown.
- The switching logic was implemented as rules on the openHAB server.
  This led to problems, if the WLAN does not work reliably.
- The MQTT messages had a proprietary message format.

From the experience of the summer of 2018 resulted this second
version of the 🏊 Smart Swimming Pool.
