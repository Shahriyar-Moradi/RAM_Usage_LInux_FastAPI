
# import schedule
import sqlite3
import time
import os
import psutil

# Function to insert data into the database
def insert_data():
    # below code is for linux operation system but I dont access linux and I use my Mac device
    # total_memory, used_memory, free_memory = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    x=dict(psutil.virtual_memory()._asdict())
    total_memory="%.3f" % float(x['total']/1024/1024) #divid /1024/1024 to convert Output in MBs
    free_memory="%.3f" % float(x['free']/1024/1024)
    used_memory="%.3f" % float(x['used']/1024/1024)
    # Connect to the SQLite database
    conn = sqlite3.connect('my_memory.db')
    c = conn.cursor()
    print("connected")

    live_data =  [
    (total_memory, used_memory, free_memory)]
    # Create Table
    c.execute('''CREATE TABLE IF NOT EXISTS Memory
                  (id INTEGER PRIMARY KEY,
                   total REAL,
                   used REAL,
                   free REAL)''')
    print("table created")

    # Insert the data into the database
    c.executemany('INSERT INTO Memory (total, used, free) VALUES (?, ?, ?)',live_data)
    conn.commit()

    # Close the database connection
    conn.close()
    print("Data inserted successfully.")

# we can use multiple way for timing
# { 1-time.sleep(60)
#   2- use schedule module
    # 3- threading module
# }
# Schedule the data insertion every minute
# schedule.every(1).minutes.do(insert_data)

# Main loop to run the scheduled jobs
while True:
    # schedule.run_pending()
    insert_data()
    time.sleep(60)