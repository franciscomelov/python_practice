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

    get_max = lambda arr : max([len(str(i)) for i in arr])
    title = f'{"name".ljust(get_max(names), " ")} | {"size".ljust(get_max(sizes), " ")} | {"created at".ljust(get_max(times), " ")} | {"Owner".ljust(get_max(owners), " ")} | '
    print(f'{title}\n{len(title)*"-"}')
    for i, _ in enumerate(names):
        name = names[i].ljust(get_max(names), " ")
        size = str(sizes[i]).ljust(get_max(sizes), " ")
        time = times[i].ljust(get_max(times), " ")
        owner = str(owners[i]).ljust(get_max(owners), " ")
        extension = type_ext[i]
        print(f'{name} | {size} | {time} | {owner} | {extension}')


def show_all(args, path =os.getcwd()):
    complete_list =sorted(os.listdir(path),key=str.lower)
    if len(args) ==1:
        print(*complete_list, sep ="  ")
        return
    elif "-fi" in args[1]: 
        show_files(complete_list, path)
        return
    elif "-i" in args[1]:
        show_info(path)
        return
    elif "-" not in args[1]: #name folder as argument
        path = join(path,args[1])
        args.pop(1)
        show_all(args, path)


def files_folders(*args):
    args = list(args)[0].split(" ")

    if "ls" in args:
        show_all(args,)






if __name__ == "__main__":
    while True:
        args = input(">> ")
        files_folders(args)

# ls print same line files folders -- OK
# ls -fi just files -- OK
# ls -i new line prin with info -- OK
#     list the file size | created date | owner

# ls <folder> name same line files folders from <folder> -- OK
#   ls <folder> -flag