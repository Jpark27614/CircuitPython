"ultrasonic sensor"
import time
import board
import adafruit_hcsr04
import neopixel
import simpleio

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

while True:
    try:
        cm=int(sonar.distance)
        print((cm,))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

    if cm >= 0 and cm <=20:
         x=simpleio.map_range(cm, 5, 20, 0, 255)
         red=255-x
         green=0
         blue=x
         dot.fill((red,green,blue))
    
    elif cm >20:
        y=simpleio.map_range(cm, 20,35, 0, 255)
        blue=255-y
        red=0
        green=y
        dot.fill((red,green,blue))
    elif cm> 35:
        dot.fill((0,255,0))
