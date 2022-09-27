"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo #imports library

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=100)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm, min_pulse=500, max_pulse=2500)

while True: #loop
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02) #defines the rate that the servo moves
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.02)
  