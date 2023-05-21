import cv2
import numpy as np

def createEmptyImage():
    image = np.zeros((600,400,1),dtype='uint8')
    cv2.imshow("Created Image",image)
    cv2.waitKey(0)
createEmptyImage()