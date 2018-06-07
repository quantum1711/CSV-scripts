import csv
import configparser
import glob
import time
import sys
import os
from itertools import islice


def sort(num):
    start_time = time.time()

    try:
        #files = glob.glob('csv/*csv')

        Config = configparser.ConfigParser()
        Config.read("settings.ini")

        num = int(num)
        foldernum = 0

        if num == 1:
            numstart = num
            foldernum = num
        else:
            numstart = (num * 10000) + 1
            foldernum = numstart

        numend = numstart + 9999

        dirname = 'js_' + str(foldernum) + ' - ' + str(foldernum + 99999)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        count = 1
        file = r'C:\Users\user\Desktop\jobstreet data 2\jobstreet.com-candidates.csv'

        for x in range(1, 11):

            print(numstart)
            print(numend)

            writer = csv.writer(open(dirname + '/' + str(numend) + '_' + Config.get('splitjscsv', 'writefile'), 'w',
                                     encoding='utf8', newline=''))

            with open(file, encoding='utf8') as fd:
                for row in islice(csv.reader(fd), numstart-1, numend, None):
                    writer.writerow(row)

            numstart = numend + 1
            numend += 10000

    except:
        print("Unexpected error:", sys.exc_info())
    else:
        print ("Ran Successfully")

    print("--- %s seconds ---" % (time.time() - start_time))
