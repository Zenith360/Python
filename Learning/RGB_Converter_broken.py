# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 09:36:49 2016

@author: james
"""

"""RGB CONVERTOR"""
def chk_color(c):
  invalid_msg = "WRONG";
  if(c < 0 or c > 255):
    print(invalid_msg) 
    return False
  else:
  	return True
   
def get_color(name, value):
  value = int(input("Enter " + name +" value: "));
  return chk_color(value)

def rgb_hex():
  red = 0;
  if(not get_color("Red", red)):
    return;
  green = 0;
  if(not get_color("Green", green)):
    return;
  blue = 0;
  if(not get_color("Blue", blue)):
    return;
  val = (red << 16) + (green << 8) + blue
  print(hex(val)[2:].upper())


def hex_rgb():
  hex_val = input("Enter a hexidec value");
  if(len(hex_val) != 6):
    print("WRONG");
    return;
  else:
    hex_val = int(hex_val, 16);
  two_hex_digits = 2**8;
  blue = hex_val % two_hex_digits
  hex_val >> 8;
  green = hex_val % two_hex_digits
  hex_val >> 8;
  red = hex_val % two_hex_digits
  print("Red: %s Green: %s Blue: %s" % (red, green, blue))
def convert():
  while(True):
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if(option == "1"):
      print("RGB to Hex")
      rgb_hex();
    elif(option == "2"):
      print("Hex to RGB");
      hex_rgb()
    elif(option == "x" or option == "X"):
      break;
    else:
      print("Error");
      
convert()