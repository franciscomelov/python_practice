import os
from os.path import isfile, join

path = os.getcwd()
complete_list =sorted(os.listdir(path),key=str.lower)
folders = []
files = []

for file in complete_list:
    if isfile(join(path, file)):
        files.append(file)
        print(file)
    else:
        folders.append(file)

print(folders)