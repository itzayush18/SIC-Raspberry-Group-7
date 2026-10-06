
import time
import board
import adafruit_dht
import digitalio

# DHT11 sensor on GPIO4 (physical pin 7)
dht11 = adafruit_dht.DHT11(board.D4)

# LED on GPIO17 (physical pin 11)
led = digitalio.DigitalInOut(board.D17)
led.direction = digitalio.Direction.OUTPUT
led.value = False

THRESHOLD = 28.3
BLINK_INTERVAL = 0.5  # seconds

led_state = False
last_blink = time.monotonic()

try:
    while True:
        try:
            temperature = dht11.temperature
            humidity = dht11.humidity

            print(f"Temperature: {temperature:.1f} °C")
            print(f"Humidity: {humidity:.1f} %")

            if temperature >= THRESHOLD:
                now = time.monotonic()

                if now - last_blink >= BLINK_INTERVAL:
                    led_state = not led_state
                    led.value = led_state
                    last_blink = now

                print("Temperature threshold reached! LED blinking")
            else:
                led.value = False
                led_state = False
                print("Temperature below threshold. LED OFF")

            print("----------------------")

        except RuntimeError as error:
            print("Sensor reading error:", error)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    led.value = False
    led.deinit()
    dht11.exit()

