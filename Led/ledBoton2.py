import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins
ledPin = 23
botonPin = 18

#entradas y salidas
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(botonPin, GPIO.IN)

estado = False
estadoAnterior = False
salida = 0

while True:
    estado = GPIO.input(botonPin)

    if estado == True and estadoAnterior == False:
        salida = 1 - salida
        time.sleep(0.03)
    
    estadoAnterior = estado   

    if salida == 1:
        print("ENCENDIDO")
        GPIO.output(ledPin, True)
    else:
        print("APAGADO")
        GPIO.output(ledPin, False)

GPIO.cleanup() #limpiar GPIO
