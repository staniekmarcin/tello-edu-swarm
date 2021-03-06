# Tello EDU Swarm for 2 drones
# Import the necessary modules
import socket
import threading
import time

import sys
from datetime import datetime

# IP and port of Tello EDU and fill with Tello EDU IP given from Access Point
tello_edu_1_address = ('192.168.0.101', 8889)
tello_edu_2_address = ('192.168.0.102', 8889)
tello_edu_3_address = ('192.168.0.103', 8889)
tello_edu_4_address = ('192.168.0.104', 8889)
tello_edu_5_address = ('192.168.0.105', 8889)

# IP and port of local computer and fill with your PC IP given from Access Point
local1_address = ('192.168.0.100', 58650)
local2_address = ('192.168.0.100', 58651)
local3_address = ('192.168.0.100', 58652)
local4_address = ('192.168.0.100', 58653)
local5_address = ('192.168.0.100', 58654)

# UDP Connection
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock1.bind(local1_address)
sock2.bind(local2_address)
sock3.bind(local3_address)
sock4.bind(local4_address)
sock5.bind(local5_address)

# Send the message to Tello EDU and allow for a delay in seconds
def send(message, delay):
  try:
    sock1.sendto(message.encode(), tello_edu_1_address)
    sock2.sendto(message.encode(), tello_edu_2_address)
    sock3.sendto(message.encode(), tello_edu_3_address)
    sock4.sendto(message.encode(), tello_edu_4_address)
    sock5.sendto(message.encode(), tello_edu_5_address)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))

  time.sleep(delay)

# Receive the message from Tello EDU
def receive():
  while True:
    try:
      response1, ip_address = sock1.recvfrom(128)
      response2, ip_address = sock2.recvfrom(128)
      response3, ip_address = sock3.recvfrom(128)
      response4, ip_address = sock4.recvfrom(128)
      response5, ip_address = sock5.recvfrom(128)
      print("Received message: from Tello EDU #1: " + response1.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #2: " + response2.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #3: " + response3.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #4: " + response4.decode(encoding='utf-8'))
      print("Received message: from Tello EDU #5: " + response5.decode(encoding='utf-8'))
    except Exception as e:
      sock1.close()
      sock2.close()
      sock3.close()
      sock4.close()
      sock5.close()
      print("Error receiving: " + str(e))
      break

# Create and start a listening thread that runs in the background
# This utilizes our receive functions and will continuously monitor for incoming messages
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

# Put Tello into command mode
send("command", 3)

# Read file and execute commands
start_time = str(datetime.now())

file_name = "commands_tello_swarm"
f = open(file_name + ".txt", "r")
commands = f.readlines()

for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()
        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print('delay %s' % sec)
            time.sleep(sec)
            pass
        else:
            send(command, 5)

print("Mission completed successfully!")
sock1.close()
sock2.close()
sock3.close()
sock4.close()
sock5.close()
