import PIL.Image as Image
from numpy import *
import numpy as np
from time import clock


def process_image():
    img = Image.open('output.jpg')
    # img.resize((988, 988))
    img = img.convert('L')
    width, height = img.size
    print(width)
    print(height)
    single_width = int(width / 9)
    single_height = int(height / 9)
    bx = 18
    by = 0
    outputlist = []
    for i in range(9):
        by -= 3
        for j in range(9):
            box = (j*single_height+bx, i*single_width+by, (j+1)*single_height+bx, (i+1)*single_width+by)
            single_img = img.crop(box)
            single_img.save('./output/'+str(i)+'_'+str(j)+'.png')
            tmp = np.matrix(single_img.getdata())
            single_sum = 0
            l, w = tmp.shape
            size = l*w
            for m in range(l):
                for n in range(w):
                    single_sum += tmp[m, n]
            single_sum /= size
            if i == 0 and j == 0:
                print(single_sum)
            if i == 2 and j == 0:
                print(single_sum)
            if i == 2 and j == 2:
                print(single_sum)
            if single_sum > 110:
                outputlist.append(-1)
            elif single_sum < 50:
                outputlist.append(1)
            else:
                outputlist.append(0)

    out = np.matrix(outputlist).reshape((9, 9))
    return out
