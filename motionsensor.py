
import time
import RPi.GPIO as GPIO

MOTION_PIN = 4  # BCM GPIO4, physical pin 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_PIN, GPIO.IN)

try:
    print("PIR motion sensor is starting...")
    time.sleep(30)  # Allow the sensor to stabilize
    print("Motion sensor is ready.")

    while True:
        if GPIO.input(MOTION_PIN):
            print("Motion detected!")
        else:
            print("No motion")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    GPIO.cleanup()

