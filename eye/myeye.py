# just main for eye
# in: jpg
# out: matrix of a board state
import cv2
import numpy as np


def see():
    img = cv2.imread('data/try0.png')
    # print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cor = cv2.findChessboardCorners(gray, (7, 9))
    print(cor)
    return [[], []]


def get_input():
    return input("Your move: ")



