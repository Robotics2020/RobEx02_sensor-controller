# RobEx02_sensor-controller

Implement a publisher that simulates a set of sensors for encoder readings (position of 6 joints) and a subscriber that simulates a set of controllers that prints such readings to stdout

## Packages

The project consists in two packages:

* [sensor_controller_pkg](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg) contains:
  * The actual executable files for both publisher and subscriber nodes in the [src](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg/src) subfolder.
  * A [.launch file](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg/launch/sensor_controller.launch) that wraps the execution of both the nodes.
* [sensor_controller_pkg_msgs](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs) contains the definition of the [SensorArray](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/SensorArray.msg) message type

### Nodes

As said, the project is an implementation of two nodes in the publisher/subscriber setting.

#### Encoders Node

The [encoders node](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg/src/encoders_node/main.py) simulates a set of 6 sensors for encoder readings, implementing the publisher. Thus it sends periodically information about the position of 6 joints.

#### Controller Node

The [controller node](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg/src/controller_node/main.py) simulates a set of 6 controllers for the joints, implementing the subscriber. It reads the information about the position of 6 joints and prints such readings to stdout.

### Messages

The information about the position of 6 joints is yielded by the [SensorArray](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/SensorArray.msg) message type.

#### SensorArray

The [SensorArray](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/SensorArray.msg) message type consists in just an array of [Sensor](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/Sensor.msg), representing the 6 sensors.

#### Sensor

The [Sensor](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/Sensor.msg) message type represents a sensor for a joint. It consists in 3 fields:

* joint_type: a character that describes the type of the joint:
  * character 'R' stands for Revolute joint.
  * character 'P' stands for Prismatic joint.
* axis: a [Point](http://docs.ros.org/en/melodic/api/geometry_msgs/html/msg/Point.html) that contains the unit vector representing the direction of the joint axis.
* position: a real number representing the absolute position of the joint, relative to its axis.
  * for revolute joints, the position is in range ]0, 2*pi[.
  * for prismatic joints, the position is in range ]0, 1[.
    * this has to be intended as relative to the joint limits.

## Usage

* To run the whole program (thus both the nodes) just run `roslaunch sensor_controller_pkg sensor_controller.launch`.
  * If you want to specify the frequency in Hz at which the joints' positions are read, run `roslaunch sensor_controller_pkg sensor_controller.launch rate:=<rate>`.
    * The default value is 0.2 Hz (once every 5 seconds).
  * If you wanto to specify the type of the 6 joints, run `roslaunch sensor_controller_pkg sensor_controller.launch joint_types:=<joint_types>`. The `joint_types` parameter is a sequence of 'R' and 'P' characters, depending on whether the joints are revolute or prismatic.
    * For example, `joint_types:=RRRPPP` specifies 3 revolute joints and 3 prismatic joints
    * The default value is `RRRRRR` (thus 6 revolute joints)
* To just run the publisher (encoders) run `rosrun sensor_controller_pkg encoders_node`.
* To just run the subscriber (controller) run `rosrun sensor_controller_pkg controller_node`.
