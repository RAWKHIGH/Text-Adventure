import random
import time

# Begining intro of the game
def GameStart():
	time.sleep(1)
	print
	print ("You are a young farmer's boy from Scotland")
	print ('you just witnessed a drunken kingsmen kill your father.')
	print ("ANGRY, you grab your grandfather's sword")
	print ("and head off after your father's killer.")
	print
	time.sleep(2)
	print ('You will need to sneak by the other kingsmen')
	print ('to find the killer')
	print ('one wrong move could cost you your life and honor')
	print 
	
def toll_1():
	choice = '0'
	while choice == '0':
		time.sleep(2)
		print ('You get to the trail but it splits')
		print ('To the East you hear the ramblings of 2 drunken kingsmen')
		print ('To the West you hear rustling in the bushes')
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
			print ('Invalid Choice')

def toll_2():
	choice2 = '0'
	while choice2 == '0':
		time.sleep(1)
		print
		print ('You slowly walk East')
		time.sleep(2)
		print
		print('you safely skirt around the drunken kingsmen by hiding in the bushes')
		print("the kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you smell cooking food')
		print ('To the West you hear what sounds like a blacksmith')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_4()
			choice2 = '1'
		elif path.lower() == 'w':
			toll_5()
			choice2 = '1'
		else:
			print ('Invalid Choice')
	
def toll_3():
	choice3 = '0'
	while choice3 == '0':
		time.sleep(1)
		print
		print ('You slowly walk West')
		time.sleep(2)
		print
		print('and a rabbit jumps out, startling you')
		print("the kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you see an outpost')
		print ('To the West you see a seemingly safe path')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_6()
			choice3 = '1'
		elif path.lower() == 'w':
			toll_7()
			choice3 = '1'
		else:
			print ('Invalid Choice')

def toll_4():
	choice4 = '0'
	while choice4 == '0':
		time.sleep(1)
		print
		print ('You slowly walk East')
		time.sleep(2)
		print
		print('you stumble upon an old outpost')
		print("the kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you ')
		print ('To the West you ')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_4()
			choice4 = '1'
		elif path.lower() == 'w':
			toll_5()
			choice4 = '1'
		else:
			print ('Invalid Choice')
		
def toll_5():
	choice5 = '0'
	while choice5 == '0':
		time.sleep(1)
		print
		print ('You slowly walk West')
		time.sleep(2)
		print
		print('hiding in a bush you see a kingsman working on his tools')
		print("the kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you ')
		print ('To the West you ')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_6()
			choice5 = '1'
		elif path.lower() == 'w':
			toll_7()
			choice5 = '1'
		else:
			print ('Invalid Choice')

def toll_6():
	choice6 = '0'
	while choice6 == '0':
		time.sleep(1)
		print
		print ('You slowly walk East')
		time.sleep(2)
		print
		print('the outpost is empty')
		print("the kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you ')
		print ('To the West you ')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_4()
			choice6 = '1'
		elif path.lower() == 'w':
			toll_5()
			choice6 = '1'
		else:
			print ('Invalid Choice')
		
def toll_7():
	choice7 = '0'
	while choice7 == '0':
		time.sleep(1)
		print
		print ('You slowly walk West')
		time.sleep(2)
		print
		print('the path is clear')
		print("the kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you ')
		print ('To the West you ')
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
		
		if path.lower() == 'e':
			toll_6()
			choice7 = '1'
		elif path.lower() == 'w':
			toll_7()
			choice7 = '1'
		else:
			print ('Invalid Choice')
		
def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		GameStart()
		toll_1()
		
		print
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()

if __name__ == "__main__": main()