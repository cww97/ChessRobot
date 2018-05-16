import PIL.Image as Image
from numpy import *
import numpy as np
from time import clock

if __name__ == '__main__':
    img = Image.open('output.jpg')
    # img.resize((988, 988))
    img = img.convert('L')
    width, height = img.size
    print(width)
    print(height)
    single_width = int(width / 9)
    single_height = int(height / 9)
    bx = -5
    by = 20
    outputlist = []
    for i in range(9):
        for j in range(9):
            box = (j*single_height+bx, i*single_width+by, (j+1)*single_height+bx, (i+1)*single_width+by)
            single_img = img.crop(box)
            single_img.save('./output/'+str(i)+'_'+str(j)+'.png')
            tmp = np.matrix(single_img.getdata())
            print(tmp)
            single_sum = 0
            l, w = tmp.shape
            size = l*w
            if i == 9:
                l = l / 2
            for m in range(l):
                for n in range(w):
                    single_sum += tmp[m, n]
            single_sum /= size
            if i == 0 and j == 0:
                print(single_sum)
            if i == 4 and j == 2:
                print(single_sum)
            if i == 1 and j == 3:
                print(single_sum)
            if single_sum > 130:
                outputlist.append(-1)
            elif single_sum < 60:
                outputlist.append(1)
            else:
                outputlist.append(0)

    out = np.matrix(outputlist).reshape((9, 9))
    print(out)