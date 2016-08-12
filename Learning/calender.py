# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 21:55:43 2016

@author: james
"""

"""Calender"""
from time import *;
username = "James";
calendar = {
  
}
def welcome():
    print("Heyo: %s") % username;
    print("Calender Opening");
    sleep(1);
    print(strftime("%A %B, %Y"))
    print(strftime("%I:%M:%S"))
    sleep(1)
    print("What would you like to do?");
def start_calendar():
  welcome();
  start = True;
  while start:
      user_choice = raw_input("A to Add, U to Update, V to View, D to Delete: ");
      user_choice = user_choice.upper();
          if(user_choice == "V"):
              if len(calendar.keys()) < 1:
                  print("There is nothing to view in the calender");
        			else:
        				print(calendar);
    		elif user_choice == "U":
    			date = raw_input("What Date?");
    			update = raw_input("Enter the update: ");
    			calendar[date] = update;
    			print("Update sucessful?");
    			print(calendar);
    		elif user_choice == "A":
    			event = raw_input("Enter event: ");
    			date = raw_input("Enter date MM/DD/YYYY: ")
    			if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
    				print("Invalid date entered");
    				try_again = raw_input("Try Again? Y for Yes, N for No: ");
    				try_again = try_again.upper();
    				if try_again == "Y":
    					continue;
    				else:
    					start = start = False;
    			else:
    				calendar[event] = date;
    				print("Good Job");
    				print(calendar);
    		elif user_choice == "D":
    			if len(calendar.keys()) < 1:
    				print("Notin in calender cannot delte empty stuff");
    			else:
    				event = raw_input("What Event?");
    				for i in calendar.keys():
    					if event == calendar[date]:
    						del calendar[date];
    						print("Done");
    					else:
    						print("Wrong");
    		elif user_choice == "X":
    			start = False;
    		else:
    			print("Wrong");
    			print(user_choice);
    			start = False;
             
             
start_calendar();