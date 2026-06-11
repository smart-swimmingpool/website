---
title: Getting Started
weight: 10
tags: ["docs", "getting-started", "tutorial"]
---

**🏊 Smart Swimming Pool: Home automation for smarter control of your swimming pool**

## Example Environment

In a typical setup, a thermal solar system heats water and supports the home heating system. The heated water is stored in a buffer tank, which has a third circulation loop for the pool. A pump attached to this loop circulates pool water through a heat exchanger:

![Example Environment](schema-environment-smart-pool.png)

## Basic Requirements

- Swimming pool with sand filter system
- Heating circuit with a pump-switchable heat exchanger
- Solar heat storage tank with an additional heating circuit for the pool

## Preparations

If a heating circuit with a heat exchanger is in place, you can start implementing the smart pool control.

The heart of the system is the [Pool Controller](https://github.com/smart-swimmingpool/pool-controller). It handles:

- Circulation scheduling for sand filter cleaning
- Switching on the heating circuit to warm the pool water
- Reporting status and temperature data for integration with Smart Home servers

The [Pool Controller](https://github.com/smart-swimmingpool/pool-controller) uses [Home Assistant MQTT discovery](https://www.home-assistant.io/integrations/mqtt/#mqtt-discovery) for seamless smart home integration. With the configuration presented here, the pool controller can be quickly set up and controlled from any Home Assistant-compatible app.

### Home Assistant Dashboard

The pool controller automatically registers all sensors and controls in Home Assistant via MQTT discovery. Below is an example of the dashboard and the corresponding configuration entries:

![Home Assistant Dashboard](/img/ha-pool-dashboard.jpg)

*Pool Controller entities shown in the Home Assistant dashboard*

![Home Assistant Device Entry](/img/ha-pool-device.jpg)

*MQTT discovery device entry with all sensors and controls*

![Home Assistant Configuration](/img/ha-pool-config.jpg)

*Configuration entries for the pool controller in Home Assistant*

## History

🏊 Smart Swimming Pool originated from an [earlier project](https://github.com/stritti/smart-swimming-pool) that was not yet modular and had all control logic implemented as openHAB rules.

The first version ran in **Summer 2018** and revealed several weaknesses:

- Controlling pumps via 433 MHz socket switches was unreliable — no feedback meant the actual state was unknown
- Switching logic lived in openHAB rules, causing problems when WiFi was unreliable
- MQTT messages used a proprietary format

Based on these lessons, the revised 🏊 Smart Swimming Pool was built: modular, resilient, and standards-based.
