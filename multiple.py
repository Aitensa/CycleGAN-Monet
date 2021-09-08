import cv2
import numpy as np

A0 = cv2.imread("A0.jpg")
A1 = cv2.imread("A1.jpg")

steps = 15

print(type(A0), A0.shape, A0.dtype)
#print(A0[:2,:2,:])
A0.astype(np.float)
A1.astype(np.float)
#print(A0[:2,:2,:])
for i in range(0, steps + 1):
    #cv2.imshow("dddd1", A0)
    middle = A1*(i/steps) + A0*(1 - i/steps)
    #print(middle[:2,:2,:])
    #middle = middle.astype(np.uint8)
    #print(middle[:2,:2,:])
    cv2.imshow("dddd", middle)
    cv2.waitKey(0)    
