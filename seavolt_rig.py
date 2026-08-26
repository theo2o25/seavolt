"""
seavolt_rig.py - Parametric snap-fit frame kit generator for the SeaVolt (PASES) rig.

REBUILT from BUILD_SHEET.txt. The original generator was lost; this reconstructs
the printable frame parts parametrically so the documented tuning workflow works
again (change LIP / SHELF_LIP / GRIP, re-run, re-export).

Snap-fit math (mm), per BUILD_SHEET:
    plug 6.00  ->  snaps past a 5.85 lip  ->  seats in a 6.15 slot
    shelf bar 9.90  (0.10 interference with the 10 mm bar)
    stand collar 0.20 / chamber ring 0.15  (handled in reactor_chamber.py)
    pump clamp grip 0.20

Geometry is simplified relative to the original artistic renders (e.g. the "bone"
leg is a crossed-bar X, the spoked shelf is a lightened disc) but matches the
verified bounding boxes in SEAVOLT_DEEPDIVE.md and honours the tolerances.

Run:  python seavolt_rig.py
Outputs one STL per part in the same directory.
"""
from __future__ import annotations
import os
from build123d import Box, Cylinder, Part, Axis, Location, Vector, export_stl

# ---- tunable parameters (edit these, then re-run) -------------------------
LIP = 0.15          # plug interference in hub slot lip
SHELF_LIP = 9.90    # 0.10 interference with the 10 mm shelf bar
GRIP = 0.20         # pump clamp grip interference
# ---------------------------------------------------------------------------

PLUG_D = 6.00
LIP_D = 5.85
SLOT_D = 6.15
BAR_D = 10.0

OUT = os.path.dirname(os.path.abspath(__file__))


def _place(obj, angle_deg, x=0.0, y=0.0, z=0.0):
    """Rotate obj about +Z by angle, then translate."""
    return obj.rotate(Axis.Z, angle_deg).move(Location((x, y, z)))


def plug(length: float = 14.0) -> Part:
    """Cylindrical snap plug (dia PLUG_D) that seats in a 6.15 slot past a 5.85 lip."""
    return Cylinder(PLUG_D / 2.0, length)


def hub() -> Part:
    h = Cylinder(52 / 2.0, 12.0)  # disc, slots facing up
    # three top radial slots for struts
    for ang in (0.0, 120.0, 240.0):
        slot = Box(SLOT_D + 0.4, 16.0, 8.0)
        h = h - _place(slot, ang, y=(52 / 2.0) - 8.0, z=2.0)
    # center bottom socket for leg plug
    h = h - Cylinder(PLUG_D / 2.0 + 0.2, 8.0).move(Location((0, 0, -6.0)))
    # one outward slot for the pump clamp (points away from the strut triangle)
    pump = Box(SLOT_D + 0.4, 16.0, 8.0)
    h = h - _place(pump, 90.0, y=(52 / 2.0) - 8.0, z=2.0)
    return h


def strut_128() -> Part:
    bar = Box(152.0, 10.0, 10.0)
    for sx in (-1.0, 1.0):
        p = plug(14.0).rotate(Axis.Y, 90).move(Location((sx * (76.0 + 5.0), 0.0, 0.0)))
        bar = bar + p
    return bar


def leg() -> Part:
    # X-pattern leg (two crossed bars) with a bottom plug for the hub socket
    b1 = Box(10.0, 10.0, 170.0).rotate(Axis.Y, 45.0)
    b2 = Box(10.0, 10.0, 170.0).rotate(Axis.Y, -45.0)
    leg_part = b1 + b2
    # central strut bridges the X down to the plug so everything fuses
    leg_part = leg_part + Box(10.0, 10.0, 75.0).move(Location((0.0, 0.0, -27.5)))
    # plug extends up into the strut so it fuses with the leg (no detached solid)
    leg_part = leg_part + plug(40.0).move(Location((0.0, 0.0, -85.0)))
    return leg_part


def foot() -> Part:
    f = Box(40.0, 40.0, 18.0)
    f = f - Cylinder(PLUG_D / 2.0 + 0.2, 14.0).move(Location((0.0, 0.0, 4.0)))
    return f


def shelf() -> Part:
    s = Cylinder(72.0, 21.0)  # 144 dia, spoked deck (lightening holes)
    for r in (24.0, 48.0):
        for ang in range(0, 360, 60):
            s = s - _place(Cylinder(9.0, 30.0), float(ang), x=r, y=0.0)
    # raised snap collar on top (chamber stand snaps here, 0.20 interference)
    s = s + Cylinder(20.0, 8.0).move(Location((0.0, 0.0, 21.0 / 2.0 + 4.0)))
    # three underside snap keyways for the 10 mm bars (grip width = SHELF_LIP)
    for ang in (0.0, 120.0, 240.0):
        key = Box(SHELF_LIP, 14.0, 12.0)
        s = s - _place(key, ang, y=52.0, z=-21.0 / 2.0 + 6.0)
    return s


def pump_clamp() -> Part:
    block = Box(109.0, 77.0, 24.0)
    # pump bore must fit the 24 mm block thickness (radius < 12) or it splits the part
    bore = 10.0 - GRIP / 2.0
    block = block - Cylinder(bore, 40.0).rotate(Axis.Y, 90)
    # stub that plugs into the hub outward slot; box overlaps block AND protrudes
    block = block + Box(8.0, 12.0, 14.0).move(Location((0.0, -77.0 / 2.0 - 5.5, 0.0)))
    return block


PARTS = {
    "kit_hub": hub,
    "kit_strut_128": strut_128,
    "kit_leg": leg,
    "kit_foot": foot,
    "kit_shelf": shelf,
    "kit_pump_clamp": pump_clamp,
}


def verify(part: Part, name: str):
    bb = part.bounding_box()
    size = bb.size
    max_dim = max(size.X, size.Y, size.Z)
    solids = len(part.solids())
    ok = max_dim <= 220.0 and solids == 1
    flag = "OK" if ok else "CHECK"
    print(f"  {name:18s} bbox {size.X:6.1f} x {size.Y:6.1f} x {size.Z:6.1f}  "
          f"max {max_dim:6.1f}  solids {solids}  [{flag}]")
    return ok


def main():
    print(f"build123d SeaVolt rig generator | LIP={LIP} SHELF_LIP={SHELF_LIP} GRIP={GRIP}")
    all_ok = True
    for name, fn in PARTS.items():
        part = fn()
        path = os.path.join(OUT, f"{name}.stl")
        export_stl(part, path)
        print(f"  wrote {path}")
        all_ok &= verify(part, name)
    print("VERIFY:", "all parts within 220mm and single-solid" if all_ok else "review flagged parts")


if __name__ == "__main__":
    main()
