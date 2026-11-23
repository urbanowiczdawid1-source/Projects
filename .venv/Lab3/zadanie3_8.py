from gpiozero import AngularServo
from time import sleep
servo = AngularServo(24,
min_angle=-30,
max_angle=30)
while True:
    servo.angle = -30
    sleep(0.1)
    servo.angle = 30
    sleep(0.1)
