# SeaVolt / PASES — Patent Update (Revised Claims + Spec Outline)

> **Status:** DRAFT for review by a registered patent attorney. Not filed text.
> **Purpose:** Addresses weaknesses in the Aug 2025 provisional (Provisional App.
> "Portable Aluminum-Seawater Energy and Desalination System"). Includes revised
> claim language and a strengthened specification outline for the upcoming
> non-provisional / PCT filing.
> **Reminder:** The 12-month deadline to file the non-provisional claiming the
> provisional's priority is ~late Aug – mid Sep 2026. Act now.

---

## What was fixed vs. the provisional

| Problem flagged | Fix in this draft |
|----------------|-------------------|
| Claim 1 was purely functional ("a heat recovery system… a turbine… an RO unit") and easy to design around | Claim 1 now recites the **integration** explicitly: single portable enclosure, reaction chamber → heat-recovery loop → heat engine → RO unit, with **simultaneous** H₂ + water output |
| Claim 7 called a thermoelectric converter "a type of turbine" (contradictory) | Turbine and thermoelectric are now **separate** claim elements (Claims 2 and 3) |
| No structural/parameter support; dependent claims trivial | Added parameter-limited claims (pellet size 2–4 mm; RO 50–70 bar; ≥1,000 L/day; 10 kW fuel-cell equivalent) and a real embodiment |
| No method or use claims | Added method claims (11–12) and a use claim (13) |
| Spec was only 8 thin paragraphs (enablement/§112 risk) | Expanded "Detailed Description" outline with parameters, control logic, and a working-example template for prototype data |

---

## A. Revised Claims (apparatus, method, use)

**1.** A portable system for co-producing potable water and hydrogen from aluminum
and seawater, the system comprising, within a single portable enclosure:
- a reaction chamber configured to receive seawater and an aluminum feedstock
  activated by an activation agent selected from the group consisting of a
  gallium–indium alloy, a tin–bismuth alloy, caffeine, imidazole, and
  combinations thereof, the reaction chamber configured to contain an exothermic
  aluminum-water reaction that produces hydrogen gas and heat;
- a hydrogen capture and storage unit fluidically coupled to the reaction chamber;
- a heat-recovery loop thermally coupled to the reaction chamber and configured to
  transfer reaction heat to a heat engine; and
- a reverse-osmosis (RO) desalination unit powered by the heat engine to produce
  potable water from seawater;
wherein the hydrogen and the potable water are produced **simultaneously** from the
same reaction within the enclosure.

**2.** The system of claim 1, wherein the heat engine comprises a turbine driven by
a working fluid selected from isobutane, ammonia, steam, or supercritical CO₂, the
turbine mechanically or electrically driving the RO unit.

**3.** The system of claim 1, wherein the heat engine comprises a thermoelectric
generator that converts the reaction heat directly to electricity to power the RO
unit.

**4.** The system of claim 1, wherein the aluminum feedstock comprises recycled
aluminum pellets sized 2–4 mm.

**5.** The system of claim 1, further comprising a fuel cell fluidically coupled to
the hydrogen storage unit and configured to generate electricity from the stored
hydrogen.

**6.** The system of claim 5, further comprising a power distribution node
configured to direct electricity from the fuel cell between internal loads and
external devices.

**7.** The system of claim 1, further comprising a portable cartridge containing
pre-activated aluminum pellets for field refueling.

**8.** The system of claim 1, wherein the RO unit operates at a pressure of 50–70
bar and produces at least 1,000 L of potable water per day from seawater while the
hydrogen capture unit stores hydrogen equivalent to at least a 10 kW fuel-cell
output.

**9.** The system of claim 1, further comprising a control and monitoring system
having sensors and valves configured to regulate flow, temperature, and pressure.

**10.** The system of claim 1, wherein byproduct aluminum hydroxide
[Al(OH)₃] is collected in a byproduct tank for recycling into alum or boehmite.

