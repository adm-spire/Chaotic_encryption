import numpy as np
index = [1,0,2]
m = [[3,2,1],[5,4,6]]
m1 = np.zeros([len(m),len(m[0])],dtype=int)

#matrix shuffling
for i in range(len(m)):
    k=0
    for j in range(len(m[0])):
        m1[i][j] = m[i][index[k]]
        k = k + 1

print("shuffled matrix",m1)

for i in range(len(m)):
    k=0
    for j in range(len(m[0])):
        m[i][index[k]] = m1[i][j]
        k = k + 1

print("unshuffled matrix",m)

