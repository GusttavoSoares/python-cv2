# Fundamentos e manipulação de imagens

import cv2
import random

img = cv2.imread('assets/image1.png', -1)
#print(img)
#print(type(img))
#print (img.shape) # (881, 760, 3) height, width, channels
#print(img[0]) # primeira linha
#print(img.shape[1])  #760

# vai percorrer o height até o tamanho 99 e toda a largura da imagem (760) e vai modificar a imagem pintando com valores
# for i in range(100):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] # tem a coluna alpha

        
tag = img[200:400, 300:550] # vai copiar parte da imagem no intervalo especificado
img[200:400, 100:350] = tag # os intervalos para colar tem que ser do mesmo tamanho

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows

'''
Como a imagem é interpretada
print(img)

  [168 159 142] 
  [168 159 142] 
  [168 159 142]]

 [[156 159 156] 
  [156 159 156] 
  [156 159 156]

Pega os pixels da imagem e carrega em um NumPi array. NumPi é uma biblioteca que faz alterações no array com uma performance maior 

Há 3 valores que representa um pixel: vermelho, verde e azul (RGB)

Para representar uma imagem é utilizado um array tri-dimensional

[
[[], [], []],
[],
[]
]

No OpenCV, a sequencia é blue, green e red
[0, 0, 0]
0-255

0 - representa nada
255 - representa tudo
Se tiver o valor 255 na posição 0, então será totalmente azul

'''
