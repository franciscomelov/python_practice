def anagrams(word, words):
    for i in words:
        word_2 = word
        from_words = i
        testing =""
        yes =[]
        if len(word_2) == len(from_words):
            testing = from_words
            while True:
                
                word_2 = list(word_2)
                from_words =list(from_words)
                if from_words[0] in word_2:
                    word_2.remove(from_words[0])
                    from_words.remove(from_words[0])
                else:
                    break



                if len(from_words) == 0 and len(word_2) == 0:
                    yes.append(testing)
                    break
    print(yes)

        
    #your code here

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) #['carer', 'racer'