import cv2
import numpy as np

img = cv2.imread("Akane.jpg")

def imageFlip(img):
    img = cv2.flip(img,1) #* 0 - отзеркалено по вертикали, 1 - по горизонтали, -1 - по вертикали и горизонтали.
    cv2.imshow("imageFlip",img)
    cv2.waitKey(0)

def imageRotate(img,angle):
    height, widht = img.shape[:2] #* Получаем высоту и ширину исходного изображения.
    point = (widht//2,height//2)  #* Точка вращения. Те точка,относительно которой будет производиься поворот.
    #* В данном случае мы зеркалим относительно центра экрана
    mat = cv2.getRotationMatrix2D(point,angle,1)
    #! Cначала передаем точку вращения,угол вращения,увеличение изображения при повороте.
    return cv2.warpAffine(img,mat,(widht,height))

    """ img = imageRotate(img,180)
    cv2.imshow("Rotated Image",img)
    cv2.waitKey(0) """

def movePhoto(x,y,img_param):
    mat = np.float32([[1,0,x],[0,1,y]]) #! 1 массив - [коорд x, коорд y,смещение по x],2 массив - [коорд x, коорд y, cмещение по y]
    return cv2.warpAffine(img_param,mat,(img_param.shape[1],img_param.shape[0]))

    """ img = movePhoto(50,100,img)
    cv2.imshow("Moved Image",img)
    cv2.waitKey(0) """

def angleGetpos(): #* Получаем все контуры и ИХ КООРДИНАТЫ
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #*  Переводим изображение в серый цвет для оптимизации вычислений
    BluredImg = cv2.GaussianBlur(grayImg,(3,3),0) #* Размываем изображение для оптимизации вычислений (контуров меньше)
    Img = cv2.Canny(BluredImg,100,140)
    #! Значение первого порога показывает, что, если яркость < n-числа, то значение будет проигнорировано( = 0)
    #! Второй порог же показывает, что, если яркость > z-числа, то значение будет приравняно к 255

    con, hirarhy = cv2.findContours(Img,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) #! Ищем ВСЕ доступные контуры
    return con
 
def PrintNewPic(): #* Рисуем картинку на основе координат, полученных нами выше.
    con = angleGetpos()
    new_img = np.zeros(img.shape,dtype='uint8')
    cv2.drawContours(new_img,con,-1,(255,0,0),thickness=1)
    cv2.imshow("Res",new_img)
    cv2.waitKey(0)

