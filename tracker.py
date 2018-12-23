from datetime import datetime
from dateutil.tz import tzutc
import ephem
import time
import serial

ser1=serial.Serial('',9600)
ser2=serial.Serial('',9600)

while True:
    utc = datetime.now(tzutc())

    data=ephem.Observer()
    
    data.lon='75.3172596'
    data.lat='19.864609599999998'
    data.elevation=567
    
    data.date=str(utc)
    values=ephem.Sun(data)

    a=float(repr(values.alt)) 
    pi=3.141593
    al_servo=(a*180)/pi
    if(al_servo<0):
        al_servo=0

    c=float(repr(values.az))
    d=(c*180)/pi
    if(d<90 and d>270):
        azi_servo=0
    else:
        azi_servo=(d-90)

    print("Altitude (upwards from horizon) = %d" %int(al_servo))
    print("Azimuth (clock-wise from North) = %d" %int(azi_servo))
    print(" ")
    ser1.write(al_servo)
    ser2.write(azi_servo)
    time.sleep(5)

