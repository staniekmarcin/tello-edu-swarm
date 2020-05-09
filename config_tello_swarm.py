# Tello Edu config script to connect to Access Point 
import threading
import socket
import time

import sys
from datetime import datetime

# IP and port of Tello EDU
tello_address = ('192.168.10.1', 8889)

# IP and port of local computer
pc_address = ('192.168.10.2', 8889)

# UDP Connection
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(pc_address)

# Send the message to Tello EDU and allow for a delay in seconds
def send(message, delay):
  try:
    sock.sendto(message.encode(), tello_address)
    print("Sending message from PC: " + message)
  except Exception as e:
    print("Error sending from PC: " + str(e))

  time.sleep(delay)

# Receive the message from Tello EUD
def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message from Tello EDU: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving from Tello EDU: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Put Tello EDU into command mode
send("command", 3)
send("battery?", 3) # Try this without send("ap SSID PASSWORD", 3) to check if connection works

# send("ap SSID PASSWORD", 3) # Fill your Access Point credentials and uncomment
send("ap TP-Link_10C4 12333882", 3) # My Access Point credentials

print("Config completed!")
sock.close()
