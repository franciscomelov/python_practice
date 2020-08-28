text = "freeCodeCamp, is an awesome resource"

finalText = "" # variable donde se guardara el nuevo texto



textArray = text.split() # array del texto searado por palabras

for word in textArray:
    finalText += word[0].capitalize() + word[1:] + " "






print(finalText)

# finalText =text[0].capitalize() + text[1:]  Solo una palabra
#finalText = " ".join([word[0].capitalize() + word[1:] for word in text.split()])

