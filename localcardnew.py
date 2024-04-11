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

# Read data from the CSV file and insert into the table
with open('Sheet3.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        card_type = row.get('Barcode')
        serialno = card_type[-8:]
        sector = card_type[8:10]
        
        # Inserting the row with specified values
        cursor.execute('''INSERT INTO accreditation_card 
                          (serialno, category, subcategory, sector, status, card_no, created_at)
                          VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (serialno, 'centralcard', 'Media', sector, 'Active', card_type, datetime.now()))
        conn.commit()  # Commit after each insert

# Close connection
conn.close()
