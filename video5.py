import cv2
import numpy as np

cap = cv2.VideoCapture('assets/plane-video.mp4')

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converte BRG para HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue) # vai trazer uma imagem somente entre o intervalo lower_blue e upper_blue, ou seja, só mostra o que é azul e seta como 1

    result = cv2.bitwise_and(frame, frame, mask=mask) # compara os bits da imagem com os bits da imagem 'frame'

    '''
    1 1 = 1
    0 1 = 0
    1 0 = 0
    0 0 = 0
    '''
    cv2.imshow('frame', result)
    cv2.imshow('mask', mask) # mascara é só preta ou branca

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows


'''
RGB: Red Green Blue
BGR: Blue Green Blue
HSV: Hue Saturation and Lightness/Brightness

'''

