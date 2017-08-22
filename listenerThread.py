import rospy
import threading
import math
import config
from inmoov_description.msg import angleArray

# Threading class for listening to a ROS topic
class listenerThread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		# Create a subscriber
		rospy.Subscriber('angles', angleArray, self.callback)

	def run(self):
		# Start listening
		rospy.spin()

	# Handling a new message when received
	# Scaling to fit the simulation is done here (deg->rad)
	def callback(self, data):
		config.angles = list(data.angles)

		# Fix finger scaling for 3 jointed fingers
		for i in range(13, 22):
			config.angles[i] = config.angles[i] * math.pi / (180 * 3)
		# Fix finger scaling for 4 jointed fingers
		for i in range(23, 26):
			config.angles[i] = config.angles[i] * math.pi / (180 * 3)

		# Set elbow to more presentable angle 
		config.angles[11] = 0.985
		config.angles[33] = 0.985 