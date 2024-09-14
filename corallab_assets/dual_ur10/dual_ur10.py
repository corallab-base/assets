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

        "urdf_path": "dual_ur10.urdf",
        "asset_root_path": "../ur10",

        # "isaac_usd_path": "/Isaac/Robots/UR10/ur10_long_suction.usd",
        # "usd_robot_root": "/ur10",
        # "usd_path": "robot/ur_description/dual_ur10e.usd",

        "base_link": "base_fixture_link",
        "ee_link": "tool0",
        "link_names": ["tool1", "tool0"],
        "collision_link_names": [
            'shoulder_link','upper_arm_link', 'forearm_link', 'wrist_1_link', 'wrist_2_link' ,'wrist_3_link', 'tool0',
            'shoulder_link_1','upper_arm_link_1', 'forearm_link_1', 'wrist_1_link_1', 'wrist_2_link_1' ,'wrist_3_link_1', 'tool1'
        ],

        # "external_robot_configs_path": "",

        "collision_spheres": 'spheres/dual_ur10e.yml',
        "collision_sphere_buffer": 0.005,

        "self_collision_ignore": {
            "upper_arm_link": ["shoulder_link","forearm_link"],
            "forarm_link": ["wrist_1_link"],
            "wrist_1_link": ["wrist_2_link","wrist_3_link"],
            "wrist_2_link": ["wrist_3_link", "tool0"],
            "wrist_3_link": ["tool0"],

            "upper_arm_link_1": ["shoulder_link_1","forearm_link_1"],
            "forarm_link_1": ["wrist_1_link_1"],
            "wrist_1_link_1": ["wrist_2_link_1","wrist_3_link_1"],
            "wrist_2_link_1": ["wrist_3_link_1", "tool1"],
            "wrist_3_link_1": ["tool1"],
        },
        "self_collision_buffer": {
            "shoulder_link": 0.05,
            "shoulder_link_1": 0.05,
        },
        "lock_joints": None,
        "mesh_link_names": [
            'shoulder_link', 'upper_arm_link', 'forearm_link', 'wrist_1_link', 'wrist_2_link', 'wrist_3_link',
            'shoulder_link_1','upper_arm_link_1', 'forearm_link_1', 'wrist_1_link_1', 'wrist_2_link_1' ,'wrist_3_link_1'
        ],

        "cspace": {
            "joint_names": [
                'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint',
                'shoulder_pan_joint_1', 'shoulder_lift_joint_1', 'elbow_joint_1', 'wrist_1_joint_1', 'wrist_2_joint_1', 'wrist_3_joint_1'
            ],
            "retract_config": [
                -1.57, -2.2, 1.9, -1.383, -1.57, 0.00,
                -1.57, -2.2, 1.9, -1.383, -1.57, 0.00
            ],
            "null_space_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0
            ],
            "cspace_distance_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0
            ],
            "max_jerk": 500.0,
            "max_acceleration": 15.0,
        }
    }
}
