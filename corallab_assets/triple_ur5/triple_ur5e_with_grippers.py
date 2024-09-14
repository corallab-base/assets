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

        "urdf_path": "triple_ur5e.urdf",
        "asset_root_path": "../ur5e",

        "base_link": "shared_base_link",
        "ee_link": "ee_link_0",
        "link_names": ["ee_link_0", "ee_link_1", "ee_link_2"],
        "collision_link_names": [
            'shoulder_link_0', 'upper_arm_link_0', 'forearm_link_0', 'wrist_1_link_0', 'wrist_2_link_0', 'wrist_3_link_0', 'ee_link_0',
            'shoulder_link_1', 'upper_arm_link_1', 'forearm_link_1', 'wrist_1_link_1', 'wrist_2_link_1', 'wrist_3_link_1', 'ee_link_1',
            'shoulder_link_2', 'upper_arm_link_2', 'forearm_link_2', 'wrist_1_link_2', 'wrist_2_link_2', 'wrist_3_link_2', 'ee_link_2'
        ],

        "external_robot_configs_path": current_dir,
        "collision_spheres": 'collision_spheres_with_grippers.yml',
        "collision_sphere_buffer": 0.005,

        "self_collision_ignore": {
            "upper_arm_link_0": ["shoulder_link_0", "forearm_link_0"],
            "forearm_link_0": ["wrist_1_link_0"],
            "wrist_1_link_0": ["wrist_2_link_0", "wrist_3_link_0"],
            "wrist_2_link_0": ["wrist_3_link_0", "ee_link_0"],
            "wrist_3_link_0": ["ee_link_0"],

            "upper_arm_link_1": ["shoulder_link_1", "forearm_link_1"],
            "forearm_link_1": ["wrist_1_link_1"],
            "wrist_1_link_1": ["wrist_2_link_1","wrist_3_link_1"],
            "wrist_2_link_1": ["wrist_3_link_1", "ee_link_1"],
            "wrist_3_link_1": ["ee_link_1"],

            "upper_arm_link_2": ["shoulder_link_2", "forearm_link_2"],
            "forearm_link_2": ["wrist_1_link_2"],
            "wrist_1_link_2": ["wrist_2_link_2", "wrist_3_link_2"],
            "wrist_2_link_2": ["wrist_3_link_2", "ee_link_2"],
            "wrist_3_link_2": ["ee_link_2"],
        },
        "self_collision_buffer": {
            "shoulder_link_0": 0.05,
            "shoulder_link_1": 0.05,
            "shoulder_link_2": 0.05,
        },
        "lock_joints": None,
        "mesh_link_names": [
            'shoulder_link_0', 'upper_arm_link_0', 'forearm_link_0', 'wrist_1_link_0', 'wrist_2_link_0', 'wrist_3_link_0',
            'shoulder_link_1', 'upper_arm_link_1', 'forearm_link_1', 'wrist_1_link_1', 'wrist_2_link_1' ,'wrist_3_link_1'
            'shoulder_link_2', 'upper_arm_link_2', 'forearm_link_2', 'wrist_1_link_2', 'wrist_2_link_2' ,'wrist_3_link_2'
        ],

        "cspace": {
            "joint_names": [
                'shoulder_pan_joint_0', 'shoulder_lift_joint_0', 'elbow_joint_0', 'wrist_1_joint_0', 'wrist_2_joint_0', 'wrist_3_joint_0',
                'shoulder_pan_joint_1', 'shoulder_lift_joint_1', 'elbow_joint_1', 'wrist_1_joint_1', 'wrist_2_joint_1', 'wrist_3_joint_1',
                'shoulder_pan_joint_2', 'shoulder_lift_joint_2', 'elbow_joint_2', 'wrist_1_joint_2', 'wrist_2_joint_2', 'wrist_3_joint_2'
            ],
            "retract_config": [
                0.00, -2.2, 1.9, -1.383, -1.57, 0.00,
                0.00, -2.2, 1.9, -1.383, -1.57, 0.00,
                0.00, -2.2, 1.9, -1.383, -1.57, 0.00
            ],
            "null_space_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0
            ],
            "cspace_distance_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0                
            ],
            "max_jerk": 500.0,
            "max_acceleration": 15.0,
        }
    }
}
