import cv2
import numpy as np

def createEmptyImage():
    image = np.zeros((600,400,3),dtype='uint8') #* Cоздаем rgb фото(матрицу), которую заполняем 0 => цвет полотна чёрный
    cv2.imshow("Created Image",image)
    cv2.waitKey(0)

def createColorfulImage():
    #! Cтандарнтый формат фото - RGB
    #! Формат фото в openCV - BGR
    image = np.zeros((600,400,3),dtype='uint8') #* Создали матрицу для последующего редактирования.
    image[:] = 255, 0, 0 #* Применение ко всем объектам матрицы следующих значений(в нашем случае - цвета)
    cv2.imshow("Colored Picture",image)
    cv2.waitKey(0)

def colorPartOfImage():
    image = np.zeros((400,400,3),dtype='uint8')
    image[image.shape[0]//4:image.shape[0]//2,image.shape[1]//4:image.shape[1]//2] = 255,0,0 #* Сначала указываем то,что хотим закрасить по высоте, затем - по ширине (отступ идет с левого
    #* верхнего края экрана)
    cv2.imshow("Colored Picture",image)
    cv2.waitKey(0)

def createRectangle():
    image = np.zeros((400,500,3),dtype='uint8')
    cv2.rectangle(image,(image.shape[1]//2,image.shape[0]//2),(100,100),(255,0,0),thickness = 1) #* Создание обводки по принципу:
    #*     источник,коорды начала рисовки с правого нижнего угла,разрешение,цвет,толщина линий.  
    cv2.imshow("rectangle",image)
    cv2.waitKey(0)
createRectangle()