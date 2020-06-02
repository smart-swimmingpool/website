---
linktitle: OpenHAB Config
summary: OpenHAB config to control the Smart Swimming Pool via openHAB
weight: 3

# page metadata.
title: OpenHAB Configuration
date: "2020-05-28"
lastmod: "2020-06-02"
draft: false
toc: true
type: docs
featured: true

tags: ["docs", "openHAB", "tutorial"]

menu:
  docs:
    parent: Dokumente
    name: OpenHAB Config
    weight: 20
---

<span style="text-shadow: none;">
<a class="github-button" href="https://github.com/smart-swimmingpool/openhab-config/subscription" data-size="large" data-show-count="true" aria-label="Watch smart-swimmingpool/openhab-config on GitHub">Watch</a>
<a class="github-button" href="https://github.com/smart-swimmingpool/openhab-config" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star this on GitHub">Star</a><script async defer src="https://buttons.github.io/buttons.js"></script>

[GitHub Project](https://smart-swimmingpool.github.io/openhab-config/)
</span>

Configuration example to use the Smart Swimming Pool system on openHAB.

## Precondition

The Smart Swimming Pool project uses Homie 3.0 based MQTT messaging. Therfor you have to install
an MQTT broker in your environment.

## Raspberry Pi

I use an Raspberry Pi (Model 3) ([Amazon](https://amzn.to/2NnqwDQ)). The latest version of openHAB has an embedded MQTT broker. I us a seperate broker [Mosquitto](https://mosquitto.org/) on Raspberry Pi.

### Install Mosquitto

- Install Mosquitto on Raspberry Pi:
  ```
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install mosquitto
  ```
- In Paper UI install add-on 'MQTT Binding' from bindings.
- Check `services/mqtt.cfg` for your environment.

# Documentation

see at [https://smart-swimmingpool.github.io/openhab-config/](https://smart-swimmingpool.github.io/openhab-config/)


[![works with MQTT Homie](https://homieiot.github.io/img/works-with-homie.svg "works with MQTT Homie")](https://homieiot.github.io/)
