from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='MakUgl',
            executable='even_number_publisher',
            name='even_pub',
            output='screen',
        ),
        Node(
            package='MakUgl',
            executable='overflow_listener',
            name='overflow_listener',
            output='screen',
        ),
    ])