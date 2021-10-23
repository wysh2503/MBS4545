// This Arduino code publishes the distance measured
// by HC-SR04 ultrasonic sensor to the topic "distance"
// 
#include <ros.h>
#include <std_msgs/Int16.h>

#define trigPin 6
#define echoPin 7

ros::NodeHandle nh;

std_msgs::Int16 int_msg;
ros::Publisher arduino_HCSR04("distance", &int_msg);

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  nh.initNode();
  nh.advertise(arduino_HCSR04); 
}
void loop() {
  long duration;
  int distance;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW); 

  duration = pulseIn(echoPin, HIGH); 
  distance = (duration/2) *0.034;
  int_msg.data = distance;

  arduino_HCSR04.publish(&int_msg);
  nh.spinOnce();
   
  delay(500);
}
