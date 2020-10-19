#!/usr/bin/python3

import rospy
from sensor_controller_pkg_msgs.msg import Joint
from geometry_msgs.msg import Point


def main():
    rospy.init_node("Node")
    joint = Joint()
    joint.point = [
        Point(x=1, y=2, z=3),
        Point(x=11, y=22, z=33)
    ]
    rospy.loginfo(str(joint.point))


if __name__ == "__main__":
    main()
