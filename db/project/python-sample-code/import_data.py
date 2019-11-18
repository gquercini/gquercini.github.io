import sqlite3
import csv
import datetime

conn = sqlite3.connect('/Users/quercini_gia/Desktop/test-db.db')

cursor = conn.cursor()


try:
    print("Import from aircraft")
    with open('clean_data/aircrafts.csv', 'r', encoding='utf-8') as csv_file:
        cursor.execute("DELETE FROM aircraft")  
        conn.commit()
        csv_reader = csv.reader(csv_file, delimiter='\t')
        next(csv_reader)
        for line in csv_reader:
            aircraft_name = line[0]
            aircraft_iata = line[1]
            aircraft_icao = line[2]
            cursor.execute("INSERT INTO aircraft VALUES(?, ?, ?)", (aircraft_name, aircraft_iata, aircraft_icao))   

    print("Import from airlines")
    with open('clean_data/airlines.csv', 'r', encoding='utf-8') as csv_file:
        cursor.execute("DELETE FROM airline")
        conn.commit()
        csv_reader = csv.reader(csv_file, delimiter='\t')
        next(csv_reader)
        for line in csv_reader:
            airline_id = int(line[0])
            airline_name = line[1]	
            country = line[2]
            airline_iata = line[3]	
            airline_icao =	line[4]
            alias = line[5]
            cursor.execute("INSERT INTO airline VALUES(?, ?, ?, ?, ?, ?)", (airline_id, airline_name, country, airline_iata, airline_icao, alias))

        print("Import from airports")
        with open('clean_data/airports.csv', 'r', encoding='utf-8') as csv_file:
            cursor.execute("DELETE FROM airport")
            conn.commit()
            csv_reader = csv.reader(csv_file, delimiter='\t')
            next(csv_reader)
            for line in csv_reader:
                airport_id = int(line[0])	
                airport_name = line[1]	
                city = line[2]	
                country = line[3]	
                airport_iata = line[4]
                airport_icao = line[5]	
                latitude = float(line[6])
                longitude = float(line[7])
                cursor.execute("INSERT INTO airport VALUES(?, ?, ?, ?, ?, ?, ?, ?)", (airport_id, airport_name, city, country, airport_iata, airport_icao, latitude, longitude))

        print("Import from customers")
        with open('clean_data/customers.csv', 'r', encoding='utf-8') as csv_file:
            cursor.execute("DELETE FROM customer")
            conn.commit()
            csv_reader = csv.reader(csv_file, delimiter='\t')
            next(csv_reader)
            for line in csv_reader:
                customer_id	= line[0]
                customer_first_name	= line[1]
                customer_family_name = line[2]	
                customer_gender	= line[3]
                customer_birth_date = datetime.datetime.strptime(line[4], "%d/%m/%Y") 
                customer_country = line[5]	
                customer_phone_number = line[6]
                cursor.execute("INSERT INTO customer VALUES(?, ?, ?, ?, ?, ?, ?)", (customer_id, customer_first_name, customer_family_name, customer_gender, customer_birth_date, customer_country, customer_phone_number))
        
        print("Import from hotels")
        with open('clean_data/hotels.csv', 'r', encoding='utf-8') as csv_file:
            cursor.execute("DELETE FROM hotel")
            conn.commit()
            csv_reader = csv.reader(csv_file, delimiter='\t')
            next(csv_reader)
            for line in csv_reader:
                hotel_id = int(line[0])
                hotel_name = line[1]
                hotel_address = line[2]	
                city = line[3]
                country = line[4]
                hotel_score = float(line[5])
                cursor.execute("INSERT INTO hotel VALUES(?, ?, ?, ?, ?, ?)", (hotel_id, hotel_name, hotel_address, city, country, hotel_score))

        print("Import from flight bookings")
        with open('clean_data/flight_bookings.csv', 'r', encoding='utf-8') as csv_file:
            cursor.execute("DELETE FROM flight_booking")
            conn.commit()
            csv_reader = csv.reader(csv_file, delimiter='\t')
            next(csv_reader)
            id = 0
            for line in csv_reader:
                booking_id = int(line[0])
                customer_id	= int(line[1])
                flight_number = line[2]	
                airline_id = int(line[3]) 	
                aircraft = line[4]	
                airport_src	= int(line[5])
                airport_dst	= int(line[6])
                departure_time = line[7]	
                departure_date = datetime.datetime.strptime(line[8], "%d/%m/%Y") 	
                flight_duration	= line[9]
                travel_class = line[10]	
                seat_number	= line[11]
                price = float(line[12]) 
                cursor.execute("INSERT INTO flight_booking VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, booking_id, customer_id, flight_number, airline_id, aircraft, \
                    airport_src, airport_dst, departure_time, departure_date, flight_duration, travel_class, seat_number, price))
                id += 1
        
        print("Import from hotel bookings")
        with open('clean_data/hotel_bookings.csv', 'r', encoding='utf-8') as csv_file:
            cursor.execute("DELETE FROM hotel_booking")
            conn.commit()
            csv_reader = csv.reader(csv_file, delimiter='\t')
            next(csv_reader)
            for line in csv_reader:
                booking_id = int(line[0]) 	
                customer_id	= int(line[1]) 	
                hotel_id = int(line[2]) 		
                check_in_date = datetime.datetime.strptime(line[3], "%d/%m/%Y") 		
                check_out_date = datetime.datetime.strptime(line[4], "%d/%m/%Y")	
                price = float(line[5])	
                breakfast_included = bool(line[6])
                
                cursor.execute("INSERT INTO hotel_booking VALUES(?, ?, ?, ?, ?, ?, ?)", (booking_id, customer_id, hotel_id, check_in_date, check_out_date, price, breakfast_included))

except sqlite3.Error as error:
    print("Error while loading the data: {}".format(error))
finally:
    conn.commit()
    cursor.close()
    conn.close()
    print("The connection to the database is now closed")
