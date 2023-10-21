import sqlite3
import sys

# Connect to the database
conn = sqlite3.connect('C:\engramar\projects\cd-block-2\customer_db')
cur = conn.cursor()

# Open the input file
fname = 'customerfile.txt'
fhand = open(fname)

# Insert records to table
count = 0 
for line in fhand:	
	fields = line.split('|')    
	customer_id = fields[0].strip() 
	name        = fields[1].strip()  
	address     = fields[2].strip() 
	dob         = fields[3].strip() 
	phone       = fields[4].strip() 
	email       = fields[5].strip() 
	
	cur.execute('''INSERT INTO customer
        (
        customer_id,
        name,
        address,
        dob,
        phone,
        email
        )  
        VALUES ( ?, ?, ?, ?, ?, ?)''',   
		(
        customer_id,
        name,
        address,
        dob,
        phone,
        email
		))
	count += 1	

conn.commit()

print ('Successfully completed. Total records inserted : ', count)