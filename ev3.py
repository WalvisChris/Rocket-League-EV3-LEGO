#!/usr/bin/env python3
from ev3dev2.sensor.lego import InfraredSensor, GyroSensor, TouchSensor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.display import Display
import ev3dev2.fonts as fonts
import socket
import time

print('Setting up touch1')
touch = TouchSensor(INPUT_1)
print('Setting up gyro2')
pitch = GyroSensor(INPUT_2)
print('Setting up gyro3')
yaw = GyroSensor(INPUT_3)
print('Setting up infra4')
infra = InfraredSensor(INPUT_4)
print('Setting up screen')
screen = Display()

HOST = "xxx.xxx.xxx.xxx"
PORT = 00000

print('Setting up connection')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    screen.clear()
    screen.draw.text((10, 10), 'Connected!', font=fonts.load('luBS14'))
    screen.update()
    
    print('resetting gyros')
    pitch.reset()
    yaw.reset()
    while True:
        data = "{} {} {} {}\n".format(infra.proximity, pitch.angle, yaw.angle, bool(touch.is_pressed))
        s.sendall(data.encode('utf-8'))

except Exception as e:
    screen.clear()
    screen.draw.text((10, 10), 'Failed to connect.', font=fonts.load('luBS14'))
    screen.draw.text((10, 30), str(e), font=fonts.load('luBS14'))
    screen.update()
    print("Error:", e)
    time.sleep(1)

finally:
    s.close()