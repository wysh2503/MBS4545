#!/usr/bin/env python

import rospy
from std_msgs.msg import Int32

def talker():
    rospy.init_node('talker_node_2', anonymous=True)
    pub = rospy.Publisher('counter', Int32, queue_size=10)
    rate = rospy.Rate(1)
    count = 0
    while not rospy.is_shutdown():
        rospy.loginfo("Data sent")
        pub.publish(count)
        count += 5
        rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass