import random
from numpy.random import randint
import unidecode
import time
import csv
from numpy.random import choice
from utils import generate_date

'''
Generation of a customer
'''

class CustomerGeneration:

    '''
    Initializes the object. Three CSV files as parameter : the one containing the men first names, the 
    one containing the women first names, the one containing the family names.
    '''
    def __init__(self, first_names_men, first_names_women, family_names):
        self.men_names = []
        self.women_names = []
        self.men_names_prob = []
        self.women_names_prob = []
        self.family_names = []
        self.family_names_prob = []
        self.duplicate_id = {}

        # Load the men first names 
        with open(first_names_men) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            total_occurrences = 0
            for row in csv_reader:
                self.men_names.append(row[0])
                total_occurrences += int(row[2])
                self.men_names_prob.append(int(row[2]))
            # Each name has an occurrence probability
            self.men_names_prob[:] = [x/total_occurrences for x in self.men_names_prob]
        
        # Load the women first names
        with open(first_names_women) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            total_occurrences = 0
            for row in csv_reader:
                self.women_names.append(row[0])
                total_occurrences += int(row[2])
                self.women_names_prob.append(int(row[2]))
            # Each name has an occurrence probability
            self.women_names_prob[:] = [x/total_occurrences for x in self.women_names_prob]
        
        # Load the family names
        with open(family_names) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            total_occurrences = 0
            for row in csv_reader:
                self.family_names.append(row[0])
                total_occurrences += int(row[1])
                self.family_names_prob.append(int(row[1]))
            # Each name has an occurrence probability
            self.family_names_prob[:] = [x/total_occurrences for x in self.family_names_prob]



    '''
    Generates a customer number with the given length.
    '''
    def generate_customer_number(self, customer_number_len=7):
        digits = '0123456789'
        while True:
            customer_number  = ''.join(random.choice(digits) for i in range(customer_number_len))
            if customer_number not in self.duplicate_id:
                self.duplicate_id[customer_number] = True
                return customer_number


    '''
    Generates a personal email address for the given 
    first and family names.
    '''
    def generate_personal_email(self, first_name, family_name):
        email_domain_names = ['google.com', 'yahoo.com', 'hotmail.com', 'mail.com', \
            'hotmail.fr', 'yahoo.fr', 'wanadoo.fr', 'orange.fr', 'free.fr', 'sfr.fr']
        selected_domain_name = email_domain_names[randint(0, len(email_domain_names))]
        
        first_name_norm = unidecode.unidecode(first_name).lower()
        family_name_norm = unidecode.unidecode(family_name).lower()
        email_names = ["{}".format(family_name_norm), "{}_{}".format(family_name_norm, first_name[0:3]), \
            "{}.{}".format(first_name_norm, family_name_norm), "{}.{}".format(family_name_norm, first_name_norm), \
                "{}_{}".format(first_name_norm, family_name_norm), "{}_{}".format(family_name_norm, first_name_norm),\
                "{}_{}".format(first_name_norm, family_name_norm[0:3])]
        
        selected_email_name = email_names[randint(0, len(email_names))]

        return "{}@{}".format(selected_email_name, selected_domain_name)


    '''
    Generates a gender.
    Returns a tuple, where the first item is either 'M' or 'F', depending on the 
    generated gender.
    '''
    def generate_gender(self):
        if random.uniform(0, 1) >= 0.5:
            return 'F'
        else:
            return 'M'

    '''
    Generate a country.
    '''
    def generate_country(self):
        countries = ["United States of America", "Canada", "Mexico", "Brazil", "Argentina", "Chile", "Colombia", \
            "Italy", "France", "Spain", "Austria", "United Kingdom", "Norway", "Sweden", "Finland", "Germany", 
            "Netherlands", "Belgium", "Greece", "Switzerland", "Nigeria", "Morocco", "Tunisia", "Lebanon", "Iran", "India", "China", 
            "Japan", "Australia", "Russia", "Turkey"]
        return countries[randint(0, len(countries))]


    '''
    Generate a phone number 
    '''
    def generate_phone_number(self, country):
        # (country_code, number of digits in phone number)
        country_codes = {"United States of America" : ("+1", 10), "Canada" : ("+1", 10), \
            "Mexico" : ("+52", 10), "Brazil" : ("+55", 10), "Argentina" : ("+54", 10), \
                "Chile" : ("+56", 9), "Colombia" : ("+57", 8), \
                    "Italy" : ("+39", 10), "France" : ("+33", 9), "Spain" : ("+34", 9), \
                        "Austria" : ("+43", 10), "United Kingdom" : ("+44", 10), "Norway" : ("+47", 8), \
                            "Sweden" : ("+46", 10), "Finland" : ("+358", 10), "Germany" : ("+49", 10),\
                            "Netherlands" : ("+31", 9), "Belgium" : ("+32", 9), "Greece" : ("+30", 10), "Switzerland" : ("+41", 10),\
                                "Nigeria" : ("+234", 10), "Morocco" : ("+212", 9), "Tunisia" : ("+216", 8), \
                    "Lebanon" : ("+961", 8), "Iran" : ("+98", 10), "India" : ("+91", 10),\
                        "China" : ("+86", 10), "Japan" : ("+81", 10), "Australia" : ("+61", 10), \
                            "Russia" : ("+7", 10) , "Turkey" : ("+90", 10)}

        digits = "0123456789"
        t = country_codes[country]
        return "{}{}".format(t[0], ''.join(random.choice(digits) for i in range(t[1])))

    

    '''
    Generate a birth date
    '''
    @classmethod
    def generate_birth_date(self):
        return generate_date("1/1/1970 11:59 PM", "12/31/1990 11:59 PM", '%m/%d/%Y %I:%M %p', random.random())

    '''
    Generates a first name
    '''
    def generate_first_name(self, gender):
        if gender == 'F':
            return choice(self.women_names, 1, self.women_names_prob).item(0)
        else:
            return choice(self.men_names, 1, self.men_names_prob).item(0)

    '''
    Generate a family name
    '''
    def generate_family_name(self):
        return choice(self.family_names, 1, self.family_names_prob).item(0)

    '''
    Generate a customer
    '''
    def generate_customer(self):
        customer = {}
        customer['id'] = self.generate_customer_number()
        customer['gender'] = self.generate_gender()
        customer['first_name'] = self.generate_first_name(customer['gender'])
        customer['family_name'] = self.generate_family_name()
        customer['birth_date'] = self.generate_birth_date()
        customer['country'] = self.generate_country()
        customer['phone_number'] = self.generate_phone_number(customer['country'])
        return customer 
