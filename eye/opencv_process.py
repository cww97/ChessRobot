from cv2 import *
import cv2
from math import ceil


def image_process(img, last_img):
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgray = cv2.medianBlur(imgray, 5)
    last_img = cv2.cvtColor(last_img, cv2.COLOR_BGR2GRAY)
    last_img = cv2.medianBlur(last_img, 5)
    edge = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    last_edge = cv2.adaptiveThreshold(last_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('edge.jpg', edge)
    cv2.imwrite('last.jpg', last_edge)
    result = cv2.bitwise_xor(edge, last_edge)
    result = cv2.medianBlur(result, 7)
    cv2.imwrite('result.jpg', result)
    return result


def cut_process(input_image):
    img = cv2.resize(input_image, None, fx=0.3, fy=0.3)
    img = cv2.medianBlur(img, 7)
    #img = img[0:700, 150:700]
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # imgray = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.imwrite('gray.jpg', imgray)
    edge = cv2.Canny(imgray, 100, 100)
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
    cv2.imwrite('output.jpg', img2)
    return img2


def get_input(result_image, chessboard_image):
    l, w = result_image.shape
    imgray = cv2.cvtColor(chessboard_image, cv2.COLOR_BGR2GRAY)
    num = 0
    single_sum = 0
    x0 = -1
    x1 = 10000
    y0 = -1
    y1 = 10000
    for i in range(l):
        for j in range(w):
            if result_image[i, j] > 0:
                num += 1
                tmp = imgray[i, j]
                single_sum += tmp
                if i > x0:
                    x0 = i
                if i < x1:
                    x1 = i
                if j > y0:
                    y0 = j
                if j < y1:
                    y1 = j
    if abs(x1 - x0) > 100 or abs(y1 - y0) > 100:
        print('None')
        return [-1, -1], 'None'
    x, y = (x0 + x1) / 2, (y0 + y1) / 2
    x, y = 8 * (x - 50) / (l - 100), 8 * (y - 40) / (w - 80)
    x, y = int(x), ceil(8 - y)
    location = [x, y]
    if num > 0:
        single_sum = single_sum / num
    if single_sum < 60:
        player = 'black'
    else:
        player = 'white'
    print('location: ', location)
    print('player', player)
    return location, player


if __name__ == '__main__':
    img = cv2.imread('../camera/start.png')
    last_img = cv2.imread('../camera/start.png')
    img = cut_process(img)
    last_img = cut_process(last_img)
    cv2.imwrite('output1.jpg', img)
    cv2.imwrite('output2.jpg', last_img)
    result = image_process(img, last_img)
    result = cv2.medianBlur(result, 7)
    cv2.imwrite('result.jpg', result)
    get_input(result, img)