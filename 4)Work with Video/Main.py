import cv2
import numpy as np

vid = cv2.VideoCapture("Oshi no ko.mp4")

def findingAngles(): #* Извлекаем из видео контуры.
    while True:
        success, frame = vid.read() #* Читаем входящий кадр
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #* Преобразуем кадр в серый цвет
        anglesImg = cv2.Canny(grayImg,50,50) #* Находим контуры

        cv2.imshow("Vid",anglesImg) #* показ видео
        if cv2.waitKey(1)&0xFF == ord('q'):
            break

findingAngles()