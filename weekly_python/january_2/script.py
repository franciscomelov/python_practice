import os
from os.path import isfile, join
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date

def show_files(complete_list, path):
    files_list = [f for f in complete_list if isfile(join(path, f))]
    print(*files_list, sep ="  ")

def show_info(path):
    
    complete_list = [f for f in os.scandir(path)]
    names = [info.name for info in complete_list]
    sizes = [info.stat().st_size for info in complete_list]
    times = [convert_date(info.stat().st_ctime) for info in complete_list]
    owners = [info.stat().st_uid for info in complete_list]
    type_ext = [os.path.splitext(f.path)[1] for f in complete_list]

    title = f'{"name".ljust(max([len(i) for i in names]), " ")} | {"size".ljust(max([len(str(i)) for i in sizes]), " ")} | {"created at".ljust(max([len(i) for i in times]), " ")} | {"Owner".ljust(max([len(str(i)) for i in owners]), " ")} | extension'
    print(title)
    print(len(title)*"-")
    for i, _ in enumerate(names):
        name = names[i].ljust(max([len(i) for i in names]), " ")
        size = str(sizes[i]).ljust(max([len(str(i)) for i in sizes]), " ")
        time = times[i].ljust(max([len(i) for i in times]), " ")
        owner = str(owners[i]).ljust(max([len(str(i)) for i in owners]), " ")
        extension = type_ext[i]
        print(f'{name} | {size} | {time} | {owner} | {extension}')


def show_all(args):
    path = os.getcwd()
    complete_list =sorted(os.listdir(path),key=str.lower)

    if "-fi" in args: 
        show_files(complete_list, path)
        return
    elif len(args)==1: 
        print(*complete_list, sep ="  ")
        return

    if "-i" in args:
         show_info(path)



def files_folders(*args):
    args = list(args)[0].split(" ")

    if "ls" in args:
        show_all(args)






if __name__ == "__main__":
    while True:
        args = input(">> ")
        files_folders(args)

# ls print same line files folders -- OK
# ls -fi just files -- OK
# ls -i new line prin with info -- OK
#     list the file size | created date | owner

# ls <folder> name same line files folders from <folder>
