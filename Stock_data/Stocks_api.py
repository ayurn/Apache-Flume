'''
@Author: Ayur Ninawe
@Date: 2021-08-04
@Last Modified by: Ayur Ninawe
@Last Modified time: 15:00:30 2021-08-04
@Title : Program to store tral time data on HDFS with flume
'''
import csv
import requests
import os
from decouple import config

key = config("KEYS")

CSV_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=5min&slice=year1month1&apikey={}'.format(key)

with requests.Session() as s:
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print(row)