import cv2 as cv
img=cv.imread("x.png",1)
cv.circle(img,[102,102],65,[0,0,0],5)
cv.imwrite("main.png",img)