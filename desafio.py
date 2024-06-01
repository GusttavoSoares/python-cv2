import cv2
import numpy as np

img = cv2.imread('assets/arcane-green-img.png')


while True:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40]) # 40 para pegar tons baixos
    upper_green = np.array([70, 255, 255]) # 255 para pegar a cor mais forte pura

    mask = cv2.inRange(hsv, lower_green, upper_green)

    result = cv2.bitwise_and(img, img, mask=mask) # vai percorrer pela imagem e a cor precisa combinar com a mascara

    counters, hierarchy  = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # vai achar o contorno 
    
    for contour in counters:
        x, y, w, h = cv2.boundingRect(contour) #  calcula a menor caixa retangular que pode circunscrever um contorno
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3) # desenha um retângulo ao redor de cada ponto com 3 de espessura

    cv2.imshow('frame', img) 

    if cv2.waitKey(0) == ord('q'):
        cv2.destroyAllWindows
        break