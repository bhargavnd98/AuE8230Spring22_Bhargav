#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
PI =3.1415926535897

def openLoop():
	rospy.init_node('robotMoveOpenLoop', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	vel = Twist()
	
	#Taking User Input
	print("Lets draw a square")
	speed = float(input("Input the speed: linear: "))
	angularSpeed = float(input("Input the speed: Angular: "))
	distance = float(input("Input the distance: "))
	isForward = float(input("Forward?: "))
	angle = float(input("Rotation Angle"))
	clockwise = float(input(" Clockwise? "))
	
	
	angularTurtle = angularSpeed*2*PI/360
	rotationAngle = angle*2*PI/360
	
	
	
	vel.linear.y = 0
	vel.linear.z = 0
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0
	i = 0
	while (i<4):
		
		t0 = rospy.Time.now().to_sec()
		current_distance = 0
		
		while(current_distance<distance):
			if(isForward):
				vel.linear.x = abs(speed)
			else:
				vel.linear.x = -abs(speed)

			
				
			pub.publish(vel)
			t1 = rospy.Time.now().to_sec()
			current_distance = speed*(t1-t0)
		vel.linear.x = 0
		pub.publish(vel)
		
		if(clockwise):
			vel.angular.z = -abs(angularTurtle)
		else:
			vel.angular.z = abs(angularTurtle)
		
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		
		t02 = rospy.Time.now().to_sec()

		current_angle = 0
		while(current_angle<rotationAngle):
			pub.publish(vel)
			t12 = rospy.Time.now().to_sec()
			current_angle = angularTurtle*(t12-t02)
	
		
		vel.angular.z = 0
		pub.publish(vel)
		#rospy.spin()
		i=i+1

if __name__ == '__main__':
	try:
		openLoop()
	except rospy.ROSInterruptException: pass




		
			
