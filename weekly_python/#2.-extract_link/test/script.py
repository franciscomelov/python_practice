 #!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import html.parser as htmlparser
parser = htmlparser.HTMLParser()



file = codecs.open("index.html", "r", "utf-8")

count =0

titulos = ""
for line in file:
    if "data-title=" in line:
        count+=1
        index_start = line.find('data-title=')

        titulos += str(count) + ": "+ parser.unescape(line[index_start+5:-2]) + "\n"

print(count)
print(titulos)




