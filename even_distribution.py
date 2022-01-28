import os
import threading


def Even_Distribution(alist, wanted_parts=1):
    length = len(alist)
    return [alist[i * length // wanted_parts: (i + 1) * length // wanted_parts]
            for i in range(wanted_parts)]

# directories = os.listdir("outputs/")
# directories.sort(key=float)


# def empty(array):
# print(array)


# ThreadsCount = 10
# ProcessedArray = split_list(directories, wanted_parts=ThreadsCount)
# for i in range(ThreadsCount):
# my_thread = threading.Thread(target=empty, args=(ProcessedArray[i],))
# my_thread.start()
