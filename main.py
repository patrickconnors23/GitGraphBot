import os
import subprocess

GIT = "/usr/local/bin/git"

def generateFileText():
    return "This is file text\r\n"

def writeToFile():
    text = generateFileText() 
    with open("content.txt", "a+") as f:
        f.write(text)
    return text

def generateCommitMessage(text):
    return text

def pushChange():
    fileText = writeToFile()
    commitMessage = generateCommitMessage(fileText)
    subprocess.call([GIT, "add", "."])
    subprocess.call([GIT, "status"])
    subprocess.call([GIT, "commit", "-m", commitMessage])


if __name__ == "__main__":
    pushChange()
