#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 15:10:47 2019

@author: joaopaulo
"""

import cv2

classificadorRelogio = cv2.CascadeClassifier('cascades/relogios.xml')

imagem = cv2.imread("outros/relogio3.jpg")
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

detectado = classificadorRelogio.detectMultiScale(imagemCinza, scaleFactor=1.1)

for (x, y, l, a) in detectado:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
    
cv2.imshow("Encontrado", imagem)
cv2.waitKey()