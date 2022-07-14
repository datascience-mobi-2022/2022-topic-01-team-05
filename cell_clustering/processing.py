from PIL import Image
from PIL import ImageFilter
import numpy as np
import cv2


def edge_enhancement(img):
    """
    applies the edge enhancement filter from the PIL package to the image
    : param img: image to be processed
    : return: image with enhanced edges
    """
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img


def median_filter(img):
    """
    applies the median filter from the PIL package to the image
    : param img: image to be processed
    : return: image processed with the median filter
    """
    img = img.filter(ImageFilter.MedianFilter)
    return img


def gauss_filter(img):
    """
    applies the gauss filter from the PIL package to the image
    : param img: image to be processed
    : return: image processed with the gauss filter
    """
    img = img.filter(ImageFilter.GaussianBlur)
    return img


def sharpen(img):
    """
    applies the sharpen filter from the PIL package to the image
    : param img: image to be processed
    : return: image processed with the sharpen filter
    """
    img = img.filter(ImageFilter.SHARPEN)
    return img


def remove_bright_spots(img, t_bright, t_background):
    """
    sets all pixels with intensity value above threshold to selected intensity
    : param img: image with bright spots to be removed
    : param t_bright: threshold 
    : param t_background: value to which intensity values above threshold are set
    : return: image without bright spots
    """
    img = img.copy()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            if img.getpixel((x,y)) > t_bright:
                img.putpixel((x,y), t_background)
    return img

def morphological_operation(img, kernel, operation:str):
    """
    applies the morphological operations Erosion, Dilation, Closing, Opening using different kernel sizes
    : param img: image for the morphological operation
    : kernel: kernelsize for morphological operation
    : operation: which operation should be applied (Erosion, Dilation, Closing, Opening)
    : return: image after the respective morphological operation
    """
    kernelsize = np.ones((kernel,kernel), np.uint8)
    if operation == "erosion" or operation == "erode":
        morphimage = cv2.erode(img, kernelsize, iterations=1)
    elif operation == "dilation" or operation == "dilate":
        morphimage = cv2.dilate(img, kernelsize, iterations=1)
    elif operation == "closing" or operation == "close":
        morphimage = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernelsize)
    elif operation == "opening" or operation == "open":
        morphimage = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernelsize)
    else:
        print("this morphological operation is not supported")
    return morphimage
    
        