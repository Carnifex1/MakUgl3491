import time
import rclpy
from rclpy.node import Node


class TimePrinterNode(Node):
    def __init__(self):
        super().__init__('time_printer_node')
        self.timer = self.create_timer(5.0, self.timer_callback)

    def timer_callback(self):
        current_time = time.strftime("%H:%M:%S", time.localtime())
        self.get_logger().info(f'Current time: {current_time}')

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinterNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()