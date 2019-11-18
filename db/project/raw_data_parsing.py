import csv
import random
from geopy.geocoders import Nominatim
from utils import normalize
from utils import uo
from time import sleep





'''
Functions to parse the raw data files.
Author: Gianluca Quercini
'''


'''
Parses the airport file (first argument) and generates a clean CSV file (second argument).
Returns a dictionary containing the identifiers of the airports.
'''
def parse_airports(airport_data_raw, airport_data_clean):
    airports = {}
    with open(airport_data_raw, 'r', encoding="utf-8") as csv_file_raw:
        csv_reader = csv.reader(csv_file_raw, delimiter=",", skipinitialspace=True)
        with open(airport_data_clean, mode='w', encoding="utf-8") as csv_file_clean:
            csv_writer = csv.writer(csv_file_clean, delimiter='\t')
            csv_writer.writerow(['airport_id', 'airport_name', 'city', 'country',
                                'airport_iata', 'airport_icao', 'latitude', 'longitude'])
            for line in csv_reader:
                
                if normalize(line[12]) == 'airport' :
                    airport_id = normalize(line[0])
                    name = normalize(line[1])
                    if "duplicate" in name.lower():
                        continue
                    city = normalize(line[2])
                    if city == "null":
                        continue
                    country = normalize(line[3])
                    iata = normalize(line[4])
                    icao = normalize(line[5])
                    latitude = normalize(line[6])
                    longitude = normalize(line[7])
                    airports[airport_id] = True
                    csv_writer.writerow([airport_id, name,  city, country, iata, icao, latitude, longitude])
    return airports
    

'''
Parses the airline file (first argument) 
and generates a clean CSV file (second argument).
Returns a dictionary containing the identifiers of the airlines.
'''
def parse_airlines(airline_data_raw, airline_data_clean):
    airlines ={}
    with open(airline_data_raw, 'r', encoding="utf-8") as csv_file_raw:
        csv_reader = csv.reader(csv_file_raw, delimiter=",", skipinitialspace=True)
        with open(airline_data_clean, mode='w', encoding="utf-8") as csv_file_clean:
            csv_writer = csv.writer(csv_file_clean, delimiter='\t')
            csv_writer.writerow(['airline_id', 'airline_name', 'country', 'airline_iata', 'airline_icao', 'alias'])
            for line in csv_reader:
                airline_id = normalize(line[0])
                name = normalize(line[1])
                country = normalize(line[6])
                if country == "null":
                    continue
                iata = normalize(line[3])
                icao = normalize(line[4])
                alias = normalize(line[2])
                if normalize(line[7]) == "Y":
                    airlines[airline_id] = True
                    csv_writer.writerow([airline_id, name, country, iata, icao, alias])
    return airlines

'''
Parses the raw  aircraft file (first argument)
and generates a clean CSV file (second argument).
Returns a dictionary containing the iata or icao code or the airlines.
'''
def parse_aircrafts(aircraft_data_raw, aircraft_data_clean):
    aircrafts = {}
    with open(aircraft_data_raw, 'r', encoding="utf-8") as csv_file_raw:
        csv_reader = csv.reader(csv_file_raw, delimiter=",", skipinitialspace=True)
        with open(aircraft_data_clean, mode='w', encoding="utf-8") as csv_file_clean:
            csv_writer = csv.writer(csv_file_clean, delimiter='\t')
            csv_writer.writerow(['aircraft_name', 'aircraft_iata', 'aircraft_icao'])
            for line in csv_reader:
                aircraft_name = normalize(line[0])
                aircraft_iata = normalize(line[1])
                aircraft_icao = normalize(line[2])
                if aircraft_iata == 'null' and aircraft_icao == 'null':
                    continue
                csv_writer.writerow([aircraft_name, aircraft_iata, aircraft_icao])
                if aircraft_iata != "null" :
                    aircrafts[aircraft_iata] = True
                else:
                    aircrafts[aircraft_icao] = True
            
    return aircrafts


