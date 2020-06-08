---
title: Getting Started
linktitle: Getting Started
description: Getting Stated on Smart Swimming Pool
type: docs  # Do not modify.
date: "2020-05-28"
publishdate: "2020-05-28"
lastmod: "2020-05-28"
featured: true
menu:
  docs:
    parent: Documents
    name: Getting Started
    weight: 10
tags: ["docs", "getting-started", "tutorial"]
toc: true
---

**🏊 Smart Swimming Pool: Pool automation for Smarter Control of your Swimming Pool**

## Overview

This project is splitted in several modules:

- [Pool Controller]({{< ref "../pool-controller/_index.md" >}}): the heart of the 🏊 Smart Swimming Pool
- [OpenHab Configuration]({{< ref "../openhab-configuration/_index.md" >}}): example of a sitemap to control 🏊 Smart Swimming Pool via App.

Additional content could be found incommuity driven [Wiki](https://github.com/smart-swimmingpool/smart-swimmingpool/wiki).

## Example Environment

In my setting I have a thermal solar system for heating water and for support of heating environment within the house. the heated water is collected within a buffer which has a third circulation for my pool.
Attached to this third circulation a pump is attached to heat via heat exchanger the water of the pool:

{{< figure library="true" src="schema-environment-smart-pool.png" title="Example Environment" lightbox="true" >}}
