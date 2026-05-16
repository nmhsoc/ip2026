import cv2
import matplotlib.pyplot as pt
import numpy as np

img = cv2.imread('IMG_0297.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('original', gray)

def change(im, a, b):
    c = np.zeros(im.shape, dtype=np.uint8)
    for i in range(len(im)):
        for j in range(len(im[i])):
            pix = a * im[i][j] + b
            if pix > 255:
                pix = 255
            if pix < 0:
                pix = 0
            c[i][j] = int(pix)
    return c

p1 = change(gray, 1.0, 50) #Brightness increases because pixel values become larger. Contrast stays almost the same because a=1.0.
H1 = [0] * 256
for row in p1:
    for p in row:
        H1[p] += 1
cv2.imshow('(1.0,50)', p1) 
print(H1)
pt.bar(range(256), H1)
pt.show()

p2 = change(gray, 1.0, -50) #Brightness decreases because pixel values become smaller. Contrast stays almost the same because a=1.0. 
H2 = [0] * 256
for row in p2:
    for p in row:
        H2[p] += 1
cv2.imshow('(1.0,-50)', p2)
print(H2)
pt.bar(range(256), H2)
pt.show()

p3 = change(gray, 1.5, 0) #Contrast increases because the difference between dark and bright pixels becomes larger. Brightness is almost unchanged because b=0.
H3 = [0] * 256
for row in p3:
    for p in row:
        H3[p] += 1
cv2.imshow('(1.5,0)', p3)
print(H3)
pt.bar(range(256), H3)
pt.show()

p4 = change(gray, 0.5, 0) #Contrast decreases because the difference between dark and bright pixels becomes smaller. Brightness is almost unchanged because b=0.
H4 = [0] * 256
for row in p4:
    for p in row:
        H4[p] += 1
cv2.imshow('(0.5,0)', p4)
print(H4)
pt.bar(range(256), H4)
pt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()