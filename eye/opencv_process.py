import numpy as np
import cv2
from matplotlib import pyplot as plt
from cv2 import *

if __name__ == '__main__':
    img = cv2.imread('test5.bmp')

    img = cv2.resize(img, None, fx=0.3, fy=0.3)
    img = img[0:700, 150:700]
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('gray.jpg', imgray)
    edge = cv2.Canny(imgray, 200, 200)
    cv2.imwrite('edge.jpg', edge)
    ret, thresh = cv2.threshold(edge, 127, 127, 127)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    x0 = 10000
    x1 = -1
    y0 = 10000
    y1 = -1
    for i in range(len(edge)):
        for j in range(len(edge[0])):
            if edge[i, j] > 0:
                if i < x0:
                    x0 = i
                if i > x1:
                    x1 = i
                if j < y0:
                    y0 = j
                if j > y1:
                    y1 = j
    print('x0', x0, 'x1', x1, 'y0', y0, 'y1', y1)
    #test = cv2.drawContours(edge, contours, 0, (0, 0, 0), 10)
    img2 = img[x0:x1, y0:y1]
    plt.imshow(edge)
    plt.show()
    cv2.imwrite('output.jpg', img2)