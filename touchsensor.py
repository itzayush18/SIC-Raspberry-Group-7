
import time
import RPi.GPIO as GPIO

TOUCH_PIN = 4  # BCM GPIO4, physical pin 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_PIN, GPIO.IN)

try:
    print("Touch sensor is ready.")

    while True:
        if GPIO.input(TOUCH_PIN):
            print("Touch detected!")
        else:
            print("Not touched")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    GPIO.cleanup()

