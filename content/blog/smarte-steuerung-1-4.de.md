---
title: "Smarte Steuerung für den Swimmingpool (1/4)"
date: 2018-10-19
authors:
  - name: "Stephan Strittmatter"
    link: https://github.com/stritti
    image: https://github.com/stritti.png
tags:
  - "Development"
  - "Deutsch"
---

In der folgenden vierteiligen Artikelserie werden wir Schritt für Schritt beschreiben, wie man einen Swimmingpool mittels selbstgebauten IoT-Modulen steuern kann. Die Kosten der benötigten elektronischen Bauteile liegen dabei unter 100 Euro.

## Ziel

1. Mit Open Source und preiswerten Elektronikkomponenten den Pool und seine Temperatur über eine Solaranlage steuern
2. Zugriff über WLAN und Internet
3. Flexible Erweiterbarkeit

## Ausgangslage

Wir haben einen Swimmingpool, der über eine Sandfilteranlage gereinigt wird. Diese Sandfilteranlage muss täglich für eine gewisse Zeit das Poolwasser filtern.

Zusätzlich haben wir eine thermische Solaranlage, welche zur Unterstützung von Heizung und Warmwasser ausgelegt ist. Da diese im Sommer viel zu viel Wärme produziert, lag die Überlegung nahe, diese Wärme im Sommer zur Beheizung des Pools zu nutzen. Dies ist über zusätzliche Anschlüsse am Wärmespeicher ohne weiteres möglich: eine Umwälzpumpe leitet das warme Solarwasser durch einen [Wärmetauscher](https://pooldoktor.at/waermetauscher-pool.html), der das Poolwasser erwärmt.

Die Pumpe für die Wasserumwälzung wird über eine Zeitschaltuhr geschaltet. Die Pumpe zur Erwärmung wird manuell nach Bedarf hinter der Zeitschaltuhr mit zugeschaltet. Das ist natürlich doof, wenn man morgens die Solaranlage mit eingebunden hat und im Laufe des Tages das Wetter umschlägt: Am Abend ist das Wasser zum Duschen und Kochen kalt, da alle Energie in den Pool geflossen ist. Das sollte sich dieses Jahr ändern!

## Anforderungen

Aus dieser Situation entstand der Wunsch, den Pool smart zu steuern. Was wird grundsätzlich dazu benötigt?

1. Sensoren für Wärmespeicher und Poolwasser
2. Schaltmöglichkeit für die Pumpen
3. Eine Regelsteuerung

All das ist mit einem ESP-Microcontroller und einem Raspberry Pi einfach umzusetzen. Die einzelnen Lösungen gibt es für sich genommen auch hier im Blog:

- [Thermometer mit OLED Display](https://www.az-delivery.de/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/thermometer-mit-oled-display?ls=de)
- [Raspberry Pi mit OpenHab](https://www.az-delivery.de/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/raspberry-mit-openhab2)
- [Was funkt denn da? 433Mhz Module](https://www.az-delivery.de/blogs/azdelivery-blog-fur-arduino-und-raspberry-pi/was-funkt-denn-da-433mhz-module-prufen?ls=de)

Die Tücken stecken jedoch im Detail der Kombination. Das werden wir in den folgenden Artikeln sehen.

## Benötigte Hardware

Folgende Bauteile und Komponenten werden für den Pool-Controller benötigt:

- 1× ESP32 Development Board
- 2× Temperatursensoren DS18B20
- 1× 433MHz Funkmodul
- 2× 4.7kΩ Widerstände
- 2× Funksteckdosen
- diverse Steckdrähte
- Platine bzw. Breadboard
- Stromversorgung

Für den OpenHAB-Server:

- 1× Raspberry Pi als Serverzentrale

## Basis für den Pool-Controller

Beginnen werden wir mit dem Herzstück, dem Pool-Controller. Um das Rad nicht immer wieder neu zu erfinden, haben wir uns entschieden, für das Projekt auf einer Basis aufzusetzen. Diese haben wir in dem Projekt [ESPBASE](https://github.com/Pedroalbuquerque/ESPBASE) gefunden. Das Projekt bietet als Template Unterstützung für die Einrichtung von WLAN über einen Accesspoint und einige andere Funktionen, um die wir uns nicht mehr selbst kümmern müssen. Der Entwickler hat in seinem Projekt ein [Beispiel](https://github.com/Pedroalbuquerque/ESPBASE/tree/master/Examples/WiFi_CFG_OTA_Telnet) für die Nutzung von ESPBASE erstellt. Auf dieser Basis werden wir den Controller aufbauen.

## Smart Home Integration

Schlussendlich wird der Pool-Controller in die Open Source Homeautomation [openHAB](https://www.openhab.org/) integriert und bietet damit auch Zugriff über Apps auf dem Smartphone.

Für die Integration benötigen wir ein Protokoll für den Nachrichtenaustausch. Wir nutzen dafür MQTT. MQTT ist ein leichtgewichtiges Nachrichtenprotokoll, das sehr häufig im Bereich IoT (Internet der Dinge) genutzt wird.

Für die Kommunikation des Pool-Controllers werden wir einen MQTT-Broker benötigen. Dazu haben wir auf dem Raspberry Pi den Broker [Mosquitto](https://mosquitto.org/) installiert (seit openHAB 2.4 gibt es auch einen integrierten MQTT-Server).

### MQTT Server Mosquitto installieren und testen

Den MQTT-Broker Mosquitto installieren wir auf dem Raspberry Pi:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mosquitto mosquitto-clients
```

Wir öffnen einen Subscriber auf dem Topic `/topic`, welcher auf Nachrichten wartet:

```bash
mosquitto_sub -h localhost -v -t /topic
```

Das Topic ist wie eine Radiofrequenz, auf der zugehört wird. So können in verschiedenen Kanälen unterschiedliche Daten wie z.B. die Temperaturen gesendet werden.

Testen können wir dies direkt auf dem Raspberry mit folgendem Kommando, welches in einem weiteren Konsolenfenster eine Nachricht publiziert:

```bash
mosquitto_pub -h localhost -t /topic -m "Hallo smart Pool"
```

Es gibt auch Clients für das Smartphone oder den Windows-PC, um die MQTT-Nachrichten zu empfangen oder zu versenden.

## Wie geht es weiter?

Nun sind die ersten Voraussetzungen geschaffen. Im folgenden Artikel werden wir den Pool-Controller auf Basis des ESP32 vorstellen, der seine Daten über den eingerichteten MQTT-Broker bereitstellt.

- [Weiter zu Teil 2: Der Pool-Controller (2/4)]({{< relref "pool-controller-2-4" >}})
