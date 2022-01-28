import os
import re
import threading

from wand import image

from even_distribution import Even_Distribution
from helpers import getPath

path = getPath()


def ConvertSprites(Data):
    threads = []
    ThreadsCount = int(Data["THR"])
    directories = os.listdir(f"{path}\\ToConvert/")
    directories.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
    ProcessedArray = Even_Distribution(directories, wanted_parts=ThreadsCount)
    for i in range(ThreadsCount):
        my_thread = threading.Thread(target=ConvertToDDS, args=(ProcessedArray[i],))
        threads.append(my_thread)
    for i in threads:
        i.start()
    for i in threads:
        i.join()


def ConvertToDDS(Array):
    for x in Array:
        NewName = str(x).replace(".png", "")
        print(NewName)
        print(path + "\\ToConvert\\" + x)
        print(os.path.isfile(path + "\\ToConvert\\" + x))
        with image.Image(filename=path + "\\ToConvert\\" + x) as img:
            img.compression = 'dxt1'
            if not os.path.isfile(
                    path + "\\FinalResult\\gfx\\animated_textures\\frontend_background\\" + NewName + ".dds"):
                print("new file")
                img.save(
                    filename=f"{path}\\FinalResult\\gfx\\animated_textures\\frontend_background\\{NewName}" + ".dds")
            else:
                print("old file replace")
                os.remove(path + "\\FinalResult\\gfx\\animated_textures\\frontend_background\\" + NewName + ".dds")
                img.save(
                    filename=f"{path}\\FinalResult\\gfx\\animated_textures\\frontend_background\\{NewName}" + ".dds")
