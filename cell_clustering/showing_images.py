import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt


def show_two_images_title(img1, img2, f_title, img1_title, img2_title):
    plt.figure(figsize=(10, 4))
    plt.suptitle(f_title, fontsize=20, y=1.1)

    s1 = plt.subplot(1, 2, 1)
    s1.grid(False)
    s1.set_title(img1_title, fontsize=14)
    plt.imshow(img1, "gray")

    s2 = plt.subplot(1, 2, 2)
    s2.grid(False)
    s2.set_title(img2_title, fontsize=14)
    plt.imshow(img2, "gray")


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


def show_four_images_two_rows_title(img1, img2, img3, img4, f_title, img1_title, img2_title, img3_title, img4_title):
    plt.figure(figsize=(15, 7))
    plt.suptitle(f_title, fontsize=20, y=1)

    s1 = plt.subplot(2, 2, 1)
    s1.grid(False)
    s1.set_title(img1_title, fontsize=14)
    plt.imshow(img1, "gray")

    s2 = plt.subplot(2, 2, 2)
    s2.grid(False)
    s2.set_title(img2_title, fontsize=14)
    plt.imshow(img2, "gray")

    s3 = plt.subplot(2, 2, 3)
    s3.grid(False)
    s3.set_title(img3_title, fontsize=14)
    plt.imshow(img3, "gray")

    s4 = plt.subplot(2, 2, 4)
    s4.grid(False)
    s4.set_title(img4_title, fontsize=14)
    plt.imshow(img4, "gray")

    plt.subplots_adjust(wspace=0.1, hspace=0.5)