
import time
import board
import adafruit_dht

# Initialize DHT11 sensor on GPIO4
dht11 = adafruit_dht.DHT11(board.D4)

try:
    while True:
        try:
            temperature = dht11.temperature
            humidity = dht11.humidity

            print(f"Temperature: {temperature:.1f} °C")
            print(f"Humidity: {humidity:.1f} %")
            print("----------------------")

        except RuntimeError as error:
            print("Sensor reading error:", error)

        time.sleep(2)

except KeyboardInterrupt:
    print("Program stopped")

finally:
    dht11.exit()

