# DeM-Landslide

A compact 2D discrete element method (DEM) landslide simulation built around a LAMMPS granular-flow model. The setup represents a granular pile resting on an inclined plane with a retaining wall, followed by a release event where the wall is removed and the material slumps and flows downslope.

## Overview

This project demonstrates a simple but representative granular collapse:

- a 2D granular pile forms on an inclined slope
- a retaining wall holds the pile in place
- the wall is removed to trigger failure
- the grains flow, settle, and deposit under gravity
- output can be rendered into image frames for visualization

## Included files

- [slope_flow_dem.txt](slope_flow_dem.txt) — LAMMPS input script defining the geometry, particle setup, contact model, walls, gravity, and simulation steps
- [ovitoRender.py](ovitoRender.py) — Python script that reads the dumped trajectory and exports selected frames as images

## Simulation setup

The model uses:

- `atom_style sphere`
- Hertzian contact model with tangential interactions
- gravity aligned with the slope angle
- a fixed base and end walls
- a removable retaining wall to trigger flow

The script is set up to run a two-stage process:

1. settle the pile against the gate
2. release the gate and simulate the flow/deposition phase

## Running the simulation

From the project root, run:

```bash
lmp -in slope_flow_dem.txt
```

You can also sweep parameter values, for example:

```bash
lmp -in slope_flow_dem.txt -var theta 25 -var mu 0.4
```

Parameters such as slope angle, grain diameter, density, stiffness, friction, and run lengths are defined near the top of the input file.

## Rendering output

To generate a few representative frames from the dump trajectory:

```bash
python ovitoRender.py
```

This script creates a `frames/` directory and writes a handful of PNG snapshots from the simulation.

## Requirements

- LAMMPS installed and available in your shell as `lmp`
- Python with OVITO installed for rendering
- a dump file named `slope.dump` produced by the simulation

## Notes

This repository is intended as a simple DEM landslide starter model and is easy to adapt for parameter studies, larger domains, or alternative particle/contact laws.
