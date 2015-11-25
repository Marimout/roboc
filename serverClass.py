# -*-coding:Utf-8 -*

import socket
import select

class Server:
    """Class representing the server"""

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

            #TODO : Separate waiting for incoming connection and handling clients' command into 2 threads
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
                        msg = client.recv(1024).decode()
                        if msg == "c":
                            print(">>>> START <<<<<")
                            self.sendStringAll("START")
                            return

    def send(self, conn, obj):
        conn.send(obj)

    def sendAll(self, obj):
        for conn in self.connectedClients:
            conn.send(obj)

    def sendString(self, conn, msg):
        conn.send(msg.encode())

    def sendStringAll(self, msg):
        for conn in self.connectedClients:
            conn.send(msg.encode())

    def __repr__(self, **kwargs):
        return "<Server listening on {0}>".format(self.port)