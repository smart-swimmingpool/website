---
title: "Der Pool-Controller (2/4)"
date: 2018-10-22
authors:
  - name: "Stephan Strittmatter"
    link: https://github.com/stritti
    image: https://github.com/stritti.png
tags:
  - "Development"
  - "Deutsch"
  - "ESP32"
---

Im [vorangegangenen Artikel]({{< relref "smarte-steuerung-1-4" >}}) haben wir einen Überblick über das Projekt des smart gesteuerten Pools gegeben. In diesem zweiten Teil werden wir auf das Herzstück, den Controller, eingehen. Dieser basiert auf einem ESP32, könnte aber mit wenigen Modifikationen auch mit einem ESP8266 umgesetzt werden.

## Aufgabe des Pool-Controllers

Der Controller wird die zentrale Steuerung übernehmen. Er misst zyklisch die Temperaturen des Poolwassers und des Wärmespeichers der Solaranlage. Zudem wird er die Pumpen (Filter und Heizung) schalten. Der ESP ist also sowohl Sensor als auch Aktor. Der Datenaustausch erfolgt über WLAN mittels MQTT.

### Temperaturen messen

Das Messen der Temperatur ist meist der Einstieg in die Programmierung von IoT-Sensoren. Es gibt diverse Projektbeispiele dazu. Dabei kommen oft die Temperatursensoren DHT11 oder der genauere DHT22 zum Einsatz. Da die Temperatursensoren im Projekt jedoch verteilt extern platziert werden müssen, verwenden wir den wasserdichten Sensor [DS18B20](https://www.az-delivery.de/collections/temperatursensoren/products/2xds18b20wasserdicht?ls=de). Einen der beiden Sensoren zur Messung der Temperatur des Poolwassers, der andere zur Messung der Temperatur im Pufferspeicher.

Die gemessenen Temperaturen werden mittels Timer alle 60 Sekunden ausgelesen und per MQTT als Nachricht veröffentlicht. Der Intervall ist ein Kompromiss zwischen der Trägheit der Erwärmung des Wassers und dem Debugging des Programms. Vermutlich würden auch Werte alle 5 Minuten ausreichen, doch auch die Integration in OpenHAB macht der minütliche Takt später wesentlich einfacher.

### Funksteckdosen steuern

Da wir in dem Projekt nicht direkt mit 230 Volt Wechselspannung hantieren möchten, schalten wir die Pumpen über Funksteckdosen. Bei den Funksteckdosen gibt es einige, die man über ESPs mit einem [433 MHz Funksender](https://www.az-delivery.de/products/433-mhz-modul?ls=de) steuern kann. Eine Liste der kompatiblen Funksteckdosen findet sich im [Wiki](https://github.com/sui77/rc-switch/wiki/List_KnownDevices) der verwendeten Bibliothek.

## Aufbau der Schaltung

Die Datenpins am ESP32 sind wie folgt belegt:

```cpp
#define PIN_DS_SOLAR 16   // Temp-Sensor Solar
#define PIN_DS_POOL 17    // Temp-Sensor Pool
#define PIN_RSSWITCH 18   // für 433MHz Sender
```

## Quellcode des Projektes

Für das Projekt verwenden wir die Entwicklungsumgebung [Platform.io IDE](https://platformio.org/platformio-ide). Damit legen wir ein Projekt für das Board `esp32dev` an.

Der komplette Quellcode des Projektes ist im GitHub-Repository des Autors zu finden: [https://github.com/stritti/smart-swimming-pool](https://github.com/stritti/smart-swimming-pool).

## Verwendete Bibliotheken

In diesem Projekt ist es uns wichtig, auf bewährte Softwarekomponenten zurückzugreifen und möglichst viel über vorhandene Bibliotheken zu lösen. Aus diesem Grund kommen folgende Libs zum Einsatz:

- **rc-switch**: Steuerung der Funksteckdosen
- **OneWire**: Unterstützung für I2C-Sensoren
- **DallasTemperature**: Auslesen der Temperatur der Sensoren
- **PubSubClient**: MQTT-Nachrichten empfangen und versenden
- **RemoteDebug**: Debugging über Telnet
- **ESPBASE**: Template für IoT-Projekte

Diese Bibliotheken sind in der Konfiguration von Platform.io (`platformio.ini`) hinterlegt und werden beim Kompilieren automatisch aus dem Internet geladen und eingebunden.

Das Programm für den Pool-Controller basiert auf ESPBASE, das wie im vorangegangenen Artikel geschrieben einige Setup-Funktionen bereitstellt. Am Anfang des Codes werden dazu einige Variablen angelegt und die Defines für die Pinbelegung definiert.

Neben den beiden Funktionen `setup()` und `loop()` sind einige weitere Funktionen implementiert. Im Wesentlichen geht es hierbei um das Empfangen und Senden von MQTT-Nachrichten und das entsprechende Umsetzen der Nachrichten. Zudem ist ein Timer implementiert, der zyklisch die Temperatursensoren ausliest und per MQTT-Nachrichten publiziert.

## Die Details

1. In der `loop`-Funktion wird die WLAN-Verbindung immer wieder geprüft und gegebenenfalls wieder hergestellt. Das war ein tückisches Problem: der ESP hat immer mal wieder die WLAN-Verbindung verloren und ohne den Reconnect konnte er keine Daten mehr versenden.
2. Die Funktion `publish` dient zum Versenden der MQTT-Nachrichten. So werden die Daten von einem Neustart und von den Temperaturmessungen als JSON-Nachrichten publiziert.
3. Der Timer für das Versenden der Temperaturen ist aufgeteilt. Grund ist, dass die eigentlichen Timer-Methoden möglichst kurz sein müssen. In der Implementierung ruft der Timer die Funktion `onTimer` auf, welche nur den volatilen `interruptCounter` inkrementiert. In der `loop`-Funktion wird dieser überprüft und die eigentliche `onTemperature`-Funktion ausgelöst. In dieser Methode wird auch die interne Temperatur des ESP ausgelesen und publiziert.
4. Die Funktion `onMQTTCallback` wird aufgerufen, wenn eine Nachricht an ein Topic, das mit `/pool/switch/` beginnt, gesendet wurde. Die Nachricht enthält die Information der Funksteckdose, ob diese ein- bzw. ausgeschaltet werden soll. Das Topic wird dabei weiter unterteilt in die Gruppe und die Gerätekodierung. Das heißt, die Kodierung der DIP-Schalter der Steckdose transformiert in 0 und 1. Dadurch ist diese Lösung flexibel auch an anderer Stelle nutzbar.

Der Quellcode des Pool-Controllers findet man direkt komplett in folgender Datei: [Pool-Controller/src/pool-control.ino](https://github.com/stritti/smart-swimming-pool/blob/master/Pool-Controller/src/pool-control.ino)

## Testing

Ist die Schaltung aufgebaut und das Projekt auf den ESP geladen, können wir bereits testen. Der ESP wird ein WLAN als Access Point öffnen, da standardmäßig kein WLAN eingerichtet ist. Wenn man sich mit dem Pool-Controller mit dem Smartphone verbindet, kann man das richtige WLAN einrichten. Danach startet der Microcontroller automatisch neu und versucht, sich mit dem angegebenen WLAN zu verbinden.

Ist alles richtig eingerichtet, so sollte bereits beim Start des ESP eine Statusnachricht via MQTT publiziert werden. Man kann mit folgendem Kommando auf dem Raspberry alle Nachrichten tracken:

```bash
mosquitto_sub -h localhost -v -t /#
```

Eventuell muss im Quellcode die IP-Adresse des MQTT-Servers angepasst werden. Danach sollten im Minutenzyklus die Temperaturen auf dem Raspberry ausgegeben werden.

In die andere Richtung können wir die Funksteckdosen schalten, indem wir eine passende Nachricht versenden. Dabei setzt sich das Topic aus `/pool/switch/<group>/<device>` zusammen. `Group` und `Device` sind die DIP-Schalter der Steckdose als 0 und 1. Als Nachricht wird `ON` bzw. `OFF` gesendet.

## Wie geht es weiter?

Damit sind die Grundlagen geschaffen: wir können die Temperaturen auslesen und wir können Steckdosen schalten.

Im folgenden Artikel verbinden wir den Pool-Controller mit der Smart Home Lösung openHAB und machen den Pool durch Regeln richtig smart.

- [Weiter zu Teil 3: Swimmingpool und OpenHAB (3/4)]({{< relref "swimmingpool-openhab-3-4" >}})
