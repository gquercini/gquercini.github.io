import csv
from raw_data_parsing import parse_airports
from raw_data_parsing import parse_airlines
from raw_data_parsing import parse_aircrafts
from raw_data_parsing import parse_routes
from raw_data_parsing import parse_hotels
from customer_generation import CustomerGeneration
from booking_generation import BookingGeneration


################## PARAMETERS ###########################
nb_customers_to_generate = 1000

raw_data = "./raw_data"
clean_data = "./clean_data"

airport_data_raw = "{}/{}".format(raw_data, "airports.raw.csv")
airport_data_clean = "{}/{}".format(clean_data, "airports.csv")

airline_data_raw = "{}/{}".format(raw_data, "airlines.raw.csv")
airline_data_clean = "{}/{}".format(clean_data, "airlines.csv")

aircraft_data_raw = "{}/{}".format(raw_data, "aircrafts.raw.csv")
aircraft_data_clean = "{}/{}".format(clean_data, "aircrafts.csv")

route_data_raw = "{}/{}".format(raw_data, "routes.raw.csv")
route_data_clean = "{}/{}".format(clean_data, "routes.csv")


hotel_data_raw = "{}/{}".format(raw_data, "hotels.raw.csv")
hotel_data_clean = "{}/{}".format(clean_data, "hotels.csv")

routes_data = "{}/{}".format(raw_data, "routes.dat.txt")

first_names_men = "{}/{}".format(raw_data, "first_names_men.csv")
first_names_women = "{}/{}".format(raw_data, "first_names_women.csv")
family_names = "{}/{}".format(raw_data, "family_names.csv")

customers_file = "{}/{}".format(clean_data, "customers.csv")
hotel_bookings_data  = "{}/{}".format(clean_data, "hotel_bookings.csv")
flight_bookings_data = "{}/{}".format(clean_data, "hotel_flights.csv")

#########################################################

#parse_airports(airport_data_raw, airport_data_clean)
#airlines = parse_airlines(airline_data_raw, airline_data_clean)
#aircrafts = parse_aircrafts(aircraft_data_raw, aircraft_data_clean)
#parse_routes(route_data_raw, route_data_clean, airports, airlines, aircrafts)
#parse_hotels(hotel_data_raw, hotel_data_clean)

# Generate customers.
cg = CustomerGeneration(first_names_men, first_names_women, family_names)
with open(customers_file, mode='w', encoding="utf-8") as csv_file_clean:
    csv_writer = csv.writer(csv_file_clean, delimiter='\t')
    csv_writer.writerow(['customer_id', 'customer_first_name', 'customer_family_name', \
        'customer_gender', 'customer_birth_date', 'customer_country', 'customer_phone_number'])
    for _ in range(nb_customers_to_generate):
        customer = cg.generate_customer()
        csv_writer.writerow([customer['id'], customer['first_name'], customer['family_name'], customer['gender'], \
            customer['birth_date'], customer['country'], customer['phone_number']])

bg = BookingGeneration(airport_data_clean, airline_data_clean, route_data_clean, hotel_data_clean, customers_file)
bg.generate_bookings(hotel_bookings_data, flight_bookings_data)

