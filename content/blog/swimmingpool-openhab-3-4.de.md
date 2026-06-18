---
title: "Swimmingpool und OpenHAB (3/4)"
date: 2018-10-23
authors:
  - name: "Stephan Strittmatter"
    link: https://github.com/stritti
    image: https://github.com/stritti.png
tags:
  - "Development"
  - "Deutsch"
  - "openHAB"
---

Nachdem wir im [vorangegangenen Blogartikel]({{< relref "pool-controller-2-4" >}}) den Controller für die Poolsteuerung erstellt haben, werden wir diesen nun über das WLAN mit OpenHAB verbinden und dort die Regeln für die smarte Steuerung implementieren.

## Installation von OpenHAB

OpenHAB ist ein "Home Automation Broker", also eine Smart Home Server Software. Diese kann auf einem Raspberry Pi installiert werden. Wir gehen hier davon aus, dass schon eine Grundinstallation von OpenHAB besteht.

Wir müssen nun unter Umständen noch einige Addons der Installation hinzufügen. Dies ist über die Oberfläche "[Paper UI](https://www.openhab.org/docs/configuration/paperui.html)" im Unterpunkt "Add-ons" möglich.

Für die Integration der Poolsteuerung benötigen wir folgende Add-ons:

- MQTT Binding
- openHAB Cloud Connector (optional für Internetzugriff über die Smartphone Apps)
- RRD4j Persistence
- JSONPath Transformation
- Basic UI

## Konfiguration

Die Konfigurationsdateien, die wir nun erstellen, liegen auf dem Raspberry normalerweise in dem Pfad `/etc/openhab2`. Die entsprechende Struktur mit den Dateien sind im GitHub-Repository hinterlegt.

### MQTT-Broker anbinden

Die Konfiguration für die Anbindung des Mosquitto Dienstes befindet sich in der Datei `services/mqtt.cfg`. Dort wird der Hostname und der Port konfiguriert. In unserem Fall laufen openHAB und Mosquitto auf demselben Raspberry.

### Sitemap mit den Items

Zunächst müssen wir nun in OpenHAB die Objekte (Items) definieren, damit wir diese auf der Sitemap steuern und auswerten können.

### pool.items

In der Datei [`pool.items`](https://github.com/stritti/smart-swimming-pool/blob/master/OpenHAB/items/2-pool.items) werden die Mess- und Steuerpunkte festgelegt. Dort werden zum Beispiel die Verknüpfungen der MQTT-Topics mit den Items vorgenommen. So gibt es die Items für die Temperaturen, welche die Daten von MQTT entgegennehmen und die Items, die Nachrichten versenden, um die Pumpen zu schalten. Das Größer- bzw. Kleiner-Zeichen in der Konfiguration gibt jeweils die Richtung der Nachrichten an:

```java
Number  Sensor_Solar_Temperature "Solar"
(gPool, gTemperature, Chart_Pool_Temperature)
["CurrentTemperature", "object:solar"] {
  mqtt="<[mqtt:/sensor/solar/temperature:state:JSONPATH($.value)]"
}
```

Für Chart-Grafiken und die Integration in Alexa sind noch einige weitere Konfigurationselemente integriert. So kann zum Beispiel über die Einstellungen der Zeitraum der Charts festgelegt werden.

Die Charts werden genutzt, um die Temperaturverläufe und die Schaltzeiten zu visualisieren. Damit die Charts richtig funktionieren, benötigen diese Daten im Abstand von maximal einer Minute. Da passt also unser Timer im Pool-Controller bestens.

Die Messdaten werden in einer RRD4j-Datenbank gespeichert. Dazu existiert ebenfalls eine Konfiguration im Repository. Da wir die Daten nicht für Langzeitauswertungen benötigen, reicht diese interne Datenbank von openHAB völlig aus.

## Wie geht es weiter?

Nun haben wir die Sitemap mit den Temperaturwerten und den Schaltmöglichkeiten für die beiden Pumpen.

Im abschließenden vierten Artikel werden wir auf die Regeln für die automatisierte Steuerung des Pools eingehen.

- [Weiter zu Teil 4: Der smarte Pool (4/4)]({{< relref "der-smarte-pool-4-4" >}})
