All model files cloned from https://github.com/alansrobotlab/inmoov_ros/tree/master/inmoov_description



Repository for simple simulation of InMoov robot within ROS. Visualization with RViz.

Steps:

1. Run 'roscore' in terminal

2. Open new terminal tab and run 'roslaunch inmoov_description display.launch' or 'roslaunch inmoov_description display_nogui.launch'


Robot can be controlled by publishing joint states appropriately. Example publisher moving one arm up and down can be found in move_arm_example.py. To run it, make sure it is an executable (run 'sudo chmod +x move_arm_example.py') and run 'rosrun inmoov_description move_arm_example.py'. 
