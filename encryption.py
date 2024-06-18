import cmath
import keygenerator as kg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread("cameraman.bmp")

plt.imshow(img,cmap='gray')
plt.show()

#generating chaotic keys
height = img.shape[0]
width = img.shape[1]

key = kg.keygenerator(0.01,4,height*width)
key_details = [0.01,4,height,width]
print("key",key)


#encryption/substitution

z=0
enimg = np.zeros(shape = [height,width,3],dtype=np.uint8)
for i in range(height):
    for j in range(width):
        #pixel value xor with key
        enimg[i,j] = img[i,j]^key[z]
        z+=1

plt.imshow(enimg,cmap='gray')
plt.show()
plt.imsave("EncryptedImage.bmp",enimg , cmap='gray')

#decryption

z=0
decimg = np.zeros(shape = [height,width,3],dtype=np.uint8)
for i in range(height):
    for j in range(width):
        #pixel xor with key
        decimg[i,j] = enimg[i,j]^key[z]
        z += 1

plt.imshow(decimg,cmap='gray')
plt.show()
plt.imsave("DecryptedImage.bmp",decimg ,cmap='gray')






