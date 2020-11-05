#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def subscriber_callback(data):
    # Check if the base scan is getting any close returns
    close_to_something = False
    for i in data.ranges:
        if i < 1:
            close_to_something = True
            break

    # Create a Twist message to send as a movement command
    move_command = Twist()

    # Turn in place if close to an object
    if close_to_something:
        rospy.loginfo(rospy.get_caller_id() + " turning!")
        move_command.angular.z = 0.5
    # Otherwise move forward
    else:
        rospy.loginfo(rospy.get_caller_id() + " moving forward!")
        move_command.linear.x = 1

    # Publish the command using the publisher object
    pub.publish(move_command)
    return

def node_init():
    global pub

    # Advertise a new node named 'fetch_controller'
    rospy.init_node('fetch_controller')

    # Register 'fetch_controller' node as a subscriber node
    rospy.Subscriber('base_scan', LaserScan, subscriber_callback)

    # Register 'fetch_controller' node as a publisher node
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

    # Keep node running until node is exited
    rospy.spin()

if __name__=='__main__':
    node_init()
