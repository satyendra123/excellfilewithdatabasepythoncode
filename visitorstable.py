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
with open('whitelist.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        item_name = row.get('item_name')
        barcode = row.get('barcode')
        sector = row.get('sector')
        cursor.execute(INSERT INTO visitortickets (matchid, item_name, barcode, sector, status, created_at)
                  VALUES (5, %s, %s, %s, 'Active', CURRENT_TIMESTAMP), (item_name, barcode, sector))



# Commit changes and close connection
conn.commit()
conn.close()
'''

#EXAMPLE-2 insert the data into the database. in this database the data is already inserted

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
cursor.execute('SELECT id FROM visitortickets ORDER BY id DESC LIMIT 1')
result = cursor.fetchone()
last_id = int(result[0]) if result else 0
# Read data from CSV and insert into the table
with open('WhitelistPBKSvsSRHTESTHoustonTestingdata.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        item_name = row.get('item_name')
        barcode = str(row.get('barcode')) # Convert to string
        sector = row.get('sector')
        cursor.execute('INSERT INTO visitortickets (matchid, item_name, barcode, sector, status, created_at) VALUES (6, %s, %s, %s, "Active", CURRENT_TIMESTAMP)',
                       (item_name, barcode, sector))

# Commit changes and close connection
conn.commit()
conn.close()


