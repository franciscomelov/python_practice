import os
from os.path import isfile, join
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def show_files(complete_list, path):
    files_list = [f for f in complete_list if isfile(join(path, f))]
    print(*files_list)

def show_all(args):
    path = os.getcwd()
    complete_list =sorted(os.listdir(path),key=str.lower)
    if "-f" in args:
        show_files(complete_list, path)
    else:
        print(*complete_list)

def files_folders(*args):
    args = list(args)[0].split(" ")

    print(args)
    if "ls" in args:
        show_all(args)






if __name__ == "__main__":
    while True:
        args = input(">> ")
        files_folders(args)

# ls print same line files folders -- OK
# ls -f just files -- OK
# ls -i new line prin with info
#     list the file size | created date | owner
# ls <folder> name same line files folders from <folder>
