# -*- coding: utf-8 -*-
"""Blackjackgame_Lily.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zyqygPJAn4F9abppYFds7PA-7JmC-ASm
"""

import random
cards = list(range(3,10))

computerMove = []
playerMove = []

def shuffle():
  move = []
  global cards
  for moves in range(0,2):
    numbers = random.randint(3,10)
    move.append(numbers)
  return move

def addition():
  global playerMove
  global computerMove
  anotherOne = input("Do you want another additional cards? yes or no")
  if anotherOne == 'yes':
    additionalCards = random.randint(3,10)
    playerMove.append(additionalCards)
    return playerMove
  else:
    pass

def compare(computerMove,playerMove):
  if computerMove == 21:
    print("you lost!")
  elif playerMove == 21:
    print("you won!")
  elif computerMove > 21:
    print("you won!")
  elif playerMove > 21:
    print("you lost!")
  elif computerMove < 21 and computerMove > playerMove:
    print("even though nobody reaches 21, your sum is smaller than computer's. You lost!")
  elif playerMove < 21 and playerMove > computerMove:
    print("even though nobody reaches 21, your sum is greater than computer's. You won!")



computerMove = shuffle()
print("the computer's numbers are", computerMove[0], "and", computerMove[1], "which add up to", sum(computerMove))
playerMove = shuffle()
print("your numbers are", playerMove[0], "and", playerMove[1], "which add up to", sum(playerMove))

addition()
if len(playerMove) == 3:
  print("Ok! You got a new number:", playerMove[2], "so your sum is", sum(playerMove))
  compare(sum(computerMove),sum(playerMove))
else:
  compare(sum(computerMove),sum(playerMove))