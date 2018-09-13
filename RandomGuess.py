#This script is a guess the number game
import random
print('Hi. What is you name?')
name = input()
secretNumber = random.randint(1,20)
print('Ok,  ' + name + ' I am thinking of a number between 1 and 20. Take a guess')

# ask the player to guess 6 times.
for guessesTaken in range (1,7):
	print('Take a guess.')
	guess = int(input())
	if guess < secretNumber:
		print('Your guess is too low, try again')
	elif guess > secretNumber:
		print( 'Your guess is too high, try again.')
	else:
		break #this condition would be the correct guess
if guess == secretNumber:
	print('Great, ' + name + ' ! You guessed my number. You took ' + str(guessesTaken) + ' guesses.')
else:	
	print('Nope. The number I was thinking of was'  + str(secretNumber))