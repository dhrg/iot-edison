import mraa
from time import sleep
import temp
import led
import lcd
import math
import sys
import uv
from pyupm_grove import GroveLight, GroveButton

# init LCD, LED, Light Sensor, Button and Touch Sensor
lcd.init_lcd()                 # LCD is on any I2C 
led.init_led(5)                # LED on D5
led.write_led(0) 
lux = GroveLight(0)            # LUX on A0
button = mraa.Gpio(3)          # Button on D3
button.dir(mraa.DIR_IN)
touch = mraa.Gpio(2)           # Touch sensor on D2
touch.dir(mraa.DIR_IN)         
relay = mraa.Gpio(7)           # Relay on D7
relay.dir(mraa.DIR_OUT)        

# togle state memory
class Toogle:
    state = 0

tog = Toogle()

# ISR 
def pressed(args):
    if tog.state==0:
        tog.state=1
        led.write_led(1)
        relay.write(1)
    else:
        tog.state=0;
        led.write_led(0)
        relay.write(0)

# ISR installing for Button and Touch Sensor

while True:
    # read temperature and lux and print on LCD
    t = temp.read_temp()
    string1= t + " C" + ", " + str(lux.value()) + " lux"
    string2= "UV: " + uv.read_uv(2)
    
    # if night/dark switch on LCD backlight
    if (lux.value() < 10):
        lcd.write_lcd(string1,string2,255,255,255,0,1)
    else:  
        lcd.write_lcd(string1,string2,40,40,40,0,1)

    # insall isr on button and touch pin
    button.isr(mraa.EDGE_RISING, pressed, button)
    touch.isr(mraa.EDGE_RISING, pressed, touch)

    sleep(0.3)
