from PIL import Image
def rgb_to_hsv(r, g, b):
    """
    converts RGB values to HSV values
    : param r: R value
    : param g: G value
    : param b: B value
    : return: HSV values
    """
    maxc = max(r, g, b)
    minc = min(r, g, b)
    rangec = (maxc-minc)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = rangec / maxc
    rc = (maxc-r) / rangec
    gc = (maxc-g) / rangec
    bc = (maxc-b) / rangec
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v

def HSVColor(img):
    """
    converts RGB image to HSV color space
    : param img: image (Image class) in RGB format
    : return: image (Image class) in HSV format
    """
    if isinstance(img, Image.Image):
        r,g,b = img.split()
        Hdat = []
        Sdat = []
        Vdat = []
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            h,s,v = rgb_to_hsv(rd/255., gn/255., bl/255.)
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge("HSV", (r,g,b))
    else:
        return None

