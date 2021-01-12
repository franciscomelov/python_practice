import codecs
import re


file = codecs.open("index.html", "r", "utf-8")
count =0
for line in file:
    count +=1
    if "<a" in line:
        index_start = line.find('href="http')
        index_end = line.find('"', index_start+7)
        if index_start >0:
            #print("index: ",index_start, index_end)
            #print("linea",count, line, end="")
            print("link: ",line[index_start+6:index_end])
            #print("")
        
