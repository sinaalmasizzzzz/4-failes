import cv2 as cv
img=cv.imread("x.png",1)
cv.putText(img,"hi",[120,90],cv.FONT_HERSHEY_COMPLEX,1,[128,0,128],1)
cv.imwrite("main.png",img)