import RPi.GPIO as GPIO




# Function to activate heater (in our prototype its a ventilator)
def activate_heater(heater_pin,heat_on):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(heater_pin, GPIO.OUT)
    GPIO.output(heater_pin, heat_on)

    # Clean up the GPIO pins 
    GPIO.cleanup()

# Function to activate cooler (in our prototype its a ventilator)
def activate_cooler(cooler_pin,heat_on):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(cooler_pin, GPIO.OUT)
    GPIO.output(cooler_pin, heat_on)

    # Clean up the GPIO pins 
    GPIO.cleanup()

# Function to activate ventilator 
def activate_ventilator(ventilator_pin,heat_on):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ventilator_pin, GPIO.OUT)
    GPIO.output(ventilator_pin, heat_on)

    # Clean up the GPIO pins 
    GPIO.cleanup()


# Function to activate humidity_water 
def activate_humidity_water(humidity_water_pin,heat_on):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(humidity_water_pin, GPIO.OUT)
    GPIO.output(humidity_water_pin, heat_on)

    # Clean up the GPIO pins 
    GPIO.cleanup()

# Function to activate irrigation
def activate_irrigation(irrigation_pin,water_on):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(irrigation_pin, GPIO.OUT)
    GPIO.output(irrigation_pin, water_on)

    # Clean up the GPIO pins 
    GPIO.cleanup()

# Function to activate lighting
def activate_led(led_pin,led_on):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, led_on)

    # Clean up the GPIO pins 
    GPIO.cleanup()



