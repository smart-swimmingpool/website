---
title: "Projekt Smart Swimmingpool — Einleitung"
date: 2018-10-17
authors:
  - name: "Stephan Strittmatter"
    link: https://github.com/stritti
    image: https://github.com/stritti.png
tags:
  - "Development"
  - "Deutsch"
---

In den folgenden vier Blogposts werde ich Schritt für Schritt beschreiben, wie man einen Swimmingpool mittels selbstgebauten IoT-Modulen steuern kann. Die Kosten der benötigten elektronischen Bauteile liegen dabei unter 100 Euro.

- **Eingangsartikel**: Smart Swimming Pool mit der Problemstellung und den Anforderungen, notwendige Hardware sowie das Ziel der Serie
- **Pool-Controller**: Der Controller, der Temperaturen misst und periodisch via MQTT versendet sowie über MQTT Steckdosen (433MHz) schalten kann, MQTT-Server auf Raspberry einrichten
- **OpenHAB**: Anbindung des Controllers, Darstellung der Messdaten, Steuern der Steckdosen
- **Der Smart Pool**: Die smarte Steuerung durch OpenHAB-Regeln, Fazit & Ausblick

## Autor

**Stephan Strittmatter** ist als Talent Scout in einem IT Beratungshaus tätig und bringt jungen Nachwuchskräften die Softwareentwicklung näher. Vor wenigen Monaten hatte er so auch über den Raspberry Pi und dem micro:bit schlussendlich Berührungspunkte mit den ESP-Controllern. Diese haben ihm den Kindheitstraum ermöglicht, endlich Hardware und Software einfach zu verbinden. Der private Pool war deshalb ein willkommenes Projekt, um IoT, Smart Home und Forschertrieb zu vereinen.

- Twitter/X: @\_stritti\_
- GitHub: [https://github.com/stritti](https://github.com/stritti)

### Weiter zur Artikelserie

- [Smarte Steuerung für den Swimmingpool (1/4)]({{< relref "smarte-steuerung-1-4" >}})
- [Der Pool-Controller (2/4)]({{< relref "pool-controller-2-4" >}})
- [Swimmingpool und OpenHAB (3/4)]({{< relref "swimmingpool-openhab-3-4" >}})
- [Der smarte Pool (4/4)]({{< relref "der-smarte-pool-4-4" >}})
