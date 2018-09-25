import random

fr = open("musicASCII.txt", "r")
while True:
	line = fr.readline()
	print(line[:-1])
	if len(line) == 0:
		break
print("\n")

fr = open("HMwords.txt", "r")
allWords = fr.readlines()
fr.close()

def buildGame():
	goal = allWords[random.randrange(0, len(allWords) )].upper()
	allWords.remove(goal.lower()) #for replayability
	goal = goal[:-1] #removes character '\n'
#	print(goal)
	
	lives = 6
	guessHist = []
	progress = []
	
	print('\n')
	print("Here is your word")
	for letter in range(len(goal)):
		print("_", end=" ")
		progress.append("_")
	print('\n')
	
	return goal, progress, lives, guessHist

def diagram():
	for i in range(19):
		line = trebleMan.readline()
		print(line[:-1])

def finalRound(guess):
	global gameActive
	if guess==goal:
		print("Well done!\n")
	else:
		trebleMan.seek(0)
		for i in range(114):
			trebleMan.readline()
		diagram()
		print("Music has DIED")
		print("The word was '{}'\n".format(goal))
	gameActive = False

def singleRound(guess):
	global progress
	global lives
	global gameActive
	
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
	
	if "_" not in progress:
		print("You win!\n")
		gameActive = False
	
	if loss:
		lives -= 1
		diagram()
		if lives==0:
			print("Music has DIED")
			print("The word was '{}'\n".format(goal))
			gameActive = False

def play(guess):
	if len(guess)==len(goal):
		finalRound(guess)
	elif guess in guessHist:
		print("You have already guessed '{}'".format(guess))
	elif len(guess)!=1 or ord(guess) > 90 or ord(guess) < 65:
		print("Please guess either a single letter or the full word")
	else:
		singleRound(guess)
	guessHist.append(guess)

while True:
	goal, progress, lives, guessHist = buildGame()
	trebleMan = open("hangTreble.txt", "r")
	gameActive = True
	while gameActive:
		guess = input().upper()
		if guess=="QUIT": break
		play(guess)
	trebleMan.close()
	
	if len(allWords) < 1:
		print("Sorry, fresh out of words!")
		break
	
	while True:
		print("Would you like to play again? (y/n)")
		ans = input().upper()
		if 'Y' in ans: break
		elif 'N' in ans: break
	if 'N' in ans:
		break	 

print("Thx for playing <3")
