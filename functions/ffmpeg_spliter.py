import os
import shutil
import subprocess
import sys
from threading import Thread

from helpers import getPath

path = getPath()
abspath = os.path.abspath(".")


def SplitVideo(Data):
    video_path = Data["PATH"]
    MoveX = int(Data["CSH"])
    MoveY = int(Data["CSV"])
    CurrentMoveX = int(Data["SPH"])
    CurrentMoveY = int(Data["SPV"])
    DefaultMoveY = int(Data["SPV"])
    MaxMoveX = int(Data["EPH"])
    MaxMoveY = int(Data["EPV"])

    while CurrentMoveX < MaxMoveX:  # H
        while CurrentMoveY < MaxMoveY:  # Y
            FolderName = str(round(CurrentMoveX / MoveX)) + "-" + str(round(CurrentMoveY / MoveY))
            if not os.path.exists(path + f"\\outputs\\{FolderName}"):
                print("1 " + str(path + f"\\outputs\\{FolderName}"))
                os.makedirs(f"{path}\\outputs\\{FolderName}")
            else:
                print("2 " + str(path + f"\\outputs\\{FolderName}"))
                shutil.rmtree(f"{path}\\outputs\\{FolderName}")
                os.makedirs(f"{path}\\outputs\\{FolderName}")
            subprocess.call(f"{abspath}\\ffmpeg\\bin\\ffmpeg.exe -i {video_path} -vf crop={MoveX}:{MoveY}:{CurrentMoveX}:{CurrentMoveY} {path}\\outputs\\{FolderName}\\%d.png", stdout=sys.stdout, stderr=sys.stderr)
            CurrentMoveY = CurrentMoveY + MoveY
        CurrentMoveY = DefaultMoveY
        CurrentMoveX = CurrentMoveX + MoveX
        print("sss")

