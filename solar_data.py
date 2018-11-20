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
print('%s %s' %(values.alt,values.az))
