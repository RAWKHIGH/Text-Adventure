# https://github.com/RAWKHIGH/Text-Adventure.git
# Name: Stephen McArthur
# Assinment 1
# Text Adventure 

# Import Statements
import random
import time

# Begining intro of the game
def GameStart():
	time.sleep(1)
	print
	print ("You are a young farmer's boy from Scotland")
	print ('You just witnessed a drunken kingsmen kill your father.')
	print ("ANGRY, you grab your Grandfather's sword")
	print ("You head off after your father's killer.")
	print
	time.sleep(2)
	print ('You will need to sneak by the other kingsmen')
	print ('to find the killer')
	print ('One wrong move could cost you your life and honor')
	print 

# First toll(desision)	
def toll_1():
	choice = '0'
	while choice == '0':
		time.sleep(2)
		print ('You get to the trail but it splits')
		print ('To the East you hear the ramblings of 2 drunken kingsmen')
		print ('To the West you hear rustling in the bushes')
		print
		print ('Would you like to go East or West? (e or w)')
		print
		path = raw_input()
# If what u entered = e or w it sends you to the appropiate destination else it repeats the question		
		if path.lower() == 'e':
			toll_2()
			choice = '1'
		elif path.lower() == 'w':
			toll_3()
			choice = '1'
		else:
			print ('Invalid Choice')

# Second toll(desision)
def toll_2():
	choice2 = '0'
	while choice2 == '0':
		time.sleep(1)
		print
		print('You safely skirt around the drunken kingsmen by hiding in the bushes')
		print("The kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you smell cooking food')
		print ('To the West you hear what sounds like a blacksmith')
		print ('You also hear rustling in the bushes to the South')
		print
		print ('Would you like to go East, West or South? (e or w or s)')
		print
		path = raw_input()
# If what u entered = e or w or s it sends you to the appropiate destination else it repeats the question		
		if path.lower() == 'e':
			toll_4()
			choice2 = '1'
		elif path.lower() == 'w':
			toll_5()
			choice2 = '1'
		elif path.lower() == 's':
			toll_3()
			choice2 = '1'	
		else:
			print ('Invalid Choice')

# Third toll(desision)			
def toll_3():
	choice3 = '0'
	while choice3 == '0':
		time.sleep(1)
		print
		print('A rabbit jumps out, startling you')
		print("The kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you see an outpost')
		print ('To the West you see a seemingly safe path')
		print ('You also hear the ramblings of 2 drunken kingsmen to the South')
		print
		print ('Would you like to go East, West or South? (e or w or s)')
		print
		path = raw_input()
# If what u entered = e or w or s it sends you to the appropiate destination else it repeats the question		
		if path.lower() == 'e':
			toll_6()
			choice3 = '1'
		elif path.lower() == 'w':
			toll_7()
			choice3 = '1'
		elif path.lower() == 's':
			toll_2()
			choice3 = '1'	
		else:
			print ('Invalid Choice')

# Fourth toll(desision)
def toll_4():
	choice4 = '0'
	while choice4 == '0':
		time.sleep(1)
		print
		print('You stumble upon an old outpost')
		print("The kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you see enterance 8 to the castle')
		print ('To the West you see enterance 7 to the castle')
		print ('You also hear what sounds like a blacksmith to the South')
		print
		print ('Would you like to go East, West or South? (e or w or s)')
		print
		path = raw_input()
# If what u entered = e or w or s it sends you to the appropiate destination else it repeats the question			
		if path.lower() == 'e':
			final_toll()
			choice4 = '1'
		elif path.lower() == 'w':
			final_toll()
			choice4 = '1'
		elif path.lower() == 's':
			toll_5()
			choice4 = '1'
		else:
			print ('Invalid Choice')

# Fifth toll(desision)			
def toll_5():
	choice5 = '0'
	while choice5 == '0':
		time.sleep(1)
		print
		print('Hiding in a bush you see a kingsman working on his tools')
		print("The kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you see enterance 3 to the castle')
		print ('To the West you see enterance 5 to the castle')
		print ('You also smell cooking food to the South')
		print
		print ('Would you like to go East, West or South? (e or w or s)')
		print
		path = raw_input()
# If what u entered = e or w or s it sends you to the appropiate destination else it repeats the question			
		if path.lower() == 'e':
			final_toll()
			choice5 = '1'
		elif path.lower() == 'w':
			final_toll()
			choice5 = '1'
		elif path.lower() == 's':
			toll_5()
			choice4 = '1'
		else:
			print ('Invalid Choice')

# Sixth toll(desision)			
def toll_6():
	choice6 = '0'
	while choice6 == '0':
		time.sleep(1)
		print
		print('The outpost is empty')
		print("The kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you see enterance 4 to the castle')
		print ('To the West you see enterance 2 to the castle')
		print ('You also see a seemingly safe path to the South')
		print
		print ('Would you like to go East, West or South? (e or w or s)')
		print
		path = raw_input()
# If what u entered = e or w or s it sends you to the appropiate destination else it repeats the question			
		if path.lower() == 'e':
			final_toll()
			choice6 = '1'
		elif path.lower() == 'w':
			final_toll()
			choice6 = '1'
		elif path.lower() == 's':
			toll_7()
			choice6 = '1'
		else:
			print ('Invalid Choice')

# Seventh toll(desision)			
def toll_7():
	choice7 = '0'
	while choice7 == '0':
		time.sleep(1)
		print
		print('The path is clear')
		print("The kingsman you're looking for isn't here")
		time.sleep(2)
		print
		print ('To the East you see enterance 1 to the castle')
		print ('To the West you see enterance 6 to the castle')
		print ('You also hear what sounds like a blacksmith to the South')
		print
		print ('Would you like to go East, West or South? (e or w or s)')
		print
		path = raw_input()
# If what u entered = e or w or s it sends you to the appropiate destination else it repeats the question			
		if path.lower() == 'e':
			final_toll()
			choice7 = '1'
		elif path.lower() == 'w':
			final_toll()
			choice7 = '1'
		elif path.lower() == 's':
			toll_6()
			choice7 = '1'
		else:
			print ('Invalid Choice')

# Final toll
# finalPath randomly picks a number between 1-8
# finalPath's random number than picks the ending that matches its number			
def final_toll():
	finalPath = random.randint(1, 8)
	if finalPath == 1:
		time.sleep(2)
		print
		print ('A wall top bowman sees you and snipes you out')
		print ('You took an arrow to the chest and die')
	elif finalPath == 2:
		time.sleep(2)
		print
		print ('Not paying close attention')
		print ('You step off a cliff and die')
	elif finalPath == 3:
		time.sleep(2)
		print
		print ('Running towards the castle you trip on a rock')
		print ('You impale yourself on a branch from a log and die')
	elif finalPath == 4:
		time.sleep(2)
		print
		print ('Sneaking towards the castle a kingsman sneaks up behind you')
		print ('He cuts off your head and you die')
	elif finalPath == 5:
		time.sleep(2)
		print
		print ('A young maiden courts you')
		print ('She stabs you and steals your gold, you die')
	elif finalPath == 6:
		time.sleep(2)
		print
		print ('The weather turns dark')
		print ('A bolt of lightning strikes you dead')
	elif finalPath == 7:
		time.sleep(2)
		print
		print ('A wild horse trots your way')
		print ('It tramples you and you die')
	elif finalPath == 8:
		time.sleep(2)
		print
		print ('You sneak up behing the kingsman who killed your father')
		print ("You stab him with your Grandfather's sword and he dies")

# Main Function		
def main():
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		GameStart()
		toll_1()
		
		print
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()

if __name__ == "__main__": main()