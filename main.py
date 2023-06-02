import pytesseract
import cv2
import numpy as np
import os


image = cv2.imread("test.png")

text = pytesseract.image_to_boxes(image).split('\n')
for x in range(len(text)):
    text[x] = text[x].split()

print(text)
height, width, _ = image.shape

'''
a = text[0]
x, y, w, h = int(a[1]), int(a[2]), int(a[3]), int(a[4])
crop = image[x,y, x+w:y+h]
cv2.imshow('img',crop)
cv2.waitKey(0)

for i in range(len(text)-1):
    a = text[i]
    x, y, w, h = int(a[1]), int(a[2]), int(a[3]), int(a[4])
    cv2.rectangle(image, (x,height-y), (w, height-h), (50,50,255), 1)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.imwrite("gello", image)
'''