"""
This is just to test if the ev3 code is working
"""

import socket

HOST = "xxx.xxx.xxx.xxx"
PORT = 00000

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
                print(f"Proximity: {received[0]}, pitch: {received[1]}, yaw: {received[2]}, touch: {received[3]}")