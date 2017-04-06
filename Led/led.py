import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 27

#salidas
GPIO.setup(ledPin, GPIO.OUT)

while True:
    GPIO.output(ledPin, True) #encender led
    time.sleep(1)
    GPIO.output(ledPin, False) #apagar led
    time.sleep(1)
    #print("led")

GPIO.cleanup() #limpiar GPIO
