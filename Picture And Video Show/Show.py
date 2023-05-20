import cv2

def image_show():
    img = cv2.imread("Picture And Video Show\Akane.jpg")
    cv2.imshow("Akane Kurokawa",img)
    cv2.waitKey(0)


def video_show():
    vid = cv2.VideoCapture("Oshi_No_Ko.mp4")
    while True: #* Тк видео состоит из множества кадров.
        success,img = vid.read()
        cv2.imshow("Vid",img)
        if cv2.waitKey(1) and 0xFF==ord("q"):
            break

image_show()
#video_show()