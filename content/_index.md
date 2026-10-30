---
title: 🏊 Smart Swimming Pool
layout: hextra-home
---

<div class="mt-6 mb-6 hero-headline-wrapper">
{{< hextra/hero-headline >}}
  Pool Automation in a Smart Way
{{< /hextra/hero-headline >}}
</div>

<div class="mb-12 hero-subtitle-wrapper">
{{< hextra/hero-subtitle >}}
  An Open Source Project to manage your Swimming Pool using Home Automation.&nbsp;<br class="sm:block hidden" />Control circulation, heating, and monitoring - all from your smartphone.
{{< /hextra/hero-subtitle >}}
</div>

<div class="mb-6 hero-button-wrapper">
{{< hextra/hero-button text="Get Started" link="docs/start-here" >}}
{{< hextra/hero-button text="Quick Start - 60 Minutes" link="docs/quickstart" >}}
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

<h2 class="home-title">✨ Why Smart Swimming Pool?</h2>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Runs on its own"
    subtitle="The control logic lives on the ESP32. Circulation and heating keep working without internet, WiFi or a smart home server."
    link="/docs/architecture/"
    icon="chip"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Circulation and solar heating"
    subtitle="Timed filter-pump circulation and solar heating with hysteresis. Operation modes: Auto, Manual, Boost and Timer."
    link="/docs/components/pool-controller/"
    icon="sun"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Smart home ready"
    subtitle="Home Assistant discovers the controller automatically via MQTT Discovery. openHAB and other MQTT systems connect with manual configuration."
    link="/docs/integrations/"
    icon="home"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Built to be reliable"
    subtitle="Settings survive reboots, a hardware watchdog recovers from faults, and the relays stay off while the controller boots."
    link="/docs/components/pool-controller/safety-model/"
    icon="shield-check"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Easy to operate"
    subtitle="Built-in web interface for configuration and control, plus over-the-air firmware updates."
    link="/docs/components/pool-controller/ota-updates/"
    icon="globe"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Open and modular"
    subtitle="MIT licensed. Start with the controller (electronics ca. 35–55 €) and add monitor, Grafana dashboard or water quality monitor later."
    link="/docs/components/"
    icon="puzzle"
    class="aspect-auto min-h-[180px]"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
{{< /hextra/feature-grid >}}

<h2 class="home-title">🧭 Where to start</h2>

<div class="home-start">
<ol>
  <li><a href="/docs/start-here/">Start Here</a> — pick the path that fits your setup</li>
  <li><a href="/docs/quickstart/">Quick Start</a> — breadboard setup in 60 minutes, or the detailed <a href="/docs/getting-started/">Build Guide</a></li>
  <li><a href="/docs/bom/">Bill of Materials</a> and <a href="/docs/checklist/">Commissioning Checklist</a> — before any pump touches mains voltage</li>
  <li><a href="/docs/integrations/home-assistant/">Home Assistant</a> or <a href="/docs/integrations/openhab/">openHAB</a> integration</li>
</ol>
<p>Everything else is in the <a href="/docs/">full documentation</a>.</p>
<p><a href="https://www.home-assistant.io/"><img src="https://img.shields.io/badge/Works%20with-Home%20Assistant-41BDF5?logo=homeassistant&logoColor=white&style=for-the-badge" alt="Works with Home Assistant" /></a></p>
</div>

