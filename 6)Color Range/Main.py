import cv2
import numpy as np

img = cv2.imread("Akane.jpg")

def RGB2HSV(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    cv2.imshow("Conv",img)
    cv2.waitKey(0)

def RGB2LAB(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2Lab)
    cv2.imshow("Conv",img)
    cv2.waitKey(0)

def BGR2RGB(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("Conv",img)
    cv2.waitKey(0)

def Layers(img):
    r,g,b = cv2.split(img)
     
    """ imgB = cv2.merge([r,g,b]) #* Cоединяем слои в пикчу
    cv2.imshow("Conv",imgB)
    cv2.waitKey(0) """

    cv2.imshow("Conv",b) #* Цвета, прибл. к указ. знач. становятся белыми на просмотре
    cv2.waitKey(0)
Layers(img)