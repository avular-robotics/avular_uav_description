# Copyright 2026 Avular Holding B.V.
# All Rights Reserved
# You may use this code under the terms of the Avular
# Software End-User License Agreement.
#
# You should have received a copy of the Avular
# Software End-User License Agreement license with
# this file, or download it from: avular.com/eula

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument

from vertex_one_description.launch_helpers import launch_robot_state_publisher


def generate_launch_description():
    ld = LaunchDescription()

    ld.add_action(
        DeclareLaunchArgument("ns", default_value="robot", description="Namespace")
    )
    ld.add_action(
        DeclareLaunchArgument(
            "tf_prefix",
            default_value="",
            description="Link/joint/frame prefix (empty = no prefix)",
        )
    )

    launch_robot_state_publisher(ld)

    return ld
