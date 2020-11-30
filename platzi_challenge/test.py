#game mastermind
#code breaking game

#X = not in phrase
#O = in phrase and in the right place
#A = in phrase but at the wrong place

import random

print('Mastermind !')

maxnumber=input('Input your maximum number between 4 and 9 (9 being the hardest) : ')

phrase = [random.randint(1,int(maxnumber))]
for x in range(3):
	a = random.randint(1,int(maxnumber))
	while a in phrase:
		a = random.randint(1,int(maxnumber))
	phrase.append(a)

playerphrase= 0000
counter = 0

maxcounter=input('How many turns do you want to give yourself (3 is not doable 4 is hard and it gets easier from 5 and above) : ')

print('\nA game where you try to figure out a phrase of 4 unique numbers between 1 and '+str(maxnumber)+'\nX = not in phrase\nO = in phrase and in the right spot\nA = in phrase but not in the right spot\nYou get '+str(maxcounter)+' tries\n\n')

while True:
	counter += 1
	checker =''
	playerphrase = input(str(counter)+' - Enter your phrase as a 4 digit number : ')
	print(playerphrase)
	for x in range(4):
		if (int(playerphrase[x]) in phrase) & (int(playerphrase[x]) != phrase[x]):
			checker = checker+'A'
		elif int(playerphrase[x]) == phrase[x]:
			checker = checker+'O'
		else:
			checker = checker+'X'
			
	print (checker)
			
	if checker == 'OOOO' :
		print ('You did it!')
		break
	else:
		if counter>=int(maxcounter):
			print('Better luck next time, the phrase was '+str(phrase))
			break