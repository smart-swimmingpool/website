---
title: Bill of Materials
weight: 9
tags: ["docs", "bom", "hardware", "shopping-list"]
---

**🏊 Smart Swimming Pool: Complete shopping list with part numbers, prices, and sourcing tips.**

This BOM covers all components needed to build the pool controller including the electronics, electrical installation, sensors, and enclosure. Prices are estimates as of 2026.

---

## 1. Controller Electronics

These parts make up the core pool controller. All items are standard maker/hobbyist components.

| # | Component | Qty | Est. Price | Details | Example Source |
|---|-----------|:---:|:----------:|---------|----------------|
| 1 | **ESP32 DevKit V1** (CP2102) | 1 | 10–15 € | 4MB flash, CP2102 USB-serial | Amazon, AZ-Delivery |
| 2 | **2-Channel 5V Relay Module** | 1 | 5–8 € | Active-low, optocoupler isolated, HW-279/HW-316 | Amazon, eBay |
| 3 | **DS18B20 temperature sensor** (waterproof) | 2 | 4–6 €/ea | Stainless steel probe, 1m cable, 3-wire | Amazon, Reichelt |
| 4 | **4.7kΩ resistor** (¼W, ±5%) | 2 | 0.10 €/ea | Metal film or carbon film | Reichelt, Pollin |
| 5 | **Breadboard** (830 tie points) | 1 | 3–5 € | For prototyping | Amazon, Reichelt |
| 6 | **Jumper wires** (M-M, M-F) | 20+ | 3–5 € | Assorted colors/lengths | Amazon |
| 7 | **USB power supply** (5V, 1A+) | 1 | 5–10 € | Quality brand (Anker, Samsung, Apple) | Local electronics store |
| 8 | **USB-A to Micro-USB cable** | 1 | 3–5 € | **Data cable** (not charge-only) | Amazon |

| | **Subtotal (controller only)** | | **~35–55 €** | |
| | (Existing BOM = 45–75 € incl. enclosure) | | | |

---

## 2. Enclosure & Mechanics

Protect the electronics from moisture and physical damage.

| # | Component | Qty | Est. Price | Details | Example Source |
|---|-----------|:---:|:----------:|---------|----------------|
| 9 | **DIN rail enclosure** (ABS, IP54+) | 1 | 8–15 € | e.g. Fibox 4-module, 100×75×105mm | Reichelt, Conrad |
| 10 | **DIN rail** (35mm, 15cm) | 1 | 2–4 € | Slotted steel rail for mounting | Reichelt |
| 11 | **PG7 cable gland** (5–7mm cable) | 4–6 | 1–2 €/ea | For sensor cables and USB entry | Amazon, Reichelt |
| 12 | **PG11 cable gland** (8–10mm cable) | 1–2 | 1–2 €/ea | For mains cable entry (if 230V in enclosure) | Amazon, Reichelt |
| 13 | **DIN rail mount adapter** for ESP32 | 1 | 3–5 € | 3D-printed optional; zip ties also work | Thingiverse |
| 14 | **Zip ties** (100mm, assortment) | 10+ | 2–3 € | Cable management inside enclosure | Any hardware store |
| 15 | **Adhesive cable tie mounts** | 5+ | 3–4 € | Stick to enclosure interior | Amazon |

| | **Subtotal (enclosure)** | | **~25–45 €** | |
| | *Not required if breadboard is used indoors* | | | |

---

## 3. Electrical Installation (230V)

For connecting the relay module to the pumps safely.

| # | Component | Qty | Est. Price | Details | Notes |
|---|-----------|:---:|:----------:|---------|-------|
| 16 | **RCD / FI circuit breaker** (30mA) | 1 | 20–35 € | 2-pole, 25A, 30mA rated residual current | **Mandatory** for 230V |
| 17 | **MCB / circuit breaker** (B10A or B16A) | 1–2 | 5–10 €/ea | For pump circuit overcurrent protection | Per pump circuit |
| 18 | **Three-core mains cable** (NYM-J 3×1.5mm²) | 5–10m | 2–3 €/m | For 230V wiring between relay and pumps | Hardware store |
| 19 | **Flexible control cable** (LiYY 3×0.75mm²) | 2–3m | 1–2 €/m | For relay → pump connection inside enclosure | Reichelt |
| 20 | **Wire ferrules** (0.75mm² and 1.5mm²) | 20+ | 3–5 € | For stranded wire termination in screw terminals | Reichelt, Amazon |
| 21 | **Ferrule crimping tool** | 1 | 8–15 € | For crimping ferrules | Reichelt, Amazon |
| 22 | **DIN rail terminal blocks** (2.5mm², grey) | 4–6 | 1–2 €/ea | For wiring distribution inside enclosure | Reichelt, Wago |
| 23 | **DIN rail grounding terminal** (green-yellow) | 2 | 2–3 €/ea | For PE / ground connection | Reichelt |
| 24 | **End brackets** for terminal blocks | 2 | 1 €/ea | Fix terminal blocks on DIN rail | Reichelt |
| 25 | **Cable markers** (numbered rings) | 1 set | 3–5 € | For identifying wires during maintenance | Reichelt |
| 26 | **Strain relief** for mains cable | 2 | 2–4 €/ea | Prevent cable pull from reaching terminals | Hardware store |

