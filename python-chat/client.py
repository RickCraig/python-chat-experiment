#!/usr/bin/python

import socket
import process
from thread import *
from random import randint

class Client:
    """Runs the client instance of this app"""

    handle = ''

    def set_handle(self, handle = "anon"):
        """Sets the user handle

        Keyword arguments:
        hangle -- string to set the handle to
        """
        Client.handle = handle;
        print '[Client] Handle set to ', handle

    def connect(self, address = 'localhost', port = 8000, type="sender"):
        """Connects to a server version of this app

        Keyword arguments:
        address -- is the address of the server
        port -- is the port number the server is running on
        type -- allows the app to be set to a sender of data or a receiver
        """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if Client.handle == '':
            Client.handle = 'anon#' + str(randint(1, 10000))

        server_address = (address, port)
        print '[Client] Connecting to', address, port
        self.sock.connect(server_address)
        if type == 'receiver':
            self.receive()
        self.connected = True

    def send(self, message):
        """Sends a message to the socket

        Keyword arguments:
        message - the message to send
        """
        package = { 'h': Client.handle, 'm': message }
        self.sock.sendall(process.encode(package))

    def receive(self):
        """Receives, formats and displays data from the socket"""
        while True:
            response = self.sock.recv(1024)
            data = process.decode(response)
            handle = data['h'] + ': '
            if data['h'] != self.handle:
                print handle + data['m']

    def close(self):
        """Closes the socket client"""
        self.sock.close()
        print '[Client] closing connection'

