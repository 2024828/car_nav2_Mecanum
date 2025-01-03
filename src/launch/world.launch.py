import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, TextSubstitution


def generate_launch_description():

    # Declare the world file argument
    world_arg = DeclareLaunchArgument(
        'world', default_value='home.sdf',
        description='Name of the Gazebo world file to load'
    )

    # Get package directories
    pkg_car_nav2_mecanum = get_package_share_directory('car_nav2_mecanum')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    # Update GZ_SIM_RESOURCE_PATH with the path to worlds folder
    gazebo_models_path = os.path.join(pkg_car_nav2_mecanum, 'worlds')
    os.environ["GZ_SIM_RESOURCE_PATH"] += os.pathsep + gazebo_models_path

    # Include Gazebo launch file
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments={
            'gz_args': [PathJoinSubstitution([
                pkg_car_nav2_mecanum,
                'worlds',
                LaunchConfiguration('world')
            ]),
            TextSubstitution(text=' -r -v -v1')],
            'on_exit_shutdown': 'true'
        }.items()
    )

    # Create launch description
    launchDescriptionObject = LaunchDescription()

    # Add actions
    launchDescriptionObject.add_action(world_arg)
    launchDescriptionObject.add_action(gazebo_launch)

    return launchDescriptionObject