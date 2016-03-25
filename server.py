#!/usr/bin/python

from socket import *
from thread import *
import select

class Server:
    """Runs the server version of the chat app"""

    def start(self, host = 'localhost', port = 8000):
        """Starts the socket server

        Keyword arguments:
        host -- the host this socket server will run under
        port -- a number representing the port
        """
        self.sock = socket()
        self.sock.bind((host, port))
        self.sock.listen(5)

        self.connections = [];
        print '[Server] Starting server on', host, port

        start_new_thread(self.check, ())

    def check(self):
        """Checks the socket for incoming connections

        This method will run in a thread of it's own
        """
        while True:
            conn, addr = self.sock.accept()
            start_new_thread(self.clientthread,(conn,))
            print '[Server] Client connected'

    def clientthread(self, conn):
        """Checks connections for incoming data

        This method will run in a thread of it's own
        """
        self.connections.append(conn);

        #infinite loop so that function do not terminate and thread do not end.
        active = True
        while active:
            try:
                data = conn.recv(1024)
                self.broadcast(data)
            except:
                # Connection is no longer active
                self.connections.remove(conn)

    def broadcast(self, message):
        """Broadcasts and incoming message to all connections"""
        if message != '':
            for connection in self.connections:
                try:
                    connection.send(message)
                except:
                    print '[Server] Failed to send to connection', connection.getsockname()

    def close(self):
        """Closes closes the socket server"""
        self.sock.close()
        print '[Server] closing connection'
