# Detecção de face e olho

import cv2
import numpy as np

cap = cv2.VideoCapture('assets/woman-video.mp4')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # o algoritmo precisa na escala gray
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #scaleFactor - quanto a imagem deve reduzir, o algoritmo foi treinado com um tamanho especifico, quanto menor, mais certeiro vai ser, mas será mais lento
    #minNeighbors - retorna as posições que provavelmente vai ter uma face.
    # Em geral, vai encontrar todas as faces na imagem
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y+ h), (0, 0, 255), 5) # vai desenhar retângulos nas faces
        roi_gray = gray[y:y+w, x:x+w] # traz a localização da face - region of interest 
        roi_color = frame[y:y+h, x:x+w] # traz a localização na imagem colorida (original). roi_gray não tem o mesmo tamanho do roi_color
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.8, 5) # traz a localização dos olhos SOMENTE na roi_gray (ou seja, é relativo a face detectada)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()





