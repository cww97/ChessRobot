# just main for eye
# in: jpg
# out: matrix of a board state
import cv2
import numpy as np
from imageProcess import process_image


def see():
    img = cv2.imread('data/try0.png')
    # print(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cor = cv2.findChessboardCorners(gray, (7, 9))
    print(cor)
    return [[], []]


def get_input(old_last):
    while True:
        last = process_image()
        test = last - old_last
        for i in range(len(test)):
            for j in range(len(test[0])):
                if test[i, j] == -1:
                    return str(i)+','+str(j), last
                if test[i, j] == 1:
                    old_last = last



if __name__ == '__main__':
    first_last = process_image()
    first_last[2, 0] = 0
    action, new_last = get_input(first_last)
    print(new_last)
    print('action', action)