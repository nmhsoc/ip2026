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

el = cv2.equalizeHist(gray)
eH = [0] * 256
for ro in el:
    for p in ro:
        eH[p] += 1
print(eH)
pt.bar(range(256), eH)
pt.show()

rsz = cv2.resize(gray, None, fx=1.5, fy=1.5)

cv2.imshow('original  Image', img)
cv2.imshow('Grayscale Image', gray)
cv2.imshow('Resized Image', rsz)
cv2.imshow('Equalized gray Image', el)

c = cv2.hconcat([gray, el])
cv2.imshow('Gray vs Equalized gray', c)
#
print(img.shape)
print(img.shape[2])
print(img.dtype)
print(img.min())
print(img.max())

print(gray.shape)
print(1)
print(gray.dtype)
print(gray.min())
print(gray.max())

cv2.waitKey(0)
cv2.destroyAllWindows()

#python3 venv/lab1/B1.py