#!/usr/bin/env python

import rospy
from std_msgs.msg import UInt32

def talker():
	rospy.init_node('talker_node_1', anonymous=True)
	pub = rospy.Publisher('talker_topic_1', UInt32, queue_size=10)
	rate = rospy.Rate(1)

	while not rospy.is_shutdown():
		msg = 12345
		rospy.loginfo("Data sent")
		pub.publish(msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass