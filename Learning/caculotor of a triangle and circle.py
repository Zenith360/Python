""" Hello! In this Area Calculator you will be able to figure out the area of an object yay!"""
#if error switch input to raw_input since we're using the 
#old python :/
from math import pi;
#if error reput in from datetime import time :/
import time;
from datetime import datetime;

now = datetime.now();

print ("The caculator is starting up, actually it's just testing to test my sleep skills");

print ("%s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute));

time.sleep(1)

hint = ("Don't forget to include the correct units! \nExiting...");
option = input("Enter C for Cirlce or T for triangle: ");
option = option.upper();

if(option == "C"):
    radius = float(input("Radius, please: "));
    area = float(pi*radius**2);
    print("The pie is baking...");
    time.sleep(1);
    print("%.2f \n%s" % (area, hint));
elif(option == "T"):
    base = float(input("Base of triangle plez"));
    height = float(input("Height of the triange..."));
    area = float((base*height)/2);
    print("Uni Bi Tri...");
    time.sleep(1);
    print("%.2f \n%s" % (area, hint));
else:
    print("No clue what that was please actually put somthing worth my while/n....Exiting");