| | **Subtotal (electrical)** | | **~60–110 €** | |
| | *Many items may already be in your distribution panel* | | | |

---

## 4. Temperature Sensor Installation

Additional materials for mounting DS18B20 sensors on pipes.

| # | Component | Qty | Est. Price | Details | Notes |
|---|-----------|:---:|:----------:|---------|-------|
| 27 | **DS18B20 stainless steel probe** (9mm × 30mm) | 2 | 4–6 €/ea | Better quality than generic — look for "Sanitary" variant | Reichelt, Amazon |
| 28 | **Sensor cable** (4-conductor, shielded, 2×0.25mm²) | 5–15m | 2–3 €/m | For extending sensor reach; **twisted-pair shielded** preferred | Reichelt |
| 29 | **Heat shrink tubing** (assorted, 3:1 ratio) | 1 set | 3–5 € | For sealing cable connections against moisture | Amazon |
| 30 | **Cable clips** (for pipe mounting) | 10+ | 2–3 € | Fix sensor cable along pipe runs | Hardware store |
| 31 | **Thermal conductive paste** (heat sink compound) | 1 tube | 3–5 € | Improves thermal contact between probe and pipe | Reichelt |
| 32 | **Cable junction box** (IP44+) | 1 | 3–5 € | For connecting sensor extension cables | Hardware store |

| | **Subtotal (sensor installation)** | | **~25–45 €** | |
| | *Depends strongly on cable lengths needed* | | | |

---

## 5. Tools & Consumables

Essential tools for assembly — not included in the controller cost.

| # | Tool | Est. Price | Required? | Notes |
|---|------|:----------:|:---------:|------|
| 33 | **Digital multimeter** | 15–30 € | ✅ **Yes** | Must measure DC voltage, continuity, resistance |
| 34 | **Wire stripper** (automatic) | 8–15 € | ✅ **Yes** | For stripping 0.75–2.5mm² wires |
| 35 | **Screwdriver set** (slotted + Phillips) | 5–10 € | ✅ Yes | For terminal blocks and DIN rail components |
| 36 | **Soldering iron** (30W+) | 15–25 € | ⬜ Optional | Only if you solder sensor extensions |
| 37 | **Heat gun** | 15–30 € | ⬜ Optional | For heat shrink tubing |
| 38 | **Cable tester** (continuity tester) | 5–10 € | ⬜ Optional | For verifying wired connections |

| | **Subtotal (tools)** | | **~60–100 €** | |
| | *May be partially available in your workshop* | | | |

---

## Order of Purchase

If you are ordering everything at once, here is the priority:

1. **Must-have (ESP32, relay, sensors, resistors, breadboard, PSU)** — ~35 €
   → Enough to flash firmware and test sensors
2. **Enclosure + glands + DIN rail** — ~25 €
   → For permanent installation
3. **Electrical (RCD, MCB, cable, terminals)** — ~60 €
   → Only if you need to extend your distribution panel
4. **Sensor installation (cable, heat shrink)** — ~25 €
   → Only if running sensors to distant pipe locations

You can start with just the **must-have items** (category 1) and expand later.

---

## Sourcing Tips

| Item | Tip |
|------|-----|
| **ESP32** | Buy from AZ-Delivery (Germany) — known quality, fast shipping. Avoid "ESP32 WROOM" from no-name sellers. |
| **DS18B20** | Search for "DS18B20 sanitary sensor" — these have better sealing. Cheap ones (<2€) often fail after 1–2 seasons. |
| **Relay module** | Ensure it says **optocoupler isolated** and **active-low**. HW-279 is the most reliable model. |
| **RCD / FI** | Buy from Hager, ABB, Schneider, or Siemens. Avoid no-name safety switches. |
| **Cable** | NYM-J is standard for fixed installation. LiYY is for flexible internal wiring. |
| **Resistors** | 4.7kΩ, ¼W, ±5% — literally 10 cents. Buy 10, keep spares. |

---

## Price Summary

| Category | Main Components | Price Range |
|----------|----------------|-------------|
| Controller Electronics | ESP32, relay, sensors, breadboard, PSU | **35–55 €** |
| Enclosure & Mechanics | Enclosure, glands, DIN rail, fittings | **25–45 €** |
| Electrical (230V) | RCD, MCB, cable, terminals, ferrules | **60–110 €** |
| Sensor Installation | Extra cable, heat shrink, junction box | **25–45 €** |
| Tools | Multimeter, stripper, screwdrivers | **60–100 €** |
| **Total (controller only)** | Categories 1–2 | **60–100 €** |
| **Total (full installation)** | Categories 1–4 | **145–255 €** |
| **Including tools** | Categories 1–5 | **205–355 €** |

> 💡 The existing "Getting Started" BOM estimates **45–75 €** for the **controller electronics + enclosure** (categories 1+2). The expanded BOM above adds the **electrical installation (230V)** and **sensor mounting** materials which are necessary for a real pool installation.
