#include <Wire.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"
import time
import board
import simpleio 
from analogio import AnalogIn
from pwmio import PWMOut


motor = PWMOut(board.D9)
potentiometer = AnalogIn(board.A1)  # potentiometer connected to A1, power & ground

while True:
    
    print((int(simpleio.map_range(potentiometer.value,0,65535,0,255))))
    time.sleep(0.25)                 
    motor.duty_cycle = potentiometer.value
