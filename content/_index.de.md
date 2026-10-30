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
{{< hextra/hero-button text="Loslegen" link="docs/start-here" >}}
{{< hextra/hero-button text="Schnellstart - 60 Minuten" link="docs/quickstart" >}}
</div>

<div class="wave-divider wave-divider--bottom">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1440 120" preserveAspectRatio="none" width="1440" height="120" aria-hidden="true">
    <defs>
      <linearGradient id="wave-dark-en" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#0077B6" stop-opacity="0.35"/>
        <stop offset="25%" stop-color="#00B4D8" stop-opacity="0.30"/>
        <stop offset="50%" stop-color="#48CAE4" stop-opacity="0.35"/>
        <stop offset="75%" stop-color="#00B4D8" stop-opacity="0.30"/>
        <stop offset="100%" stop-color="#0077B6" stop-opacity="0.35"/>
      </linearGradient>
      <linearGradient id="wave-light-en" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#90E0EF" stop-opacity="0.25"/>
        <stop offset="30%" stop-color="#CAF0F8" stop-opacity="0.20"/>
        <stop offset="60%" stop-color="#90E0EF" stop-opacity="0.25"/>
        <stop offset="100%" stop-color="#CAF0F8" stop-opacity="0.20"/>
      </linearGradient>
    </defs>
    <path d="M0,80 C320,100 380,40 720,60 C1060,80 1120,30 1440,50 L1440,120 L0,120 Z" fill="url(#wave-dark-en)"/>
    <path d="M0,100 C240,85 480,110 720,95 C960,80 1200,105 1440,90 L1440,120 L0,120 Z" fill="url(#wave-light-en)"/>
    <path d="M0,108 C360,100 540,118 720,112 C900,106 1080,118 1440,108 L1440,120 L0,120 Z" fill="#CAF0F8" fill-opacity="0.15"/>
  </svg>
</div>

{{< safety-notice type="230v" >}}

<h2 class="home-title">✨ Warum Smart Swimming Pool?</h2>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Arbeitet eigenständig"
    subtitle="Die Steuerlogik läuft auf dem ESP32. Umwälzung und Heizung funktionieren auch ohne Internet, WLAN oder Smarthome-Server weiter."
    link="/docs/architecture/"
    icon="chip"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Umwälzung und Solarheizung"
    subtitle="Zeitgesteuerte Filterpumpe und Solarheizung mit Hysterese. Betriebsarten: Auto, Manuell, Boost und Timer."
    link="/docs/components/pool-controller/"
    icon="sun"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Smarthome-fähig"
    subtitle="Home Assistant erkennt den Controller automatisch per MQTT Discovery. openHAB und andere MQTT-Systeme binden sich mit manueller Konfiguration an."
    link="/docs/integrations/"
    icon="home"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Auf Zuverlässigkeit ausgelegt"
    subtitle="Einstellungen überstehen Neustarts, ein Hardware-Watchdog fängt Fehler ab, und die Relais bleiben beim Booten aus."
    link="/docs/components/pool-controller/safety-model/"
    icon="shield-check"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Einfach zu bedienen"
    subtitle="Integrierte Weboberfläche für Konfiguration und Steuerung sowie Firmware-Updates über die Luft (OTA)."
    link="/docs/components/pool-controller/ota-updates/"
    icon="globe"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Offen und modular"
    subtitle="MIT-Lizenz. Starte mit dem Controller (Elektronik ca. 35–55 €) und ergänze später Monitor, Grafana-Dashboard oder Wasserqualitätsmonitor."
    link="/docs/components/"
    icon="puzzle"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
{{< /hextra/feature-grid >}}

<h2 class="home-title">🧭 Wo anfangen?</h2>

<div class="home-start">
<ol>
  <li><a href="/docs/start-here/">Hier beginnen</a> — wähle den Weg, der zu deinem Aufbau passt</li>
  <li><a href="/docs/quickstart/">Schnellstart</a> — Aufbau auf dem Steckbrett in 60 Minuten, oder die ausführliche <a href="/docs/getting-started/">Bauanleitung</a></li>
  <li><a href="/docs/bom/">Stückliste</a> und <a href="/docs/checklist/">Inbetriebnahme-Checkliste</a> — bevor eine Pumpe an Netzspannung kommt</li>
  <li>Anbindung an <a href="/docs/integrations/home-assistant/">Home Assistant</a> oder <a href="/docs/integrations/openhab/">openHAB</a></li>
</ol>
<p>Alles Weitere steht in der <a href="/docs/">vollständigen Dokumentation</a>.</p>
<p><a href="https://www.home-assistant.io/"><img src="https://img.shields.io/badge/Works%20with-Home%20Assistant-41BDF5?logo=homeassistant&logoColor=white&style=for-the-badge" alt="Works with Home Assistant" /></a></p>
</div>

