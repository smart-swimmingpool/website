---
title: OpenHAB Configuration | 🏊 Smart Swimmingpool 
date: "2020-05-28"
lastmod: "2020-06-02"
draft: false
toc: true
type: docs
featured: true

tags: ["docs", "openHAB", "tutorial"]

menu:
  docs:
    parent: OpenHAB
    name: Configuration
    weight: 30
---

<span style="text-shadow: none;">
<a class="github-button" href="https://github.com/smart-swimmingpool/openhab-config/subscription" data-size="large" data-show-count="true" aria-label="Watch smart-swimmingpool/openhab-config on GitHub">Watch</a>
<a class="github-button" href="https://github.com/smart-swimmingpool/openhab-config" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star this on GitHub">Star</a><script async defer src="https://buttons.github.io/buttons.js"></script>

[GitHub Project](https://github.com/smart-swimmingpool/openhab-config)
</span>

Configuration example to use the Smart Swimming Pool system on openHAB.

## Features

- [x] Switch Modes: Auto, Manual, Boost, Timer
- [x] Monitor current temparature of pool water and solar heating
- [x] Configuration of
    - start and end time of cleaning circulation time
    - max. temparature of pool water
    - min temparature of solar heating 
    - hystesis
- [x] Compatible with Alexa openHAB Add-on

## OpenHAB BasicUI Sitemap

| openHAB Pool Automation: Overview            | openHAB Pool Automation: Settings         |
|----------------------------------------------|----------------------------------------------|
| <img alt="openHAB Pool Automation overview" src="openhab-basicui-overview.png"  width="220">  | <img alt="openHAB Pool Automation temperature" src="openhab-basicui-settings.png"  width="220"> |

## Mobile App (openHAB iOS)

This configuration running on openHAB iOS App:

| openHAB Pool Automation: Overview            | openHAB Pool Automation: Temparature         |
|----------------------------------------------|----------------------------------------------|
| <img alt="openHAB Pool Automation overview" src="openhab-pool-automation-overview.png"  width="220">  | <img alt="openHAB Pool Automation temperature" src="openhab-pool-automation-temparature.png"  width="220"> |


| openHAB Pool Automation: Settings            | openHAB Pool Automation: Settings            |
|----------------------------------------------|----------------------------------------------|
| <img alt="openHAB Pool Automation settings" src="openhab-pool-automation-settings-1.png" width="220"> | <img alt="openHAB Pool Automation settings" src="openhab-pool-automation-settings-2.png" width="220"> |



## Precondition

The Smart Swimming Pool project uses Homie 3.0 based MQTT messaging. Therfor you have to install 
an MQTT broker in your environment.

### Raspberry Pi

I use an Raspberry Pi (Model 3) ([Amazon](https://amzn.to/2NnqwDQ)). The latest version of openHAB has an embedded MQTT broker. In this example a seperate broker [Mosquitto](https://mosquitto.org/) on same Raspberry Pi is configured.

### Install Mosquitto

- Install Mosquitto on Raspberry Pi:
  ``` 
  sudo apt-get update
  sudo apt-get upgrade
  sudo apt-get install mosquitto
  ```
- In Paper UI install add-on 'MQTT Binding' from bindings.
- Check `services/mqtt.cfg` for your environment.
