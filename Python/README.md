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
* [Pi Headless Accelerometer](#Headless_Accelerometer)

## Python_Dice_Roller


### Assignment Description

The purpose of this assignment was to create a program that can automatically roll dice. The program also took user input to decide whether another dice should be rolled, or if the program should exit. The spicy version added complexity by asking the user to specify the number of sides on the dice and the number of dice to be rolled at a time. The user was then asked whether they wanted to roll again with the same settings, change the settings, or exit the program. 

### Evidence 

![Screenshot of code](https://user-images.githubusercontent.com/56133021/145438777-a774e7a3-914f-4f21-a6e9-df8dee5bde3b.jpg)

### Wiring

N/A

### Reflection

This assignment was relatively simple, but was definitely helpful because I haven't coded in Python in several months. Nesting the options menu took me a few tries to get right and I was wonderfully reawkened to the world of input().

## Python_Calculator

### Assignment Description
The purpose of this assignment was to create a program that takes two user-inputed numbers and finds their sum, difference, product, quotient, modulo, and both their factorials.
### Evidence 
![Screenshot of code](https://user-images.githubusercontent.com/56133021/145438769-f6dbd721-f0f5-435c-b280-e7c6150756af.jpg)

### Wiring
N/A

### Reflection

This was a good memory jog on how to format functions and definitely reminded me to watch my strings vs integers. Listing all the equation types as if statements in the function felt a bit clunky, but it works well. I initially started to write the code to calculate factorials from scratch, but python is great and math.factorial() has already been written for me, so I just had to import math and let it do its magic. 

## Quadratic_Solver

### Assignment Description
The purpose of this assignment was to create a program that takes a user inputed quadratic equation and returns the equation, the real roots, and the equation in vertex form. If the equation doesn't have real roots, the program just returns the equation. 

### Evidence 
![Screenshot of code](https://user-images.githubusercontent.com/56133021/145438036-ec66d573-f9b4-4d26-a0a9-1955e9baadf6.png)

### Wiring
N/A

### Reflection

I was able to reuse a good bit of code from the previous assignments, but figuring out how to call the real roots or not outside of the function was tricky. Also I had mostly forgotten how to find the vertex form of a quadratic equation, so writing somewhat concise code for that took a few iterations. I initially found some code online for finding the highest common demominator, but after struggling for a while to get it to work, I discovered that there is a hcf function in the python math library (which, don't get me wrong, was nice, but why couldn't I have dicovered that earlier!).  

## Strings_and_Loops

### Assignment Description
The purpose of this assignment was to create a program that splits an input into individual charaters using for loops. For example, "Hi There" would return "H,i,-,T,h,e,r,e,-". 
### Evidence 
![Screenshot of code](https://user-images.githubusercontent.com/56133021/145438037-3765d85d-1c7a-4d59-9a17-d181564f9de9.png)

### Wiring
N/A

### Reflection

I had no idea how versitile for loops were. I was trying to add in all this extra stuff into the for loops, and it turns out once I declare i, the computer's got it from there! Also the split() seems like a useful tool to have for future projects.  


## Man-Shaped_Piñata

### Assignment Description

The purpose of this assignment was to create a functioning hangman game (also known as a man-shaped piñata gmae). Player 1 enters in a word and player 2 is then prompted to guess letters in that word. If their guess is correct, the position of their guessed letter in the word is revealed. If their guess is incorrect, another peice of the piñata is built. If the piñata is fully built, player 2 looses the game. If player 2 can guess the entire word before the piñata is fully built, they win.

### Evidence 
![Screenshot of code](https://user-images.githubusercontent.com/56133021/145438007-bb34690c-2347-48eb-a464-c166bec158b3.jpg)
![Screenshot of code](https://user-images.githubusercontent.com/56133021/145438009-8674eeb5-500a-496a-b99f-0dfe221768da.jpg)
### Wiring
N/A

### Reflection
This was a more challenging assignment. I was stuck for a long time in this assignment trying to replace the array of blanks with player 2's correct guess. I was attempting to get it to work with functions like 'pop()' and 'append()', but these functions just weren't able to do what I needed them to be able to. So, I learned the value of using my classmates as a resourse. Alden, who had already completed the assignment, used a different method to replace the array. I looked at his github and was able to adapt a few lines of his code to my logic (thank you Alden).  


## Blinking_LEDs

### Assignment Description

The purpose of this assignment was to create blinking LEDs using a Raspberry Pi and a T Cobbler. When one led turns on, the other turns off and vice versa.

### Evidence 
![Screenshot of LED blinking](https://user-images.githubusercontent.com/56133021/145438758-6dc730cd-d2d0-496c-9c63-38d909cc27bb.jpg)

### Wiring
![Screenshot of wiring](https://user-images.githubusercontent.com/56133021/145438757-f97f84fe-76b8-4fd7-8006-d253a41add88.jpg)
![Screenshot of wiring](https://user-images.githubusercontent.com/56133021/145440749-da90380f-76e6-4889-b6d5-a6063ebe1ef3.jpg)
### Reflection
Using BeagleTerm and a Raspberry Pi is a bit strange, but REMEMBER TO SHUTDOWN THE PI BEFORE CHANGING WIRING. It's very easy to forget. Googling is really your friend on these simple assignments. Looked up the GPIO library and had a solution in seconds. 


## Safe_restart_shutdown_interrupt

### Assignment Description

The purpose of this assignment was to create a button that can be pressed briefly to reboot the Raspberry Pi and held down to shut it down. It should be very useful as Pis need to be shutdown everytime they are removed from a computer. I followed and used the code from [this](
https://learn.sparkfun.com/tutorials/raspberry-pi-safe-reboot-and-shutdown-button/all) tutorial.

### Evidence 
![GIF of button working](https://user-images.githubusercontent.com/56133021/145439622-e5232663-9424-425f-8e60-e0621f5c1828.gif)

### Wiring
![Screenshot of wiring](https://user-images.githubusercontent.com/56133021/145439623-05d9c089-4df5-4247-9847-3397c9bc3653.jpg)

### Reflection
Even though I was following a tutorial, the button still didn't work the first time I tested it. Especially because of the layout of linux, it can be easy to make several small typos or mistakes that prevent your code from working. It takes a lot of meticulous rereading and double checking to find why your code might not be working. 

## I2C
### Assignment Description

The purpose of this assignment was to print accelerometer values on an OLED display using a Raspberry Pi and to learn the basics of I2C communication. 

### Evidence 
![GIF of data being displayed](https://user-images.githubusercontent.com/56133021/145442297-0760cb4b-4f19-49a8-aa40-97851a91f223.gif)

### Wiring
![picture of wiring](https://user-images.githubusercontent.com/56133021/145439649-ced70adf-44d6-4267-b332-1666db4fbee3.jpg)

### Reflection

The Raspberry Pi still struggles with occasionally timing out or not connecting to the internet. I had to reboot it many times. The example codes in the libraries of the accelerometer and display were very useful in figuring out how to get them working. Writing the code was as simple as stitching two of the example codes together. I also found it was much easier to write the code in Github and then 'git pull origin main' over in BeagleTerm than attempting to write the code directly in the terminal.


## Headless_Accelerometer
### Assignment Description
The goal of this assignment was to use what we learned about the accelerometer and display in the last assignment to create a simple visual that changes in some way depending on the data collected by the accelerometer. I decided to have an ellipse that changes width or height based on the x or y direction acceleration. Additionally, the code had to run on startup of the Pi.

### Evidence 
![GIF of data being displayed](https://user-images.githubusercontent.com/56133021/145443923-5fa63a96-4e7e-4f54-b363-b20662eff659.gif)

### Wiring
![picture of wiring](https://user-images.githubusercontent.com/56133021/145439649-ced70adf-44d6-4267-b332-1666db4fbee3.jpg)

### Reflection
I used the code from shapes.py to figure out how to draw ellipses on the display. It took a couple of tries to scale the data correctly and keep the ellipse centered. Getting it to run on startup wasn't too difficult, although I mistyped one line, which caused me to have to spend 5 minutes trying to fix it. 

