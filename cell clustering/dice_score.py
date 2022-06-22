import numpy as np

 
def dice_foreground(gt, img):
    """
    calculates the dice score for the foreground of the picture, that is all white pixels (intensity value 255)
    : param gt: ground truth image
    : param img: output image of the k-means clustering algorithm
    : return: dice score (float between 0 and 1)
    """
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    h = gt.shape[0]
    w = gt.shape[1]
    for i, j in np.ndindex((h, w)):
        if gt[i, j][0] == 255:
            if img[i, j][0] == 255:
                tp += 1
            else:
                fn += 1
        else:
            if img[i, j][0] == 255:
                fp += 1
            else:
                tn += 1
    dsc = 2* tp / (2*tp + fn + fp)
    return print("Dice similarity score is {}".format(dsc))


def dice_background(gt, img):
    """
    calculates the dice score for the background of the picture, that is all black pixels (intensity value 0)
    : param gt: ground truth image
    : param img: output image of the k-means clustering algorithm
    : return: dice score (float between 0 and 1)
    """
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    h = gt.shape[0]
    w = gt.shape[1]
    for i, j in np.ndindex((h, w)):
        if gt[i, j][0] == 0:
            if img[i, j][0] == 0:
                tp += 1
            else:
                fn += 1
        else:
            if img[i, j][0] == 0:
                fp += 1
            else:
                tn += 1
    dsc = 2* tp / (2*tp + fn + fp)
    return print("Dice similarity score is {}".format(dsc))