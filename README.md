# autorob_tutorial 

This repo is for the AutoRob course ROS tutorial. It provides three basic ROS nodes:

1. simple_subscriber demonstrates how to subscribe to a topic
2. simple_publisher demonstrates how to pubish to a topic
3. fetch_controller puts the two together to move the fetch around

### To install:

1. Requires ROS, Fetch packages, and a catkin workspace
2. Clone this repo into your catkin workspace
3. Rebuild your catkin workspace

### To run:

```
$ roslaunch fetch_gazebo playground.launch

$ rosrun autorob_tutorial fetch_controller.py
```
