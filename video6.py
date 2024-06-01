# Deteccção de cantos

import cv2
import numpy as np

img = cv2.imread('assets/mesa-xadrez.png')
img = cv2.resize(img, (0, 0), fx=3, fy=3)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # tem que converter para gray para usar o método

corners = cv2.goodFeaturesToTrack (gray, 100, 0.01, 10) # imagem que deseja analisar, 100 melhores corners (cantos), 0.01 de precisão, 10 de distância entre os corners
corners = np.int0(corners) #transforma os pontos para inteiros

for corner in corners:
    x, y = corner.ravel() # [[1,2], [2,1]] -> [1,2,2,1], ou seja, transforma em um flat array (1 dimensão)
    cv2.circle(img, (x,y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range (i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3))) # vai retornar um int para cada valor
        cv2.line(img, corner1, corner2, color, 1)

cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




