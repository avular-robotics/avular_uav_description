## Unreleased
- Removed `cmake_avular` usage from `vertex_one_description`
- Added `prefix` xacro arg to prefix link/joint names for multi-robot simulations
- Refactored launch files into shared helpers (xacro processing + RViz template rendering)
- Updated Gazebo resource hooks (GZ_SIM_RESOURCE_PATH / IGN_GAZEBO_RESOURCE_PATH) to use `gz_resources` for mesh discovery
