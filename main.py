import os
import subprocess

def generateCommitMessage():
    return "This will be default message"

def pushChange():
    git = "/usr/local/bin/git"
    commitMessage = generateCommitMessage()
    subprocess.call([git, "add", "."])
    subprocess.call([git, "status"])
    subprocess.call([git, "commit", "-m", commitMessage])


if __name__ == "__main__":
    pushChange()
