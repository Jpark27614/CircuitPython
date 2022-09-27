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

    