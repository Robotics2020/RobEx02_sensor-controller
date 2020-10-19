#!/usr/bin/python3
import rospy
from sensor_controller_pkg_msgs.msg import SensorArray


def on_sensor_array_received(sensor_array: SensorArray):
    rospy.loginfo(''.join([
        f"\nPosition of joint #{i + 1}:\n{point}\n------" for i, point in enumerate(sensor_array.points)
    ]))


def main():
    rospy.init_node("Subscriber")
    rospy.Subscriber("sensors", SensorArray, on_sensor_array_received)
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
