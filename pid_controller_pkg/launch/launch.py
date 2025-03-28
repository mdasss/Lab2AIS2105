from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

#ros2 launch pid_controller_pkg launch.py kp:=0.1 ki:=0.05 kd:=0.01


def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('joint_sim'), 
        'config',
        'parameters.yaml'
    )

    return LaunchDescription([
        DeclareLaunchArgument('kp', default_value='1.0'),
        DeclareLaunchArgument('ki', default_value='0.0'),
        DeclareLaunchArgument('kd', default_value='0.0'),

        Node(
            package='pid_controller_pkg',
            executable='pid_controller_node',
            name='pid_controller',
            output='screen',
            parameters=[{
                'p': LaunchConfiguration('kp'),
                'i': LaunchConfiguration('ki'),
                'd': LaunchConfiguration('kd')
            }]
        ),

        Node(
            package='joint_sim',
            executable='test1',
            name='JointSimulatorPublisher',
            output='screen',
            parameters=[config]
        ),

        Node(
            package='reference_input_node_cpp',
            executable='set_reference_server',
            name='set_reference_server',
            output='screen'
        )
    ])

