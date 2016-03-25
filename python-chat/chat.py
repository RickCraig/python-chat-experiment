#!/usr/bin/python

import code
from server import Server
from client import Client
from startup import Startup


# Set up the classes for the server client and introduction
server = Server()
client = Client()
startup = Startup(client, server)

def initialise(event, type):
    """Initialise the start of chat after the startup is complete

    Keyword arguments:
    event -- the name of the event
    type -- the type of chat instance started
    """
    if type == 'sender':
        input()

def input():
    """Prepends "Say:" to the next line"""
    message = raw_input('Say: ')
    say(message)

def say(message):
    """Convenience method for calling client.send()

    Keyword arguments:
    message -- a string message to send to the server
    """
    client.send(message)
    input()

# Start the introduction wizard process
startup.addListener(initialise)
startup.begin()
