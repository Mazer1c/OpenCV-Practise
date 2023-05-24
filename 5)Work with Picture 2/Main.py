import cv2
import numpy as np

img = cv2.imread("Akane.jpg")

def imageFlip(img):
    img = cv2.flip(img,1) #* 0 - отзеркалено по вертикали, 1 - по горизонтали, -1 - по вертикали и горизонтали.
    cv2.imshow("imageFlip",img)
    cv2.waitKey(0)

def imageRotate(img,angle):
    height, widht = img.shape[:2] #* Получаем высоту и ширину исходного изображения.
    point  #* Точка вращения. Те точка,относительно которой будет производиься поворот.ж