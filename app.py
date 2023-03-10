# import sqlite3
# connect = sqlite3.connect('data.db')

# connect.execute("DROP TABLE IF EXISTS CUSTOMER")
# connect.execute('''CREATE TABLE CUSTOMER 
#             (ID INT PRIMARY KEY NOT NULL,
#             NAME TEXT NOT NULL,
#             AGE INT NOT NULL);
# ''')

# connect.execute("INSERT INTO CUSTOMER (ID, NAME, AGE) \
#         VALUES (1, 'Bailey', 99)")
# connect.execute("INSERT INTO CUSTOMER (ID, NAME, AGE) \
#         VALUES (2, 'Daniel', 39)")


# all_data = connect.execute('''SELECT * FROM CUSTOMER''')
# for row in all_data:
#     print(row)

# connect.close()

# https://api.tomitokko.repl.co/ 
# This is the API endpoint

import requests
import json

response = requests.get("https://")

res = json.loads(response.text)

# for data in res:    
#     print(data)

from assignment import Assignment
from queue import PriorityQueue

pq = PriorityQueue()

assignment1 = Assignment("CS 400 P1W2", "2012-07-01T23:59:00-06:00", 1, "You must define a public class HashtableMap that implements this provided MapADT.")

pq.put(assignment1, assignment1.prio)

