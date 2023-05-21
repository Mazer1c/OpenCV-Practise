import cv2
import numpy as np

img = cv2.imread("Akane K.jpg")

def getResolution():
    print(img.shape) #* <-- получаем разрешение фото. На выходе получаем кортеж из 3-х значений (высота,ширина,к-во слоев).

def pressImage():
    pressedImage = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2)) #*Получаем высоту и ширину входного фото, уменьшаем разрешение в 2 раза.
    cv2.imshow("Resized Akane",pressedImage) #* Вывод на экран
    cv2.waitKey(0)

def cutImage():
    cv2.imshow("cutted Image",img[0:100,0:300]) #* Обрезаем изображение, от 0 до 100 px по ширине, от 0 до 150 px по ширине
    cv2.waitKey(0)
    
def blurImage():
    bluredImg = cv2.GaussianBlur(img,(3,3),0) #* Блюр картинки, в кортеж передавай только нечетные значения, а иначе - бан!
    cv2.imshow("Blured image",bluredImg)
    cv2.waitKey(0)

def RGBtoWhiteBlack():
    WhiteNBlackPic = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #* Перевод из РГБ в Черно-белое изображение
    cv2.imshow("GrayPic",WhiteNBlackPic)
    print(WhiteNBlackPic.shape) #* У нас и так черно-белое изображение, но теперь у нас только 1 слой, а было 3.
    cv2.waitKey(0)

def findAngles(img):
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #* Сначала переведем изображение в черно-белый вид, чтобы библиотеке было проще
    #* определять контуры.
    img = cv2.Canny(grayImg,92,92) #* Определение контуров. Чем больше значение, тем больше деталей игнорируется.
    #matrix = np.ones((5,5),np.uint8)
    #img = cv2.dilate(img,matrix,iterations = 0) #* Увеличение "жирности" обводки, чем больше iterations, чем она жирнее.
    img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2)) #* Сжатие серого изображения
    cv2.imshow("Angles",img)
    cv2.waitKey(0)

findAngles(img)