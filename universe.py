SPEED_OF_LIGHT = 299792458.0
#speed of light (meter/second)

FEET_PER_METER = 3.28084
#feet

SECONDS_PER_YEAR = 365 * 24 * 60 * 60

MINUTES_PER_YEAR = SECONDS_PER_YEAR / 60

def meters_to_feet(meters):
  return FEET_PER_METER * meters
  
def feet_to_meters(feet):
  return feet / FEET_PER_METER
  
 
def distance(light_travel_time):
  """ calculates the distance to the sun
  :param light_travel_time: time in years
  :returns: the distance in meters
  """
  return SPEED_OF_LIGHT * light_travel_time * SECONDS_PER_YEAR
  
