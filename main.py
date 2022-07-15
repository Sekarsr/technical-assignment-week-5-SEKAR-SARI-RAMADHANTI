import time
import board
import Adafruit_DHT
import psutil

for proc in psutil.process_iter():
    if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
        proc.kill()
sensor = Adafruit_DHT.DHT11
DHT_PIN = 4
dataSuhu = []
while True:
    try:
        humidity, temperature = Adafruit_DHT.read(sensor, DHT_PIN)
        print("Temperature: {}*C   Humidity: {}%".format(temperature, humidity))
        if temperature == None:
            print("Suhu tidak terdeteksi")
        elif temperature >= 30.0:
            print("Pendingin dinyalakan")
        elif temperature <= 25.0:
            print("Pemanas dinyalakan")
        else:
            print("Suhu normal")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(5.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error
    time.sleep(5.0)
