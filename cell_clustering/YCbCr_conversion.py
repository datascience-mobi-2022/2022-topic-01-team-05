from PIL import Image
def rgb_to_ycbcr(r, g, b):
    """
    converts RGB values to YCbCr values
    : param r: R value
    : param g: G value
    : param b: B value
    : return: YCbCr values in 255 format (8 bit)
    """
    y = .299*r + .587*g + .114*b
    cb = 128 -.168736*r -.331364*g + .5*b
    cr = 128 +.5*r - .418688*g - .081312*b
    return y, cb, cr

def YCbCrColor(img):
    """
    converts RGB image (must be Image class) in YCbCr image
    : param img: image in RGB format
    : return: image in YCbCr format (Image class)
    
    """
    if isinstance(img, Image.Image):
        r,g,b = img.split()
        Ydat = []
        Cbdat = []
        Crdat = []
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            Y,Cb,Cr = rgb_to_ycbcr(rd, gn, bl)
            Ydat.append(int(Y))
            Cbdat.append(int(Cb))
            Crdat.append(int(Cr))
        r.putdata(Ydat)
        g.putdata(Cbdat)
        b.putdata(Crdat)
        return Image.merge("YCbCr", (r,g,b))
    else:
        return None
    
