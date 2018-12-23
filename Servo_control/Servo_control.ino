#include<Servo.h>
Servo al_servo;
Servo azi_servo;
void setup() 
{
  al_servo.attach(9);
  azi_servo.attach(13);
  al_servo.write(0);
  azi_servo.write(0);
  Serial.begin(9600);
}

void loop() 
{
  bool count=0;
  if(Serial.available() && count==0)
  {
    al_servo.write(Serial.read());
    count=1;
  } 
  else if(Serial.available() && count==1)
  {
    azi_servo.write(Serial.read());
    count=0;
  }
}
