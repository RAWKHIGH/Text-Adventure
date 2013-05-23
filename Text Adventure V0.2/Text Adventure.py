import random
import time

# Begining intro of the game
def GameStart():
	print
	print ("you are a young farmer's boy from Scotland")
	print ('you just witnessed a drunken kingsmen kill your father.')
	print ("ANGRY, you grab your father's, father's sword")
	print ("and head off after your father's killer.")
	print
	print ('You will need to sneak by the other kingsmen')
	print ('to find the killer')
	print ('one wrong move cound cost you your life and honor')
	print 
	
def toll_1():
	choice = '0'
	while choice == '0':
		print ('You get to the trail but it splits')
		print ('Too the East you hear the rambling of 2 drunken kingsmen')
		print ('Too the West you hear rustling in the bushes')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_2()
			choice = '1'
		elif path.lower() == 'w':
			toll_3()
			choice = '1'
		else:
			print ('wrong')

def toll_2():
	print
	print ('You slowly walk East')
	print('')
	
def toll_3():
	print
	print ('You slowly walk West')
	print('')
	
def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		GameStart()
		toll_1()
		
		print
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()