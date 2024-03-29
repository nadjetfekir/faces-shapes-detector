import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # black image
# print(img)
# img[200:300,100:300]=255,0,0  #color an image

# cv2.line(img,(0,0),(300,300),(0,255,0)) #the begenning the end and the color
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0))  # til the end of the image
cv2.rectangle(img, (0, 0), (255, 350), (0, 0, 255))
# cv2.rectangle(img,(0,0),(255,350),(0,0,255),cv2.FILLED)#to fill the rectangle
cv2.circle(img, (400, 50), 30, (255, 255, 0))
cv2.putText(img, " Open Cv ", (300, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 150, 0), 1)

cv2.imshow("image", img)
cv2.waitKey(0)
