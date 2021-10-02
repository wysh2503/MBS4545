#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def subscriberCallBack():
	rospy.loginfo(rospy.get_caller_id() + “  Receiving….  %s”, data.data)


def listener():
	rospy.init_node(‘subscriber_node’, anonymous=True)
	rospy.Subscriber(‘talker’, String, subscriberCallBack)
	rospy.spin()

if __name__ == ‘__main__’:
	listener()
