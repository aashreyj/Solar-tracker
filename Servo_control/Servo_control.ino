#include<Servo.h>
Servo al_servo;
Servo azi_servo;
bool count=0;

void setup() 
{
  al_servo.attach(9); //attach altitude servo to digital pin 9
  azi_servo.attach(13); //attach azimuth servo to digital pin 13
  al_servo.write(0); //init
  azi_servo.write(90); //init
  Serial.begin(9600); //begin serial comm
}

void loop() 
{
  if(Serial.available() && count==0) //if data is available, control servos
  {
    al_servo.write(int(Serial.read()));
    count=1;
  } 
  else if(Serial.available() && count==1)
  {
    azi_servo.write(int(Serial.read()));
    count=0;
  }
}
