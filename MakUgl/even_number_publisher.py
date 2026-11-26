import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')

        self.declare_parameter('frequency', 8.0)
        self.declare_parameter('overflow_threshold', 80)
        self.declare_parameter('overflow_topic', '/overflow')
        self.declare_parameter('even_topic', '/even_numbers')

        self.frequency = self.get_parameter('frequency').value
        self.overflow_threshold = self.get_parameter('overflow_threshold').value
        self.overflow_topic = self.get_parameter('overflow_topic').value
        self.even_topic = self.get_parameter('even_topic').value

        if self.frequency <= 0:
            self.get_logger().error('Frequency must be greater than 0. Setting to default value of 8.0 Hz.')
            self.frequency = 8.0
        if self.overflow_threshold <= 0:
            self.get_logger().error('Overflow threshold must be greater than 0. Setting to default value of 80.')
            self.overflow_threshold = 80
        
        self.even_publisher = self.create_publisher(
            Int32,
            self.even_topic,
            10
        )

        self.overflow_publisher = self.create_publisher(
            Int32,
            self.overflow_topic,
            10
        )

        self.number = 0
        timer_period = 1.0 / self.frequency

        self.timer = self.create_timer(
            timer_period,
            self.publish_number
        )

        self.get_logger().info(f'The publisher started: {self.frequency} Hz, overflow threshold: {self.overflow_threshold}, even topic: {self.even_topic}, overflow topic: {self.overflow_topic}')

    def publish_number(self):
        if self.number >= self.overflow_threshold:
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