import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')

        self.even_publisher = self.create_publisher(
            Int32,
            'even_numbers',
            10
        )

        self.overflow_publisher = self.create_publisher(
            Int32,
            'overflow',
            10
        )

        self.number = 0

        self.timer = self.create_timer(
            0.1,
            self.publish_number
        )

        self.get_logger().info('The publisher has been started')

    def publish_number(self):
        if self.number >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.number
            self.overflow_publisher.publish(overflow_msg)

            self.get_logger().warning(f'Overflow! The sent message: {self.number}')
            self.number = 0
        
        msg = Int32()
        msg.data = self.number

        self.even_publisher.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.number += 2

def main():
    rclpy.init()
    node = EvenNumberPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()