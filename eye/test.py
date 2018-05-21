import numpy as np
import cv2
from matplotlib import pyplot as plt
from cv2 import *
from math import *
import os
if __name__ == '__main__':
    path = os.getcwd()
    print(os.path.isfile('../camera/chessboard.png'))
    img = cv2.imread('../camera/chessboard.png')
    # img = cv2.imread('./test5.bmp')

    img = cv2.resize(img, None, fx=0.3, fy=0.3)
    # img = cv2.medianBlur(img, 5)
    #img = img[0:700, 150:700]
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgray = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # edge = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    edge = cv2.Canny(imgray, 50, 50)
    cv2.imwrite('edge.jpg', edge)
    circles = cv2.HoughCircles(imgray, cv2.HOUGH_GRADIENT, 1, len(imgray)/12, param1=116, param2=45, minRadius=0, maxRadius=0)
    minLineLength = 200
    maxLineGap = 40
    lines = cv2.HoughLinesP(edge, 1, np.pi / 180, 100, minLineLength, maxLineGap)
    average_radius = 0
    print(lines)
    for x1, y1, x2, y2 in lines[:, 0]:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        print(x1, x2, y1, y2)
    for i in circles[0, :]:
        average_radius += i[2]
    average_radius /= len(circles[0, :])
    for i in circles[0, :]:
        print(i)
        if i[2] < average_radius:
            cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 0), 2)
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    cv2.imwrite('gray.jpg', img)