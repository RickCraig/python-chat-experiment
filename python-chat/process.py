#!/usr/bin/python

import json

def encode(message):
    """Returns a json string

    Keyword argument:
    message -- a dictionary
    """
    return json.dumps(message)

def decode(message):
    """Returns a dictionary

    Keyword arguments:
    message -- a json string
    """
    return json.loads(message)
