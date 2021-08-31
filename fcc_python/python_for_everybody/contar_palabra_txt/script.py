handle = open("texto.txt","r")
counts = dict()
for line in handle:
    for word in line.split():
        counts[word] = counts.get(word,0) +1

for key, value in counts.items():
    print(key, value)