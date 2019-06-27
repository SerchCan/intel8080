import numpy as np
mem = [0x01 for i in range(0x2400,0x4000)]
print(len(mem))

pixels=[]
for i in mem:
    for bit in range(7,-1,-1):
        px=(i>>bit) & 0x01
        pixels.append(px)
print(len(pixels))
mat = np.array(pixels)
mat = np.resize(mat,(256,224))
print(mat)
T = mat.transpose()

print(T)