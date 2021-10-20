#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32

def myCallBack(data):
	rospy.loginfo(rospy.get_caller_id() + "  Receiving...  %s", data.data)


def listener():
	rospy.init_node('listener_node_1', anonymous=True)
	rospy.Subscriber('talker_topic_1', UInt32, myCallBack)
	rospy.spin()

if __name__ == '__main__':
	listener()