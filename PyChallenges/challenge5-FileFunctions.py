import os
import time

def createFile():
  f = open("demofile.txt", "w")

def editFile():
  f = open("demofile.txt", "a")
  f.write("File has more content.")

def CustomEditFile():
  f = open("demofile.txt", "a")
  f.writelines(f" {edit_prompt}")

def readFile():
  f = open("demofile.txt", "r")
  print(f.read())

def closeFile():
  f = open("demofile.txt", "w")
  f.close()

def deleteFile():
  if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
  else:
    print("File does not exist.")

def dealWithQuit():
  closeFile()
  deleteFile()
  quit(0)


print("--File Handling Test--\n")

prompt = input("Do you wish to create a file? (Y/N) ").lower()
if prompt == "y":
  createFile()
  editFile()
if prompt == "n":
  dealWithQuit()

time.sleep(.5)

prompt2 = input("Do you want to read the file? (Y/N) ").lower()
if prompt2 == "y":
  readFile()
  print("\n")
if prompt2 == "n":
  dealWithQuit()


time.sleep(.5)

prompt3 = input("Do you want to edit the file? (Y/N) ").lower()
if prompt3 == "y":
  edit_prompt = input("Edit here: ")
  CustomEditFile()
  time.sleep(.1)
  readFile()
if prompt3 == "n":
  dealWithQuit()


time.sleep(.5)

prompt4 = input("Do you want to delete the file? (Y/N) ").lower()
if prompt4 == "y":
  closeFile()
  deleteFile()
if prompt4 == "n":
  dealWithQuit()


print("\n")

print("--END OF TEST--")
quit(0)