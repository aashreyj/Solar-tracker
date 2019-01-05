from datetime import datetime
from dateutil.tz import tzutc
import ephem
import time
import serial

#ser1=serial.Serial('',9600) #Enter arduino port
#ser2=serial.Serial('',9600) #Enter arduino port

while True:
    utc = datetime.now(tzutc())

    data=ephem.Observer()
    
    data.lon='87.28854'
    data.lat='23.54799'
    data.elevation=84
    pi=3.141593
    
    data.date=str(utc)
    values=ephem.Sun(data)

    a=float(repr(values.alt)) 
    al_servo=(a*180)/pi
    if(al_servo<=0):
        al_servo=0

    c=float(repr(values.az))
    d=(c*180)/pi
    if(d<90 and d>270) or al_servo<0:
        azi_servo=0
    else:
        azi_servo=(d-90)

    print("Altitude (upwards from Horizon) = %d" %int(al_servo))
    print("Azimuth (clock-wise from East) = %d\n" %int(azi_servo))

    #ser1.write(al_servo.encode())
    #ser2.write(azi_servo.encode())

    time.sleep(10)

