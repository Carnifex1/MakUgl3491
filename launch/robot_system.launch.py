import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

PACKAGE_NAME = 'MakUgl'

def launch_setup(context, *args, **kwargs):
    mode = LaunchConfiguration('mode').perform(context)

    if mode == 'fast':
        frequency = 20.0
        overflow_threshold = 50
        default_even_topic = '/even_numbers_fast'

    elif mode == 'slow':
        frequency = 5.0
        overflow_threshold = 150
        default_even_topic = '/even_numbers_slow'
    
    elif mode == 'default':
        frequency = float(LaunchConfiguration('frequency').perform(context))
        overflow_threshold = int(LaunchConfiguration('overflow_threshold').perform(context))
        default_even_topic = '/even_numbers'
    else:
        raise ValueError(f"Invalid mode: {mode}. Valid modes are 'fast', 'slow', or 'default'.")
    
    even_topic_override = LaunchConfiguration('even_topic').perform(context)
    overflow_topic = LaunchConfiguration('overflow_topic').perform(context)
    publiser_name = LaunchConfiguration('publisher_name').perform(context)
    listener_name = LaunchConfiguration('listener_name').perform(context)

    even_topic = even_topic_override if even_topic_override else default_even_topic
    package_share = get_package_share_directory(PACKAGE_NAME)
    params_file = os.path.join(package_share, 'config', 'params.yaml')

    publisher_node = Node(
        package=PACKAGE_NAME,
        executable='even_number_publisher',
        name='even_number_publisher',
        parameters=[params_file, {
            'frequency': frequency,
            'overflow_threshold': overflow_threshold,
            'even_topic': even_topic,
            'overflow_topic': overflow_topic
        }]
    )

    listener_node = Node(
        package=PACKAGE_NAME,
        executable='overflow_listener',
        name=listener_name,
        output='screen',
        parameters=[{
            'overflow_topic': overflow_topic
        }]
    )

    return [publisher_node, listener_node]

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('mode', default_value='default', description="Mode of operation: 'fast', 'slow', or 'default'."),
        DeclareLaunchArgument('frequency', default_value='8.0', description='Frequency of publishing in Hz.'),
        DeclareLaunchArgument('overflow_threshold', default_value='80', description='Threshold for overflow.'),
        DeclareLaunchArgument('even_topic', default_value='', description='Topic name for even number publishing (optional).'),
        DeclareLaunchArgument('overflow_topic', default_value='/overflow', description='Topic name for overflow messages (optional).'),
        DeclareLaunchArgument('publisher_name', default_value='even_number_publisher', description='Name of the publisher node.'),
        DeclareLaunchArgument('listener_name', default_value='overflow_listener', description='Name of the listener node.'),
        OpaqueFunction(function=launch_setup)
    ])