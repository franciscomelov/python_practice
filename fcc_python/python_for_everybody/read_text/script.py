# Print each line
xfile = open("texto.txt")
#for line in xfile: print(line)



#Reading whole file and save in variable
#inp = xfile.read()
#print(len(inp))


#Search through a file
for line in xfile:
    line = line.rstrip() #delete white space
    if line.startswith("Yo"):
        print(line)
