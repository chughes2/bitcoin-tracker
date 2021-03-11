import requests
import csv
import os
from datetime import datetime
from time import sleep


while True:
    #get bitcoin api
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/gbp')
    #sets months,days,years and hours,mins and secs
    date = datetime.now().strftime('%m/%d/%Y')
    time = datetime.now().strftime('%H/%M/%S')
    #get bpi,gbp and rate
    value = req.json()['bpi']['GBP']['rate']
    #gets the "," and removes them
    value = value.split(',')
    value = ''.join(value)

    #this will open the file and add: date,time and value
    with open('bcoins.csv','a+', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel', delimiter=',')
        if sum(1 for _ in csvfile) < 1:
            writer.writerow(['date', 'time', 'value'])
        writer.writerow([date, time, value])
    #repeats every hours
    sleep(60 * 60)
