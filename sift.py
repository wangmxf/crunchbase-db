import cv2
import numpy as np

img = cv2.imread('test-images/vungle-logo.png')
#gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = img

sift = cv2.SIFT()
kp = sift.detect(gray, None)

img=cv2.drawKeypoints(gray,kp)

cv2.imwrite('sift_keypoints.jpg',img)
