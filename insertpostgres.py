import csv
import configparser
import glob
import time
import sys
import os
import psycopg2

start_time = time.time()


folder = 'js_1 - 100000'
files = glob.glob(folder + '/*csv')


for file in files:
    print(file)

    with open(file, 'r', encoding='utf8') as f:
        reader = csv.reader(f, escapechar='\\')
        #next(reader)  # Skip the header row.
        conn = psycopg2.connect("host=localhost dbname=jobstreet user=postgres password=p@$$w0rd")
        cur = conn.cursor()

        for row in reader:
            print(row)
            cur.execute(
                u"INSERT INTO candidate_info VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s,\
                %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)", row
                #u"INSERT INTO candidate_info VALUES (%r, %r, %r, %r,%r, %r, %r, %r,%r, %r, %r, %r, %r, %r, %r, %r,%r,\
                #%r, %r, %r,%r, %r, %r, %r,%r, %r, %r, %r, %r, %r, %r, %r,%r, %r, %r, %r,%r, %r, %r, %r,%r);",
                #row
            )

        conn.commit()

print("--- %s seconds ---" % (time.time() - start_time))