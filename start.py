#!/bin/env python3
import client

import sys
import importlib
import openssl

passwords = {"username":"mdp","guest":"guest"}

if len(sys.argv)>1:
    if sys.argv[1] == 1:
        user = "votreuser"
    elif sys.argv[2] == 2:
        user = "guest"
        
if "user" not in locals():
    user = "votreuser"

c = client.Connection()
c.CHAP(user,passwords[user])
print("log as "+user)
USER = user
PASSWORD = passwords[USER]


