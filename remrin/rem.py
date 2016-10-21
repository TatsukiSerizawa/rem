#レムを表示するプログラム

#coding: utf-8

import numpy as np
import cv2

#画像読み込み
img = imread('rem1.py', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Rem', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
