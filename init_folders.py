import os

from helpers import getPath


def InitData():
    path = getPath()
    abspath = os.path.abspath(".")
    if not os.path.exists(f"{path}\\FinalResult\\gfx\\animated_textures\\frontend_background"):
        os.makedirs(f"{path}\\FinalResult\\gfx\\animated_textures\\frontend_background")
    if not os.path.exists(path + f"\\outputs"):
        os.makedirs(f"{path}\\outputs")
    if not os.path.exists(path + f"\\ToConvert"):
        os.makedirs(f"{path}\\ToConvert")
    if not os.path.exists(path + f"\\FinalResult"):
        os.makedirs(f"{path}\\FinalResult")
    if not os.path.exists(abspath + f"\\data.txt"):
        open(abspath + f"\\data.txt", 'a').close()

