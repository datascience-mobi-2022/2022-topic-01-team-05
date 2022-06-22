from PIL import Image
import numpy as np
def rgb_to_lab(r, g, b):
    """
    converts RGB values to LAB values
    : param r: R value
    : param g: G value
    : param b: B value
    : return: LAB values
    """
    RGB = [r,g,b]
    num = 0
    for value in RGB:
        value = float(value)/255
        if value > 0.04045:
            value = ((value + 0.055) / 1.055) ** 2.4
        else:
            value = value / 12.92
        
        RGB[num] = value *100
        num = num + 1
    
    XYZ = [0,0,0]

    X = RGB[0] * 0.4124 + RGB[1] * 0.3576 + RGB[2] * 0.1805
    Y = RGB[0] * 0.2126 + RGB[1] * 0.7152 + RGB[2] * 0.0722
    Z = RGB[0] * 0.0193 + RGB[1] * 0.1192 + RGB[2] * 0.9505

    XYZ[0] = round(X, 4)
    XYZ[1] = round(Y, 4)
    XYZ[2] = round(Z, 4)

    XYZ[0] = float(XYZ[0]) / 95.047         # ref_X =  95.047   Observer= 2°, Illuminant= D65
    XYZ[1] = float(XYZ[1]) / 100.0          # ref_Y = 100.000
    XYZ[2] = float(XYZ[2]) / 108.883        # ref_Z = 108.883

    num = 0
    for value in XYZ :

       if value > 0.008856 :
           value = value ** (1/3)
       else :
           value = ( 7.787 * value ) + ( 16 / 116 )

       XYZ[num] = value
       num = num + 1

  

    L = (116 * XYZ[1]) - 16
    A = 500 * (XYZ[0] - XYZ[1])
    B = 200 * (XYZ[1] - XYZ[2])

    return L, A, B

def LABColor(img):
    """
    converts RGB image (must be Image class) in LAB image
    : param img: image in RGB format
    : return: image in LAB format (Image class)
    
    """
    if isinstance(img, Image.Image):
        r,g,b = img.split()
        Ldat = []
        Adat = []
        Bdat = []
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            L,A,B = rgb_to_lab(rd, gn, bl)
            Ldat.append(L)
            Adat.append(A)
            Bdat.append(B)
        r.putdata(Ldat)
        g.putdata(Adat)
        b.putdata(Bdat)
        return Image.merge("LAB", (r,g,b))
    else:
        return None
