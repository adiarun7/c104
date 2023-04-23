import cv2

img = cv2.imread("butterfly.jpg")
cv2.imshow("display image",img)
grayimg=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray scale",grayimg)
cv2.waitKey(0)