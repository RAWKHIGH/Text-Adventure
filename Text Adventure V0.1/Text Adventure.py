import random
import time

# Begining intro of the game
def GameStart():
	print ("you are a young farmer's boy from Scotland")
	print ('you just witnessed a drunken kingsmen kill your father.')
	print ("ANGRY, you grab your father's, father's sword")
	print ("and head off after your father's killer")
	print
	print ('you will need to sneak by the other kingsmen')
	print ('to find the killer')
	print ('one wrong move cound cost you your life and honor')
	print 
	
def choosePath1():
	path1 = ''
	while path1 != 'e' and path1 != 'w':
		print ('You get to the trail but it splits')
		print ('Too the East you hear the ramble of 2 drunken kingsmen')
		print ('Too the West you hear rustling in the bushes')
		print ('Would you like to go East or West? (e or w)')
		path1 = raw_input()
	return path1
	
def checkPath1(chosenPath1):
	print ('You approach the cave...')
	time.sleep(2)
	print ('It is dark and spooky...')
	time.sleep(2)
	print ('A large dragon jumps out in front of you! He opens his jaws and...')
	print
	time.sleep(2)

	safePath1 = random.randint(1, 2)
	if safePath1 == 1:
		direction = 'east'
	else:
		direction = 'west'
	
	if chosenPath1 == str(direction):
		print ('Gives you his treasure!')
	else:
		print ('Gobbles you down in one bite!')

def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		GameStart()
		caveNumber = choosePath1()
		checkPath1(caveNumber)
	
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()