import cv2
import numpy as np
import matplotlib.pyplot as plt

def indexgen(x,r,n):
    index = []
    k = []

    for i in range(n):
        x = r*x*(1-x) #logistic map
        k.append(x) #generating the key
        index.append(i) #generating the index
    
    for i in range(n):
        for j in range(n):
            if(k[i] > k[j]):
                k[i] , k[j] = k[j] , k[i] #re-arranging keys

                index[i] , index[j] = index[j] , index[i]
    
    return index


def shuffleimg(img,index,x,y):
    for i in range(x):
        k=0
        for j in range(y):
            ecrimg[i][j] = img[i][index[k]]
            k = k + 1
    
    return ecrimg

def reshuffle(img,index,x,y):
    ecrimg = np.zeros(shape = [width,height],dtype=np.uint8)
    for i in range(x):
        k=0
        for j in range(y):
            ecrimg[i][index[j]] = img[i][j]
            k = k + 1
        
    return ecrimg


img = cv2.imread("cameraman.bmp",0)
plt.imshow(img,cmap=plt.cm.gray)
plt.show()
height = img.shape[0]
width = img.shape[1]
ecrimg = np.zeros(shape=[width,height],dtype=np.uint8)

key = indexgen(0.1,3.91,height)
ecrimg = shuffleimg(img,key,width,height)

plt.imshow(ecrimg,cmap = plt.cm.gray)
plt.show()
ecrimg1 = np.zeros(shape=[width,height],dtype=np.uint8)

key = indexgen(0.1,3.91,height)
ecrimg1 = reshuffle(ecrimg,key,width,height)

plt.imshow(ecrimg1,cmap=plt.cm.gray)
plt.show()


