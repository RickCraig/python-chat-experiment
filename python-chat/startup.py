#!/usr/bin/python

class Startup:
    """The startup introduction wizard"""

    def __init__(self, client, server):
        self.listeners = []
        self.server = server
        self.client = client

    def begin(self):
        """Begins the process of asking questions related\
        to how this chat script runs
        """
        type = raw_input('Choose the app purpose (server, client): ');
        print '-' * 20
        if type == 'server':
            self.start_server()
        elif type == 'client' or type == '':
            self.start_client()
        else:
            self.begin()

    def start_server(self):
        """Starts the server startup wizard"""
        config = raw_input('Would you like the default config (Y/n): ')

        if config == '' or config == 'Y':
            print '-' * 20
            self.server.start()
            self.notify('complete', 'server')
        else:
            address = raw_input('Server address (localhost):')
            port = raw_input('Server port (8000):')
            print '-' * 20
            self.server.start(address=address or 'localhost', port=port or 8000)
            self.notify('complete', 'server')

    def start_client(self):
        """Starts the client startup wizard"""
        type = raw_input('Is this a sender or receiver window (S/r): ')

        full_type = 'receiver' if type == 'r' else 'sender'

        handle = raw_input('Please add a user handle (random): ')

        if handle != '':
            self.client.set_handle(handle)

        config = raw_input('Would you like the default config (Y/n): ')

        if config == '' or config == 'Y':
            print '-' * 20
            self.client.connect(type=full_type)
            self.notify('complete', full_type)
        else:
            address = raw_input('Server address (localhost):')
            port = raw_input('Server port (8000):')
            print '-' * 20
            client.connect(address=address or 'localhost', port=port or 8000, type=full_type)
            self.notify('complete', full_type)

    def addListener(self, listener):
        """Adds listener functions to the listeners list

        Keyword arguments:
        listener -- a function to add to the list
        """
        self.listeners.append(listener)

    def notify(self, event, type):
        """Notifies all listeners of an event

        Keyword arguments:
        event -- the name of an event
        type -- the type of instance this window is running
        """
        for listener in self.listeners:
            listener(event, type)
