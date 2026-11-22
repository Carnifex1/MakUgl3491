import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')

        self.subscription = self.create_subscription(
            Int32,
            'overflow',
            self.overflow_callback,
            10
        )

        self.get_logger().info('Overflow listener has been started')
    
    def overflow_callback(self, msg):
        self.get_logger().warning(f'!!!OVERFLOW!!! The message has been received: {msg.data}')

def main():
    rclpy.init()
    node = OverflowListener()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()