import cv2
import numpy as np

img = cv2.imread('assets/arcane-img.jpg', 0) #gray scale
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)
template = cv2.imread('assets/belt-arcane.png', 0)

h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods: # vai mostrar o resultado de todos os métodos
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc) # precisa desenhar um retangulo nas posições encontradas
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + w) # w e h é do template. Desse modo, é possível saber o fim do retângulo
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




