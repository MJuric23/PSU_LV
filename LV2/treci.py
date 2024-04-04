import matplotlib.pyplot as plt
import numpy as np
import skimage.io

img = skimage.io.imread('tiger.png', as_gray=True)

height = img.shape[0]
width = img.shape[1]

#povecanje brightness -> a)
p = int(100)
for i in range(0, height):
    for j in range(0, width):
        if 255 - img[i][j] <= p:
            img[i][j] = 255        
        else:
            img[i][j] += p    

#rotacija u smjeru kazaljke na satu -> b)
img2 = np.zeros((width, height), np.uint8)
for i in range(0, width):
    t = height - 1
    for j in range(0, height):
        img2[i][t] = img[j][i]
        t -= 1

# c) zrcaljenje
img_mirr = np.zeros((height, width), np.uint8)
for i in range(0, width):
    img_mirr[:, width - i - 1] = img[:, i]

# d) smanjivanje rezolucije

plt.figure(1)
plt.imshow(img_mirr, cmap='gray', vmin=0, vmax=255)
plt.show()   