import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/carnifex/ros2_ws/src/MakUgl/install/MakUgl'
