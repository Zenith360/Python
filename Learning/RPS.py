# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 15:47:42 2016

@author: james
"""

"""ROck Paper Scissors mate"""

from random import randint;
from time import sleep;

options = ["R", "P", "S"];
lose = "You Lost!";
win = "You Won!";

def decide_winner(user_choice, computer_choice):
  print("You chose %s" % user_choice);
  print("Computer selecting...");
  sleep(1);
  print("Computer chose %s" % computer_choice);
  user_choice_index = options.index(user_choice);
  computer_choice_index = options.index(computer_choice);
  if(user_choice_index == computer_choice_index):
    print ("Tie...wow");
  elif(user_choice_index == 0 and computer_choice_index == 2):
    print(win);
  elif(user_choice_index == 1 and computer_choice_index == 0):
    print(win);
  elif(user_choice_index == 2 and computer_choice_index == 1):
    print(win);
  elif(user_choice_index > 2):
    print("Congrats you broke my code in a way that is impossible unless you actually changed my code...dont you have anything better to do with you life?");
  else:
    print(lose);
  
def play_RPS():
    print("W3lc0m3 t0 R0ck Pap3r Sciss0rs");
    user_choice = input("Put R for rock P for paper and S for sccissors/n");
    sleep(1);
    user_choice = user_choice.upper();
    computer_choiceIndex = randint(0, len(options)-1);
    computer_choice = options[computer_choiceIndex];
    decide_winner(user_choice, computer_choice);
    
    return;
    
play_RPS();