# Avular Vertex One URDF

This directory contains the URDF/xacro description for the Avular Vertex One, along with the mesh files it references.

```
urdf/
├── vertex_one.urdf.xacro   # Robot description
└── meshes/                 # body + propeller meshes
```

The xacro is the single source of truth for the robot's kinematic and visual
description. It is consumed by `robot_state_publisher` (via the package's
launch files) and converted to SDF at simulation launch time by the
`avular_simulations` / `gazebo_simulation` packages

## Model overview

| Link        | Type    | Notes                                                  |
|-------------|---------|--------------------------------------------------------|
| `base_link` | root    | Body collision box (0.5 × 0.5 × 0.25), `body.dae` visual |
| `rotor_FL`  | continuous | Front-left rotor, `prop_l.dae`                        |
| `rotor_FR`  | continuous | Front-right rotor, `prop_r.dae`                       |
| `rotor_RL`  | continuous | Rear-left rotor, `prop_l.dae`                         |
| `rotor_RR`  | continuous | Rear-right rotor, `prop_l.dae`                        |
| `imu_link`  | fixed   | At `base_link` origin                                  |
| `gnss_link` | fixed   | At `(-0.17, 0.22, 0)` from `base_link`                 |

Layout is a symmetric X-quad with rotor arms at `±0.20613 m` (x) and
`±0.20047 m` (y).

The rotor joints are `continuous`; driving them requires a
`/<ns>/joint_states` topic (the launch file remaps to `/robot/joint_states`
by default).

## Xacro arguments

| Arg      | Default | Description                                                          |
|----------|---------|----------------------------------------------------------------------|
| `prefix` | `""`    | Optional link/joint prefix. When non-empty, every link/joint name is prefixed with `<prefix>_`. Use this to spawn multiple Vertex Ones in the same world without TF name collisions. |

## Rendering the xacro manually

```bash
# Plain render
xacro vertex_one.urdf.xacro > vertex_one.urdf

# With a prefix (e.g. for multi-robot setups)
xacro vertex_one.urdf.xacro prefix:=uav1 > vertex_one_uav1.urdf
```

In normal use you don't need to do this — the launch files in
[../launch/](../launch/) process the xacro for you and pass it to
`robot_state_publisher` via the `robot_description` parameter.

## Meshes

Meshes are referenced as
`package://vertex_one_description/urdf/meshes/<file>.dae` with a uniform
`0.001 0.001 0.001` scale (the meshes are authored in millimeters). The body
visual is rotated `-π/2, 0, π/2` rpy to align the mesh with the URDF frame
convention (x-forward, z-up).
