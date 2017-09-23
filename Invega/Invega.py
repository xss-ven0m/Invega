import os
import subprocess
import sys
import webbrowser
import time
import random
def menu():
    print """
  _____
 |_   _|
   | |  _ ____   _____  __ _  __ _
   | | | '_ \ \ / / _ \/ _` |/ _` |
  _| |_| | | \ V /  __/ (_| | (_| |
 |_____|_| |_|\_/ \___|\__, |\__,_|
                        __/ |
                       |___/
  ___            _            _
 |   \ _____ __ | |_ ___  ___| |
 | |) / _ \ \ / |  _/ _ \/ _ \ |
 |___/\___/_\_\  \__\___/\___/_|


    """
    print ("---------------------")
    print ("Invega Menu")
    print ("Made by : Bunn E")
    print ("---------------------")
    print ("[1] Simple Search")
    print ("[2] Intense Search")
    print ("[3] Revserse Lookup Tool")
    choice = raw_input("Enter:")

    if choice == "1":
        print ("Loading....")
        time.sleep(2)
        execfile("l1.py")

    if choice == "2":

        print ("Loading....")
        time.sleep(2)

        execfile("l2.py")

    if choice == "3":
        print ("Loading....")
        time.sleep(2)
        execfile("l3.py")

menu()
