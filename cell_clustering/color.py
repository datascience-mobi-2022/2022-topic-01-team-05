from PIL import Image

from HSV_conversion import HSVColor
from LAB_conversion import LABColor
from YCbCr_conversion import YCbCrColor

def convert(img: Image.Image, color_space):
    """
    converts RGB image in other color space
    : param img: image in RGB format
    : param color_space: color space (HSV, LAB, YCbCr)
    : return: image in other color space
    """
    if color_space == "HSV":
        colorspaceimage = HSVColor(img)
        return colorspaceimage
    elif color_space == "LAB":
        colorspaceimage = LABColor(img)
        return colorspaceimage
    elif color_space == "YCbCr":
        colorspaceimage = YCbCrColor(img)
        return colorspaceimage
    else:
        print("invalid color_space, color_space has to be: HSV, LAB or YCbCr")
        exit()
    