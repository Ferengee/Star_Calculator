#star_calculator
from universe import SPEED_OF_LIGHT, SECONDS_PER_YEAR, distance
import sys        # to be able to exit the script

# Lets make a dictionary of stars containing star and light travel time to the star (light years)
stars= {
  "sun": 0.000016,
  "proxima centauri": 4.242,
  "alpha centauri" : 4.365,
  "barnard star" : 5.96,
  "WISE 1049-5319" : 6.52,
  "wolf 359" : 7.7825,
  "lalande 21185" : 8.2905,
  "sirius" : 8.5828,
  "luyten 726-8" : 8.7280,
  "ross 154" : 9.6813,
  "ross 248" : 10.322,
  
  
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
    if star in stars:
      break
    if i == 5:  						
      print "Try again later!"  			                        #say bye
      sys.exit()						                                         
      #end of program

else:					          # if star is in stars
  pass					        # just continue
ltts = stars[star]
  
values = (
  SPEED_OF_LIGHT, 
  SECONDS_PER_YEAR, 
  SECONDS_PER_YEAR / 60, 
  SPEED_OF_LIGHT * SECONDS_PER_YEAR, 
  ltts, 
  star, 
  distance(ltts)
)
message  = """The speed of light is %r meters/second.
There are %r seconds in a year.
Which equals %r minutes per year.
Light travels %r meters per year.

Can you believe that?

It takes light ~%r light-years to get from Earth to %r
Which is %r meter away from the earth""" % values
print(message)
