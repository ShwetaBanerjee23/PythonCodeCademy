# language used: Python 2

""" This is a Number Guess game. The program rolls a pair of dice and calculates the total value of the dice roll. The user has to guess the sum. If the user guesses correctly, they win! Otherwise the computer wins. """

from random import randint
from time import sleep


def get_user_guess():
  """ This function prompts the user for their guess """
  guess = int(raw_input("Guess a number: "))
  return guess


def roll_dice(numberOfSides):
  """ This function simulates the dice rolling and depending on the user's guess decides whether it is the user or the computer that wins """

  first = randint(1, numberOfSides)
  second = randint(1, numberOfSides)

  # maximum value that the program can possibly roll depending on specificied numberOfSides
  maxVal = numberOfSides * 2
  print "%d is the maximum possible value that can be rolled with two dice" % (maxVal)
  
  # prompts user for a guess until the guess entered is a valid integer
  valid = False
  
  while not valid:
    try:
      
      guess = get_user_guess()
      
      if guess > maxVal or guess <= 0:
        print "Invalid input. Please guess a number less than the maximum value that can be obtained by rolling the two dice and greater than 0."
      else:
        print("Rolling...")
        sleep(2)
        print "The first dice rolled a %d" % (first)
        sleep(1)
        print "The second dice rolled a %d" % (second)
        sleep(1)

        total = first + second

        print "The total is %d" % (total)
        print "Result..."
        sleep(1)

        if guess == total:
          print "You win!"
        else:
          print "Computer wins!"
        
        valid = True

    except ValueError:
      print "Please enter integers only!"

roll_dice(6)
