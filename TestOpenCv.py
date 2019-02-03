import cv2

print(cv2.__version__)

imagem = cv2.imread('opencv-python.jpg')
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", imagem)
cv2.imshow("Cinza", imagem_cinza)

cv2.waitKey()