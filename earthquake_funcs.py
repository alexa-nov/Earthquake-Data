from urllib.request import *
from json import *
from datetime import *
from operator import *
from math import *

def get_json(url):
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
    
class Earthquake:
   """ A class to represent an earthquake.
   Attributes:
       mag - a float
       longitude - a float
       latitude - a float
       time - an int
       place - a string"""
   def __init__ (self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = float(mag)
      self.longitude = float(longitude)
      self.latitude = float(latitude)
      self.time = int(time)

   def __eq__(self, other):
      return isclose(self.mag, other.mag) and isclose(self.longitude, other.longitude) and isclose(self.latitude, other.latitude) and self.time == other.time and self.place == other.place

   def __str__(self):
      return "(%.2f) %40s at %s (%.3f, %.3f)" %(self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude)
    
def read_quakes_from_file(filename):
   file = open(filename, "r")
   quakes = []
   quakes_str = ''
   for line in file:
      attr = line.split()
      quakes.append(Earthquake(' '.join(attr[4:]), attr[0], attr[1], attr[2], attr[3]))
   file.close()
   return quakes

def filter_by_mag(quakes, low, high):
   filtered = []
   for quake in quakes:
      if quake.mag >= low and quake.mag <= high:
         filtered.append(quake)
   return filtered
     
def filter_by_place(quakes, word):   
   filtered = []
   for quake in quakes:
      if word in quake.place:
          filtered.append(quake)
      elif word.lower() in quake.place.lower():
         filtered.append(quake)
      elif word.upper() in quake.place.upper():
         filtered.append(quake)
   return filtered

def sort_by_mag(quakes):
   sort_mag = []
   quakes.sort(key=attrgetter('mag'), reverse = True)
   for quake in quakes:
      sort_mag.append(quake)
   return sort_mag

def sort_by_time(quakes):
   sort_time = []
   quakes.sort(key=attrgetter('time'), reverse = True)
   for quake in quakes:
      sort_time.append(quake)
   return sort_time

def sort_by_longitude(quakes):
   sort_longitude = []
   quakes.sort(key=attrgetter('longitude'))
   for quake in quakes:
      sort_longitude.append(quake)
   return sort_longitude

def sort_by_latitude(quakes):
   sort_latitude = []
   quakes.sort(key=attrgetter('latitude'))
   for quake in quakes:
      sort_latitude.append(quake)
   return sort_latitude

def quake_from_feature(feature):
   res = []
   for val in feature:
      place = feature['properties']['place']
      mag = feature['properties']['mag']
      longitude = feature['geometry']['coordinates'][0]
      latitude = feature['geometry']['coordinates'][1]
      time = feature['properties']['time'] // 1000
   res.append(Earthquake(place, mag, longitude, latitude, time))
   return join(res)

