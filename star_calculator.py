#star_calculator

sol = 299792458.0 
#speed of light (meter/second)

meter = 3.28084 
#feet

#Time 
#---------------------
year = 365.0
#days

hour = 24.0
#hours in a day

minute = 60.0
#seconds

second = 60.0 
#seconds in a minute

mid = hour * minute
#minutes in day

sid = hour * minute * second
#seconds in day

yis = year * sid
#year in seconds

yim = year * mid
#year in minutes

#Distance
#----------------------
dlpy = sol * yis
#distance of light per year (meters)

ltts = 8.3
#light's time to sun (minutes)

dts = sol * ltts * second
#distance to sun (meters)

print "The speed of light is %r meters/second." % sol
print "There are %r seconds in a year." % yis
print "Which equals %r minutes per year." % yim
print "Light travels %r meters per year." % dlpy
print "Can you belive that?"
print "It takes light only %r minutes to get from the sun to earth" % ltts
print "That means light travels %r meters in %r minutes" % (dts, ltts)

