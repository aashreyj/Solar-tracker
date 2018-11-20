from datetime import datetime
from dateutil.tz import tzutc
import ephem

utc = datetime.now(tzutc())

data=ephem.Observer()
data.lon='87.28856189999999'
data.lat='23.548013599999997'
data.elevation=84
data.date=str(utc)
values=ephem.Sun(data)

a=float(repr(values.alt)) 
pi=3.141593
b=(a*180)/pi
if(b<0):
    b=0
c=float(repr(values.az)) 
d=(c*180)/pi
    
print("Altitude = %d" %int(b))
print("Azimuth = %d" %int(d))

