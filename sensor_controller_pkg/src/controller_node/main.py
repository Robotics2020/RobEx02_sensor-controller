#!/usr/bin/python3
import rospy
from sensor_controller_pkg_msgs.msg import SensorArray


def on_sensor_array_received(sensor_array: SensorArray):
    rospy.loginfo(''.join([
        f"\nPosition of {'Revolute' if chr(sensor.joint_type) is 'R' else 'Prismatic'} joint #{i + 1}:\n"
        f"{round(sensor.position, 4)}\n"
        f"with respect to axis {list(map(lambda c: round(c, 4), [sensor.axis.x, sensor.axis.y, sensor.axis.z]))}\n"
        f"------" for i, sensor in enumerate(sensor_array.sensors)
    ]))


def main():
    rospy.init_node("Controller")
    rospy.Subscriber(rospy.get_param("/sensor_controller_pkg/topic_name"), SensorArray, on_sensor_array_received)
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
