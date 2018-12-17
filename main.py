import os, subprocess, random

def generateFileText():
    path = "words.txt"
    with open("words.txt", "r") as f:
        words = [line for line in f.readlines()]
    # numWords = random.randint(6, 14) 
    text = [words[random.randint(0, len(words) -1)] for _ in range(random.randint(6, 14))]

    return " ".join(text)+"\r\n"

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

def main():
    if random.random() < 0.75:
        for _ in range(random.randint(1, 5)):
            pushChange()

if __name__ == "__main__":
    main()
