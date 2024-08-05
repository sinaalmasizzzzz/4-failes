import cv2 as cv
img=cv.imread("1.png",1)
img=cv.cvtColor(img,cv.COLOR_HSV2BGR)
imgc=cv.cvtColor(img,cv.COLOR_Lab2BGR)
img1=cv.imread("2.png",1)
img1=cv.cvtColor(img,cv.COLOR_HSV2BGR)
img1c=cv.cvtColor(img,cv.COLOR_Lab2BGR)

cv.imshow("1",img)
cv.imshow("2",imgc)
cv.imshow("3",img1)
cv.imshow("4",img1c)
cv.waitKey()