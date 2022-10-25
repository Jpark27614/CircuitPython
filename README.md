# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython Sensor](#CircuitPython_Ultrasonic_Sensor)
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

![Magnificent Esboo-Fulffy](https://user-images.githubusercontent.com/113122312/193298186-b576e8db-4a3c-4f32-9f25-337945b12ca3.png)

### Reflection

This assignment was very challenging and reinversed me into coding again. I was still ajusting to python so I used a refrence online using the adafruit website. For the button I had to learn how to code buttons in python with the help of the adafruit website and peers (mostly matthew) once I knew the buttons were working I inputed the condition (<180) and how much the servo moves (angle=angle+5) after that it was still iffy so I asked Mr. H for help. This assignment was informative and very challenging, it was a good assignment for python and I now know a lot more about python.

## CircuitPython_LCD

### Description & Code

We were assigned to use an LCD backpack to count the number of times the button was pressed and (in this case) if the switch was "up" or "down"

```python
import board

#input libraries
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull 

#sets buttons and switch as Inputs 
btn= DigitalInOut(board.D9)
btn.direction = Direction.INPUT
btn.pull = Pull.DOWN

switch = DigitalInOut(board.D10)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

value = 0 #sets the value to 0 to count up from there
SwitchState = switch.value

lcd.print("Button:") 
lcd.set_cursor_pos(0,8) #sets position of the LCD in the 2 by 16 grid

prev_state = btn.value

while True: #sets button to add up and not count when held down
    cur_state = btn.value
    if cur_state != prev_state:
        if not cur_state:
            value+=1
            lcd.set_cursor_pos(0,8)
            lcd.print(str(value))
    if switch.value == True: # prints switch is up if switch value is true
      lcd.set_cursor_pos(1,0)
      lcd.print("Up  ")
    else: #if the switch isn't true then it prints "down"
      lcd.set_cursor_pos(1,0) 
      lcd.print("Down")

    prev_state = cur_state
 

```

### Evidence

https://user-images.githubusercontent.com/113122312/197560238-b7a8103e-4618-45dc-b2e6-a44944bc3f0a.mp4


### Wiring

![Screenshot 2022-10-24 111225](https://user-images.githubusercontent.com/113122312/197561563-2dc43b58-a914-4b52-9279-a19577b89128.png)


### Reflection

This assignment was challenging but fun, I definitly needed outsdide help. One problem I faced was working with the libraries and getting familiar with the code for the LCD. Another was after I did it in the serial monitor I had to move it to the LCD; I fixed this by instead of Serial.print I used lcd.print and then set a coordinate on the LCD. I also had trouble making sure that the button only counts once when held down, I asked Matthew to help me and I used prev and current state to make sure when it reads the last state if it's different then it stops counting. Lastly I had issues with printing the switch but then I learned that it is very similar to the button. Overall this assignment helped me to better understand LCDs and printing & reading values.

## CircuitPython_Ultrasonic_Sensor


### Description & Code

For this assignment we were supposed to make the board light up different colors based on the different distances from the LCD. For the spicy part we were supposed to keep these colors but make it fade from the RGB values.

```python
"ultrasonic sensor"
#imports variable
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

#connects to board light
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

#sets pins for sensor
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        cm=int(sonar.distance)
        print((cm,))
    except RuntimeError:  
        print("Retrying!") #print to monitor
    time.sleep(0.1)

    if cm >= 0 and cm <=20: #shows range of the if satement
         x=simpleio.map_range(cm, 5, 20, 0, 255) #maps one value to another
         red=255-x
         green=0
         blue=x
         dot.fill((red,green,blue)) #fades colors
    
    elif cm >20: 
        y=simpleio.map_range(cm, 20,35, 0, 255)
        blue=255-y
        red=0
        green=y
        dot.fill((red,green,blue))
    elif cm> 35:
        dot.fill((0,255,0))


```

### Evidence

![ezgif-1-1bf9b3c9d8](https://user-images.githubusercontent.com/113122312/197564301-66d1a245-6b8b-4826-96ff-5e0ea7abb789.gif)

### Wiring
(https://user-images.githubusercontent.com/113122357/197229576-1ee94bfb-3387-4934-84f3-4033f21a40d9.png)
*credit to Dylan Halbert*
### Reflection
For the first part of this assignment it wans't that hard because it was just reading values from the sensor to print a color. For the second part it was a lot harder because I had to make the board fade through the colors. At first I was struggling a lot to get it to fade and didn't know I had to use maps. I asked Matthew for help and he explained how I need to map the values for the colors and use dot.fill((red, green,blue)) to fill in the colors to fade. Then, he explained the math of the RGB and the variables like x. The variables like x and 255 minus x are so that when 1 color goes up the other goes down. Also I was struggling with the condition but I learned you can put a limit in one line like cm >= 0 and cm <=20. Overall this assignment was difficult but informitive, it helped me to better understand maps and variables.

# CAD

## Table of contents
* [Launcher](#Launcher)
* [Swing Arm](#Swing Arm)
* [Multi Part Studio](#Multi Part Studio)

## Launcher

### Description

For this assignment we were assigned to a partner to create a launcher splitting the work half and half. There was also branching involved in this assignment with seperate workspaces and different onshape techniques.

### Evidence 

[onshape link](https://cvilleschools.onshape.com/documents/48111212671d7a3e3e18628f/w/cebe40ddfbbd8f11bf9459b8/e/6bdc8776a13d74f69e66bf52)

### Image 

![image](https://user-images.githubusercontent.com/113122312/197812475-21b55cd1-3b50-4481-8774-6feef31210a7.png)


### Reflection
