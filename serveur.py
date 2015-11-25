# -*-coding:Utf-8 -*

from tools import *
from serverClass import *
from pickle import *

currentMap = selectMap()

print("Waiting for client...")

server = Server(currentMap)

# start the server
server.start()

# wait for client to connect. Wait will end when receive a "c" command from client
server.waitForClient()

# send chosen map to all clients
server.sendAll(pickle.dumps(currentMap))

# calculate position for each robot and send it
for i in range(len(server.connectedClients)):


# Avoid program from exiting
input()