# -*-coding:Utf-8 -*

import socket
import select
import pickle

class Server:
    """Class representing the server"""
    MSG_LEN = 1024

    connectedClients = []

    def __init__(self, map):
        self.host = 'localhost'
        self.port = 1908
        self.map = map

    def start(self):
        self.mainConnection = socket.socket()
        self.mainConnection.bind((self.host, self.port))
        self.mainConnection.listen(5)
        print("Server listening on {0}:{1}...".format(self.host, self.port))

    def waitForClient(self):
        """ Wait for client to connect (and block main program)
        Return the number of connected clients when exit
        """
        while True:
            # wait for incoming clients by listening on mainConnection for 0.05s (50ms)
            incomingConnections, wlist, xlist = select.select([self.mainConnection], [], [], 0.05)
            for iConnection in incomingConnections:
                conn, info = iConnection.accept()
                self.connectedClients.append(conn)
                print("Client {0} connected".format(info))
                self.sendString(conn, "Welcome ! You're the client number {0}".format(len(self.connectedClients)))
                self.sendStringAll("{0} clients connected".format(len(self.connectedClients)))

            # if number of clients is >= 2 then listen to clients and start the game if a "c" command is entered
            if (len(self.connectedClients) >=2):
                toReadClient = []
                try:
                    toReadClient, wlist, xlist = select.select(self.connectedClients, [], [], 0.05)
                except select.error:
                    pass
                else:
                    #read command sent by clients
                    for client in toReadClient:
                        msg = client.recv(self.MSG_LEN).decode().rstrip()
                        if msg == "c":
                            print(">>>> START <<<<<")
                            self.sendStringAll("START")
                            return

    def sendObject(self, conn, obj):
        conn.send(pickle.dumps(obj))

    def sendObjectAll(self, obj):
        for conn in self.connectedClients:
            conn.send(pickle.dumps(obj))

    def sendString(self, conn, msg):
        """Send a string to a specific connection"""
        conn.send(msg.ljust(self.MSG_LEN).encode())

    def sendStringAll(self, msg):
        for conn in self.connectedClients:
            conn.send(msg.ljust(self.MSG_LEN).encode())

    def __repr__(self, **kwargs):
        return "<Server listening on {0}>".format(self.port)
