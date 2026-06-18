---
title: "Project Smart Swimming Pool"
date: 2018-12-01
authors:
  - name: "Stephan Strittmatter"
    link: https://github.com/stritti
    image: https://github.com/stritti.png
tags:
  - "Development"
---

Smart Control for the Swimming Pool — In the following four series of articles, we will describe step by step, how to control a swimming pool by means of self-built IoT modules. The cost of the required electronic components are less than 100 euros.

## Goal

1. Control the pool and its temperature via a solar system with open source and low-cost electronic components
2. Access via WiFi and Internet
3. Flexible expandability

## Starting Position

We have a swimming pool, which is cleaned by a sand filter system. This sand filter system has to filter the pool water daily for a certain amount of time.

In addition, we have a thermal solar system, which is designed to support heating and hot water. As this produces too much heat in the summer, it was natural to use this heat in the summer to heat the pool. This is easily possible via additional connections to the heat storage: a circulation pump directs the warm solar water through a [heat exchanger](https://pooldoktor.at/waermetauscher-pool.html), which heats the pool water.

The pump for the water circulation is switched by a timer. The pump for heating is switched on manually as required behind the timer. Of course this is stupid, if one has integrated the solar system in the morning and changes the weather in the course of the day: In the evening, the water for showering and cooking is cold, since all the energy has flowed into the pool. That should change this year!

## Requirements

From this situation arose the desire to control the pool smart. What are the basic requirements?

1. Sensors for heat accumulators and pool water
2. Switching possibility for the pumps
3. Control system

All this is easy to implement with an ESP micro controller and a Raspberry Pi. The individual solutions are also available in the web. The pitfalls, however, are in the detail of the combination.

## Required Hardware

The following parts and components needed for the pool controller:

- 1× ESP32 NodeMCU
- 2× temperature sensors DS18B20
- 1× 433MHz radio module
- 2× 4.7kΩ resistors
- 2× radio sockets
- various plug wires
- board or breadboard
- power supply

For the openHAB server:

- 1× Raspberry Pi

## Basis for the Pool Controller

Let's start with the heart of the game, the pool controller. In order not to reinvent the wheel again and again, I decided to set up the project on a basis. I found these in the [ESPBASE](https://github.com/Pedroalbuquerque/ESPBASE) project. As a template, the project offers support for setting up WiFi via an access point and some other functions that I no longer have to take care of myself. In his project, the developer created an [example](https://github.com/Pedroalbuquerque/ESPBASE/tree/master/Examples/WiFi_CFG_OTA_Telnet) for the use of ESPBASE. We will build the controller on this basis.

## Smart Home Integration

Finally, the pool controller is integrated into the open source home automation system [openHAB](https://www.openhab.org/) and thus also offers access via apps on the smartphone.

For the integration we need a protocol for the message exchange. We use MQTT for this. MQTT is a lightweight messaging protocol that is widely used in IoT (Internet of Things).

For the communication of the pool controller we will need an MQTT broker. For this purpose we have installed the broker [Mosquitto](https://mosquitto.org/) on the Raspberry Pi (since openHAB 2.4 there will be inbuild MQTT-server, too).

### Installing and Testing MQTT Server Mosquitto

We install the MQTT broker Mosquitto on the Raspberry Pi:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mosquitto mosquitto-clients
```

We open a Subscriber on the topic "/topic" which waiting for messages:

```bash
mosquitto_sub -h localhost -v -t /topic
```

The topic is like listening to a radio frequency. Different data such as temperatures can be transmitted in different channels.

We can test this directly on the Raspberry with the following command, which publishes a message in another console window:

```bash
mosquitto_pub -h localhost -t /topic -m "Hello smart Pool"
```

There are also clients for the smartphone or the Windows PC to receive or send the MQTT messages.

## Task of the Pool Controller

The pool controller will take over the central control. It cyclically measures the temperatures of the pool water and the heat storage of the solar system. He will also switch the pumps (filter and heater). The ESP is thus both sensor and actuator. The data exchange takes place via WiFi using MQTT.

### Temperature Measurement

Measuring the temperature is usually the entry into the programming of IoT sensors. There are various project examples. Often the temperature sensors [DHT11](https://amzn.to/2D28cJs) or the more accurate [DHT22](https://amzn.to/2Bf1e41) are used. However, since the temperature sensors in the project have to be distributed externally, we use the waterproof sensor [DS18B20](https://amzn.to/2HKjSXc). One of the two sensors for measuring the temperature of the pool water, the other for measuring the temperature in the buffer tank.

The measured temperatures are read by timer every 60 seconds and published by MQTT as a message. The interval is a compromise between the inertia of heating the water and debugging the program. Probably values would be sufficient every 5 minutes, but also the integration in openHAB makes the minute clock later much easier.

### Controlling Radio-controlled Sockets

Since I do not want to handle 230 volts AC directly in the project, I switch the pumps via radio-controlled sockets. There are some radio sockets that can be controlled via ESPs with a 433 MHz radio transmitter.

## Layout of the Circuit

The data pins on the ESP32 are assigned as follows:

```cpp
#define PIN_DS_SOLAR 16   // temp sensor solar
#define PIN_DS_POOL 17    // temp sensor pool
#define PIN_RSSWITCH 18   // for 433MHz transmitter
```

## Source Code of the Project

For the project we use the development environment [Platform.io IDE](https://platformio.org/platformio-ide). With this we create a project for the board `esp32dev`.

> The full source code of the project can be found in the GitHub repository: [https://github.com/stritti/smart-swimming-pool](https://github.com/stritti/smart-swimming-pool).

### Libraries Used

In this project, it is important to use proven software components and to solve as much as possible about existing libraries. For this reason, the following libs are used:

- **rc-switch**: Control of the radio-controlled sockets
- **OneWire**: Support for I2C sensors
- **DallasTemperature**: Reading out the temperature of the sensors
- **PubSubClient**: Receiving and sending MQTT messages
- **RemoteDebug**: Debugging via Telnet
- **ESPBASE**: Template for IoT projects

These libraries are stored in the configuration of Platform.io (`platformio.ini`) and are automatically loaded and integrated from the internet during compilation.

### The Details

1. In the `loop` function, the WiFi connection is repeatedly checked and, if necessary, restored. That was a treacherous problem: the ESP has repeatedly lost the wireless connection and without the reconnect it could no longer send any data.
2. The function `publish` is used to send the MQTT messages. Thus the data of a restart and the temperature measurement are published as JSON messages.
3. The timer for sending the temperatures is split. The reason is that the actual timer methods have to be as short as possible. In the implementation, the timer calls the `onTimer` function, which only increments the volatile `interruptCounter`. The `loop` function checks this and the actual `onTemperature` function is triggered. This method also reads and publishes the internal temperature of the ESP.
4. The function `onMQTTCallback` is called when a message is sent to a topic starting with `/pool/switch/`. The message contains the information of the radio-controlled socket whether it should be switched on or off. The topic is further subdivided into the group and the device coding. This means that the coding of the DIP switches of the socket is transformed into 0 and 1. As a result, this solution can also be used flexibly elsewhere.

The source code of the pool controller can be found directly in the following file: [Pool-Controller/src/pool-control.ino](https://github.com/stritti/smart-swimming-pool/blob/master/Pool-Controller/src/pool-control.ino)

## Testing

Once the circuit has been set up and the project loaded onto the ESP, we can already test it. The ESP will open a WiFi as an access point because there is no WiFi setup by default. If you connect with the pool controller with the smartphone, you can set up the right wireless. Thereafter, the micro controller restarts automatically and tries to connect to the specified WiFi.

If everything is set up correctly, a status message via MQTT should be published already at the start of the ESP. You can do this with the following command on the Raspberry track all messages:

```bash
mosquitto_sub -h localhost -v -t /#
```

It may be necessary to change the IP address of the MQTT server in the source code. Thereafter, the temperatures should be shown on the Raspberry in a minute cycle.

In the other direction we can switch the radio sockets by sending a suitable message. The topic consists of `/pool/switch/<group>/<device>`. `Group` and `Device` are the dip switches of the socket as 0 and 1. The message "ON" or "OFF" is sent.

## Swimming Pool and OpenHAB

After we created the controller for the pool control, we will now connect it via WiFi with OpenHAB and implement the rules for the smart control.

### Installation of OpenHAB

OpenHAB is a "Home Automation Broker", which is a Smart Home Server software that can be installed on a Raspberry Pi. There is a very good [documentation](https://www.openhab.org/docs/installation/openhabian.html).

I assume here that a basic installation of openHAB already exists.

We now need to add some addons to the installation under certain circumstances. This is possible via the "[Paper UI](https://www.openhab.org/docs/configuration/paperui.html)" interface under "Add-ons".

For the integration of the pool control, we need the following add-ons:

- MQTT Binding
- openHAB Cloud Connector (optional for internet access via smartphone apps)
- RRD4j Persistence
- JSONPath Transformation
- Basic UI

### Configuration

The configuration files that we create now are usually located in the path on the Raspberry `/etc/openhab2`. The corresponding structure with the files are stored in the GitHub repository.

### Connect MQTT Broker

The configuration for connecting the Mosquitto service can be found in the file `services/mqtt.cfg`. The host name and the port are configured there. In our case, openHAB and Mosquitto run on the same Raspberry.

### Sitemap with the Items

First we have to define the objects (items) in openHAB so that we can control and evaluate them on the sitemap.

### pool.items

The measuring and control points are defined in the file [`pool.items`](https://github.com/stritti/smart-swimming-pool/blob/master/OpenHAB/items/2-pool.items). There, for example, the links between the MQTT topics and the items are made. So there are the items for the temperatures, which receive the data from MQTT and the items send the messages to switch the pumps. The greater or lesser character in the configuration indicates the direction of the messages.

## The Smart Swimming Pool

Now it's all about making the controller really smart: the regulation is automatic and can be adjusted via WLAN or Internet.

### Rule Control of Pool

I have implemented three modes for the heating of the pool:

### Mode: Auto

The fully automatic mode switches the filter pump time-controlled and automatically heats the pool water up to a maximum temperature. However, this only as long as the minimum temperature in the heat storage is not exceeded.

### Mode: Boost

Similar to the "Auto" mode, but without considering the minimum temperature in the heat accumulator.

### Mode: Manual

The pumps are manually switched on and off via the app. Regardless of rules and thresholds.

### The Limit Values

The following three parameters are required to control the temperature of the pool:

- **Maximum pool temperature**: How warm should the pool be?
- **Minimum heat storage temperature**: What temperature must the water in the storage tank at least have, that the pool can be co-heated?
- **Hysteresis**: How big should the temperature deviation be before the min/max rules affect?

### The Smart Heart: pool.rules

The rules in the `pool.rules` are the rules of openHAB. These rules use the configuration values that you can set in the settings.

The values of the temperature sensors are compared here and the radio sockets are then controlled on the basis of the hysteresis. Hysteresis is necessary so that the pumps are not constantly switched on and off at very low temperature differences. A value of 0.5 Kelvin has proved to be completely sufficient.

The rules are divided and thus operate the individual operating modes.

### Add-On: Display Module

To monitor the temperatures even without an app, we put a small monitoring application in an old screw box. This module was based on the LCD display, which was also featured in a [blog article](https://www.az-delivery.de/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/lcd-display-16-x-2-produkteinfuhrung?ls=de).

This pool monitor is based on an ESP8266 and a LCD display 16×2. The ESP receives the temperature values — also via MQTT — and updates the display.

The source code for this is also located in the code repository and was derived from the pool controller.

The case is an old screw box that has been padded with some filler material. Something tricky was the hole for the micro USB plug. Maybe next year this box will be upgraded and equipped with a solar cell. Then this can also be installed outside near the pool.

## Open Source

The aim from the beginning was to create a project based on open source. So, of course, again an open source project was created.

The entire project is available on GitHub:

[https://github.com/stritti/smart-swimming-pool](https://github.com/stritti/smart-swimming-pool)

## Conclusion

The pool controller has been in use since May and after a few improvements has worked reliably over the complete summer.

The main problem was actually the missing check, whether the WiFi connection still exists. We always thought we had a leak in the code somewhere, but occasionally the ESP controller just lost the connection over the WiFi. Now the controller runs reliably, provides data and controls the pumps.

Since this year, so there is a nice warm pool and still always enough hot water in the home. A project with clear added value in terms of comfort with relatively little financial input.

## Outlook

There are still a few ways to improve and expand the project over the coming winter. We think of:

- Temperature sensor directly on the solar circuit to check whether the heater is in solar or heating mode
- Outdoor sensor for ambient temperature and water temperature with solar cell supply
- The control directly in the ESP code on the pool controller (only update the configuration and monitoring via MQTT)
- Greater security through encryption of MQTT communication
- Measurement of water quality (pH, chlorine) by additional sensors
- Inclusion of weather forecast to better allocate the buffer memory
- Switch inbuild MQTT service of openHAB 2.4+ (and use Homie 3.0 conform MQTT messages)

I am looking forward to replicas, inspired projects and suggestions for further improvements. Also available as pull requests on GitHub.

## Author

**Stephan Strittmatter** is talent scout at an IT consulting company and brings software development closer to young professionals. A few months ago he finally had contact points with the ESP controllers via the Raspberry Pi and the BBC micro:bit. They made his childhood dream possible, to finally connect hardware and software easily. The private pool was therefore a welcome project to combine IoT, Smart Home and research drive.
