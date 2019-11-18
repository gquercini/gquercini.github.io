import time
from datetime import datetime, timedelta
import certifi
import urllib
from random import choices
from random import randint
from random import random
from math import sin, cos, sqrt, atan2, radians


'''
Useful functions
Author: Gianluca Quercini
'''


'''
Returns a URL to connect over HTTPS
'''
def uo(args, **kwargs):
    return urllib.request.urlopen(args, cafile=certifi.where(), **kwargs)

'''
Generate a date between two dates
'''
def generate_date(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime("%d/%m/%Y", time.localtime(ptime))


'''
Normalize the input string.
'''
def normalize(s):
    s = s.strip()
    if len(s) == 0 or s == "\\N" or s.lower()=='null':
        s = "null"
    return s

def distance(lat1, lon1, lat2, lon2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(float(lat1))
    lon1 = radians(float(lon1))
    lat2 = radians(float(lat2))
    lon2 = radians(float(lon2))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance

def generate_trip_dates(nb_intervals):
    lower_bound = "1/1/2010 11:59 PM"
    upper_bound = "12/31/2018 11:59 PM"

    lower_bound_date = datetime.strptime(lower_bound, '%m/%d/%Y %I:%M %p')
    upper_bound_date = datetime.strptime(upper_bound, '%m/%d/%Y %I:%M %p') 

    trip_intervals = []
    for i in range(0, nb_intervals):
        trip_duration = randint(5, 31)
        departure_date = generate_date(lower_bound, upper_bound, '%m/%d/%Y %I:%M %p', random())
        return_date = datetime.strptime(departure_date, "%d/%m/%Y") + timedelta(days=trip_duration)
        trip_intervals.append((departure_date, datetime.strftime(return_date, "%d/%m/%Y")))
        lower_bound_date = return_date + timedelta(days=5)
        lower_bound = datetime.strftime(lower_bound_date, '%m/%d/%Y %I:%M %p')
        if lower_bound_date > upper_bound_date:
            break
    return trip_intervals



'''
Generates a time interval
'''
def generate_times(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

'''
Picks a list of n times from a given list.
'''
def pick_times(n):
    return sorted(choices([dt.strftime('%H:%M') for dt in 
       generate_times(datetime(2016, 9, 1, 6), datetime(2016, 9, 1, 11+12), 
       timedelta(minutes=15))], k = n))