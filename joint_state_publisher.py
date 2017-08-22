#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import config
import threading
from listenerThread import listenerThread


# ROS Publisher function
def talker():
    # Create publisher
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    # Initialize new ROS node 
    rospy.init_node('joint_state_publisher')
    # Create timer (Hz)
    rate = rospy.Rate(10)

    # Create and start a thread for listener
    listener = listenerThread()
    listener.start()

    # Loop as long as ROS is running
    while not rospy.is_shutdown():
        # Create new joint state message
        new_states = JointState()
        # Set header and timestamp
        new_states.header = Header()
        new_states.header.stamp = rospy.Time.now()

        # Set joint names
        new_states.name = [ 'waist_rotate', 'waist_lean', 'head_tilt', 'head_updown', 
                            'head_leftright', 'jaw', 'eyes_updown', 'eye_leftright', 
                            'left_eye_leftright', 'right_shoulder_up', 'right_bicep_rotate', 'right_bicep', 
                            'right_shoulder_side', 'right_thumb1', 'right_thumb', 'right_thumb3', 
                            'right_index1', 'right_index', 'right_index3', 'right_middle1', 
                            'right_middle', 'right_middle3', 'right_ring1', 'right_ring', 
                            'right_ring3', 'right_ring4', 'right_pinky1', 'right_pinky', 
                            'right_pinky3', 'right_pinky4', 'right_hand', 'left_shoulder_up', 
                            'left_bicep_rotate', 'left_bicep', 'left_shoulder_side', 'left_thumb1', 
                            'left_thumb', 'left_thumb3', 'left_index1', 'left_index', 
                            'left_index3', 'left_middle1', 'left_middle', 'left_middle3', 
                            'left_ring1', 'left_ring', 'left_ring3', 'left_ring4', 
                            'left_pinky1', 'left_pinky', 'left_pinky3', 'left_pinky4', 
                            'left_hand']

        # Set joint positions
        new_states.position = config.angles
        
        # Set velocity and effort
        new_states.velocity = []
        new_states.effort = []

        # Publish the message
        pub.publish(new_states)

        # Sleep timer
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass