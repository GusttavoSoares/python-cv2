import numpy as np
import cv2

cap = cv2.VideoCapture('assets/plane-video.mp4')

while True:
    ret, frame = cap.read() 
    width = int(cap.get(3)) 
    height = int(cap.get(4)) 

    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10) # vai desenhar uma linha azul do inicio ao fim (uma hipotenusa) 
    img = cv2.line(img, (0,height), (width, 0), (0,255,0), 5) 
    
    # lembrar que no topo na esquerda é (0,0), para direita e baixo aumenta
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128, 5))

    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    img = cv2.putText(img, "Vrumm!", (100, height - 50), font, 5, (0,0, 0), 5,  cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): 
        break

cap.release() 
cv2.destroyAllWindows