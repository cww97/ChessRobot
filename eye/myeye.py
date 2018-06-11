# just main for eye
# in: jpg
# out: matrix of a board state

import cv2
import numpy as np

from eye.opencv_process import *
import time

def see():
    img = cv2.imread('data/try0.png')
    # print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cor = cv2.findChessboardCorners(gray, (7, 9))
    print(cor)
    return [[], []]


def get_input(old_last):
    while True:
        now = cv2.imread('../camera/chessboard.png')
        now = cut_process(now)
        result_img = image_process(now, old_last)
        result_img = cv2.medianBlur(result_img, 7)
        location, player = get_input_result(result_img, now)
        if player == 'black':
            old_last = now
            print('Now is the AI')
        elif player == 'white':
            print('Now is the player')
            old_last = now
            return location
        time.sleep(3)


def get_keyboard_input():
    result = input("Please input the location:\n")
    return result

if __name__ == '__main__':
    # last = cv2.imread('../camera/start.png')
    # last = cut_process(last)
    # get_input(last)
    get_keyboard_input()