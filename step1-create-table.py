import sqlite3

conn = sqlite3.connect('customer_db') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS customer
          ([customer_id] INTEGER PRIMARY KEY, 
           [name] TEXT,
           [address] TEXT,
           [dob] TEXT,
           [phone] TEXT,
           [email] TEXT)
          ''')
                      
conn.commit()