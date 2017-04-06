import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinServo = 18
pinBoton = 23

#entradas y salidas
GPIO.setup(pinServo, GPIO.OUT)
GPIO.setup(pinBoton, GPIO.IN)

#PWM - Modulacion por ancho de pulsos
servo = GPIO.PWM(pinServo, 50) #50 pulsos
servo.start(7.5) #7.5 pulsos = centro

while True:
    if GPIO.input(pinBoton) == True:
        print("Servo izquierda")
        servo.ChangeDutyCycle(4.5) #girar a la izquierda
        time.sleep(0.1)

    if GPIO.input(pinBoton) == False:
        print("Servo derecha")
        servo.ChangeDutyCycle(10.5) #girar a la derecha
        time.sleep(0.1)

GPIO.cleanup() #limpiar GPIO
