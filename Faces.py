#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:09:58 2019

@author: joaopaulo
"""
import cv2

classificador = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('pessoas/pessoas2.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificador.detectMultiScale(imagemCinza, scaleFactor=1.1, minNeighbors=9, minSize=(30,30))

print(len(facesDetectadas))

print(facesDetectadas)

for (x, y, l, a) in facesDetectadas:
    print(x, y, l, a)
    # coloca o retangulo nas faces encontradas
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 2)
    
cv2.imshow("Faces encontradas", imagem)
cv2.waitKey()