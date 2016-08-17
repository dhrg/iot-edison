import mraa     # For accessing the GPIO
import time     # For sleeping between blinks

global led

def init_led(pin):
    global led
    led = mraa.Gpio(pin)        # Get the LED pin object
    led.dir(mraa.DIR_OUT)       # Set the direction as output
    led.write(0)

def write_led(signal):
    global led
    led.write(signal)

def main():
    pin = 5                   # we are using D5 pin
    led = mraa.Gpio(pin) # Get the LED pin object
    led.dir(mraa.DIR_OUT)     # Set the direction as output
    ledState = False               # LED is off to begin with
    led.write(ledState)

    # One infinite loop coming up
    while True:
        if ledState == False:
            # LED is off, turn it on
            led.write(1)
            ledState = True        # LED is on
        else:
            led.write(0)
            ledState = False

        print "LED is: %s" %(ledState)
   	    # Wait for some time
        time.sleep(1)


if __name__ == '__main__':
    main()
    del led