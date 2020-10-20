#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
from sensor_controller_pkg_msgs.msg import Sensor, SensorArray

import sys
from random import uniform
from math import pi
from numpy.random import rand
from numpy.linalg import norm


N = 6  # Number of joints


def random_unit_vector(d: int):
    v = rand(d)
    v /= norm(v)
    unravel = lambda *args: args
    return unravel(*v)


def init_sensor_array() -> SensorArray:
    sensor_array = SensorArray()
    for _ in range(N):
        x, y, z = random_unit_vector(3)
        sensor_array.sensors.append(Sensor(angle=0.0, axis=Point(x=x, y=y, z=z)))
    return sensor_array


def main(hz: float):
    rospy.init_node("Publisher")
    pub = rospy.Publisher("sensors", SensorArray, queue_size=1)
    rate = rospy.Rate(hz)
    sensor_array = init_sensor_array()
    while not rospy.is_shutdown():
        for sensor in sensor_array.sensors:
            sensor.angle = uniform(0, 2*pi)
        pub.publish(sensor_array)
        rate.sleep()


if __name__ == "__main__":
    try:
        hz = float(sys.argv[1])
        main(hz)
    except rospy.ROSInterruptException:
        pass
