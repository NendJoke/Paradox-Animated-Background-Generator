import re
import threading

from PIL import Image
import os

from even_distribution import Even_Distribution
from helpers import getPath

path = getPath()


def MergeSprites(Data):
    threads = []
    ThreadsCount = int(Data["THR"])
    directories = os.listdir(f"{path}\\outputs/")

    ProcessedArray = Even_Distribution(directories, wanted_parts=ThreadsCount)
    for i in range(ThreadsCount):
        my_thread = threading.Thread(target=MergeSpritesThreaded, args=(ProcessedArray[i],))
        threads.append(my_thread)
    for i in threads:
        i.start()
    for i in threads:
        i.join()


def MergeSpritesThreaded(Array):
    max_frames_row = 100000
    frames = []
    tile_width = 0
    tile_height = 0

    spritesheet_width = 0
    spritesheet_height = 0
    for current_directory in Array:
        FolderName = str(current_directory)
        cur_dir_path = os.listdir(f"{path}\\outputs/{FolderName}")
        cur_dir_path.sort(key=lambda var: [int(x) if x.isdigit() else x for x in re.findall(r'[^0-9]|[0-9]+', var)])
        # for i in cur_dir_path:
        # print(i[:-4])
        # redacted_cur_dir.append(i[:-4])
        # sorted_cur_dir = sorted(cur_dir_path, key=float)
        # print(sorted_cur_dir)
        for current_file in cur_dir_path:
            print(current_file)
            with Image.open(f"{path}\\outputs/{str(current_directory)}\\{current_file}") as im:
                frames.append(im.getdata())

        tile_width = frames[0].size[0]
        tile_height = frames[0].size[1]

        spritesheet_width = tile_width * len(frames)
        spritesheet_height = tile_height

        spritesheet = Image.new("RGBA", (int(spritesheet_width), int(spritesheet_height)))

        for current_frame in frames:
            # print(frames.index(current_frame))
            left = tile_width * (frames.index(current_frame) % max_frames_row)
            box = [left, 0, left + tile_width, tile_height]
            cut_frame = current_frame  # .crop((0, 0, tile_width, tile_height))

            spritesheet.paste(cut_frame, box)

        if not os.path.isfile(path + "\\ToConvert\\" + "spritesheet-" + FolderName + ".png"):
            spritesheet.save(path + "\\ToConvert\\" + "spritesheet-" + FolderName + ".png", "PNG")
        else:
            os.remove(path + "\\ToConvert\\" + "spritesheet-" + FolderName + ".png")
            spritesheet.save(path + "\\ToConvert\\" + "spritesheet-" + FolderName + ".png", "PNG")

        # spritesheet.save(path + "\\ToConvert\\" + "spritesheet-" + str(current_directory) + ".png", "PNG")
        frames = []
        tile_width = 0
        tile_height = 0
        spritesheet_width = 0
        spritesheet_height = 0
