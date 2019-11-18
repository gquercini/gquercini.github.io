import csv
import random
from utils import normalize
from utils import pick_times
from random import choices
from random import choice
from utils import generate_date
from utils import generate_trip_dates
from utils import distance
import datetime

'''
Generate booking information
Author: Gianluca Quercini
'''


'''
Information on a single flight
'''
class Flight:
    def __init__(self, flight_number, airline, aircraft, airport_src, airport_dst, departure_time, \
         departure_date, flight_duration, travel_class, seat_number, price):
        self.flight_number = flight_number
        self.airline = airline
        self.aircraft = aircraft
        self.airport_src = airport_src
        self.airport_dst = airport_dst
        self.departure_time = departure_time
        self.departure_date = departure_date
        self.flight_duration = flight_duration
        self.travel_class = travel_class
        self.seat_number = seat_number
        self.price = price

class HotelBooking:
    def __init__(self, hotel_id, check_in_date, check_out_date, price, breakfast_included):
        self.hotel_id = hotel_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.price = price
        self.breakfast_included = breakfast_included


class BookingGeneration:

    '''
    Initialization. 
    Input parameters: the cleaned files with the data on  the airports,  airlines, the routes and the hotels
    '''
    def __init__(self, airports_data_clean, airlines_data_clean, routes_data_clean, hotels_data_clean, customers_data):
        self.airports = {}

        '''
        Get all the airports.
        '''
        with open(airports_data_clean, 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            next(csv_reader)
            for line in csv_reader:
                self.airports[line[0]] = {'id' : line[0], 'city' : line[2], 'country' : line[3], 'out' : 0, 'lat' : line[6], 'long': line[7]}

        '''
        Get all the airlines.
        '''
        self.airlines ={}
        with open(airlines_data_clean, 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            next(csv_reader)
            for line in csv_reader:
                # We register the iata code of the airline, if available, otherwise the icao code.
                if line[3] != "null":
                    self.airlines[line[0]] = {'code': line[3]}
                else:
                    self.airlines[line[0]] = {'code': line[4]}

        '''
        Get the routes.
        For each route, list the airlines and the aircrafts serving that route.
        Also, we count the number of routes leaving each airport (in order to get the importance of the airport).
        '''
        self.routes = {airport: {} for airport in self.airports}
        with open(routes_data_clean, 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            next(csv_reader)
            for line in csv_reader:
                airport_src = line[1]
                airport_dst = line[2]
                airline = line[0]
                aircrafts = line[3].split(" ")
                self.routes[airport_src][airport_dst] = []
                '''
                Generate the departure times for the given airline (between 1 and 4 flights per day)
                The probability of one flight is 30%, 2 flights 30% ....
                '''
                departure_times = pick_times(choices([1, 2, 3, 4], [0.3, 0.3, 0.2, 0.2])[0])
                self.routes[airport_src][airport_dst].append({"airline": airline, "aircrafts": aircrafts, "departure_times":departure_times})
                # Increment the number of routes leaving the source airport
                self.airports[airport_src]['out'] += 1
        # sometimes the routes are not bidirectional :-S
        for airport_src in self.routes:
            for airport_dst in self.routes[airport_src]:
                if airport_src not in self.routes[airport_dst]:
                    self.routes[airport_dst][airport_src] = [route for route in self.routes[airport_src][airport_dst]]
                    self.airports[airport_dst]['out'] += 1

        '''
        List the airports by country
        '''
        self.airports_by_country = {country: [] for country in [item['country'] for item in self.airports.values()]}
        for a in self.airports:
            self.airports_by_country[self.airports[a]['country']].append(self.airports[a])

        '''
        Normalize the counts for "out", so that the sum of all the "out", given a country, is 1.
        In practice, given a country, we'll have a probability distribution for its airports.
        '''
        for country in self.airports_by_country:
            sum_out = 0
            for airport in self.airports_by_country[country]:
                sum_out += airport['out']
            if sum_out > 0:
                for airport in self.airports_by_country[country]:
                    airport['out'] /= sum_out

        '''
        Get the hotels
        '''
        self.hotels = {}
        with open(hotels_data_clean, 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            next(csv_reader)
            for line in csv_reader:
                hotel_id = line[0]
                hotel_city = line[3]
                hotel_country= line[4]
                hotel_score = line[5]
                self.hotels[hotel_id] = {'id': line[0], 'city': hotel_city, 'country': hotel_country, 'rate' : hotel_score}
        
        self.customers = []
        with open(customers_data, 'r', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter="\t")
            next(csv_reader)
            for line in csv_reader:
                customer_id = line[0]
                customer_country = line[5]
                self.customers.append({'id': customer_id, 'country': customer_country})

    
    def estimate_flight_duration(self, airport_src_id, airport_dst_id):
        flight_distance = distance(self.airports[airport_src_id]['lat'], self.airports[airport_src_id]['long'], \
            self.airports[airport_dst_id]['lat'], self.airports[airport_dst_id]['long'])
        # 804 kph + 30 minutes take off and landing
        flight_duration = flight_distance / 804 + 0.5
        hours = int(flight_duration)
        minutes = int(60 * (flight_duration % 1))
        return "{:02d}:{:02d}".format(hours, minutes)


    def generate_flight_number(self, airline_id, departure_time):
        return self.airlines[airline_id]['code'] + departure_time[0:2] + departure_time[3:]

    def estimate_flight_price(self, flight_distance, travel_class):
        if travel_class == 'economy':
            return int(0.09 * flight_distance)
        else:
            return int(0.09 * flight_distance) + 400

    def select_destination(self, airport_src_id):
         # We get all the possible (direct) destinations from the source airport.
        # For each destination, we count the number of lines connecting the source to the destination.
        # This measures the importance of the route.
        destinations = [(airport_dst_id, len(lines)) for airport_dst_id, lines in self.routes[airport_src_id].items() ]
        # Normalize the importance of the route, so that it is a prob distribution.
        total = 0
        for dest in destinations:
            total += dest[1]
        destinations_id = [t[0] for t in destinations]
        destinations_prob = [t[1]/total for t in destinations]

        # We pick a destination
        return self.airports[choices(destinations_id, destinations_prob)[0]]


    '''
    Generates a flight from a given airport (the identifier is given).
    Input parameters: the flight number, the identifier of the source airport, the identifier of the destination airport, 
    the airline id, the aircraft code, the departure date, the flight duration, the departure time, the flight duration, the travel class, the seat number  and the price
    
    Returns an object of the class Flight
    '''
    '''def generate_flight(self, flight_number, airport_src_id, airport_dst_id, airline_id, aircraft_code, departure_date, flight_duration, departure_time, \
        travel_class, seat_number, price):

        return Flight(flight_number, airline_id, aircraft_code, airport_src_id, airport_dst_id, departure_time, \
         departure_date, flight_duration, travel_class, seat_number, price)'''


    def generate_flight(self, airport_src_id, airport_dst_id, departure_date):
        # We pick a specific route (airline, aircraft, departure time)
        route = choices(self.routes[airport_src_id][airport_dst_id])[0]
        airline_id = route['airline']
        aircraft_code = choice(route['aircrafts'])
        departure_time = choice(route['departure_times'])
        flight_duration = self.estimate_flight_duration(airport_src_id, airport_dst_id)
        travel_class = choice(['economy', 'business'])
        if travel_class == 'economy':
            seat_number = str(choice([i for i in range(1, 11)])) + choice(list('ABCDEFGHIJ'))
        else:
            seat_number = str(choice([i for i in range(11, 45)])) + choice(list('ABCDEFGHIJ'))

        flight_number = self.generate_flight_number(airline_id, departure_time)

        price = self.estimate_flight_price(distance(self.airports[airport_src_id]['lat'], self.airports[airport_src_id]['long'], \
            self.airports[airport_dst_id]['lat'], self.airports[airport_dst_id]['long']), travel_class)

        return Flight(flight_number, airline_id, aircraft_code, airport_src_id, airport_dst_id, departure_time, \
         departure_date, flight_duration, travel_class, seat_number, price)

    def get_hotels(self, city, country):
        return  [self.hotels[hotel_id] for hotel_id in self.hotels if self.hotels[hotel_id]['city'] == city and self.hotels[hotel_id]['country'] == country] 

    def generate_hotel_booking(self, hotel, check_in_date, check_out_date):
        stay_duration = abs((datetime.datetime.strptime(check_out_date, "%d/%m/%Y") - datetime.datetime.strptime(check_in_date, "%d/%m/%Y")).days)
        price = stay_duration * (int(float(hotel['rate'])/2) * 30)
        breakfast_included = choice([True, False])
        return HotelBooking(hotel['id'], check_in_date, check_out_date, price, breakfast_included)

    '''
    Generate bookings for a given customer.
    '''
    def generate_bookings(self, hotel_bookings_data, flight_bookings_data):
        with open(flight_bookings_data, mode='w', encoding="utf-8") as csv_flight_booking_clean:
            csv_flight_booking_writer = csv.writer(csv_flight_booking_clean, delimiter='\t')
            csv_flight_booking_writer.writerow(['booking_id', 'customer_id', 'flight_number', 'airline_id', 
            'aircraft', 'airport_src', 'airport_dst', 'departure_time', \
            'departure_date', 'flight_duration', 'travel_class', 'seat_number', 'price'])
            
            with open(hotel_bookings_data, mode='w', encoding="utf-8") as csv_hotel_booking_clean:
                csv_hotel_booking_writer = csv.writer(csv_hotel_booking_clean, delimiter='\t')
                csv_hotel_booking_writer.writerow(['booking_id', 'customer_id', 'hotel_id', 'check_in_date', \
                    'check_out_date', 'price', 'breakfast_included'])

                booking_id = 0
                for customer in self.customers:
                    customer_id = customer['id']
                    country = customer['country']
                    nb_bookings = random.randint(1, 10)
                    trip_dates = generate_trip_dates(nb_bookings)

                    for (departure_date, return_date) in trip_dates:
                        airport_src = choices(self.airports_by_country[country],  [a['out'] for a in self.airports_by_country[country]])[0]
                        airport_dst = self.select_destination(airport_src['id'])
                        outbound_flight = self.generate_flight(airport_src['id'], airport_dst['id'], departure_date)
                        inbound_flight = self.generate_flight(airport_dst['id'], airport_src['id'], return_date)
                        
                        hotels = self.get_hotels(airport_dst['city'], airport_dst['country'])
                        if len(hotels) > 0:
                            hotel = choice(hotels)
                            hotel_booking = self.generate_hotel_booking(hotel, departure_date, return_date)
                            csv_hotel_booking_writer.writerow([booking_id, customer_id, hotel_booking.hotel_id, hotel_booking.check_in_date, \
                                hotel_booking.check_out_date, hotel_booking.price, hotel_booking.breakfast_included])

                        csv_flight_booking_writer.writerow([booking_id, customer_id, outbound_flight.flight_number, outbound_flight.airline, \
                            outbound_flight.aircraft, outbound_flight.airport_src, outbound_flight.airport_dst, \
                                outbound_flight.departure_time, outbound_flight.departure_date, \
                                    outbound_flight.flight_duration, outbound_flight.travel_class, \
                                        outbound_flight.seat_number, outbound_flight.price])
                        
                        csv_flight_booking_writer.writerow([booking_id, customer_id, inbound_flight.flight_number, inbound_flight.airline, \
                            inbound_flight.aircraft, inbound_flight.airport_src, inbound_flight.airport_dst, \
                                inbound_flight.departure_time, inbound_flight.departure_date, \
                                    inbound_flight.flight_duration, inbound_flight.travel_class, \
                                        inbound_flight.seat_number, inbound_flight.price])
                        
                        booking_id += 1
                        

    
        


        



        
