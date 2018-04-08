import csv
import configparser
import glob
import time
import sys

start_time = time.time()

try:
    files = glob.glob('csv/*csv')

    Config = configparser.ConfigParser()
    Config.read("settings.ini")

    writer = csv.writer(open(Config.get('csv', 'writefile'), 'w', newline=''))

    for file in files:
        with open(file) as csvfile:
            csvReader = csv.reader(csvfile)
            next(csvReader)

            for row in csvReader:
                if str.isdigit(row[14]):
                    if int(str(row[14])[:2]) >= 90 and "bin" not in row[1].lower() \
                            and "mohd" not in row[1].lower() and "bt" not in row[1].lower()\
                            and "nur" not in row[1].lower() and "a/l" not in row[1].lower()\
                            and "a/p" not in row[1].lower():
                        writer.writerow(row)

except:
    print("Unexpected error:", sys.exc_info())
else:
    print ("Ran Successfully")

print("--- %s seconds ---" % (time.time() - start_time))
