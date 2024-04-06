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

# Get the last serial number from the table
cursor.execute('SELECT serialno FROM accreditation_card ORDER BY serialno DESC LIMIT 1')
result = cursor.fetchone()
last_serial_no = int(result[0]) if result else 0

# Read data from the second CSV file and insert into the table
with open('tataneu.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        card_type = row.get('Card type')
        sector = row.get('SECTOR')
        unique_id_from = int(row.get('UNIQUEID-FROM'))
        unique_id_to = int(row.get('UNIQUEID-TO'))
        for unique_id in range(unique_id_from, unique_id_to + 1):
            serial_no = f'{last_serial_no + 1:021d}'
            cursor.execute('''INSERT INTO accreditation_card 
                              (serialno, category, subcategory, sector, status, card_no, created_at)
                              VALUES (%s, %s, %s, %s, 'Active', %s, %s)''',
                           (serial_no, 'tataneu', card_type, sector, unique_id, datetime.now()))
            conn.commit()  # Commit after each insert
            last_serial_no += 1  # Increment serial number counter

# Close connection
conn.close()
