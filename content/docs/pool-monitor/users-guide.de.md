---
source: https://github.com/smart-swimmingpool/monitor/tree/main
file: users-guide.de.md
lastmod: 23. May 2026
---
---
title: Users Guide of Pool Controller
date: '2022-06-11'
draft: false
tags:
- docs
- monitor
- tutorial
---

## Setup

Connecting the device to power it createsinitial a hotspot called "pool-monitor".
Please connect this hotsppot by smartphone. Thenthe device will show captivate website to add
WiFi credentials and connection parameters of MQTT broker.

Following data is required to connect the device:

* SSID of the WiFi network
* Password of WiFi network
* MQTT broker hostname or IP address
* MQTT broker port number (default: 1883)

After pressing "Save" the device will reboot automatically and tries to connect to the MQTT broker.

After some seconds the device will show data if connection was successful.
