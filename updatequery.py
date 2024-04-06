import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mohali_stad_tickets'
)
cursor = conn.cursor()

# Select data from the table
cursor.execute("SELECT id, card_no FROM accreditation_card")
rows = cursor.fetchall()

# Update the rows with the extracted serial numbers
for row in rows:
    card_no = row[1]
    serial_no = card_no[-8:]
    cursor.execute("UPDATE accreditation_card SET serialno = %s WHERE id = %s", (serial_no, row[0]))

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
