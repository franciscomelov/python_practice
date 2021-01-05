import os
from os.path import isfile, join


def files_folders():
    path = os.getcwd()

    complete_list =sorted(os.listdir(path),key=str.lower)
    show_folder = input("Want to see folders ? Y   N: ").lower()

    if show_folder =="y":
        print(*complete_list, sep="\n")
    else:
        files_list = [f for f in complete_list if isfile(join(path, f))]
        print(*files_list, sep="\n")



if __name__ == "__main__":
    files_folders()

# ls print same line files folders
# ls -f just files
# ls -i new line prin with info
# ls <folder> name same line files folders from <folder>
