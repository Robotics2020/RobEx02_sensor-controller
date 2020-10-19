#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
from sensor_controller_pkg_msgs.msg import SensorArray

from random import random


N = 6  # Number of joints


def main():
    rospy.init_node("Publisher")
    pub = rospy.Publisher("sensors", SensorArray, queue_size=1)
    rate = rospy.Rate(1/10)

    sensors = SensorArray()

    while not rospy.is_shutdown():
        sensors.points = [Point(x=random(), y=random(), z=random()) for _ in range(N)]
        pub.publish(sensors)
        rate.sleep()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
