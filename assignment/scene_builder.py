"""
DIGM 131 - Assignment 1: Procedural Scene Builder
==================================================

OBJECTIVE:
    Build a simple 3D scene in Maya using Python scripting.
    You will practice using maya.cmds to create and position geometry,
    and learn to use descriptive variable names.

REQUIREMENTS:
    1. Create a ground plane (a large, flat polygon plane).
    2. Create at least 5 objects in your scene.
    3. Use at least 2 different primitive types (e.g., cubes AND spheres,
       or cylinders AND cones, etc.).
    4. Position every object using descriptive variable names
       (e.g., house_x, tree_height -- NOT x1, h).
    5. Add comments explaining what each section of your code does.

GRADING CRITERIA:
    - [20%] Ground plane is created and scaled appropriately.
    - [30%] At least 5 objects are created using at least 2 primitive types.
    - [25%] All positions/sizes use descriptive variable names.
    - [15%] Code is commented clearly and thoroughly.
    - [10%] Scene is visually coherent (objects are placed intentionally,
            not overlapping randomly).

TIPS:
    - Run this script from Maya's Script Editor (Python tab).
    - Use maya.cmds.polyCube(), maya.cmds.polySphere(), maya.cmds.polyCylinder(),
      maya.cmds.polyCone(), maya.cmds.polyPlane(), etc.
    - Use maya.cmds.move(x, y, z, objectName) to position objects.
    - Use maya.cmds.scale(x, y, z, objectName) to resize objects.
    - Use maya.cmds.rename(oldName, newName) to give objects meaningful names.
"""

import maya.cmds as cmds

# ---------------------------------------------------------------------------
# Clear the scene so we start fresh each time the script runs.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# ---------------------------------------------------------------------------
# Ground Plane - smaller and to the side slightly
# ---------------------------------------------------------------------------
# Descriptive variables for the ground plane dimensions and position.
ground_width = 20
ground_depth = 20
ground_x_position = -3.5

ground = cmds.polyPlane(
    name="ground_plane",
    width=ground_width,
    height=ground_depth,
    subdivisionsX=1,
    subdivisionsY=1,
)[0]
cmds.move(ground_x_position, 0, 0, ground)

# ---------------------------------------------------------------------------
# Example Object 1 -- a simple building (cube)
# This is provided as an example. Study it, then add your own objects below.
# I started by scene with a small bench or chair, utilizing a cube.
# ---------------------------------------------------------------------------
bench_width = 6
bench_height = 2
bench_depth = 3
bench_x = -5
bench_z = 2

bench = cmds.polyCube(
    name="bench_01",
    width=bench_width,
    height=bench_height,
    depth=bench_depth,
)[0]
# Raise the building so its base sits on the ground plane.
cmds.move(bench_x, bench_height / 2.0, bench_z, bench)

# ---------------------------------------------------------------------------
# TODO: Add Object 2
# Create a second object using a DIFFERENT primitive type than the cube above.
# Remember to:
#   - Use descriptive variable names for size and position.
#   - Name the object meaningfully with the 'name' parameter or cmds.rename().
#   - Position it so it sits on the ground (not floating or buried).
# I created the stem to a mushroom that is also the bench umbrella or shade.
# ---------------------------------------------------------------------------
stem_height = 16
stem_radius = 2
stem_x = 3
stem_y = 8
stem_z = 0

stem = cmds.polyCylinder(
    name="mushroom_stem_01",
    height=stem_height,
    radius=stem_radius,
)[0]
cmds.move(stem_x, stem_y, stem_z, stem)

# ---------------------------------------------------------------------------
# TODO: Add Object 3
# The back of the bench or the bench rest.
# ---------------------------------------------------------------------------
benchback_width = 6
benchback_height = 4
benchback_depth = 1.5
benchback_x = -5
benchback_y = 3.5
benchback_z = 4.5

benchback = cmds.polyCube(
    name="benchback_01",
    width=benchback_width,
    height=benchback_height,
    depth=benchback_depth,
)[0]
cmds.move(benchback_x, benchback_y, benchback_z, benchback)

# ---------------------------------------------------------------------------
# TODO: Add Object 4
# A second medium sized mushroom stem, behind the bench.
# ---------------------------------------------------------------------------
stem_height = 12
stem_radius = 1.5
stem_x = -5
stem_y = 6
stem_z = 10

stem = cmds.polyCylinder(
    name="mushroom_stem_02",
    height=stem_height,
    radius=stem_radius,
)[0]
cmds.move(stem_x, stem_y, stem_z, stem)

# ---------------------------------------------------------------------------
# TODO: Add Object 5
# A small sized mushroom stem to the right of the bench.
# ---------------------------------------------------------------------------
stem_height = 8
stem_radius = 1
stem_x = -11
stem_y = 4
stem_z = 0

stem = cmds.polyCylinder(
    name="mushroom_stem_03",
    height=stem_height,
    radius=stem_radius,
)[0]
cmds.move(stem_x, stem_y, stem_z, stem)

# ---------------------------------------------------------------------------
# TODO (Optional): Add more objects to make your scene more interesting!
# Consider: trees, lamp posts, fences, vehicles, animals, etc.
# Three different sized mushroom caps.
# ---------------------------------------------------------------------------
cap_height = 5
cap_radius = 1
cap_x = -11
cap_y = 10
cap_z = 0

cap = cmds.polyCone(
    name="mushroom_cap_03",
    height=stem_height,
    radius=stem_radius,
)[0]
cmds.move(cap_x, cap_y, cap_z, cap)

cap_height = 4
cap_radius = 1
cap_x = -5
cap_y = 14
cap_z = 10

cap = cmds.polyCone(
    name="mushroom_cap_02",
    height=stem_height,
    radius=stem_radius,
)[0]
cmds.move(cap_x, cap_y, cap_z, cap)

cap_height = 8
cap_radius = 1
cap_x = 3
cap_y = 18
cap_z = 0

cap = cmds.polyCone(
    name="mushroom_cap_01",
    height=stem_height,
    radius=stem_radius,
)[0]
cmds.move(cap_x, cap_y, cap_z, cap)
cmds.scale(6, .75, 6, "mushroom_cap_01")
cmds.scale(5, .5, 5, "mushroom_cap_02")
cmds.scale(4, .25, 4, "mushroom_cap_03")

# ---------------------------------------------------------------------------
# Frame All -- so the whole scene is visible in the viewport.
# (This is provided for you -- do not remove.)
# ---------------------------------------------------------------------------
cmds.viewFit(allObjects=True)
print("Scene built successfully!")
