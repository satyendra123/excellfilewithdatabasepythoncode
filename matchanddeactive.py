import csv
import pymysql
from datetime import datetime  # Import datetime module

# MySQL database credentials
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'mohali_stad_tickets'

# Connect to the MySQL database
with pymysql.connect(host=db_host, user=db_user, password=db_password, database=db_name) as db_connection:
    cursor = db_connection.cursor()

    # Read the CSV file and process each row
    with open('Sheet2.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            barcode = row[0]

            cursor.execute("SELECT * FROM accreditation_card WHERE card_no = %s", (barcode,))
            result = cursor.fetchone()

            if result:
                # Barcode exists, update the status and created_at
                existing_status = result[1]
                new_status = 'Active' if existing_status == 'Deactive' else 'Deactive'
                cursor.execute("UPDATE accreditation_card SET status = %s, created_at = %s WHERE card_no = %s", (new_status, datetime.now(), barcode))

    db_connection.commit()

print("Processing completed.")







