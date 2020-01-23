#!/usr/bin/env python
import time
import datetime
import Adafruit_MCP3008
import RPi.GPIO as GPIO

# How many times you will run the test
#TESTRUNS = 30
TESTRUNS = 30

# Number of seconds waited between each reads
#SLEEP_BETWEEN_READS = 300
SLEEP_BETWEEN_READS = 300

#READS_PER_LIGHT_SEGMENT = 12
READS_PER_LIGHT_SEGMENT = 12

#Actual number of lights is 5, but using them grouped together equals 3
NUMBER_OF_LIGHT_SEGMENTS = 3

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setwarnings(False)
#5=Left 3=Right 7=Top
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

def turn_on_lights(light_set):
    if light_set == 0:
        GPIO.output(3,GPIO.HIGH)
    elif light_set == 1:
        GPIO.output(4,GPIO.HIGH)
    elif light_set == 2:
        GPIO.output(2,GPIO.HIGH)

def turn_off_lights(light_set):
    if light_set == 0:
        GPIO.output(3,GPIO.LOW)
    elif light_set == 1:
        GPIO.output(4,GPIO.LOW)
    elif light_set == 2:
        GPIO.output(2,GPIO.LOW)   

def run_tests():
    for x in range (TESTRUNS): 
        filename = "Sunflower_Test_" + str(x) + ".csv"
        print(filename)
        
        # opens the file for writing
        csv = open(filename, "w")
        csv.write("{0}\n".format(datetime.datetime.now()))
        
        for y in range (NUMBER_OF_LIGHT_SEGMENTS):
            turn_on_lights(y)
        
            for z in range (READS_PER_LIGHT_SEGMENT):
                time.sleep(2)
                voltage = mcp.read_adc(0)
                csv.write("{0},{1},{2}\n".format(datetime.datetime.now(), y, voltage))
                time.sleep(SLEEP_BETWEEN_READS)
            
            turn_off_lights(y)
                
        csv.close()

if __name__ == "__main__":
    turn_off_lights(0)
    turn_off_lights(1)
    turn_off_lights(2)
    run_tests()
    turn_off_lights(0)
    turn_off_lights(1)
    turn_off_lights(2)
