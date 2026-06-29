---
title: 🏊 Smart Swimming Pool
layout: hextra-home
---

<div class="mt-6 mb-6 hero-headline-wrapper">
{{< hextra/hero-headline >}}
  Pool Automatisierung auf smarte Weise
{{< /hextra/hero-headline >}}
</div>

<div class="mb-12 hero-subtitle-wrapper">
{{< hextra/hero-subtitle >}}
  Ein Open-Source-Projekt zur smarten Verwaltung deines Swimming Pools&nbsp;<br class="sm:block hidden" />über die Heimautomatisierung. Steuere Zirkulation, Heizung und Überwachung - alles vom Smartphone.
{{< /hextra/hero-subtitle >}}
</div>

<div class="mb-6 hero-button-wrapper">
{{< hextra/hero-button text="Erste Schritte" link="docs/getting-started" >}}
</div>

<div class="wave-divider wave-divider--bottom">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" preserveAspectRatio="none" width="1440" height="120" aria-hidden="true">
    <defs>
      <linearGradient id="wave-dark-de" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0077B6" stop-opacity="0.35"/>
        <stop offset="25%" stop-color="#00B4D8" stop-opacity="0.30"/>
        <stop offset="50%" stop-color="#48CAE4" stop-opacity="0.35"/>
        <stop offset="75%" stop-color="#00B4D8" stop-opacity="0.30"/>
        <stop offset="100%" stop-color="#0077B6" stop-opacity="0.35"/>
      </linearGradient>
      <linearGradient id="wave-light-de" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#90E0EF" stop-opacity="0.25"/>
        <stop offset="30%" stop-color="#CAF0F8" stop-opacity="0.20"/>
        <stop offset="60%" stop-color="#90E0EF" stop-opacity="0.25"/>
        <stop offset="100%" stop-color="#CAF0F8" stop-opacity="0.20"/>
      </linearGradient>
    </defs>
    <path d="M0,80 C320,100 380,40 720,60 C1060,80 1120,30 1440,50 L1440,120 L0,120 Z" fill="url(#wave-dark-de)"/>
    <path d="M0,100 C240,85 480,110 720,95 C960,80 1200,105 1440,90 L1440,120 L0,120 Z" fill="url(#wave-light-de)"/>
    <path d="M0,108 C360,100 540,118 720,112 C900,106 1080,118 1440,108 L1440,120 L0,120 Z" fill="#CAF0F8" fill-opacity="0.15"/>
  </svg>
</div>

{{< safety-notice type="230v" >}}

<div class="water-texture-bg">
<div class="hextra-max-page-width" style="margin-left:auto; margin-right:auto; padding: 0 1.5rem;">

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
- ✅ Gut dokumentiert
- ✅ Einfach einzurichten

[![Works with Home Assistant](https://img.shields.io/badge/Works%20with-Home%20Assistant-41BDF5?logo=homeassistant&logoColor=white&style=for-the-badge "Works with Home Assistant")](https://www.home-assistant.io/)

</div>
</div>

<div class="wave-divider wave-divider--top">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" preserveAspectRatio="none" width="1440" height="120" aria-hidden="true">
    <defs>
      <linearGradient id="wave-dark-top-de" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0077B6" stop-opacity="0.35"/>
        <stop offset="25%" stop-color="#00B4D8" stop-opacity="0.30"/>
        <stop offset="50%" stop-color="#48CAE4" stop-opacity="0.35"/>
        <stop offset="75%" stop-color="#00B4D8" stop-opacity="0.30"/>
        <stop offset="100%" stop-color="#0077B6" stop-opacity="0.35"/>
      </linearGradient>
      <linearGradient id="wave-light-top-de" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#90E0EF" stop-opacity="0.25"/>
        <stop offset="30%" stop-color="#CAF0F8" stop-opacity="0.20"/>
        <stop offset="60%" stop-color="#90E0EF" stop-opacity="0.25"/>
        <stop offset="100%" stop-color="#CAF0F8" stop-opacity="0.20"/>
      </linearGradient>
    </defs>
    <path d="M0,40 C320,20 380,80 720,60 C1060,40 1120,90 1440,70 L1440,0 L0,0 Z" fill="url(#wave-dark-top-de)"/>
    <path d="M0,20 C240,35 480,10 720,25 C960,40 1200,15 1440,30 L1440,0 L0,0 Z" fill="url(#wave-light-top-de)"/>
    <path d="M0,12 C360,20 540,2 720,8 C900,14 1080,2 1440,12 L1440,0 L0,0 Z" fill="#CAF0F8" fill-opacity="0.15"/>
  </svg>
</div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Pool Controller"
    subtitle="Das smarte Gehirn Ihres Pools. Zentrale Steuerlogik auf ESP8266 mit Home Assistant MQTT Discovery. Kosten unter 100€."
    link="/docs/pool-controller/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/pool-controller_breadboard.png"
    imageClass="top-[40%] left-[24px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="openHAB Integration"
    subtitle="Reibungslose Integration mit dem openHAB-Smarthome-Server. Steuerung des Pools per App auf Android und iOS."
    link="/docs/openhab-integration/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/openhab-sitemap-pool-automation.jpg"
    imageClass="top-[40%] left-[36px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Pool Monitor"
    subtitle="Überwachen Sie Ihre Pooltemperatur mit einem solarbetriebenen Display. Kabellos und energieeffizient."
    link="/docs/pool-monitor/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/pool-monitor-prototype.jpg"
    imageClass="top-[40%] left-[36px] w-[110%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Open Source"
    subtitle="MIT-Lizenziert - kostenlos nutzbar, modifizierbar und teilbar. Beiträge willkommen!"
    icon="sparkles"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.08),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Home Assistant Kompatibel"
    subtitle="Verwendet Home Assistant MQTT Discovery für nahtlose Smarthome-Integration."
    icon="globe-alt"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.08),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Grafana Dashboard"
    subtitle="Visualisieren Sie Ihre Pool-Daten mit einem schönen Grafana-Dashboard. Verfolgen Sie Temperaturtrends und Systemstatus."
    link="/docs/grafana-dashboard/"
    icon="chart-bar"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.08),hsla(0,0%,100%,0));"
  >}}
{{< /hextra/feature-grid >}}

<div class="wave-divider wave-divider--bottom">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" preserveAspectRatio="none" width="1440" height="120" aria-hidden="true">
    <defs>
      <linearGradient id="wave-footer-de" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0077B6" stop-opacity="0.30"/>
        <stop offset="25%" stop-color="#00B4D8" stop-opacity="0.25"/>
        <stop offset="50%" stop-color="#48CAE4" stop-opacity="0.30"/>
        <stop offset="75%" stop-color="#00B4D8" stop-opacity="0.25"/>
        <stop offset="100%" stop-color="#0077B6" stop-opacity="0.30"/>
      </linearGradient>
    </defs>
    <path d="M0,80 C320,100 380,40 720,60 C1060,80 1120,30 1440,50 L1440,120 L0,120 Z" fill="url(#wave-footer-de)"/>
    <path d="M0,100 C240,85 480,110 720,95 C960,80 1200,105 1440,90 L1440,120 L0,120 Z" fill="#90E0EF" fill-opacity="0.2"/>
  </svg>
</div>

<div class="cta-section">
  <h2>Bereit einzutauchen?</h2>
  <p class="hx:text-lg hx:text-gray-600 hx:dark:text-gray-400">Starte noch heute deine smarte Pool-Automatisierung.</p>
  <div class="mt-4">
    {{< hextra/hero-button text="Erste Schritte" link="docs/getting-started" >}}
  </div>
</div>
