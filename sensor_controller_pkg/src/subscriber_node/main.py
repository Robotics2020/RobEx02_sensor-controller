#!/usr/bin/python3
import rospy
from sensor_controller_pkg_msgs.msg import SensorArray


def on_sensor_array_received(sensor_array: SensorArray):
    rospy.loginfo(''.join([
        f"\nPosition of joint #{i + 1}:\n"
        f"{round(sensor.angle, 4)} rad.\n"
        f"with respect to axis {list(map(lambda c: round(c, 4), [sensor.axis.x, sensor.axis.y, sensor.axis.z]))}\n"
        f"------" for i, sensor in enumerate(sensor_array.sensors)
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
