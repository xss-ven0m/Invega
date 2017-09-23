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
    print ("Simple Search")
    print ("---------------")
    print ("[1] Search Google")
    print ("[2] Search Youtube")
    print ("[3] Search Flicker")
    print ("[4] Search Instagram")
    print ("[0] Back to Main Menu")
    choice = raw_input("Enter:")

    if choice == "1":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Username:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://www.google.com/search?dcr=0&source=hp&q=""intext:"+ search +"&oq=here&gs_l=psy-ab.3...2782.3130.0.3177.4.4.0.0.0.0.0.0..0.0....0...1.1.64.psy-ab..4.0.0....0.AbTZdrdXkkQ")


    if choice == "2":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Username:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/results?search_query=" + search +"")

    if choice == "3":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Username:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://www.flickr.com/search/?text=" + search +"")

    if choice == "4":
        print ("Loading..")
        time.sleep(1)
        search = raw_input("Targets Username:")
        print ("Searching....")
        time.sleep(1)
        webbrowser.open("https://www.instagram.com/" + search +"/")


    if choice == "0":
        execfile("Invega.py")

menu()