**11.** A method of co-producing potable water and hydrogen, comprising:
introducing seawater and an activated aluminum feedstock into a reaction chamber of
a portable system; initiating an exothermic aluminum-water reaction to generate
hydrogen gas and heat; capturing and storing the hydrogen; transferring the
reaction heat via a heat-recovery loop to a heat engine; and driving a
reverse-osmosis desalination unit with the heat engine to produce potable water,
wherein the hydrogen and the potable water are produced simultaneously within the
portable system.

**12.** The method of claim 11, further comprising generating electricity with a
fuel cell from the stored hydrogen and distributing the electricity via a power
distribution node.

**13.** Use of a portable aluminum-seawater system according to claim 1 for
providing potable water and energy in remote, military, disaster-response, or
maritime environments.

---

## B. Strengthened Specification Outline (add to non-provisional)

**Title:** Portable Aluminum-Seawater Energy and Desalination System

**Technical Field:** renewable energy + water purification; simultaneous H₂, heat,
and potable water from a single portable unit.

**Background (expand):** cite the unmet need; contrast prior art that does *either*
H₂ *or* desalination, but not both from waste heat of the same reaction. Note MIT
2024–25 work as inspiration but distinguish: prior art does not integrate RO driven
by the reaction's waste heat in one portable enclosure.

**Summary:** as Claim 1.

**Detailed Description (expand the provisional's 8 paragraphs to include):**

- **Embodiment 1 — reaction chamber:** seawater inlet, aluminum pellet hopper,
  activator application (Ga-In islands via cold spray / low-melt solder wipe; or
  Sn-Bi coating; or caffeine/imidazole seawater soak). Pellet size **2–4 mm**, NaOH
  surface roughening. Reaction: `2Al + 6H₂O → 2Al(OH)₃ + 3H₂ + heat`.
- **Heat-recovery loop:** working fluid (isobutane/ammonia/steam/sCO₂) in a heat
  exchanger on the chamber wall; drives turbine OR thermoelectric generator.
- **RO unit:** membrane rated **50–70 bar**; brine reject routed to byproduct /
  further H₂ feed; fresh output ≥ **1,000 L/day**.
- **Hydrogen path:** captured, compressed (350–700 bar) or liquefied; fed to PEM
  fuel cell (~50% efficiency) → electricity.
- **Control system:** sensors (temp, pressure, flow, H₂), valves, regulators;
  safety interlocks for high-pressure H₂ (prefer metal hydrides).
- **Byproduct:** Al(OH)₃ sludge → settling/filtration → recycle to alum/boehmite.

**Working Example (template — INSERT PROTOTYPE MEASURED DATA):**
- Input: ~5.4 kg Al/hr + seawater → 0.6 kg H₂/hr (≈ 6,675 L STP; ~26 L @ 350 bar).
- Heat: ~23.2 kWh thermal/hr → RO needs ~0.126 kWh/hr; surplus ~2.3–3.5 kWh/hr
  (10–15% ORC) available for external loads.
- Output observed: ___ L/day water, ___ kWh exported (from prototype testing).

**Advantages:** simultaneous dual output; off-grid; waste-aluminum feedstock;
circular byproduct; low carbon.

**Figures (already on file):** Fig. 1 system overview; Fig. 2 cartridge; Fig. 3
H₂ storage + fuel cell; Fig. 4 RO + water outputs; Fig. 5 byproduct tank; Fig. 6
control; Fig. 7 power node; Fig. 8 numeral key.

---

## C. Open action items before filing
1. **File non-provisional/PCT this week** claiming provisional priority (petition
   for late filing if >12 months).
2. **Prior-art search** (patent + non-patent, incl. MIT filings) for freedom-to-
   operate and claim shaping.
3. **Insert real prototype test data** into the Working Example above.
4. Confirm **exact USPTO filing date** of the provisional from the filing receipt.
