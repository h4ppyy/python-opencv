#-*-coding:utf-8-*-

import cv2
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui
from matplotlib import pyplot as plt

#ImageGrab.grab().save("screen.jpg", "JPEG")
ImageGrab.grab().save("screen.png", "PNG")

img = cv2.imread("screen.png",0)
img2 = img.copy()
template = cv2.imread("cookie.png",0)

# template 이미지의 가로/세로
w,h = template.shape[::-1]

# Template Match Method
methods = [
    #'cv2.TM_CCOEFF',
    'cv2.TM_CCOEFF_NORMED',
    #'cv2.TM_CCORR',
    #'cv2.TM_CCORR_NORMED',
    #'cv2.TM_SQDIFF',
    #'cv2.TM_SQDIFF_NORMED'
]

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    res = cv2.matchTemplate(img,template,method)
    min_val,max_val,min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0]+w,top_left[1]+h)
    cv2.rectangle(img,top_left,bottom_right,255,5)

    print('top_left -> ', top_left)
    print('bottom_right -> ', bottom_right)

    pyautogui.moveTo(top_left[0], top_left[1])

    plt.subplot(121),plt.title(meth),plt.imshow(res,cmap='gray'),plt.yticks([]),plt.xticks([])
    plt.subplot(122),plt.imshow(img,cmap='gray')
    plt.show()
