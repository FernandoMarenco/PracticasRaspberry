import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pinServo = 18

#PWM - Modulacion por anchode pulsos
GPIO.setup(pinServo, GPIO.OUT)
servo = GPIO.PWM(pinServo, 50) #50 pulsos
servo.start(7.5) #7.5 pulsos = centro


while True:
    servo.ChangeDutyCycle(4.5) #girar a la izquierda
    time.sleep(0.5)
    servo.ChangeDutyCycle(10.5) #girar a la derecha
    time.sleep(0.5)

GPIO.cleanup() #limpiar GPIO
