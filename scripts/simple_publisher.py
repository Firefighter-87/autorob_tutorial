#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def node_init():
    # Advertise a new node named 'simple_publisher'
    rospy.init_node('simple_publisher')

    # Register 'simple_publisher' node as a publisher node
    # Parameters:
    #    'time_update' specifies that this node will publish to the 'time_update' topic
    #    String        specifies that the topic's message type is std_msgs/String
    #    queue_size=10 specifies maximum queue size before messages are dropped
    pub = rospy.Publisher('time_update', String, queue_size=10)

    # Publish once per second
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        message_string = "Uptime is %s" % rospy.get_time()
        pub.publish(message_string);
        rate.sleep()

if __name__=='__main__':
    node_init()
