#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Point
from sensor_controller_pkg_msgs.msg import Sensor, SensorArray

import sys
from random import uniform
from math import pi
from numpy.random import rand
from numpy.linalg import norm


N = 6                       # Number of joints
JOINT_TYPES = {'P', 'R'}    # Joints can be Prismatic ('P') or Revolute ('R')


def random_unit_vector(d: int):
    v = rand(d)
    v /= norm(v)
    unravel = lambda *args: args
    return unravel(*v)


def init_sensor_array(joint_types: str) -> SensorArray:
    return SensorArray(sensors=[Sensor(
        joint_type=ord(joint_types[i]),
        axis=[Point(x=x, y=y, z=z) for x, y, z in [random_unit_vector(3)]][0],
        position=0.0
    ) for i in range(N)])


def main(joint_types: str, hz: float):
    rospy.init_node("Encoders")
    pub = rospy.Publisher("sensors", SensorArray, queue_size=1)
    rate = rospy.Rate(hz)
    sensor_array = init_sensor_array(joint_types)
    while not rospy.is_shutdown():
        for sensor in sensor_array.sensors:
            sensor.position = uniform(0, 2*pi) if chr(sensor.joint_type) is 'R' else rand()
        pub.publish(sensor_array)
        rate.sleep()


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2 + 3:
            raise Exception("Bad parameters. Specify joint types and reading rate.")
        
        joint_types = str(sys.argv[1])
        if set(joint_types).union(JOINT_TYPES) != JOINT_TYPES:
            raise Exception("Bad joint types. Use only 'R' and 'P'.")
        if len(joint_types) != N:
            raise Exception("The number of joints must be 6.")
        
        hz = float(sys.argv[2])
        
        main(joint_types, hz)
    except rospy.ROSInterruptException:
        pass
