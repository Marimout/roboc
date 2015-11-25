# -*-coding:Utf-8 -*

import time
import sys

from threading import *

from clientClass import *

displayLock = RLock()
gameStarted = False
myTurn = False
command = ""

def getUserInput():
    while True:
        with displayLock:
            print("Enter a command: ", end="", flush=True)
        msg = input()

        if not gameStarted:     # if the game hasn't started yet => send command immediately to server
            client.send(msg)
        elif myTurn:            # if it's my turn then check if input is valid
            if (isValidCommand(msg)):
                command = msg
                # wait for command to be handled by other thread
                while command != "":
                    time.sleep(0.001)
        else:
            pass

def getServerResponse():
    while True:
        msg = client.receive()
        if msg == "START":
            gameStarted = True
            myTurn = False
            # if receive START then next object in the pipe is the map
            client.receiveMap()
            # then my position
            client.receivePosition()
            return
        elif msg == "TURN":
            myTurn = True
            # make my move
            if len(client.remainingMove) > 0:       # if there is some move in stock then move it
                client.move()
            else:                                   # else wait till having a valid input then move it
                while command == "":
                    time.sleep(0.001)
                client.addMove(command)
                client.move()
        elif not msg == "":
            with displayLock:
                print()
                print(">> SERVER : {0}".format(msg))
                print("Still waiting for your command...")
        else:
            return

# Connect to server
client = Client("localhost", 1908)
while True:
    try:
        client.connect()
        break
    except:
        print("ERROR : Cannot connect to server. Will try in 5 seconds")
        for i in range(5):
            print(". ", end="", flush=True)
            time.sleep(1)
        print()

# Get welcome message from server
print(client.receive())

# Start 2 threads : one to get user's input, other to communicate with server
getUserInputThread = Thread(target=getUserInput)
getServerResponseThread = Thread(target=getServerResponse)

getServerResponseThread.start()
getUserInputThread.start()

# block the program till receive the map from server
getServerResponseThread.join()

print(client.currentMap)
print(client.currentMap.labyrinthe)