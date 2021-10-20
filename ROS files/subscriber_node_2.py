#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def myCallBack(data):
	rospy.loginfo(rospy.get_caller_id() + "  Receiving...  %s", data.data)


def listener():
	rospy.init_node('listener_node_2', anonymous=True)
	rospy.Subscriber('counter', Int32, myCallBack)
	rospy.spin()

if __name__ == '__main__':
	listener()