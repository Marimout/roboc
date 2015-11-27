# -*-coding:Utf-8 -*

from tools import *
from serverClass import *
from pickle import *
from random import * 

def sendMapToAll():
    """Send map representation to all clients"""
    for client in server.connectedClients:
        server.sendString(client, currentMap.labyrinthe.reprWithOneMainRobot(client))

currentMap = selectMap()

print("Waiting for client...")

server = Server(currentMap)

# start the server
server.start()

# wait for client to connect. Wait will end when receive a "c" command from client
server.waitForClient()

# calculate position for each robot
for client in server.connectedClients:
    robot = choice(currentMap.labyrinthe.allFreeCase())
    currentMap.labyrinthe.robots[client] = robot

sendMapToAll()

# game loop :
#     - get next client
#     - notify him that it's his turn
#     - wait for client input
#     - move the robot
#     - send the updated map
currentClientIndex = -1
nbClients = len(server.connectedClients)
while not currentMap.labyrinthe.hasExited:
    # switch to next client and tell him that it's his turn
    currentClientIndex = (currentClientIndex + 1) % nbClients
    currentClient = server.connectedClients[currentClientIndex]
    server.sendString(currentClient, "TURN")
    print("Player {0}'s turn".format(currentClientIndex + 1))

    # wait for client's input
    clientMove = currentClient.recv(server.MSG_LEN).decode().rstrip()
    
    # move his robot
    currentMap.labyrinthe.robots[currentClient] = currentMap.labyrinthe.move(currentMap.labyrinthe.robots[currentClient], clientMove)

    # send the updated map to all players
    sendMapToAll()

# Avoid program from exiting
input("Press any key to exit")

