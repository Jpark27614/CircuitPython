# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
We were assigned to make the board light up and control the color of it. It also introduced importing libraries and an intro to circuit python.

Here's how you make code look like code:

```python
"Light up board"
import board
import neopixel

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((204, 0, 153))

```


### Evidence

![unnamed](https://user-images.githubusercontent.com/113122312/193068923-696fccd2-2f26-430c-8853-429a9b058300.jpg)

And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
No Wiring

### Reflection

This assignment was a good lesson in code and importing libraries. I learned to not crowd my circuit py with thousands of libraries and instead select individual ones. Also to find the libraries on the internet or assigment. I also learned about the different RGB colors and values with the line dot.fill((Red, Green, Blue)). overall this assignment was fun and a good into to circuit py.



## CircuitPython_Servo

### Description & Code

For this assignment we were assigned to make a servo go back and forth 180 and for the spicy part to make it move with a button.

```python
"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo #imports library
from digitalio import DigitalInOut, Direction, Pull 


btn1= DigitalInOut(board.D2)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

btn2= DigitalInOut(board.D3)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN


# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=100)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

angle = 90

while True:
    if btn1.value and angle <180: # states the condition of the if statement
        print("button 1 pressed") #prints to serial monitor
        angle = angle +5 
        my_servo.angle = angle
        time.sleep(0.1) #controls how much the servo moves
    elif btn2.value and angle >0:
        print("button 2 pressed")
        angle = angle -5
        my_servo.angle = angle 
        time.sleep(0.1)
    else:
        print("servo off")
        time.sleep(0.1)
  
```

### Evidence

https://user-images.githubusercontent.com/113122312/193072135-81b0ef1a-f0c4-47f9-9056-ee5ba5955ba4.mp4


### Wiring


### Reflection



## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence

### Wiring

### Reflection
