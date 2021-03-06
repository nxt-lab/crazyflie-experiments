#!/usr/bin/env python

import rospy
import math
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Time

def roseGoal():
    rospy.init_node('roseGoal', anonymous=True)
    y_offset = float(rospy.get_param("~y", "0"))
    pubname = rospy.Publisher('goal', PoseStamped, queue_size=10) 
    pubtime = rospy.Publisher('time', Time, queue_size=10)
    inputpoints = numpy.linspace(0.0, 2*math.pi, num = 600, endpoint=True)
    coords = []
    radius = 0.35
    for radians in range(0,len(inputpoints)-1):
        x = (2 + math.cos(4*radians)) * math.cos(radians) * radius
        y = (2 + math.cos(4*radians)) * math.sin(radians) * radius
	z = 1
        coords.append((x,y,z))
    while(i<len(coords)-1):
        d = math.sqrt(((coords[i+1][0]-coords[i][0])**2)+((coords[i+1][1]-coords[i][1])**2))
        if (d <= 0.1):
            del coords[i]
            print(d)
            i+=1
    loop_rate = 30
    rate = rospy.Rate(loop_rate)
    pos = PoseStamped()
    j = 0       
    while not rospy.is_shutdown() and j != 500:
        pos.pose.position.x = 0
        pos.pose.position.y = y_offset
        pos.pose.position.z = 1
        j+=1
        pubtime.publish(pos.header.stamp)
        pubname.publish(pos)
        rate.sleep()
    while not rospy.is_shutdown():
        for i in range (0,len(coords)-1):
        pos.pose.position.x = coords[i][0]
        pos.pose.position.y = coords[i][1]+y_offset
        pos.pose.position.z = coords[i][2]
        pubtime.publish(pos.header.stamp)
        pubname.publish(pos)
        rate.sleep()

if __name__=="__main__":
    try:
        roseGoal()
    except rospy.ROSInterruptException:
        pass

'''
import numpy
import math

radius = 0.5
inputpoints = numpy.linspace(0.0, 2*math.pi, num = 600, endpoint=True)
coords = []
for radians in range(0,len(inputpoints)-1):
        x = (2 + math.cos(4*radians)) * math.cos(radians) * radius
        y = (2 + math.cos(4*radians)) * math.sin(radians) * radius
        z = 1
        coords.append((x,y,z))
i = 0
while(i<len(coords)-1):
        d = math.sqrt(((coords[i+1][0]-coords[i][0])**2)+((coords[i+1][1]-coords[i][1])**2))
        if (d <= 0.1):
                del coords[i]
                print(d)
        i+=1
print("length: ")
print(len(coords))
for i in range (0, len(coords)-1):
        print(coords[i])
'''
