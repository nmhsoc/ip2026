import cv2
import matplotlib.pyplot as pt

img = cv2.imread('IMG_0297.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
H = [0] * 256
for row in gray:
    for p in row:
        H[p] += 1
print(H)
pt.bar(range(256), H)
pt.show()

def thres(I, T):
    B = I.copy()
    for i in range(len(I)):
        for j in range(len(I[i])):
            if I[i][j] > T:
                B[i][j] = 255
            else:
                B[i][j] = 0
    return B

b1 = thres(gray, 80)
b2 = thres(gray, 120)
b3 = thres(gray, 160)

cv2.imshow('T=80', b1)
cv2.imshow('T=120', b2)
cv2.imshow('T=160', b3)

cv2.waitKey(0)
cv2.destroyAllWindows()


