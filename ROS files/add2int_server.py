#!/usr/bin/env python

from __future__ import print_function

from tutorial1.srv import add2int,add2intResponse
import rospy

def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return add2intResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', add2int, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()
 
if __name__ == "__main__":
    add_two_ints_server()