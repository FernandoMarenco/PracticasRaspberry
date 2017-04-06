import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 27
botonPin = 17

#entradas y salidas
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(botonPin, GPIO.IN)

while True:

    if GPIO.input(botonPin) == False:
        print("Led apagado")
        GPIO.output(ledPin, False) #apagar led (False o 0)
        time.sleep(0.1)
        GPIO.setup(botonPin, GPIO.IN, GPIO.PUD_UP)
    
    if GPIO.input(botonPin) == True:
        print("Led encendido")
        GPIO.output(ledPin, True) #encender led (True o 1)
        time.sleep(0.1)
        GPIO.setup(botonPin, GPIO.IN, GPIO.PUD_DOWN)

GPIO.cleanup() #limpiar GPIO
