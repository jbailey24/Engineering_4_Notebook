# Engineering_4_Notebook

## Table of Contents
* [Python_Dice_Roller](#PythonDiceRoller)
* [Python_Calculator](#Python_Calculator)
* [Python Quadratic Solver](#Quadratic_Solver)
* [Python Strings and Loops](#Strings_and_Loops)
* [Python Man-Shaped Piñata](#Man-Shaped_Piñata)
* [Pi Blinking LEDs](#Blinking_LEDs)
* [Pi Shutdown Button](#Safe_restart_shutdown_interrupt)
* [Pi I2C](#I2C)

## Python_Dice_Roller


### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

![Screenshot of code](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8253.jpg?raw=true)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was definitely helpful because I haven't coded in Python in several months. Nesting the options menu took me a few tries to get right and I was wonderfully reawkened to the world of input().

## Python_Calculator

### Assignment Description
The purpose of this assignment was to create a program that takes two user-inputed numbers and finds their sum, difference, product, quotient, modulo, and both their factorials.
### Evidence 
![Screenshot of code](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8255.jpg?raw=true)

### Wiring
N/A

### Reflection

This was a good memory jog on how to format functions and definitely reminded me to watch my strings vs integers. Listing all the equation types as if statements in the function felt a bit clunky, but it works well. I initially started to write the code to calculate factorials from scratch, but python is great and math.factorial() has already been written for me, so I just had to import math and let it do its magic. 

## Quadratic_Solver

### Assignment Description
The purpose of this assignment was to create a program that takes a user inputed quadratic equation and returns the equation, the real roots, and the equation in vertex form. If the equation doesn't have real roots, the program just returns the equation. 

### Evidence 
![Screenshot of code](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/Screenshot%202021-09-21%20113645.png?raw=true)

### Wiring
N/A

### Reflection

I was able to reuse a good bit of code from the previous assignments, but figuring out how to call the real roots or not outside of the function was tricky. Also I had mostly forgotten how to find the vertex form of a quadratic equation, so writing somewhat concise code for that took a few iterations. I initially found some code online for finding the highest common demominator, but after struggling for a while to get it to work, I discovered that there is a hcf function in the python math library (which, don't get me wrong, was nice, but why couldn't I have dicovered that earlier!).  

## Strings_and_Loops

### Assignment Description
The purpose of this assignment was to create a program that splits an input into individual charaters using for loops. For example, "Hi There" would return "H,i,-,T,h,e,r,e,-". 
### Evidence 
![Screenshot of code](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/Screenshot%202021-09-21%20121400.png?raw=true)

### Wiring
N/A

### Reflection

I had no idea how versitile for loops were. I was trying to add in all this extra stuff into the for loops, and it turns out once I declare i, the computer's got it from there! Also the split() seems like a useful tool to have for future projects.  


## Man-Shaped_Piñata

### Assignment Description

The purpose of this assignment was to create a functioning hangman game (also known as a man-shaped piñata gmae). Player 1 enters in a word and player 2 is then prompted to guess letters in that word. If their guess is correct, the position of their guessed letter in the word is revealed. If their guess is incorrect, another peice of the piñata is built. If the piñata is fully built, player 2 looses the game. If player 2 can guess the entire word before the piñata is fully built, they win.

### Evidence 
![Screenshot of code](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/Screenshot%202021-10-05%20115445.jpg?raw=true)
![Screenshot of code](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/Screenshot%202021-10-05%20115624.jpg?raw=true)
### Wiring
N/A

### Reflection
This was a more challenging assignment. I was stuck for a long time in this assignment trying to replace the array of blanks with player 2's correct guess. I was attempting to get it to work with functions like 'pop()' and 'append()', but these functions just weren't able to do what I needed them to be able to. So, I learned the value of using my classmates as a resourse. Alden, who had already completed the assignment, used a different method to replace the array. I looked at his github and was able to adapt a few lines of his code to my logic (thank you Alden).  


## Blinking_LEDs

### Assignment Description

The purpose of this assignment was to create blinking LEDs using a Raspberry Pi and a T Cobbler. When one led turns on, the other turns off and vice versa.

### Evidence 
![Screenshot of LED blinking](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8669.jpg?raw=true)

### Wiring
![Screenshot of wiring](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8665.jpg?raw=true)
![Screenshot of wiring](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8666.jpg?raw=true)
### Reflection
Using BeagleTerm and a Raspberry Pi is a bit strange, but REMEMBER TO SHUTDOWN THE PI BEFORE CHANGING WIRING. It's very easy to forget. Googling is really your friend on these simple assignments. Looked up the GPIO library and had a solution in seconds. 


## Safe_restart_shutdown_interrupt

### Assignment Description

The purpose of this assignment was to create a button that can be pressed briefly to reboot the Raspberry Pi and held down to shut it down. It should be very useful as Pis need to be shutdown everytime they are removed from a computer. I followed and used the code from [this](
https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button/all) tutorial.

### Evidence 
![GIF of button working](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8712.GIF?raw=true)

### Wiring
![Screenshot of wiring](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8710.jpg?raw=true)

### Reflection
Even though I was following a tutorial, the button still didn't work the first time I tested it. Especially because of the layout of linux, it can be easy to make several small typos or mistakes that prevent your code from working. It takes a lot of meticulous rereading and double checking to find why your code might not be working. 

## I2C
### Assignment Description

The purpose of this assignment was to print accelerometer values on an OLED display using a Raspberry Pi and to learn the basics of I2C communication. 

### Evidence 
![GIF of data being displayed](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_8783.GIF?raw=true)

### Wiring
![picture of wiring](https://github.com/jbailey24/Engineering_4_Notebook/blob/main/Python/media/IMG_1575.jpg?raw=true)

### Reflection

The Raspberry Pi still struggles with occasionally timing out or not connecting to the internet. I had to reboot it many times. The example codes in the libraries of the accelerometer and display were very useful in figuring out how to get them working. Writing the code was as simple as stitching two of the example codes together. I also found it was much easier to write the code in Github and then 'git pull origin main' over in BeagleTerm than attempting to write the code directly in the terminal.
