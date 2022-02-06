""" Welcome to Rock, Paper, Scissors! This program prompts the user to select Rock, 
Paper, or Scissors. Then the computer randomly selects one of the three and compares 
it with the user's choice to determine the winner. """

import random

options = ["rock", "paper", "scissors"]

message = {
  "tie" : "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
}


def winner(cmpChoice, usrChoice):
  print
  print "User choice: %s" % usrChoice
  print "Computer choice: %s" % cmpChoice
  print

  if usrChoice == cmpChoice:
    print message["tie"]
  elif (usrChoice == "rock" and cmpChoice == "scissors") \
  or (usrChoice == "paper" and cmpChoice == "rock") \
  or (usrChoice == "scissors" and cmpChoice == "paper"):
    print message["won"]
  else:
    print message["lost"]


def play():
  valid = False
  while not valid:
    usrChoice = raw_input("Choose rock, paper, or scissors: ")
    lower = usrChoice.lower()
    if lower in options:
      valid = True
    else:
      print "Invalid input: Not an option"

  cmpChoice = options[random.randint(0, 2)]

  winner(cmpChoice, lower)

play()
