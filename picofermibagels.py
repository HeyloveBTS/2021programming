# -*- coding: utf-8 -*-
"""PicoFermiBagels.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wCZzvd_n_A1NOHGM-sa4XFl47ceOS5SX
"""

import random

#Player have 10 guesses in total
maxGuess = 10
playerGuess = 0

#Shuffle a number list
list_of_numbers = list(range(0,10))
random.shuffle(list_of_numbers)
if list_of_numbers[0] == 0: #The number should not start with a 0
  random.shuffle(list_of_numbers)
else:
  pass
print(list_of_numbers)

#Instructions for the game
print('I am thinking of a 3 digit number.')
print('Try to guess what it is.')
print('Here are some clues:')
print('When I say:    That means:')
print('  pico         One digit is correct but in the wrong position.')
print('  fermi        One digit is correct and in the right position.')
print('  bagels       No digit is correct.')
print('There are no repeated digits in the number.')

#Picking a three digit number
def shuffle():
  secretNo = ''
  for num in range(0,3):
    secretNo += str(list_of_numbers[num]) #Select the first three numbers in the list_of_numbers
  return secretNo

#Player input + Check if the player input the correct digits
def playGame():
  global playerGuess
  guess = input()
  while True:
    if len(guess) != 3:
      print("Sorry, please input a 3 digit number")
      guess = input() #The player try again
    else:
      break
  return guess

#Create a function for clue
def getClue(guess,secretNo):
  #Create clues -> when the player inserted partly correct
  clues = []
  for compare in range(0,3): #Compare player's guess and the actual secret number 1 by 1
    if guess[compare] == secretNo[compare]:
      clues.append("fermi")
    elif guess[compare] in secretNo:
      clues.append("pico")

  #When player did not guess any numbers correctly
  if len(clues) == 0:
    return'bagel'
    
  return ''.join(clues)

#Play again?
def restart():
    tryagain = input("Do you want to try again? yes or no")
    if tryagain == 'yes':
      global maxGuess
      maxGuess = 10
      global playerGuess 
      playerGuess = 0
    else:
      global game
      game = not True
      print("Ok! See you next time")

#Game code    
game = True

while game == True:
  secretNo = shuffle()
  print("You have",maxGuess,"guesses")

  while playerGuess < maxGuess:
    guess = playGame() # player guess

    #if player guess the correct number
    if guess == secretNo:
      print("Congrats, you got it!")
      tryagain = restart()
      break
      
    print(getClue(guess,secretNo)) #Print the computer's clue
    playerGuess +=1
    print("You have",maxGuess-playerGuess,"more guesses")


  if playerGuess == maxGuess: #When the player used up all the guesses
    print("Sorry, you have run out of guesses. The numbers are ", secretNo)
    tryagain = restart()
    break