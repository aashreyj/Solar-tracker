from datetime import datetime
from dateutil.tz import tzutc
import ephem
import time
import serial

#ser1=serial.Serial('',9600) #enter Arduino port
#ser2=serial.Serial('',9600) #enter Arduino port

while True:
    utc = datetime.now(tzutc()) #obtain time from utc zone

    data=ephem.Observer() #data object
    
    data.lon='87.28854' #longitude of observer
    data.lat='23.54799' #latitude of observer
    data.elevation=84 #elevation of observer
    pi=3.141593 #pi constant
    
    data.date=str(utc) #convert date to string
    values=ephem.Sun(data) #obtain data of the sun using values in data object

    a=float(repr(values.alt)) #actual altitude value
    al_servo=(a*180)/pi #value written to altitude servo
    if(al_servo<=0): #for sunset
        al_servo=0

    c=float(repr(values.az)) #actual azimuth value
    d=(c*180)/pi #value written to azimuth servo
    if(d<90 and d>270) or al_servo<0: #for sunset
        azi_servo=0
    else:
        azi_servo=(d-90)

    print("Altitude (upwards from Horizon) = %d" %int(al_servo)) #print altitude 
    print("Azimuth (clock-wise from East) = %d\n" %int(azi_servo)) #print azimuth

    #ser1.write(al_servo.encode()) #write value to arduino
    #ser2.write(azi_servo.encode())

    time.sleep(10)

