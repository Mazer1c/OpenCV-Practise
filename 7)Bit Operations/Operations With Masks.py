import cv2
import numpy as np

img = cv2.imread("Akane.jpg")
mat = np.zeros(img.shape[:2],dtype="uint8")

circle = cv2.circle(mat.copy(),(mat.shape[1]//2,mat.shape[0]//2),mat.shape[1]//8,(255,0,0),thickness=cv2.FILLED) 
#* Создаем одно изображение с кругом
rectangle = cv2.rectangle(mat.copy(),(0,0),(mat.shape[0],mat.shape[1]//8),(255,0,0),thickness=cv2.FILLED)
#* Другое - с прямоугольником

#img = cv2.bitwise_and(img,img,mask=circle) #* Накладываем фото на фото по маске
#img = cv2.bitwise_or(img,img,mask=circle)
#img = cv2.bitwise_xor(img,img,mask=circle)
#img = cv2.bitwise_not(img,img,mask=circle)


cv2.imshow("Result",img)
cv2.waitKey(0)
