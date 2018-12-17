import os
import subprocess

def generateFileText():
    return "This is file text\r\n"

def writeToFile():
    text = generateFileText() 
    with open("content.txt", "a+") as f:
        f.write(text)
    return text

def generateCommitMessage(text):
    return text

def gitCommand(args):
    GIT = "/usr/local/bin/git"
    subprocess.call([GIT]+args)


def pushChange():
    fileText = writeToFile()
    commitMessage = generateCommitMessage(fileText)
    gitCommand(["add", "."])
    gitCommand(["commit", "-m", commitMessage])
    gitCommand(["push"]) 

if __name__ == "__main__":
    pushChange()
