import csv
import configparser
import glob
import time
import sys
import os

def sort(num):
    start_time = time.time()

    try:
        files = glob.glob('csv/*csv')

        Config = configparser.ConfigParser()
        Config.read("settings.ini")

        dirname = 'js_' + str(num)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        headers = ['DataA', 'DataB', 'DataC', 'DataD']

        writer = csv.writer(open(dirname + '/' + Config.get('jscsv', 'writefile'), 'w', encoding='utf8', newline=''))
        count = 1
        
        for file in files:
            print(file)
            
            with open(file, encoding='utf8') as csvfile:
                csvReader = csv.reader(csvfile)
                     
                next(csvReader)
                next(csvReader)
                
                if count == 1:
                    writer.writerow(next(csvReader))

                for row in csvReader:
                    if str.isdigit(row[25]):
                        if int(str(row[25])) == 150 and int(str(row[17])) == 2 and int(str(row[16]).split('-')[0]) > 1990: 
                            writer.writerow(row)

            print(count)
            count+=1
                

    except:
        print("Unexpected error:", sys.exc_info())
    else:
        print ("Ran Successfully")

    print("--- %s seconds ---" % (time.time() - start_time))
