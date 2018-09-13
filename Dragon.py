#Dragon
import random
import time

def displayIntro():
    print('You are in land of Dragons')
    print('you see 2 caves')
    print('In one cave the dragon is ferocious and he will eat you')
    print( 'In the other cave the dragon is friendly and will give you a treasure')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('which cave will you enter?')
        print ('enter 1 or 2')
        cave= input()
        return cave   

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print ( 'A large dragon jumps out in front of you! He opens his mouth and ...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print ('Gives you his treasure!')
    else:
        print('Eats you')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':

       displayIntro()

       caveNumber = chooseCave()

       checkCave(caveNumber)
       print ('Do you want to play again? (yes or no)')
       playAgain = input()
       
