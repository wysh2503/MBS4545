#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
	rospy.init_node('talker_node', anonymous=True)
	pub = rospy.Publisher('talker_topic', String, queue_size=10)
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		msg = "This is published"
		rospy.loginfo("Data sent")
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass