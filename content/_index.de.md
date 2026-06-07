---
title: 🏊 Smart Swimming Pool
layout: hextra-home
---

<div class="mt-6 mb-6">
{{< hextra/hero-headline >}}
  Pool Automatisierung auf smarte Weise
{{< /hextra/hero-headline >}}
</div>

<div class="mb-12">
{{< hextra/hero-subtitle >}}
  Ein Open-Source-Projekt zur smarten Verwaltung deines Swimming Pools&nbsp;<br class="sm:block hidden" />über die Heimautomatisierung. Steuere Zirkulation, Heizung und Überwachung - alles vom Smartphone.
{{< /hextra/hero-subtitle >}}
</div>

<div class="mb-6">
{{< hextra/hero-button text="Erste Schritte" link="docs/getting-started" >}}
</div>

<span style="text-shadow: none;"><a class="github-button" href="https://github.com/smart-swimmingpool/pool-controller" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star this on GitHub">Star</a><script async defer src="https://buttons.github.io/buttons.js"></script></span>

## Vision

Die Module dieses Projekts unterstützen Sie dabei, Ihren Swimmingpool in ein Smart Swimmingpool zu verwandeln:

- ✅ Automatisierung der Zirkulationszeit des Wassers zur Reinigung
- ✅ Einfache und ökologische Temperatursteuerung mit Sonnenenergie
- ✅ Steuerung der Wassererwärmung durch zusätzliche Pumpe für den Heizungs- bzw. Solar-Kreislauf
- ✅ Unabhängigkeit von einzelnen Smarthome-Servern
- ✅ Open Source (MIT-Lizenz)
- ✅ Offen für Vorschläge und Verbesserungen
- ✅ Unterstützung von Standards
- ✅ Funktioniert ohne ständige WLAN-Verbindung
- ✅ Kann über Smartphone bedient werden
- ✅ Modulare Erweiterbarkeit
- ⬜ Kann über Hardware bedient werden
- ⬜ Gut dokumentiert
- ⬜ Einfach einzurichten

[![works with MQTT Homie](https://homieiot.github.io/img/works-with-homie.svg "works with MQTT Homie")](https://homieiot.github.io/)

---

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Pool Controller"
    subtitle="Das smarte Gehirn Ihres Pools. Zentrale Steuerlogik auf ESP8266 mit MQTT Homie Protokoll. Kosten unter 100€."
    link="https://github.com/smart-swimmingpool/pool-controller"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/pool-controller_breadboard.png"
    imageClass="top-[40%] left-[24px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="openHAB Integration"
    subtitle="Reibungslose Integration mit dem openHAB-Smarthome-Server. Steuerung des Pools per App auf Android und iOS."
    link="https://github.com/smart-swimmingpool/openhab-config"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/openhab-sitemap-pool-automation.jpg"
    imageClass="top-[40%] left-[36px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Pool Monitor"
    subtitle="Überwachen Sie Ihre Pooltemperatur mit einem solarbetriebenen Display. Kabellos und energieeffizient."
    link="https://github.com/smart-swimmingpool/monitor"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/pool-monitor-prototype.jpg"
    imageClass="top-[40%] left-[36px] w-[110%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Open Source"
    subtitle="MIT-Lizenziert - kostenlos nutzbar, modifizierbar und teilbar. Beiträge willkommen!"
    icon="sparkles"
  >}}
  {{< hextra/feature-card
    title="Standardkonform"
    subtitle="Verwendet MQTT Homie Konvention für IoT-Kommunikation. Einfache Integration in jedes Smarthome-System."
    icon="globe-alt"
  >}}
  {{< hextra/feature-card
    title="Grafana Dashboard"
    subtitle="Visualisieren Sie Ihre Pool-Daten mit einem schönen Grafana-Dashboard. Verfolgen Sie Temperaturtrends und Systemstatus."
    link="https://github.com/smart-swimmingpool/grafana-dashboard"
    icon="chart-bar"
  >}}
{{< /hextra/feature-grid >}}
