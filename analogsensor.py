
import RPi.GPIO as GPIO
import time

SOUND_PIN = 17  # BCM GPIO 17, physical pin 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup(SOUND_PIN)
GPIO.setup(SOUND_PIN, GPIO.IN)

print("KY-037 Sound Sensor Test")
print("Clap near the microphone.")
print("Press Ctrl+C to stop.\n")

try:
    while True:
        value = GPIO.input(SOUND_PIN)

        if value == GPIO.LOW:
            print("Sound trigger detected! (DO = LOW)")
        else:
            print("No trigger (DO = HIGH)")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nTest stopped.")

finally:
    GPIO.cleanup()

