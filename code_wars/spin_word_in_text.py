def spin_words(sentence):
    sentence = sentence.split(" ")
    for word in range(len(sentence)):
        if len(sentence[word]) >=5:
            string  = list(sentence[word])
            sentence[word] = "".join(reversed(string))
    return " ".join(sentence)


#Spin word if >= than 5
print(spin_words("Hey fellow warriors"))
#Hey wollef sroirraw