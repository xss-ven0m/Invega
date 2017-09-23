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
    print ("------------------------------")
    print ("Reverse lookup tool Kit")
    print ("------------------------------")
    print ("[1] Reverse Email Search")
    print ("[2] Reverse Car Plate Lookup NewZeland")
    print ("[3] Reverse Phone Number Lookup")
    print ("[4] Revserse IP Lookup")
    print ("[0] Back to Main Menu")
    choice = raw_input("Enter:")

    if choice == "1":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Email:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("http://www.addresssearch.com/results.php?type=reverse&email="+ search + "")


    if choice == "2":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Plate:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://www.carjam.co.nz/car/?plate="+ search + "")

    if choice == "3":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Number:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://pipl.com/search/?q="+ search + "&l=&sloc=&in=5")

    if choice == "4":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets IP:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://who.is/whois-ip/ip-address/"+ search + "")






    if choice == "0":
        execfile("Invega.py")



menu()
