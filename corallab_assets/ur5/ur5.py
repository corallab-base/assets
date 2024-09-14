##
## Copyright (c) 2023 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
##
## NVIDIA CORPORATION, its affiliates and licensors retain all intellectual
## property and proprietary rights in and to this material, related
## documentation and any modifications thereto. Any use, reproduction,
## disclosure or distribution of this material and related documentation
## without an express license agreement from NVIDIA CORPORATION or
## its affiliates is strictly prohibited.
##

import os


current_path = os.path.realpath(__file__)
current_dir = os.path.dirname(current_path)

robot_cfg = {
    "kinematics": {
        "use_usd_kinematics": False,

        "external_asset_path": current_dir,

        "urdf_path": "ur5.urdf",
        "asset_root_path": "../ur5",

        # "isaac_usd_path": "/Isaac/Robots/UR10/ur10_long_suction.usd",
        # "usd_robot_root": "/ur10",
        # "usd_path": "robot/ur_description/dual_ur10e.usd",

        "base_link": "base_fixture_link",
        "ee_link": "ee_link",
        "link_names": ["ee_link"],
        "collision_link_names": [
            'shoulder_link', 'upper_arm_link', 'forearm_link', 'wrist_1_link', 'wrist_2_link', 'wrist_3_link', 'ee_link',
        ],

        "external_robot_configs_path": current_dir,
        "collision_spheres": 'collision_spheres.yml',
        "collision_sphere_buffer": 0.005,

        "self_collision_ignore": {
            "upper_arm_link": ["shoulder_link", "forearm_link"],
            "forarm_link": ["wrist_1_link"],
            "wrist_1_link": ["wrist_2_link", "wrist_3_link"],
            "wrist_2_link": ["wrist_3_link", "ee_link"],
            "wrist_3_link": ["ee_link"],
            "ee_link": ["wrist_3_link"]
        },
        "self_collision_buffer": {
            'upper_arm_link': 0,
            'forearm_link': 0,
            'wrist_1_link': 0,
            'wrist_2_link': 0,
            'wrist_3_link' : 0,
            'tool0': 0.025,
        },
        "lock_joints": None,
        "mesh_link_names": [
            'shoulder_link', 'upper_arm_link', 'forearm_link', 'wrist_1_link', 'wrist_2_link', 'wrist_3_link',
        ],

        "cspace": {
            "joint_names": [
                'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint',
            ],
            "retract_config": [
                0.00, -2.2, 1.9, -1.383, -1.57, 0.00,
            ],
            "null_space_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
            ],
            "cspace_distance_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
            ],
            "max_jerk": 500.0,
            "max_acceleration": 12.0,
            "position_limit_clip": 0.1
        }
    }
}
