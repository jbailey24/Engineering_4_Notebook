# Automatic Dice Roller
# Written by Julia Bailey

from random import randint

sides = 6
dice = 1

print("Automatic Dice Roller")
print("Press Enter to roll")
print("Enter x to quit")
imp = input("Enter c to customize")
    
while True:
    
    if imp == "x":
        break
    
    if imp == 'c':
        print("Enter s to change number of sides")
        imp2 = input("Enter d to change number of dice")
        
        if imp2 == "s":
            sides = input("How many sides?")
            imp = 'back'
        if imp2 == "d":
            dice = input("How many dice?")
            imp = 'back'
        
    else:
        for x in range(int(dice)):
            print((randint(1,int(sides))))
        
        imp = input("Enter c for options")
        
    print()
