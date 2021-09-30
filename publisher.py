#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def publishMethod():
	rospy.init_node(‘publisher_node’, anonymous=True)
	pub = rospy.Publisher(‘talker’, String, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		publishString = “This is published”
		# rospy.loginfo(“Data sent”)
		pub.publish(publishString)
		rate.sleep()

if __name__ == ‘__main__’:
	try:
		publishMethod()
	except rospy.ROSInterruptException:
		pass
