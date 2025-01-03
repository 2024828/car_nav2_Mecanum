# car_nav2_mecanum
Using ROS2 Jazzy and Gazebo Harmonic for autonomous navigation simulation of a robot car with Mecanum wheels.

This project is based on the BME MOGI - ROS course, with the camera part removed, and the mapping and navigation features retained. For further learning, please refer to https://github.com/MOGI-ROS.

This project is for personal learning purposes only. If there are any copyright infringements, please contact us for removal.

The other version is a two-wheeled robot with differential wheels. For more details, please refer to:https://github.com/2024828/car_nav2

You need to do this:

1.Run the following command to clone the car_nav2 repository to your local machine:

    git clone https://github.com/2024828/car_nav2_mecanum.git

2.The file uses some Gazebo models, which you can download from:https://drive.google.com/file/d/1tcfoLFReEW1XNHPUAeLpIz2iZXqQBvo_/view.

If you want to learn more about Gazebo models, please visit:https://github.com/MOGI-ROS/Week-3-4-Gazebo-basics.

Make sure to let Gazebo know about their location by running:

    export GZ_SIM_RESOURCE_PATH=~/gazebo_models

3.Build the package and run:
    
    colcon build
    . install/setup.bash
    ros2 launch car_nav2_mecanum spawn_robot.launch.py

Open a new terminal and run:
    
    export GZ_SIM_RESOURCE_PATH=~/gazebo_models
    . install/setup.bash
    ros2 launch car_nav2_mecanum navigation_with_slam.launch.py

You can use the `2D goal pose` in the RViz2 toolbar to control the robot's movement and mapping. The robot will automatically plan the path.

You can also click the `+` on rviz2 to add the `NAV2 Goal` tool. Then, click on the `Waypoint/NavThrough Poses Mode` under the Nav2 plugin. You can use the `Nav2 Goal` to set multiple waypoints in sequence. By clicking the `StartWaypoint Following` at the bottom, you can start waypoint navigation, and the robot will move towards the preset target locations in order.
