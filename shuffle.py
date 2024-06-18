import numpy as np
a = [10,20,30,40,50]
index = [3,2,0,1,4]
print("original array",a)
b = []
for i in range(5):
    b.append(a[index[i]])
print("shuffled array",b)
c = np.zeros(5,dtype=int)

for i in range(5):
    c[index[i]] = b[i]
print("reshuffled array",c)