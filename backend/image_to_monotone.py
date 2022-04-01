import cv2
import numpy as np
import base64
def cv_to_base64(im):
    _, encoded = cv2.imencode(".jpg", im)
    img_str = base64.b64encode(encoded).decode("ascii")

    return img_str
    
def image_monotone():
    im = cv2.imread('uploads/image.png')
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    img_str = cv_to_base64(im_gray)
    return img_str
