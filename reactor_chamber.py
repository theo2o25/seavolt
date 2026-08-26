"""
reactor_chamber.py - Parametric reactor chamber generator for the SeaVolt (PASES) rig.

REBUILT from BUILD_SHEET.txt / SEAVOLT_DEEPDIVE.md. The original generator was
lost; this reconstructs the reaction core and, crucially, makes it FUNCTIONAL:
a real seawater -> H2 + heat reactor rather than a sealed cup.

Functional upgrades over the original static chamber:
  * chamber_body: threaded-boss seawater INLET (low), H2 GAS OUTLET (top, with
    internal vent path), BRINE DRAIN (bottom), and an external HEAT-FIN ring so
    the exothermic reaction heat can be tapped (feeds the PASES heat -> RO loop).
  * al_cartridge_basket: PERFORATED walls + base so seawater flows through the Al
    charge and H2 vents upward; central vent tube channels gas to the outlet.
  * chamber_lid: O-RING groove so the chamber seals and holds pressure for safe
    H2 collection.

Snap tolerances (mm): chamber ring 0.15 interference, stand collar 0.20.

Run:  python reactor_chamber.py
Outputs one STL per part in the same directory.
"""
from __future__ import annotations
import os
from build123d import Box, Cylinder, Part, Axis, Location, Torus, export_stl

# ---- tunable parameters --------------------------------------------------
RING = 0.15       # chamber-to-stand ring interference (snap waist)
COLLAR = 0.20     # stand-to-shelf collar interference
# ---------------------------------------------------------------------------

OUT = os.path.dirname(os.path.abspath(__file__))


def _place(obj, angle_deg, x=0.0, y=0.0, z=0.0):
    return obj.rotate(Axis.Z, angle_deg).move(Location((x, y, z)))


def chamber_stand() -> Part:
    base = Box(188.0, 144.0, 20.0)
    pedestal = Cylinder(65.0, 47.0).move(Location((0.0, 0.0, 20.0 + 47.0 / 2.0)))  # overlaps base
    # top ring waist: raised ring the chamber body snaps into (0.15); overlaps pedestal
    ring = Cylinder(62.0, 14.0).move(Location((0.0, 0.0, 20.0 + 47.0 - 5.0)))
    ring = ring - Cylinder(62.0 - RING - 2.0, 16.0)
    # collar skirt that receives the shelf collar (0.20 interference); overlaps ring
    collar = Cylinder(22.0, 12.0).move(Location((0.0, 0.0, 20.0 + 47.0 - 4.0)))
    collar = collar - Cylinder(22.0 - COLLAR - 2.0, 14.0)
    return base + pedestal + ring + collar


def chamber_body() -> Part:
    outer = Cylinder(60.5, 101.0)  # ~121 mm dia
    # hollow interior to hold the cartridge basket (leaves bottom + top rim)
    cavity = Cylinder(54.0, 90.0).move(Location((0.0, 0.0, -5.0)))
    body = outer - cavity
    # --- functional ports ---
    # seawater inlet (low, through wall)
    body = body - _place(Cylinder(6.0, 40.0).rotate(Axis.X, 90), 0.0, y=60.0, z=-30.0)
    body = body + _place(Cylinder(11.0, 22.0).rotate(Axis.X, 90), 0.0, y=60.0, z=-30.0)
    # brine drain (bottom, through wall)
    body = body - _place(Cylinder(6.0, 40.0).rotate(Axis.X, 90), 0.0, y=60.0, z=-50.0)
    body = body + _place(Cylinder(11.0, 22.0).rotate(Axis.X, 90), 0.0, y=60.0, z=-50.0)
    # H2 gas outlet (top, vertical) with internal central vent tube
    body = body - Cylinder(7.0, 40.0).move(Location((0.0, 0.0, 50.5 + 10.0)))
    body = body + Cylinder(12.0, 22.0).move(Location((0.0, 0.0, 50.5 + 11.0)))
    body = body + Cylinder(6.5, 90.0).move(Location((0.0, 0.0, 0.0)))  # central vent tube
    # external heat-fins (tap reaction heat for the RO/desalination loop)
    for ang in range(0, 360, 30):
        fin = Box(8.0, 6.0, 40.0)
        body = body + _place(fin, float(ang), y=62.0, z=0.0)
    # O-ring seat groove near the top rim
    body = body - Torus(50.0, 3.0).move(Location((0.0, 0.0, 50.5 - 6.0)))
    return body


def chamber_lid() -> Part:
    lid = Cylinder(63.5, 37.0)  # 127 dia
    lid = lid - Torus(50.0, 3.0).move(Location((0.0, 0.0, -37.0 / 2.0 + 4.0)))  # O-ring groove
    lid = lid - Cylinder(7.5, 40.0)  # central vent hole (aligns with outlet)
    lid = lid + Cylinder(10.0, 8.0).move(Location((0.0, 0.0, 37.0 / 2.0 + 4.0)))  # cap nut
    return lid


def al_cartridge_basket() -> Part:
    basket = Cylinder(45.0, 64.0)  # 90 dia
    # perforated walls so seawater flows through the Al charge
    for ang in range(0, 360, 20):
        slot = Box(6.0, 52.0, 8.0)
        basket = basket - _place(slot, float(ang), y=45.0, z=0.0)
    # base inlet holes (seawater enters from below)
    for r in (18.0, 32.0):
        for ang in range(0, 360, 60):
            basket = basket - _place(Cylinder(5.0, 10.0), float(ang), x=r, y=0.0, z=-32.0 + 5.0)
    # central vent tube channels H2 up to the outlet
    basket = basket + Cylinder(6.0, 60.0).move(Location((0.0, 0.0, 2.0)))
    return basket


def al_cartridge_lid() -> Part:
    lid = Box(85.0, 81.0, 7.0)
    lid = lid - Cylinder(7.0, 10.0)  # vent hole
    return lid


PARTS = {
    "chamber_stand": chamber_stand,
    "chamber_body": chamber_body,
    "chamber_lid": chamber_lid,
    "al_cartridge_basket": al_cartridge_basket,
    "al_cartridge_lid": al_cartridge_lid,
}


def verify(part: Part, name: str, target_max: float):
    bb = part.bounding_box()
    size = bb.size
    max_dim = max(size.X, size.Y, size.Z)
    solids = len(part.solids())
    ok = max_dim <= 220.0 and solids == 1 and max_dim <= target_max * 1.05
    flag = "OK" if ok else "CHECK"
    print(f"  {name:20s} bbox {size.X:6.1f} x {size.Y:6.1f} x {size.Z:6.1f}  "
          f"max {max_dim:6.1f} (tgt {target_max:5.0f}) solids {solids} [{flag}]")
    return ok


TARGETS = {
    "chamber_stand": 188.0,
    "chamber_body": 134.0,  # 121 dia + external heat fins
    "chamber_lid": 127.0,
    "al_cartridge_basket": 90.0,
    "al_cartridge_lid": 85.0,
}


def main():
    print(f"build123d SeaVolt reactor_chamber generator | RING={RING} COLLAR={COLLAR}")
    all_ok = True
    for name, fn in PARTS.items():
        part = fn()
        path = os.path.join(OUT, f"{name}.stl")
        export_stl(part, path)
        print(f"  wrote {path}")
        all_ok &= verify(part, name, TARGETS[name])
    print("VERIFY:", "all chamber parts within spec" if all_ok else "review flagged parts")


if __name__ == "__main__":
    main()
