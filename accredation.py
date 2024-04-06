'''
import csv
import mysql.connector
from datetime import datetime

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mohali_stad_tickets'
)
cursor = conn.cursor()

# Generate the starting and ending card numbers
start_card_no = 698069871007110000001
end_card_no = 698069871007110000800

# Read data from CSV and insert into the table
with open('team.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        card_type = row.get('Card type')
        issuer = row.get('ISSUER')
        location = row.get('LOCATION')
        event = row.get('EVENT')
        sector = row.get('SECTOR')
        discount = row.get('DISCOUNT')
        ticket_type = row.get('TICKETTYPE')
        unique_id_from = int(row.get('UNIQUEID-FROM'))
        unique_id_to = int(row.get('UNIQUEID-TO'))
        for unique_id in range(unique_id_from, unique_id_to + 1):
            cursor.execute(INSERT INTO accreditation_card 
                              (serialno, category, subcategory, sector, status, card_no, created_at)
                              VALUES (%s, %s, %s, %s, 'Active', %s, %s),
                           (unique_id, 'centralcard', card_type, sector, unique_id, datetime.now()))

# Commit changes and close connection
conn.commit()
conn.close()

'''
'''
import csv
import mysql.connector
from datetime import datetime

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mohali_stad_tickets'
)
cursor = conn.cursor()

# Initialize serial number counter
serial_counter = 1

# Read data from CSV and insert into the table
with open('team.csv', 'r') as file:
    reader = csv.DictReader(file)
    for idx, row in enumerate(reader, start=1):
        card_type = row.get('Card type')
        issuer = row.get('ISSUER')
        location = row.get('LOCATION')
        event = row.get('EVENT')
        sector = row.get('SECTOR')
        discount = row.get('DISCOUNT')
        ticket_type = row.get('TICKETTYPE')
        unique_id_from = int(row.get('UNIQUEID-FROM'))
        unique_id_to = int(row.get('UNIQUEID-TO'))
        for unique_id in range(unique_id_from, unique_id_to + 1):
            serial_no = f'{serial_counter:021}'
            cursor.execute(INSERT INTO accreditation_card 
                              (serialno, category, subcategory, sector, status, card_no, created_at)
                              VALUES (%s, %s, %s, %s, 'Active', %s, %s),
                           (serial_no, 'centralcard', card_type, sector, unique_id, datetime.now()))
            serial_counter += 1  # Increment serial number counter

# Commit changes and close connection
conn.commit()
conn.close()
'''

import csv
import mysql.connector
from datetime import datetime

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mohali_stad_tickets'
)
cursor = conn.cursor()

# Read data from CSV and insert into the table
with open('Central.csv', 'r') as file:
    reader = csv.DictReader(file)
    serial_counter = 1
    id_counter = 1
    for row in reader:
        card_type = row.get('Card type')
        issuer = row.get('ISSUER')
        location = row.get('LOCATION')
        event = row.get('EVENT')
        sector = row.get('SECTOR')
        discount = row.get('DISCOUNT')
        ticket_type = row.get('TICKETTYPE')
        unique_id_from = int(row.get('UNIQUEID-FROM'))
        unique_id_to = int(row.get('UNIQUEID-TO'))
        for unique_id in range(unique_id_from, unique_id_to + 1):
            serial_no = f'{serial_counter:021}'
            cursor.execute('''INSERT INTO accreditation_card 
                              (serialno, category, subcategory, sector, status, card_no, created_at)
                              VALUES (%s, %s, %s, %s, 'Active', %s, %s)''',
                           (serial_no, 'centralcard', card_type, sector, unique_id, datetime.now()))
            conn.commit()  # Commit after each insert
            serial_counter += 1  # Increment serial number counter
            id_counter += 1  # Increment id counter

# Close connection
conn.close()
