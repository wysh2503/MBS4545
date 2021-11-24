#! /usr/bin/env python

# Publisher and Subscriber in same node

import rospy
from sensor_msgs.msg import LaserScan 
from geometry_msgs.msg import Twist

disToObstacle = 1

def callback(msg): 
  rospy.loginfo(rospy.get_caller_id() + " The distance to obstacle is -  %s",msg.ranges[300])

#If the distance to an obstacle in front of the robot is larger than 1 meter, the robot will keep moving forward
  if msg.ranges[300] > disToObstacle:
      move.linear.x = 0.5
      move.angular.z = 0.0

#If the distance to an obstacle in front of the robot is less than 1 meter, the robot will turn left
  if msg.ranges[300] <= disToObstacle: 
      move.linear.x = 0.
      move.angular.z = 0.5

  pub.publish(move)
  

rospy.init_node('sub_node')
sub = rospy.Subscriber('/scan', LaserScan, callback) #subscribe to the laser topic
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=2)
rate = rospy.Rate(2)
move = Twist()


rospy.spin()