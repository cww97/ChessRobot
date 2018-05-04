import PIL.Image as Image
from numpy import *
import numpy as np
from time import clock

if __name__ == '__main__':
    img = Image.open('test2.jpg')
    img.resize((988, 988))
    img = img.convert('L')
    width, height = img.size
    print(width)
    print(height)
    single_width = int(width / 19)
    single_height = int(height / 19)
    b = 30
    outputlist = []
    for i in range(19):
        for j in range(19):
            box = (j*single_height+b, i*single_width+b, (j+1)*single_height+b, (i+1)*single_width+b)
            single_img = img.crop(box)
            single_img.save('./output/'+str(i)+'_'+str(j)+'.png')
            #single_img.show()
            #print(np.matrix(single_img.getdata()))
            tmp = np.matrix(single_img.getdata())
            single_sum = 0
            l, w = tmp.shape
            size = l*w
            for m in range(l):
                for n in range(w):
                    single_sum += tmp[m, n]
            if i == 18 or j == 18:
                single_sum += (size / 2)*100
            single_sum /= size
            if single_sum > 200:
                outputlist.append(-1)
            elif single_sum < 100:
                outputlist.append(1)
            else:
                outputlist.append(0)

    out = np.matrix(outputlist).reshape((19, 19))
    print(out)