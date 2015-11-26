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
    
    def receiveMap(self):
        print("Waiting for map")
        map = self.connection.recv(self.MSG_LEN).rstrip()
        self.currentMap = pickle.loads(map)

    def receivePosition(self):
        print("Waiting for position")
        robot = self.connection.recv(self.MSG_LEN)
        self.robot = pickle.loads(robot)

    def send(self, msg):
        return self.connection.send(msg.ljust(self.MSG_LEN).encode())

    def move(self):
        print("TODO : move")
        pass

    def addMove(self, command):
        print("TODO : addMove")
        pass    