import os.path

path = os.path.abspath(".") + "\\OUTPUT\\"


def getFramesCount():
    directoryList = os.listdir(f"{path}\\outputs/0-0/")  # dir is your directory path
    numberFiles = len(directoryList)
    return numberFiles


def getPath():
    return path
