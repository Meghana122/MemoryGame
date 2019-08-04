
import os

def path(filename):
    filepath = os.path.realpath(__file__)
    dirpath = os.path.dirname(filepath)
    fullpath = os.path.join(dirpath, filename)
    return fullpath
