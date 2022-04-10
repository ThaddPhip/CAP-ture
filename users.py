# User class that has many features including setting names, uploading files (.mp4 or .csv) and playing videos
from pathlib import Path  # Necessary for determining if a file is in the directory
import playVideo  # Necessary for video playback


class Users:

    def __init__(self):  # Constructor: Every new account starts with the name "Guest" and an empty array for .mp4
        # and .csv files
        self.name = "Guest"
        self.filename = []
        self.csvfile = []
        print("New account created.")

    def __del__(self):
        print("Deleting " + self.name + ".")

    def setName(self, name):  # Allows the user to change their account name to any string
        self.name = name
        print("Name set as " + self.name)

    def setVideoFile(self, filename):  # Puts video file in your account if it is already in the directory
        if filename[-4:] != ".mp4":
            print(filename + " is not an .mp4 file. It has not been added to your account.")
            return
        file = Path(filename)
        if file.is_file():
            print(filename + " is in the directory and has been added to your account.")
            self.filename.append(filename)
        else:
            print(filename + " does NOT exist in the directory and has not been added to your account.")

    def setCSVFile(self, filename):  # Puts .csv file in your account if it is already in the directory
        file = Path(filename)
        if file.is_file():
            print(filename + " is in the directory and has been added to your account.")
            self.csvfile.append(filename)
        else:
            print(filename + " does NOT exist in the directory and has not been added to your account.")

    def getName(self):  # Returns name set on account. Returns guest if no name was set.
        return self.name

    def videoFileExist(self, filename):  # Returns 1 if .mp4 file exists on the account. Returns 0 otherwise.
        print("Searching for filename \"" + filename + "\" in \"" + self.name + "\"")
        for i in self.filename:
            if filename == i:
                print(filename + " exist.")
                return 1
        print(filename + " does NOT exist.")
        return 0

    def csvFileExist(self, filename):  # Returns 1 if .csv file exists on the account. Returns 0 otherwise.
        print("Searching for filename \"" + filename + "\" in \"" + self.name + "\"")
        for i in self.filename:
            if filename == i:
                print(filename + " exist.")
                return 1
        print(filename + " does NOT exist.")
        return 0

    def playVideo(self, filename):  # Imports playVideo.py | If .mp4 file exist on the account, play it.
        if self.videoFileExist(filename):
            playVideo.playVideo(filename)


# Code for debugging purposes
Andrew = Users()  # Creating User "Andrew" and putting 2 files in his account
Andrew.setName("Andrew")
Andrew.setVideoFile("test.mp4")
Andrew.setVideoFile("test2.mp6")

print()

Isaias = Users()  # Creating User "Isaias" and putting 1 files in his account
Isaias.setName("Isaias")
Isaias.setVideoFile("test3.mp4")

print()

LJ = Users()  # Creating Guest User "LJ" and putting no files in her account
print("The name of this account is: " + LJ.name)

print()

Andrew.videoFileExist("test2.mp4")

Isaias.playVideo("test.mp4")
Andrew.playVideo("test.mp4")

print("\nEnd of program.\n")
