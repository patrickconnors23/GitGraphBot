import os, subprocess, random

def generateFileText():
    """
    Generate random text for file
    """
    path = "words.txt"
    with open("words.txt", "r") as f:
        words = [line for line in f.readlines()]
    text = [words[random.randint(0, len(words) -1)].strip() for _ in range(random.randint(6, 14))]

    return " ".join(text)+"\r\n"

def writeToFile():
    """
    Write to content.txt so that there is change to commit
    """
    text = generateFileText() 
    with open("content.txt", "a+") as f:
        f.write(text)
    return text

def generateCommitMessage(text):
    """
    Shorten file text to generate commit message"
    """
    text = text.split()[:4]
    return " ".join(text)

def gitCommand(args):
    """
    Wrapper to execute git command via python
    """
    GIT = "/usr/local/bin/git"
    subprocess.call([GIT]+args)

def pushChange():
    """
    Write change and push to remote
    """
    # Get File text
    fileText = writeToFile()
    # Shorten text into commit message
    commitMessage = generateCommitMessage(fileText)
    # Push to remote
    gitCommand(["add", "."])
    gitCommand(["commit", "-m", commitMessage])
    gitCommand(["push"]) 

def main():
    """
    Randomly create change to push to github
    This script should be run daily
    """
    if random.random() < 0.75:
        for _ in range(random.randint(1, 5)):
            pushChange()

if __name__ == "__main__":
    main()
