#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 23:22:31 2019

@author: joaopaulo
"""

import cv2

classificadorFace = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
classificadorOlhos = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

imagem = cv2.imread('pessoas/beatles.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetectadas = classificadorFace.detectMultiScale(imagemCinza)

for (x, y, l, a) in facesDetectadas:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
    regiao = imagem[y: y + a, x: x + l]
    regiaoCinzaOlho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
    olhosDetectados = classificadorOlhos.detectMultiScale(regiaoCinzaOlho, scaleFactor=1.1, minNeighbors=2)
    print(olhosDetectados)
    
    for (ox, oy, ol, oa) in olhosDetectados:
       cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2) 
        
    
cv2.imshow("Faces e olhos detectados", imagem)
cv2.waitKey()