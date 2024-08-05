import cv2 as cv
img=cv.imread("x.png",1)
img1=img[41:117,0:64]
cv.imwrite("main.png",img1)