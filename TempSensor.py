
import time
import board
import analogio 
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = board.I2C()
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

sensor=analogio.AnalogIn(board.A0)

def tempOut (x):
    if x > 79:
        return "Too hot"
    if 77 < x < 79 :
        return "nice"
    if x < 77:
        return "Brrr it's cold"

while True:
    celcius= (((sensor.value/19859.0909091)*1000)-500)/10
    farenheit= (celcius*9/5)+32

    lcd.print(tempOut(farenheit))
    lcd.set_cursor_pos(1,0)
    print(str(farenheit))
    time.sleep(.05)
    lcd.clear()
    

