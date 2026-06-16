---
title: "🏊 Smart Swimming Pool"
layout: hextra-home
--- 

<div class="mt-6 mb-6">
{{< hextra/hero-headline >}}
  Pool Automation in a Smart Way
{{< /hextra/hero-headline >}}
</div>

<div class="mb-12">
{{< hextra/hero-subtitle >}}
  An Open Source Project to manage your Swimming Pool using Home Automation.&nbsp;<br class="sm:block hidden" />Control circulation, heating, and monitoring - all from your smartphone.
{{< /hextra/hero-subtitle >}}
</div>

> **⚠️ WARNING: This project involves 230V AC mains voltage!**
> - **Only proceed if you have basic electronics knowledge.**
> - **Always use a Residual Current Device (RCD/FI circuit breaker) for the pump circuit.**
> - **Disconnect power before working on the circuit.**
> - **This project is NOT certified (no CE/UL mark). For personal use only!**

<div class="mb-6">
{{< hextra/hero-button text="🚀 Quick Start Guide" link="docs/quick-start" >}}
{{< hextra/hero-button text="❓ FAQ & Troubleshooting" link="docs/faq" >}}
</div>

## Vision

The modules of this project support you to transform your swimming pool into a smart swimming pool:

- ✅ Automation of the circulation time for cleaning water
- ✅ Simple and ecological temperature control with solar energy
- ✅ Manage water heating by additional pump for heating (solar) circuit
- ✅ Independent of specific smarthome servers
- ✅ Open Source (MIT License)
- ✅ Open for suggestions and improvements
- ✅ Supporting standards
- ✅ Works without permanent WiFi connection
- ✅ Can be operated via smartphone
- ✅ Modular to extend
- ✅ Well documented
- ✅ Easy to setup

[![Works with Home Assistant](https://img.shields.io/badge/Works%20with-Home%20Assistant-41BDF5?logo=homeassistant&logoColor=white&style=for-the-badge "Works with Home Assistant")](https://www.home-assistant.io/)

---

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="🚀 Quick Start"
    subtitle="New to the project? Start here with our step-by-step guide for beginners."
    link="/docs/quick-start/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    icon="rocket"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="❓ FAQ & Troubleshooting"
    subtitle="Find solutions to common issues and get your system running smoothly."
    link="/docs/faq/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    icon="question-mark-circle"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Pool Controller"
    subtitle="The smart brain of your pool. Central control logic running on ESP32 with Home Assistant MQTT discovery. Cost of components less than 100€."
    link="/docs/pool-controller/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/pool-controller_breadboard.png"
    imageClass="top-[40%] left-[24px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(75,180,227,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="openHAB Integration"
    subtitle="Smooth integration with openHAB smart home server. Control your pool via mobile app on Android and iOS."
    link="/docs/openhab-configuration/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/openhab-sitemap-pool-automation.jpg"
    imageClass="top-[40%] left-[36px] w-[180%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,150,200,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Pool Monitor"
    subtitle="Monitor your pool temperature with a solar-powered display. Wireless and energy-efficient."
    link="/docs/pool-monitor/"
    class="aspect-auto md:aspect-[1.1/1] max-md:min-h-[280px]"
    image="/img/pool-monitor-prototype.jpg"
    imageClass="top-[40%] left-[36px] w-[110%] sm:w-[110%] dark:opacity-80"
    style="background: radial-gradient(ellipse at 50% 80%,rgba(0,180,220,0.15),hsla(0,0%,100%,0));"
  >}}
  {{< hextra/feature-card
    title="Open Source"
    subtitle="MIT Licensed - free to use, modify, and share. Contributions welcome!"
    icon="sparkles"
  >}}
  {{< hextra/feature-card
    title="Works with Home Assistant"
    subtitle="Uses Home Assistant MQTT discovery for seamless smart home integration."
    icon="globe-alt"
  >}}
  {{< hextra/feature-card
    title="Grafana Dashboard"
    subtitle="Visualize your pool data with a beautiful Grafana dashboard. Track temperature trends and system status."
    link="/docs/grafana-dashboard/"
    icon="chart-bar"
  >}}
{{< /hextra/feature-grid >}}