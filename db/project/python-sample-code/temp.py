import csv
import random

def generate_nbr():
    digits = '0123456789'
    return ''.join(random.choice(digits) for i in range(7))

doublons = {}
print("getting all customers")
with open('clean_data/customers.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    with open('clean_data/customers_clean.csv', 'w', encoding='utf-8') as csv_wr:
        csv_writer = csv.writer(csv_wr, delimiter='\t')
        csv_writer.writerow(next(csv_reader))
        for line in csv_reader:
            if line[0] in doublons:
                while True:
                    new_nbr = generate_nbr()
                    if new_nbr not in doublons:
                        break
                csv_writer.writerow([new_nbr] + [line[i] for i in range(1, len(line))])
            else:
                doublons[line[0]] = True
                csv_writer.writerow(line)