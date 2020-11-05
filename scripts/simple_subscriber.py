#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def subscriber_callback(data):
    rospy.loginfo(rospy.get_caller_id() + " node received laser scan message!")
    return

def node_init():
    # Advertise a new node named 'simple_subscriber'
    rospy.init_node('simple_subscriber')

    # Register 'simple_subscriber' node as a subscriber node
    # Parameters:
    #    'base_scan'       specifies that this node will subscribe to the 'base_scan' topic
    #    LaserScan         specifies that the topic's message type is sensor_msgs/LaserScan
    #    listener_callback specifies the callback function used when a 'base_scan' message is received
    rospy.Subscriber('base_scan', LaserScan, subscriber_callback)

    # Keep node running until node is exited
    rospy.spin()

if __name__=='__main__':
    node_init()
