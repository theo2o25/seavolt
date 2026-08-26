# PASES — Portable Aluminum-Seawater Energy System

**Project codename:** SeaVolt
**Status:** Provisional patent filed (August 2025). Patent-pending. All rights reserved.
**Document type:** Research summary / technical brief

---

## Abstract

PASES is a portable, off-grid system that uses waste aluminum pellets (activated
with a gallium-indium alloy, or alternatives such as caffeine/imidazole) and
seawater to simultaneously produce **clean (desalinated) water, hydrogen fuel, and
usable heat/electricity**. The concept is built as a closed-loop
distillation/desalination setup, with the exothermic aluminum-water reaction
driving the entire process.

---

## 1. Summary

The system is designed to deliver dual outputs — fresh water and hydrogen — from
abundant, low-cost inputs (seawater and scrap aluminum), with no connection to a
power grid and no direct carbon emissions.

---

## 2. Core Process (Step-by-Step)

### 2.1 Aluminum Activation
Waste aluminum pellets are pre-treated to break through the protective oxide
layer. Options include:
- **Gallium-indium (Ga-In) alloy** for penetration and activation.
- **Gallium-free alternatives** such as a tin-bismuth (Sn-Bi) coating to create
  micro-galvanic sites, or **caffeine (imidazole)** solutions to accelerate
  reactions in seawater.
- **Prep methods:** chop pellets to 2–4 mm for higher surface area, clean/roughen
  with a mild NaOH dip, then apply sparse "islands" of activator (e.g., via wiping
  low-melt solder or cold spray) to avoid clumping or continuous coating.

### 2.2 Reaction
Activated aluminum reacts with seawater:

> 2Al + 6H₂O → 2Al(OH)₃ + 3H₂ + heat

**Outputs:** hydrogen gas (captured for storage / fuel cells), thermal energy, and
aluminum hydroxide sludge (a byproduct recyclable into alum for water treatment,
or neutralized/disposed of safely).

### 2.3 Heat Capture and Utilization
The exothermic reaction generates heat, captured via a working fluid (e.g.,
isobutane, ammonia, or steam) in a heat exchanger. This drives an expansion
turbine, creating mechanical pressure to power a **reverse osmosis (RO)** membrane
system.
- RO pushes seawater through the membrane, separating fresh water from brine.
- Brine can be repurposed (e.g., as feedstock for further hydrogen production or
  industrial uses).

### 2.4 Hydrogen Storage and Use
Captured H₂ is stored (compressed, liquid, or in tanks) and fed into a fuel cell
for electricity generation (e.g., powering more desalination cycles, cooling/
heating, or external loads).

### 2.5 Byproducts and Sustainability
- **Aluminum hydroxide:** recyclable (e.g., into boehmite for semiconductors or
  water-treatment coagulants).
- **No carbon emissions**; reduces reliance on fossil fuels for desalination or
  hydrogen production.
- Runs off-grid, using waste aluminum and abundant seawater.

---

## 3. System Specifications

| Parameter | Value |
|-----------|-------|
| Fresh-water output | ~1,000 L/day (portable unit) |
| Energy output | Portable H₂ for fuel cells |
| Capital cost | $10,000 – $15,000 |
| Operating cost | $0.30 – $0.50 per 10 L (pellet + alloy refills) |

**Revenue model:** sell units cheaply; profit from refills of pre-treated pellets
and Ga-In alloy (inspired by Nespresso pods / printer ink). Partner with scrap
dealers for aluminum supply.

**Market potential:** estimated $1.2 – 3.8 billion (13% CAGR), targeting off-grid
needs — disaster relief (Red Cross / UNICEF), military / remote offshore rigs,
maritime islands, survivalists, and ships.

**Unique selling points:** dual outputs (water + fuel), works with any waste
aluminum, no power grid required.

---

## 4. Power / Energy Calculations

