from time import sleep
import pyupm_i2clcd as lcd

global myLcd

def init_lcd():
    global myLcd
    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

def write_lcd(input1,input2,R,G,B,C1,C2):
    global myLcd
    myLcd.setCursor(C1,0)
    # RGB Blue
    #myLcd.setColor(53, 39, 249)

    # RGB Red
    myLcd.setColor(R, G, B)
    myLcd.write(input1)
    myLcd.setCursor(C2,0)
    myLcd.write(input2)


def main():
    # Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

    myLcd.setCursor(0,0)
    # RGB Blue
    #myLcd.setColor(53, 39, 249)

    # RGB Red
    myLcd.setColor(255, 0, 0)
    myLcd.write('T: 24C')
    myLcd.setCursor(1,1)
    myLcd.write('B')
    sleep(5)
    del myLcd

if __name__ == '__main__':
	main()