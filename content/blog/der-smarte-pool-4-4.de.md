---
title: "Der smarte Pool (4/4)"
date: 2018-10-24
authors:
  - name: "Stephan Strittmatter"
    link: https://github.com/stritti
    image: https://github.com/stritti.png
tags:
  - "Development"
  - "Deutsch"
  - "openHAB"
---

In den [vorangegangenen Artikeln]({{< relref "swimmingpool-openhab-3-4" >}}) haben wir den Pool-Controller mit openHAB verbunden. Über die Oberfläche der Sitemap in openHAB können in der Sektion Einstellungen die Parameter für die Temperaturen einfach eingestellt werden. Die Regeln reagieren auf diese Änderungen.

Nun geht es darum, die Steuerung auch wirklich smart zu machen: die Regelung verläuft automatisch und kann über WLAN bzw. Internet angepasst werden.

## Regelsteuerung des Pools

Für die Erwärmung des Pools haben wir drei Modi implementiert:

### Modus: Auto

Der vollautomatische Modus schaltet die Filterpumpe zeitgesteuert und erwärmt automatisch das Poolwasser bis zu einer Maximaltemperatur. Dies jedoch nur so lange, wie die Mindesttemperatur im Wärmespeicher nicht unterschritten wird.

### Modus: Boost

Vergleichbar mit dem Modus "Auto", jedoch ohne Berücksichtigung der Mindesttemperatur im Wärmespeicher.

### Modus: Manuell

Die Pumpen werden über die App manuell ein- und ausgeschaltet. Unabhängig von Regeln und Schwellwerten.

## Die Grenzwerte

Für die Steuerung der Temperatur des Pools werden folgende drei Parameter benötigt:

- **Maximale Pooltemperatur**: Wie warm soll der Pool werden?
- **Minimale Wärmespeichertemperatur**: Welche Temperatur muss das Wasser im Pufferspeicher mindestens haben, damit der Pool mitgeheizt werden kann?
- **Hysterese**: Wie groß soll die Temperaturabweichung sein, bevor die min/max-Regeln sich auswirken?

## Das smarte Herz: pool.rules

Die Regeln in der `pool.rules` sind die Regeln von openHAB hinterlegt. Diese Regeln verwenden die Konfigurationswerte, die man über die Einstellungen festlegen kann.

Hier werden die Werte der Temperatursensoren verglichen und anhand der Hysterese dann die Funksteckdosen gesteuert. Die Hysterese ist notwendig, damit bei sehr geringen Temperaturdifferenzen die Pumpen nicht ständig ein- und ausgeschaltet werden. Ein Wert von 0,5 K hat sich als völlig ausreichend erwiesen.

Die Regeln sind aufgeteilt und bedienen so die einzelnen Betriebsmodi.

## Add-On: Anzeigemodul

Um die Temperaturen auch ohne App zu verfolgen, haben wir eine kleine Monitoring-Anwendung in eine alte Schraubenbox gesteckt. Dieses Modul entstand auf Basis des LCD-Displays 16×2.

Dieser Pool-Monitor basiert auf einem ESP8266 und einem LCD Display 16×2. Der ESP empfängt die Temperaturwerte — ebenfalls über MQTT — und aktualisiert das Display.

Der Quellcode dazu befindet sich ebenfalls im Code-Repository und ist vom Pool-Controller abgeleitet.

Das Gehäuse ist eine alte Schrauben-Box, die mit etwas Füllmaterial ausgepolstert wurde. Etwas tricky war die Bohrung für den Micro-USB Stecker. Vielleicht wird nächstes Jahr diese Box upgegraded und mit einer Solarzelle ausgestattet. Dann kann diese auch draußen in der Nähe des Pools installiert werden.

## Open Source

Ziel war es von Anfang an, ein Projekt basierend auf Open Source zu erstellen. So ist natürlich auch wieder ein Open Source Projekt entstanden.

Das gesamte Projekt ist auf GitHub verfügbar:

[https://github.com/stritti/smart-swimming-pool](https://github.com/stritti/smart-swimming-pool)

## Fazit

Der Pool-Controller ist seit Mai im Einsatz und hat nach ein paar Verbesserungen den Sommer über zuverlässig funktioniert.

Hauptproblem war eigentlich die fehlende Prüfung, ob die WLAN-Verbindung noch besteht. Wir dachten immer, wir hätten irgendwo ein Leak im Code, dabei hat der ESP-Controller gelegentlich nur die Verbindung über das WLAN verloren. Jetzt läuft der Controller zuverlässig, liefert Daten und steuert die Pumpen.

Seit diesem Jahr gibt es also einen schönen warmen Pool und trotzdem immer genügend warmes Wasser im Haushalt. Ein Projekt mit klarem Mehrwert an Komfort mit relativ geringem finanziellem Einsatz. Dadurch hat das Projekt auch einen sehr hohen [Woman Acceptance Factor](https://de.m.wikipedia.org/wiki/Woman_acceptance_factor) erzielt.

## Ausblick

Es gibt noch einige Möglichkeiten, das Projekt über den kommenden Winter zu verbessern und zu erweitern. Wir denken da an:

- Temperatursensor direkt am Solarkreislauf, um zu prüfen, ob die Heizung im Solar- oder Heizmodus ist
- Outdoor-Sensor für Umgebungstemperatur und Wassertemperatur mit Versorgung über Solarzellen
- Die Regelsteuerung direkt im ESP-Code auf dem Pool Controller (nur noch Update der Konfiguration und Monitoring über MQTT)
- Mehr Sicherheit durch Verschlüsselung der MQTT-Kommunikation
- Messung der Wasserqualität (pH, Chlor) durch zusätzliche Sensoren
- Einbeziehen der Wettervorhersage, um den Pufferspeicher noch optimaler einzuteilen

Wir freuen uns über Nachbauten, inspirierte Projekte und Vorschläge für weitere Verbesserungen. Gerne auch als Pull-Requests auf GitHub.
