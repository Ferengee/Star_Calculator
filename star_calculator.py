#star_calculator

import sys        # to be able to exit the script

# Lets make a dictionary of stars containing star and light travel time to the star (light years)
stars= {
  "sun": 0.000016,
  "proxima centauri": 4.242,
  "alpha centauri" : 4.365,
  "barnard star" : 5.96,
}


star = raw_input("Name a Star: ") 
star = star.lower()    #to get rid of capital letters

if star not in stars:    					                                      
    #check if we know the star
  i=0
  while i <= 5:							                                          
      #let's give user 5 tries
    i+=1
    print "I don't know this one. Maybe you misspelled it.  Try again!"	      #print info
    star = raw_input("Tell me a Star: ") 			                        
    #ask for new input
    star = star.lower()								
    if i == 5:  						
      print "Try again later!"  			                        #say bye
      sys.exit()						                                         
      #end of program

else:					          # if star is in stars
  pass					        # just continue
      

sol = 299792458.0
#speed of light (meter/second)

meter = 3.28084
#feet

#Time
#---------------------
year = 365.0
second = 60.0				#only year and second are used more times

mid = 24.0 * 60.0		
#minutes in day

sid = 24.0 * 60.0 * second
#seconds in day

yis = year * sid
#year in seconds

yim = year * mid
#year in minutes

#Distance
#----------------------
dlpy = sol * yis
#distance of light per year (meters)

ltts = stars[star]
#light's time to sun (years)

dts = sol * ltts * second
#distance to sun (meters)

print "The speed of light is %r meters/second." % sol
print "There are %r seconds in a year." % yis
print "Which equals %r minutes per year." % yim
print "Light travels %r meters per year." % dlpy
print ""
print "Can you belive that?"
print ""

print "It takes light %r light-years to get from the %r to Earth" % (ltts, star)     #I removed "only"
# print "That means light travels %r meters in %r minutes" % (dts, ltts)      #didn't finish the counting, have to go
