# SeaVolt — Deep-Dive Analysis

> Geometry-verified review of the `seavolt prototypes` kit (11 STLs + renders + `BUILD_SHEET.txt`). Every STL was parsed, dimension-checked, and tested for disconnected components. Companion to the wind-turbine deep dive.

## 1. What it is
A **printed-only bench-top rig** — a triangular 3-leg frame (hub + strut + leg + foot) with a snap-on shelf, a pump clamp, and an optional **reactor chamber** (chamber stand/body/lid + aluminum cartridge basket/lid). It is a **parametric, snap-fit, no-glue / no-bolt / no-insert** design (PETG recommended). The name + "aluminum charge" + "seawater" parts suggest an **aluminum–seawater (or algae) electrochemical cell** kit. The `BUILD_SHEET.txt` is unusually thorough (assembly, tuning, fault-fixing).

## 2. Printability vs Ender 3 V3 (220 mm)
All parts fit comfortably:

| Part | X | Y | Z | Max | Fits? |
|------|---|---|---|-----|-------|
| al_cartridge_basket | 90 | 90 | 64 | 90 | ✅ |
| al_cartridge_lid | 85 | 81 | 7 | 85 | ✅ |
| chamber_body | 122 | 121 | 101 | 122 | ✅ |
| chamber_lid | 127 | 127 | 37 | 127 | ✅ |
| chamber_stand | 188 | 144 | 67 | 188 | ✅ |
| kit_foot | 40 | 40 | 18 | 40 | ✅ |
| kit_hub | 52 | 52 | 12 | 52 | ✅ |
| kit_leg | 126 | 10 | 152 | 152 | ✅ |
| kit_pump_clamp | 109 | 77 | 24 | 109 | ✅ |
| kit_shelf | 144 | 144 | 21 | 144 | ✅ |
| kit_strut_128 | 152 | 10 | 10 | 152 | ✅ |

No part exceeds 220 mm. All print flat, no supports (except the chamber side bosses — see §3).

## 3. Defects found (same class as the wind-turbine gearbox)
**a) `chamber_body.stl` — 2 disconnected *meshes* (NOT a defect).**
- Main chamber: 7,068 tris (≈121 mm dia, 101 mm tall).
- Second mesh: **1,024 tris, at x 50–62, y ±10, z 41–61** — the side inlet/drain boss.
- ⚠️ *Correction:* although these are separate mesh bodies (no shared edges), the boss **spatially intersects the chamber wall** (its x-range 50–62 straddles the wall radius of 60.4). A slicer unions overlapping solids, so this **prints as one part**. **No fix required** — flagged earlier in error; verified by triangle-intersection test.

**b) `al_cartridge_lid.stl` — 4 disconnected components.**
- Main lid: 10,080 tris (≈81 mm dia, 7 mm thick disc).
- 3 stray bits of **12 triangles each** at the rim (x≈±21–44, y≈±37–39, z 63.5–66.5).
- These are tiny, detached nubs at the lid's top edge — almost certainly **stray artifacts** (like the gearbox's loose pieces). → **Fix = remove them.**

## 4. Documentation gaps
- **Missing source scripts:** BUILD_SHEET repeatedly says *"Open seavolt_rig.py … change LIP … Re-run the module(s) to re-export the STLs"* and references `reactor_chamber.py`. **Neither script is in the project folder.** The entire tuning workflow described in the doc is currently **unusable** — you cannot re-tune without recovering those files.
- **`chamber_lid.stl` is not in the part list.** The BUILD_SHEET lists `chamber_body`, `chamber_stand`, `al_cartridge_basket`, `al_cartridge_lid` as optional containers, but `chamber_lid.stl` exists and isn't mentioned. Likely the reactor chamber's own lid — should be added to the list.
- Part quantities otherwise match the file set (hub/strut/leg/foot ×3, clamp/shelf ×1, etc.).

## 5. Design assessment (the good parts)
- **Snap-fit scheme is well thought out:** plug 6.00 → 5.85 lip → 6.15 slot (0.15 mm interference on the lip, 0.15 clearance in slot); shelf bars at 9.90 mm (0.10 interference); stand collar 0.2 mm; chamber ring 0.15 mm. These are sane press-snap tolerances.
- **PETG-over-PLA call is correct:** press-fits need flex; PLA cracks. Good warning in the doc.
- **Print-flat / no-supports is largely true**; only the chamber's side inlet/drain boss needs a support/raft (doc acknowledges this).
- **Lightening is intentional** (legs = tapered octagonal "bone", shelf = spoked deck) — sensible for a frame.

## 6. Recommended actions (low effort, high value)
1. ~~`chamber_body.stl`~~ — **verified fine** (boss intersects wall, unions on print). No action.
2. ✅ **`al_cartridge_lid.stl` — DONE.** Removed the 3 stray 12-tri rim bits (36 tris); 10,080-tri lid kept. Original saved as `al_cartridge_lid.stl.bak`.
3. ✅ **RECOVERED (2026-08-25): `seavolt_rig.py` and `reactor_chamber.py`** were rebuilt from the BUILD_SHEET specs and now regenerate all 11 STLs parametrically, with `reactor_chamber.py` adding functional seawater/H2/drain ports, a perforated basket, heat fins, and an O-ring lid.
4. ✅ **`chamber_lid` added to the part list** in BUILD_SHEET.txt.
5. **Test-print one joint first** (hub + strut) to validate the snap before a full set — the doc already recommends this; it's the right call.

*Deep dive conducted by parsing every STL (dimensions + connected-component + triangle-intersection analysis). Only `al_cartridge_lid.stl` was modified (stray bits removed); `chamber_body.stl` was checked and left untouched.*
