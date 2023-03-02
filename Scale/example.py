#! /usr/bin/python3

import time
import sys
import RPI.GPIO as GPIO

from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
from hx711 import HX711

def exit(signum, frame):
    exit(1)

def cleanAndExit():
    GPIO.cleanup()
    sys.exit()

def display_text(text):
    lcd = LCD()
    signal(SIGTERM, exit)
    signal(SIGHUP, exit)

    try:
        lcd.text("Gewicht:", 1)
        lcd.text(text + " g", 3)
    except KeyboardInterrupt:
        pass

def main():
    reference_unit = 460

    hx = HX711(5, 6)
    hx.set_reading_format("MSB", "MSB")
    hx.set_reference_unit(reference_unit)
    hx.reset()
    hx.tare()

    print("To stop this programm press Ctrl+c")

    while True:
        try:
            val = max(0, int(hx.get_weight(5)))
            display_text(str(val))

            hx.power_down()
            hx.power_up()
            time.sleep(0.1)

        except (KeyboardInterrupt, SystemExit):
            cleanAndExit()

if __name__ == "__main__":
    main()
