Repository for simple simulation of InMoov robot within ROS. Visualization with RViz.

Steps:
For all steps, make sure you are installing matching version depending on your OS and ROS versions. Tested to work with Ubuntu 16 (Xenial) and ROS Kinetic.

1. Install ROS (full install): http://wiki.ros.org/indigo/Installation/Ubuntu

2. Setup Catkin workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace

3. Git-clone this repository into your ~/catkin_ws/src/ (or wherever your workspace is)

4. Navigate to ~/catkin_ws/ and run 'catkin_make' and 'source devel/setup.bash'

5. Run 'roscore' in terminal

6. Open new terminal tab (ctrl+shift+T) and run 'roslaunch inmoov_description display.launch' or 'roslaunch inmoov_description display_nogui.launch'


Robot can be controlled by publishing joint states appropriately. Example publisher moving one arm up and down can be found in move_arm_example.py. To run it, make sure it is an executable (run 'sudo chmod +x move_arm_example.py') and run 'rosrun inmoov_description move_arm_example.py'. 


Random tips:

- To see the control message, run display.launch according to step 7, open new terminal tab and run 'rostopic echo /joint_states'.

- To disable joint coordinate arrows in RViz for nicer visuals, untick TF in the left-side menu.
