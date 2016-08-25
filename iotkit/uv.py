import mraa
import math

def read_uv(pin):

    sensorValue = mraa.Aio(2)
    Vsig = sensorValue.read()*4980/1023

    if Vsig < 50 :
        #print "UV Index: 0.Exposure level - NONE (You're probably at home!)"
        index = "0 NONE"
    elif Vsig < 227:
        #print "UV Index: 1.Exposure level - LOW (You're probably at home!)"
        index = "1 LOW"
    elif Vsig < 318:
        #print "UV Index: 2.Exposure level - LOW (You can go outside and have fun)"
        index = "2 LOW"
    elif Vsig < 408:
        #print "UV Index: 3.Exposure level - MODERATE (Sun starts to annoy you)"
        index = "3 MODERATE"
    elif Vsig < 503:
        #print "UV Index: 4.Exposure level - MODERATE (Sun starts to annoy you)"
        inde = "4 MODERATE"
    elif Vsig < 606:
        #print "UV Index: 5.Exposure level - MODERATE (Sun starts to annoy you)"
        index = "5 MODERATE"
    elif Vsig < 696:
        #print "UV Index: 6.Exposure level - HIGH (Get out from the sunlight)"  
        index = "6 HIGH"
    elif Vsig < 795:
        #print "UV Index: 7.Exposure level - HIGH (Get out from the sunlight)"  
        index = "7 HIGH"
    elif Vsig < 881:
        #print "UV Index: 8.Exposure level - VERY HIGH (Get out from the sunlight)"  
        index = "8 VHIGH"
    elif Vsig < 976:
        #print "UV Index: 9.Exposure level - VERY HIGH (If you value your health, don't go outside, just stay at home!)"
        index = "9 VHIGH"
    elif Vsig < 1079:
        #print "UV Index: 10.Exposure level - VERY HIGH (If you value your health, don't go outside, just stay at home!)"
        index = "10 VHIGH"
    elif Vsig < 1170:
        #print "UV Index: 11.Exposure level - EXTREME (If you value your health, don't go outside, just stay at home!)"
        index = "11 EXTRM"
    else :
        #print "UV Index: 12.Exposure level - EXTREME (You will probably die...)"  
        index = "12 EXTRM" 
    return str(index)


def main():
    print "UV Index: " + read_uv(2)

if __name__ == '__main__':
    main()