### 4.1 Hydrogen for a 10 kW Fuel Cell
1. Fuel cell efficiency: 50% (typical PEM).
2. Required H₂ energy input: 10 kW / 0.5 = **20 kW** (thermal equivalent).
3. H₂ energy density: ~33.3 kWh/kg (lower heating value).
4. H₂ mass needed: 20 kW / 33.3 kWh/kg ≈ **0.6 kg/hour**.
5. Volume at STP (density 0.08988 kg/m³): 0.6 / 0.08988 ≈ **6,675 L**.
6. Compressed storage: ~26 L/hour at 350 bar; ~15 L/hour at 700 bar; ~8.6 L/hour
   as liquid H₂.

### 4.2 Aluminum Needed for H₂
1. From reaction: 2Al (54 g) → 3H₂ (6 g).
2. H₂ yield: 6 g / 54 g Al = 0.111 g H₂ / g Al.
3. For 0.6 kg H₂: 600 / 0.111 ≈ **5.4 kg Al/hour**.
4. Water consumed: ~10.8 L/hour (negligible vs. desalination output).

### 4.3 Heat for Desalination
- Reaction heat: ~139 kJ/g H₂.
- For 0.6 kg H₂: ~83,400 kJ ≈ **23.2 kWh thermal/hour**.
- RO energy need: ~3 kWh per m³ of fresh water (typical seawater RO).
- For 1,000 L/day (~0.042 m³/hour): ~0.126 kWh/hour.
- With 10–15% heat-to-power (e.g., ORC turbine): ~2.3 – 3.5 kWh available — more
  than sufficient for RO, leaving excess energy for other uses.

---

## 5. Prior Art and Foundations

The concept is based on established science, particularly **MIT's work by PhD
student Aly Kombarji and team** on activating aluminum with Ga-In or imidazole
(from coffee grounds) for rapid hydrogen production from seawater. Their 2024–2025
papers demonstrate 90–100% hydrogen yield in minutes, with full Ga-In recovery to
reduce costs. The reaction works in saltwater without prior desalination.

**Proven elements:**
- H₂ from Al-seawater demonstrated at MIT / KFUPM.
- RO driven by waste heat mirrors solar-thermal desalination.
- H₂ fuel cells are commercial (e.g., maritime use).

---

## 6. Novelty and Differentiation

- **Dual outputs:** unlike most Al-H₂ systems that target only fuel, PASES
  integrates RO for fresh water using waste heat and pressure — a novel integration
  for portable, off-grid desalination + energy. No exact prior art combines this.
- **Efficiency / sustainability:** off-grid viability for remote/disaster areas;
  circular byproduct recycling (Al(OH)₃ → alum).
- **Cost-effective:** waste aluminum is cheap and abundant; activators are
  recoverable.

---

## 7. Potential Challenges and Improvements

- **Activation cost / safety:** Ga-In is effective but expensive and rare
  (~$75 / 100 g). Focus on recovery (MIT achieves 99%) or cheaper alternatives
  (Sn-Bi, caffeine). Avoid Hg/lead for environmental reasons.
- **Byproduct handling:** Al(OH)₃ sludge in brine could clog systems; use
  filtration / settling tanks. Recycling to boehmite requires partners.
- **Efficiency losses:** heat-to-pressure (turbine) may be 5–15% efficient;
  optimize with supercritical CO₂. Reaction in seawater is ~2× slower than pure
  water — scale pellets accordingly.
- **Scalability / safety:** portable units are great, but high-pressure H₂ storage
  poses leak/explosion risk — consider metal hydrides. Test RO membranes for
  brine corrosion.
- **Environmental impact:** brine discharge could harm marine life if not diluted;
  integrate diffusion technology. Ensure no Ga-In leaching.

---

## 8. Suggested Next Steps

- Prototype with MIT-inspired caffeine activation for cheaper seawater
  compatibility.
- Add solar assist for startup heat or excess power.
- **Patent the integrated heat-RO-H₂ loop** (searches show no exact matches).
- Partner with firms such as Millipore Sigma (alloys) or scrap recyclers.

---

## 9. Patent Status

A provisional patent application was filed in **August 2025**. This document is a
research summary and does **not** constitute the filed application. All
specifications, claims, and drawings are maintained separately and are not
included here.

*This concept has strong real-world potential, particularly in water-scarce
regions, and could disrupt the desalination market (global ~$20B) and the green H₂
market (~$150B by 2030).*
