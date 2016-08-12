# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 12:24:19 2016

@author: james
"""

"""Dice game"""
from random import *
from time import *

def get_user_guess():
    user_guess = int(input("Guess the number"));
    return user_guess;
def roll_dice(number_of_sides):
    first_roll = randint(1, number_of_sides);
    second_roll = randint(1, number_of_sides)
    max_val = number_of_sides * 2;
    print("The max value is " + str(max_val));
    sleep(1);
    user_guess = get_user_guess();
    if(user_guess > max_val):
        print("Invalid number. Next time make sure your number is less than the max!");
        return;
    else: 
        print("Rolling...");
        sleep(2);
        print("The first roll is %d" % first_roll)
        sleep(1);
        print("The second roll is %d" % second_roll);
        sleep(1);
        total_roll = first_roll + second_roll;
        print("Your roll was... %d" % user_guess);
        print("Results....");
        sleep(1);
        if(user_guess > total_roll):
          	print("You won... bye");
          	return;
        else:
          	print("You lost");
          	return;
roll_dice(6);