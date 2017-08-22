#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

# ROS Puhblisher function
def talker():
    # Create publisher
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    # Initialize new ROS node 
    rospy.init_node('test')
    # Create timer (Hz)
    rate = rospy.Rate(2)

    new_position = 0
    # Going up(1) or down(2)
    direction = 1
    # Loop as long as roscore is running
    while not rospy.is_shutdown():
        # Set new direction if limits are reached
        if direction == 1 and new_position > 3.14:
            direction = 0
        elif direction == 0 and new_position < 0:
            direction = 1
        # Set new position depending on current direction
        if direction == 1:
            new_position += 0.1
        elif direction == 0:
            new_position -= 0.1


        # Create new joint state message
        new_states = JointState()
        # Set header and timestamp
        new_states.header = Header()
        new_states.header.stamp = rospy.Time.now()

        # Set joint names
        new_states.name = ['waist_rotate', 'waist_lean', 'head_tilt', 'head_updown', 
                            'head_leftright', 'jaw', 'eyes_updown', 'eye_leftright', 
                            'left_eye_leftright', 'right_shoulder_up', 'right_bicep_rotate', 
                            'right_bicep', 'right_shoulder_side', 'right_thumb1', 'right_thumb', 
                            'right_thumb3', 'right_index1', 'right_index', 'right_index3', 
                            'right_middle1', 'right_middle', 'right_middle3', 'right_ring1', 
                            'right_ring', 'right_ring3', 'right_ring4', 'right_pinky1', 
                            'right_pinky', 'right_pinky3', 'right_pinky4', 'right_hand', 
                            'left_shoulder_up', 'left_bicep_rotate', 'left_bicep', 
                            'left_shoulder_side', 'left_thumb1', 'left_thumb', 'left_thumb3', 
                            'left_index1', 'left_index', 'left_index3', 'left_middle1', 
                            'left_middle', 'left_middle3', 'left_ring1', 'left_ring', 
                            'left_ring3', 'left_ring4', 'left_pinky1', 'left_pinky', 
                            'left_pinky3', 'left_pinky4', 'left_hand']

        # Set joint positions
        new_states.position = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, new_position, 
                                0.0, 0.985, 0.0, 0.0, 0.0, 0.0, 
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.985, 
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 
                                0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        
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