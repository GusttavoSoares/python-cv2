import numpy as np
import cv2

cap = cv2.VideoCapture('assets/plane-video.mp4')

while True:
    ret, frame = cap.read() # ret serve para saber se a câmera iniciou corretamente, caso esteja sendo utilizada por outro serviço vai dar erro
    width = int(cap.get(3)) # pega a largura do vídeo
    height = int(cap.get(4)) # pega a altura do vídeo

    image = np.zeros(frame.shape, np.uint8) # vai iniciar com tela toda preta (0,0,0)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #top left
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180) #top right
    image[height//2:, width//2:] = smaller_frame #bottom right

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): # vai esperar 1 milisegundo, retorna o valor ascii da tecla que for clicada. Se for igual a 'q', vai sair do loop
        break

cap.release() # libera a câmera para ser utilizada por outro serviço
cv2.destroyAllWindows