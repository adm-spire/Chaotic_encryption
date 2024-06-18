def keygenerator(x,r,size):
    key = []
    for i in range(size):
        x = r*x*(1-x)
        key.append(int(x*pow(10,16)%256))

    return key

#print(keygen(0.001,3.91524,10))