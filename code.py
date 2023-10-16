import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the LED
led_pin = 17

# Set up the GPIO pin for the LED as an output
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(led_pin, GPIO.HIGH)
        print("LED is ON")
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(led_pin, GPIO.LOW)
        print("LED is OFF")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Turn off the LED and clean up the GPIO pins on program exit
    GPIO.output(led_pin, GPIO.LOW)
    GPIO.cleanup()
