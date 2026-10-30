---
title: Publications
weight: 62
tags: ["docs", "publication"]
---

Also available as [blog posts](/blog/) on this site.

- [Project Smart Swimming Pool](https://medium.com/diy-my-smart-home/project-smart-swimmingpool-4c40eb6741f6), _December 2018_

  Blogpost of version 1 of Smart Swimming Pool

  📄 [Read on this site]({{< relref "/blog/smart-swimming-pool-project" >}})

- [Smart Swimming Pool: Introduction]({{< relref path="/blog/projekt-smart-swimmingpool-einleitung" lang="de" >}}), _October 2018_

  Four-part German blog series on AZ-Delivery Blog about version 1 of the Smart Pool Controller.

  - [Smarte Steuerung für den Swimmingpool (1/4)]({{< relref path="/blog/smarte-steuerung-1-4" lang="de" >}})
  - [Der Pool-Controller (2/4)]({{< relref path="/blog/pool-controller-2-4" lang="de" >}})
  - [Swimmingpool und OpenHAB (3/4)]({{< relref path="/blog/swimmingpool-openhab-3-4" lang="de" >}})
  - [Der smarte Pool (4/4)]({{< relref path="/blog/der-smarte-pool-4-4" lang="de" >}})

## Project History

🏊 Smart Swimming Pool originated from an [earlier project](https://github.com/stritti/smart-swimming-pool) that was not yet modular and had all control logic implemented as openHAB rules.

The first version ran in **Summer 2018** and revealed several weaknesses:

- Controlling pumps via 433 MHz socket switches was unreliable — no feedback meant the actual state was unknown
- Switching logic lived in openHAB rules, causing problems when WiFi was unreliable
- MQTT messages used a proprietary format

Based on these lessons, the revised 🏊 Smart Swimming Pool was built: modular, resilient, and standards-based.
