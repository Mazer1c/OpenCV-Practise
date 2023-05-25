import cv2
import numpy as np

img = np.zeros((400,400),dtype="uint8") #* Создаем матрицу, сост. из 0

circle = cv2.circle(img.copy(),(img.shape[1]//2,img.shape[0]//2),img.shape[1]//8,(255,0,0),thickness=cv2.FILLED) 
#* Создаем одно изображение с кругом
rectangle = cv2.rectangle(img.copy(),(0,0),(img.shape[0],img.shape[1]//8),(255,0,0),thickness=cv2.FILLED)
#* Другое - с прямоугольником

def findCrossing(): #* Выведется ничего, тк нет пересечений в двух картинках.
    img = cv2.bitwise_and(circle,rectangle)
    cv2.imshow("Crossing",img)
    cv2.waitKey(0)

def joinAll(): #* Объединение 2-х изображений
    img = cv2.bitwise_or(circle,rectangle)
    cv2.imshow("Join",img)
    cv2.waitKey(0)

def Xor(img): #* 2 объекта будут показаны в 1 пикче, в местах пересечений значения перемнных будут = 0
    rectangle = cv2.rectangle(img.copy(),(0,0),(img.shape[0],img.shape[1]),(255,0,0),thickness=cv2.FILLED)
    img = cv2.bitwise_xor(rectangle,circle)
    cv2.imshow("Xor",img)
    cv2.waitKey(0)

def Inversion():
    img = cv2.bitwise_not(circle)
    cv2.imshow("Inversion",img)
    cv2.waitKey(0)
Inversion()
""" cv2.imshow("2",rectangle)
cv2.waitKey(0) """