# python-chat-experiment
Uses the python interactive interpreter to create a basic command line chat program

## Notes
The chat app requires a server instance of the application to run to allow client instances to join.

A client instance consists of a sender in which you can type your chat messages and a receiver in which 
all chat traffic is displayed. In total a client should have 2 terminal windows open.

This is just a project for me to learn python, so the coding may not be perfect and I might not be doing
things in a 'best practice' way. As I am learning I welcome any input that will improve my code.

## Running a server
To run a server change directory to the directory the chat.py script can be found and start the script with the following:

```ssh
python -i chat.py
```

Type `server` to start the server wizard.

You will be prompted to add information on the basic setup of the server. If you choose the default configuration 
the server will be setup using the address `localhost` and the port `8000`. If you choose not to use the default config 
you may add your own address and port.

## Running a client
A client is run in two terminal windows, a sender and receiver. This is to allow you to type and send messages in one 
and receive messages in a seperate window from other clients

A client is run in exactly the same way as a server, change directory to the directory with `chat.py` and start the 
script with the following:

```ssh
python -i chat.py
```

Type `client` to start the client wizard

At this point you will get the option to start a sender or receiver, you will need one of each to be able to both chat and
receive chat from others.

###Important
**You will be asked for a handle, if you want your messages to be labelled correctly in both sender and receiver windows 
make sure the handles you enter into both windows match exactly (case sensitive)**

