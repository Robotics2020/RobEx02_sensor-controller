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

#### Publisher Node

The [publisher node](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg/src/publisher_node/main.py) simulates a set of 6 sensors for encoder readings. Thus it sends periodically information about the position of 6 joints.

#### Subscriber Node

The [subscriber node](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg/src/subscriber_node/main.py) simulates a set of 6 controllers for the joints. It reads the information about the position of 6 joints and prints such readings to stdout.

### Messages

The information about the position of 6 joints is yielded by the [SensorArray](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/SensorArray.msg) message type.

#### SensorArray

The [SensorArray](https://github.com/Robotics2020/RobEx02_sensor-controller/tree/master/sensor_controller_pkg_msgs/msg/SensorArray.msg) message type consists in just an array of [geometry_msgs/Point](http://docs.ros.org/en/melodic/api/geometry_msgs/html/msg/Point.html): each point represents the position of a joint.

## Usage

* To run the whole program (thus both the nodes) just run `roslaunch sensor_controller_pkg sensor_controller.launch`
  * If you want to specify the frequency at which the joints' positions are read, run `roslaunch sensor_controller_pkg sensor_controller.launch rate:=<rate>`. The default value is 0.2 Hz (once every 5 seconds).
* To just run the publisher (encoders) run `rosrun sensor_controller_pkg publisher_node`
* To just run the subscriber (controllers) run `rosrun sensor_controller_pkg subscriber_node`
