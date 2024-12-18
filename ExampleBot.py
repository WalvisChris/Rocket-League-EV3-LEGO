"""
Note: this is only 1 file of the GoslingUtils-Master. Replace its contents with this.
Make sure to edit the bots name in the ExampleBot.cfg. To update the bots code, restart RLBotGUI.
"""

from tools import *
from objects import *
from routines import *
import socket
import threading

HOST = "xxx.xxx.xxx.xxx"
PORT = 00000

touch = False
yaw = 0
pitch = 0
proximity = 0

lock = threading.Lock()

def socket_listener():
    global touch, yaw, pitch, proximity
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print("Waiting for connection...")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            buffer = ""
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                buffer += data.decode('utf-8')
                
                while '\n' in buffer:
                    message, buffer = buffer.split('\n', 1)
                    received = message.split(" ")
                    
                    with lock:
                        proximity = int(received[0])
                        pitch = float(received[1])
                        yaw = float(received[2])
                        touch = received[3].lower() == "true"

                    print(f"Proximity: {proximity}, pitch: {pitch}, yaw: {yaw}, touch: {touch}")

listener_thread = threading.Thread(target=socket_listener, daemon=True)
listener_thread.start()

class ExampleBot(GoslingAgent):
    def run(agent):
        flag = False
        with lock:
            current_touch = touch
            current_yaw = yaw
            current_pitch = pitch
            current_proximity = proximity
        
        if agent.me.airborne:
            agent.controller.yaw = -0.5 if current_yaw < -15 else 0.5 if current_yaw > 15 else 0
            agent.controller.pitch = 0.5 if current_pitch < -15 else -0.5 if current_pitch > 15 else 0
        else:
            agent.controller.throttle = 1 if current_touch else 0
            agent.controller.steer = -0.7 if current_yaw < -15 else 0.7 if current_yaw > 15 else 0
            if current_proximity > 6 and not flag:
                agent.controller.jump = True
                flag = True
            elif current_proximity < 5:
                agent.controller.jump = False
                flag = False