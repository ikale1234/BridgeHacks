import pygame
import random
import os


def getPic():
    pictureDirectory = ["trash", "recycle",  "yardtrim"]
    trashTypeNum = random.randrange(0, 3)
    trashType = os.listdir(pictureDirectory[trashTypeNum])
    randomPic = trashType[random.randrange(0, len(trashType))]
    path = os.path.join(pictureDirectory[trashTypeNum], randomPic)
    return path, trashTypeNum
