import random as r
print("Hello welcome to Adv/DAdv Dice Roller.\nAre you rolling with (A)dvantage or (D)isadvantage?")
inplay = True;
while(inplay):
    choice1 = input("A or D?\n");
    choice1 = str.upper(choice1)
    mod = input("Whats your modifer, just put +X or -X\n")
    if(mod[0] == "+"):
        modNum = int(mod[1:])
        #print(modNum)          #debugging purposes
    elif(mod[0] == "-"):
        modNum = -int(mod[1:])
        print(modNum)
    else:
        print("Please put yout modifer in the following format +X or -X")
        choice1 = "BAD INPUT"
    if(choice1 == "A"):
        print("Rolling with Advantage I see, nice!")
        dice1 = r.randint(1, 20);
        dice2 = r.randint(1, 20);
        #print(dice1, dice2, sep= " ")  #debugging purposes
        if(dice1 > dice2):
            fDice = dice1
        else:
            fDice = dice2

        if(fDice == 20):
            print("Natural 20!!")
        elif(fDice == 1):
            print("Crit fail! With Advantage, dang!")
        elif(fDice <= 9):
            print("Oooo, sad-vantage :(")
        
        if((fDice-modNum) < 1):
            print("Well you got below a zero which is just a 1")
            print("Total is a 1! (The subzero number is: " +  str(fDice+modNum) + ")");
        else:
            print("Total is a " + str(fDice+modNum) + "!");
    if(choice1 == "D"):
        print("Rolling with Disadvantage I see, may Rudd's blesssing be upon ye!")
        dice1 = r.randint(1, 20);
        dice2 = r.randint(1, 20);
        #print(dice1, dice2, sep= " ")  #debugging purposes
        if(dice1 < dice2):
            fDice = dice1
        else:
            fDice = dice2
        if(fDice == 20):
            print("Natural 20 with disadvantage, WOW")
        elif(fDice == 1):
            print("Crit fail! Rats")
        if((fDice+modNum) < 1):
            print("Well you got below a zero which is just a 1")
            print("Total is a 1! (The subzero number is: " +  str(fDice+modNum) + ")");
        else:
            print("Total is a " + str(fDice+modNum) + "!");

