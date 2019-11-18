import sqlite3
import csv
import datetime

# Connect to the database contained in the file my_db.db
conn = sqlite3.connect('my_db.db')

# Create an object cursor, used to do read/write operations on the 
# database
cursor = conn.cursor()
try:
    # Open the input CSV file
    with open('test.csv', 'r', encoding='utf-8') as csv_file:
        # Delete all data from the table test
        cursor.execute("DELETE FROM test") 
        # Commit the modification. 
        conn.commit()
        csv_reader = csv.reader(csv_file, delimiter='\t')
        # Skip the header of the CSV file
        next(csv_reader)
        for line in csv_reader:
            # The values of the first column must be stored as strings.
            string_column = line[0]
            # The values of the second column must be stored as integer numbers.
            integer_column = int(line[1])
            # The values of the third column must be stored as real numbers.
            float_column = float(line[2])
            # The values of the fourth column must be stored as dates (format dd/mm/yyyy).
            date_column = datetime.datetime.strptime(line[3], "%d/%m/%Y") 
            # Insert the values into the table
            cursor.execute("INSERT INTO test VALUES(?, ?, ?, ?)",\
                 (string_column, integer_column, float_column, date_column))
# If anything goes wrong, raise an exception
except sqlite3.Error as error:
    # Print the reason of the exception.
    print("Error while loading the data: {}".format(error))
# Wheter an exception is raised or not, at the end, the following 
# instructions are executed.
finally:
    # Commit the modifications to the database.
    conn.commit()
    # Closes the connection to the database.
    cursor.close()
    conn.close()
    print("The connection to the database is now closed")