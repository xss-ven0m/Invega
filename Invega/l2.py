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
    print ("---------------")
    print ("Intense Search")
    print ("---------------")
    print ("[1] Search Pipl Database")
    print ("[2] Search Spokeo Database")
    print ("[0] Back to Main Menu")
    choice = raw_input("Enter:")

    if choice == "1":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Username:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://pipl.com/search/?q=" + search +"&l=&sloc=&in=6")


    if choice == "2":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Username:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://www.spokeo.com/social/profile?q=" + search +"")



    if choice == "0":
        execfile("Invega.py")



menu()
