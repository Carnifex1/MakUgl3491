import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):

    def __init__(self):
        super().__init__('talker')
        self.publisher_ = self.create_publisher(String, 'my_chat_topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Talker node has been started.')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, Now it is {self.get_clock().now().to_msg().sec}'
        self.publisher_.publish(msg)
        self.get_logger().info(msg.data)

def main():
    rclpy.init()
    node = Talker()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()