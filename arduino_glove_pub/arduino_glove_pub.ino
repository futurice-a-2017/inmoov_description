// Include the servo library to add servo-control functions:
// Include ROS libraries and message type

#include <ros.h>
#include <inmoov_description/angleArray.h>

// Create ROS node handle, message and publisher
ros::NodeHandle nh;
inmoov_description::angleArray angle_array;
ros::Publisher angle_pub("angles", &angle_array);

// Define the analog input pins to measure flex sensor positions:
const int indexpin = 0; 
const int middlepin = 1; 
const int ringpin = 2; 
//const int pinkypin = 0; 


void setup() 
{ 
  // Initialize ROS node and set publisher
  nh.initNode();
  nh.advertise(angle_pub);
} 


void loop() 
{ 
  // Initialize values
  int indexposition;
  int middleposition;
  int ringposition;
  //int pinkyposition;

  // Read the position of the flex sensor (0 to 1023):
  indexposition = analogRead(indexpin);
  middleposition = analogRead(middlepin);
  ringposition = analogRead(ringpin);
  //pinkyposition = analogRead(pinkypin);

  // Map values from range to another
  indexposition = map(indexposition, 590, 830, 0, 180);
  middleposition = map(middleposition, 650, 830, 0, 180);
  ringposition = map(ringposition, 590, 830, 0, 180);
  //pinkyposition = map(pinkyposition, 650, 880, 0, 180);
  // servoposition = constrain(servoposition, 0, 180);

  // Assign servo postion to message and publish it
  for (int i = 0; i < 53; i++) {
    // Right index finger
    if (i >=16  && i <= 18) {
      angle_array.angles[i] = float(indexposition);
    }
    // Right middle finger
    else if (i >=19  && i <= 21) {
      angle_array.angles[i] = float(middleposition);
    }
    // Right ring finger
    else if (i >=23  && i <= 25) {
      angle_array.angles[i] = float(ringposition);
    }
    // Others
    else {
      angle_array.angles[i] = 0;
    }
  }
  angle_pub.publish(&angle_array);
  nh.spinOnce();

  delay(20);  // wait 20ms
}
