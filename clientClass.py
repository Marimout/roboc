import socket
import pickle

class Client:
    MSG_LEN = 1024

    def __init__(self, serverHost, serverPort):
        self.serverHost = serverHost
        self.serverPort = serverPort
        self.connection = socket.socket()
        self.remainingMove = []

    def connect(self):
        self.connection.connect((self.serverHost, self.serverPort))

    def receive(self):
        msg = self.connection.recv(self.MSG_LEN)
        self.receivedValue = msg.decode().rstrip()
        return self.receivedValue
    
    def send(self, msg):
        return self.connection.send(msg.ljust(self.MSG_LEN).encode())

    def move(self):
        """ Get the next move and send to server for processing"""
        # get the next move
        nextMove = self.remainingMove[0]
        # remove it from the stack
        del(self.remainingMove[0])
        # send the move to server
        self.connection.send(nextMove.encode())

    def addMove(self, command):
        """ expand the move and add to remaningMove
        ex : n3 => nnn
        """
        if command[0].upper() in ('N', 'S', 'E', 'O'):
            if len(command) > 1:
                rep = int(command[1:])
                for i in range(rep):
                    self.remainingMove.append(command[0].upper())
            else:
                self.remainingMove.append(command[0].upper())
        else:
            # if it's a command to create/destroy a wall then add it directly
            self.remainingMove.append(command.upper())
        
        print(self.remainingMove)