'''
Parses the raw route file (first argument) and generates a clean CSV file (second argument).
The other arguments are (in the order): the dictionaries returned by the function parse_airports, parse_airlines and parse_aircrafts.
'''
def parse_routes(routes_data_raw, routes_data_clean, airports, airlines, aircrafts):
    with open(routes_data_raw, 'r', encoding='utf-8') as csv_file_raw:
        csv_reader = csv.reader(csv_file_raw, delimiter=",", skipinitialspace=True)
        with open(routes_data_clean, mode='w', encoding="utf-8") as csv_file_clean:
            csv_writer = csv.writer(csv_file_clean, delimiter='\t')
            csv_writer.writerow(['airline_id', 'airport_src', 'airport_dst', 'aircrafts'])
            for line in csv_reader:
                airline_id = normalize(line[1])
                if airline_id not in airlines:
                    continue
                airport_src = normalize(line[3])
                if airport_src not in airports:
                    continue
                airport_dst = normalize(line[5])
                if airport_dst not in airports:
                    continue
                route_aircrafts = normalize(line[8]).split(" ")
                # we only retain the aircrafts that exist.
                route_existing_aircrafts = [aircraft for aircraft in route_aircrafts if aircraft in aircrafts]
                # if no airline exists, we discard the route.
                if len(route_existing_aircrafts) == 0:
                    continue
                csv_writer.writerow([airline_id, airport_src, airport_dst, " ".join(route_existing_aircrafts)])





'''
Parses the hotel file (first argument) and generates a clean CSV file (second argument).
'''
def parse_hotels_raw(hotel_data_raw):
    # used get city and country names from (lat, long)
    geolocator = Nominatim()
    geolocator.urlopen = uo 
    parsed_locations = {}
    counter = 0

    parsed_hotels = {}
    with open("hotel_clean_intermediate.csv", 'r', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t", skipinitialspace=True)
        next(csv_reader)
        for line in csv_reader:
            parsed_hotels[line[0]] = line[2]

    with open(hotel_data_raw, 'r', encoding="utf-8") as csv_file_raw:
        csv_reader = csv.reader(csv_file_raw, delimiter=",", skipinitialspace=True)
        with open("hotel_clean_intermediate_final.csv", mode='w', encoding="utf-8") as csv_file_clean:
            '''
            We create an intermediate file, where a column has the address returned by the geocoder.
            In a second step, the address will be parsed to get the city and country out of it
            '''
            csv_writer = csv.writer(csv_file_clean, delimiter='\t')
            csv_writer.writerow(['hotel_name', 'hotel_address', 'hotel_address_parsed', 'hotel_score'])
            next(csv_reader)
            for line in csv_reader:
                hotel_address = line[0]
                hotel_name = line[4]
                review_score = line[3]
                latitude = line[15]
                longitude = line[16]

                if hotel_name in parsed_hotels:
                    csv_writer.writerow([hotel_name, hotel_address, parsed_hotels[hotel_name], review_score])    
                else:
                    location_to_parse = "{0}, {1}".format(latitude, longitude)
                    # Get the location from Open Street Maps
                    if location_to_parse not in parsed_locations:
                        counter += 1
                        print("Parsing,", location_to_parse, counter)
                        try:
                            location = geolocator.reverse(location_to_parse, language='en')
                            parsed_locations[location_to_parse] = {'address': location.address}
                            sleep(2)
                            csv_writer.writerow([hotel_name, hotel_address, parsed_locations[location_to_parse]['address'], review_score])
                        except Exception:
                            print("exception. ignoring this hotel")


def parse_hotels(hotel_data_raw, hotels_data_clean):
    parsed_hotels = {}
    with open(hotel_data_raw, mode='r', encoding="utf-8") as csv_file_raw:
        csv_reader = csv.reader(csv_file_raw, delimiter="\t", skipinitialspace=True)
        next(csv_reader)

        with open(hotels_data_clean, mode='w', encoding="utf-8") as csv_file_clean:
            csv_writer = csv.writer(csv_file_clean, delimiter='\t')
            csv_writer.writerow(['hotel_id', 'hotel_name', 'hotel_address', 'city', 'country', 'hotel_score'])
            hotel_id = 0
            for line in csv_reader:
                hotel_name = line[0]
                if hotel_name  not in parsed_hotels:
                    parsed_hotels[hotel_name] = True
                    hotel_address = line[2]
                    hotel_score = line[3]
                    hotel_address_components = hotel_address.split(",")
                    country = hotel_address_components[len(hotel_address_components) - 1].strip()
                    if country == "Italy":
                        city = hotel_address_components[len(hotel_address_components) - 4].strip()
                    elif country =="Austria":
                        city = hotel_address_components[len(hotel_address_components) - 3].strip()
                    else:
                        city = hotel_address_components[len(hotel_address_components) - 5].strip()
                    csv_writer.writerow([hotel_id, hotel_name, hotel_address, city, country, hotel_score])
                    hotel_id += 1