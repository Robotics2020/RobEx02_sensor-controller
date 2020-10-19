#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
from sensor_controller_pkg_msgs.msg import SensorArray

import sys
from random import random


N = 6  # Number of joints


def main(hz: float):
    rospy.init_node("Publisher")
    pub = rospy.Publisher("sensors", SensorArray, queue_size=1)
    rate = rospy.Rate(hz)

    sensors = SensorArray()

    while not rospy.is_shutdown():
        sensors.points = [Point(x=random(), y=random(), z=random()) for _ in range(N)]
        pub.publish(sensors)
        rate.sleep()


if __name__ == "__main__":
    try:
        hz = float(sys.argv[1])
        main(hz)
    except rospy.ROSInterruptException:
        pass
