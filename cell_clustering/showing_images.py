import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt


def show_four_images_title(img1, img2, img3, img4, f_title, img1_title, img2_title, img3_title, img4_title):
    plt.figure(figsize=(15, 8))
    plt.suptitle(f_title, fontsize=20, y=0.75)

    s1 = plt.subplot(1, 4, 1)
    s1.set_title(img1_title, fontsize=14)
    plt.imshow(img1)

    s2 = plt.subplot(1, 4, 2)
    s2.set_title(img2_title, fontsize=14)
    plt.imshow(img2)

    s3 = plt.subplot(1, 4, 3)
    s3.set_title(img3_title, fontsize=14)
    plt.imshow(img3, "gray")

    s4 = plt.subplot(1, 4, 4)
    s4.set_title(img4_title, fontsize=14)
    plt.imshow(img4, "gray")