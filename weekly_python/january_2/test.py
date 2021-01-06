import os

from datetime import datetime


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

#print(help(os.scandir))
files = os.scandir(os.getcwd())
arr=[ f for f in files]

print("size   | created at  |  owner")
#print(arr)
info = arr[0].stat()
filename, file_extension = os.path.splitext(arr[1].path)
print(filename)
print(f'{info.st_size} bites| {convert_date(info.st_ctime)}  | {info.st_uid}')
