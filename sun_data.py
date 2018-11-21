import ephem
gatech=ephem.Observer()
gatech.lon='87.28856189999999'
gatech.lat='23.548013599999997'
gatech.elevation=84
gatech.date='2018/11/21 20:21:00'
v=ephem.Sun(gatech)
print('%s %s' %(v.alt,v.az))
