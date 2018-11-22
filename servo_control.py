from datetime import datetime
from dateutil.tz import tzutc
import ephem
import time
while True:
    utc = datetime.now(tzutc())

    data=ephem.Observer()
    data.lon='87.28856189999999'
    data.lat='23.548013599999997'
    data.elevation=84
    data.date=str(utc)
    values=ephem.Sun(data)
    pi=3.141593
    
    a=float(repr(values.alt)) 
    al_servo=(a*180)/pi
    if(al_servo<0):
        al_servo=0

    c=float(repr(values.az))
    d=(c*180)/pi
    azi_servo1=0
    azi_servo2=0

    if(al_servo<=0): 
        azi_servo1=0; 
        azi_servo2=0
    elif(d>=90 and d<=270): 
        azi_servo2=(d-90)
    elif(d>270 and d<360): 
        azi_servo1=(d-270)
    else:                   
        azi_servo1=(d+90)
    print("Altitude servo reading %d "%al_servo)
    print("North servo reading %d "%azi_servo1)
    print("South servo reading %d "%azi_servo2)
    print(" ")
    time.sleep(5)

