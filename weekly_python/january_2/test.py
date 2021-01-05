import os
from os.path import isfile, join
from datetime import datetime
from os import stat

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

print(help(os.scandir))
files = os.scandir(os.getcwd())
arr=[ f for f in files]
print(arr[1].stat())
print("size   | created at  |  owner")
info = arr[1].stat()
print(f'{info.st_size} bites| {convert_date(info.st_ctime)}  | {info.st_uid}')
