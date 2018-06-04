#!/usr/bin/python3

import requests

def get_status_code(url):
    try:
        u.requests.head(url) #Get request with head
        return u.status_code
    except StandardError:
        return None

