import random

fr = open("HMwords.txt", "r")
allWords = fr.readlines()
fr.close()

def buildGame():
	goal = allWords[random.randrange(0, len(allWords) )]
	goal = goal[:-1] #removes character '\n'
	lives = 6
	#print(goal)
	
	progress = []
	for letter in range(len(goal)):
		print("_", end=" ")
		progress.append("_")
	print("\n")
	#print(progress)
	
	return goal, progress, lives

#def finalRound():
	

def singleRound(guess):
	global progress
	global lives
	i = 0
	loss = True
	for letter in goal:
		if guess==letter:
			print(letter, end=' ')
			progress[i] = letter
			loss = False
		else:
			print(progress[i], end=' ')
		i += 1
	print("\n")
	if loss:
		#call diagram(lives - 1)
		lives -= 1
		if lives==0:
			#more
			print("you lose")
			print("The word was {}".format(goal))

def play(guess):
	if len(guess)>1:
		print("") #one round
	else:
		singleRound(guess)

goal, progress, lives = buildGame()
while True:
	guess = input()
	if guess=="quit": break
	play(guess)
