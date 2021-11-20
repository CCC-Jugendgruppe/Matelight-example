#!/usr/bin/env python3

import matelight
import socketserver
import socket
import threading

def fill(r, g, b):
    for x in range(0, ml.width):
        for y in range(0, ml.height):
            ml.set_pixel(x, y, r, g, b)
    ml.show()
    
class MyTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

class MatelightTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        priviledged = False
        while 1:
            try:
                # Receive Data
                data = self.request.recv(1024)
                if not data:
                    break
                data = data.decode()
                print(data)
                
                # Regular Commands
                if data.startswith("PX "):
                    parts = data.split(" ")
                    if len(parts)!=4:
                        self.request.sendall("Invalid argument count".encode())
                        continue
                    if len(parts[3].strip())!=6:
                        self.request.sendall("Unrecognized color value".encode())
                        continue
                    print(parts)
                    x = int(parts[1])
                    y = int(parts[2])
                    color = parts[3]
                    r = int(color[0:2], base=16)
                    g = int(color[2:4], base=16)
                    b = int(color[4:6], base=16)
                    print(r, g, b)
                    ml.set_pixel(x, y, r, g, b)
                    ml.show()
                elif data.strip()=="SIZE":
                    self.request.sendall(("SIZE " + str(ml.width) + " " + str(ml.height)).encode())
                elif data.strip()=="ALARM":
                    image = ml.strip.leds[:]
                    for _ in range(0, 5):
                        for r in range(0, 255, 2):
                            fill(r, 0, 0)
                        for r in range(255, 0, -2):
                            fill(r, 0, 0)
                    ml.strip.leds = image
                    ml.show()
                
                # Priviledged Commands
                elif data.strip()=="MATEFLUTPRIVILEDGEDMODE":
                    priviledged = True
                elif data.startswith("FILL ") and priviledged:
                    color = data.split(" ")[1]
                    r = int(color[0:2], base=16)
                    g = int(color[2:4], base=16)
                    b = int(color[4:6], base=16)
                    fill(r, g, b)
                
                #Unknown Command
                else:
                    self.request.sendall("INVALID OR UNSUPPORTED COMMAND".encode())
            except:
                self.request.sendall("Something went wrong".encode())

# hier startet das eigentliche Script
HOST = "0.0.0.0"
PORT = 1234

ml = matelight.Matelight(2, 3)

server = MyTCPServer((HOST, PORT), MatelightTCPHandler)

try:
    server.serve_forever()
except:
    pass
server.shutdown()
