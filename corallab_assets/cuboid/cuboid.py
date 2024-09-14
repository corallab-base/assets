import os


current_path = os.path.realpath(__file__)
current_dir = os.path.dirname(current_path)

robot_cfg = {
    "kinematics": {
        "use_usd_kinematics": False,

        "external_asset_path": current_dir,

        "urdf_path": "cuboid.urdf",
        "asset_root_path": ".",

        "base_link": "base_link",
        "ee_link": "cuboid",
        "link_names": ["cuboid"],
        "collision_link_names": ['cuboid'],

        "external_robot_configs_path": current_dir,
        "collision_spheres": 'collision_spheres.yml',
        "collision_sphere_buffer": 0.005,

        "self_collision_ignore": {},
        "self_collision_buffer": {},
        "lock_joints": None,
        "mesh_link_names": ['cuboid'],

        "cspace": {
            "joint_names": [
                'cuboid'
            ],
            "retract_config": [
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0
            ],
            "null_space_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0
            ],
            "cspace_distance_weight": [
                1.0, 1.0, 1.0, 1.0, 1.0, 1.0
            ],
            "max_jerk": 500.0,
            "max_acceleration": 15.0,
        }
    }
}
