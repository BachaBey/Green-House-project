import math


#fake environement
###########
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO # Fake GPIO
sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

############

import RPi.GPIO as GPIO
import dht11

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)         #setting the pin numbering scheme to BCM .


# Function to read the light intensity
def read_light(light_pin):

    GPIO.setmode(GPIO.BOARD)

    #setting pin as an input.
    GPIO.setup(light_pin, GPIO.IN)     

    # defining Constants for the LDR circuit
    VCC = 3.3                      #voltage supply 
    R_LDR = 10000                  #resistance of the LDR in darkness
    R_FIX = 1000                   #resistance of the fixed resistor

    #calculating the voltage across the LDR using Ohm's law and the formula for a voltage divider circuit. 
    voltage = VCC * (R_FIX / (R_FIX + GPIO.input(light_pin) * R_LDR))
    
    #calculating the lux value 
    lux = 10000 * ((math.log(VCC / voltage - 1)) ** -1.4)
    
    # Clean up the GPIO pins 
    GPIO.cleanup()
         
    return lux

# Function to read Moisture value
def read_moisture(moisture_pin):
    GPIO.setmode(GPIO.BOARD)

    #setting pin as an input.
    GPIO.setup(moisture_pin, GPIO.IN)

    # Read the moisture sensor's value
    moisture_value = GPIO.input(moisture_pin)
    
    # Clean up the GPIO pins 
    GPIO.cleanup()

    return moisture_value
# Function to read Temperature value
def read_temperature(temperature_pin):
    temp_value=dht11.read(dht11.DHT11,temperature_pin).temperature
    return temp_value

# Function to read Humidioty value
def read_humidity(humidity_pin):
    humidity_value=dht11.read(dht11.DHT11,humidity_pin).humidity
    return humidity_value