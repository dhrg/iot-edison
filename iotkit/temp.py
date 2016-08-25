#!/usr/bin/python

import mraa
import time
import math

# More info here -> http://www.seeedstudio.com/wiki/Grove_-_Temperature_Sensor
def read_temp():
    B=3975
    ain = mraa.Aio(1)
    a = ain.read()
    resistance = (1023-a)*10000.0/a
    temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15
    temp = round(temp,1)
    return str(temp)

def main():
    while True:
        print "Temperature now is " + read_temp()

if __name__ == '__main__':
    main()



