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
    s1.grid(False)
    s1.set_title(img1_title, fontsize=14)
    plt.imshow(img1)

    s2 = plt.subplot(1, 4, 2)
    s2.grid(False)
    s2.set_title(img2_title, fontsize=14)
    plt.imshow(img2)

    s3 = plt.subplot(1, 4, 3)
    s3.grid(False)
    s3.set_title(img3_title, fontsize=14)
    plt.imshow(img3, "gray")

    s4 = plt.subplot(1, 4, 4)
    s4.grid(False)
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


def show_eight_images_two_rows_title(img1, img2, img3, img4, img5, img6,img7, img8, f_title, img1_title, img2_title, img3_title, img4_title, img5_title, img6_title, img7_title, img8_title):
    plt.figure(figsize=(15, 7))
    plt.suptitle(f_title, fontsize=20, y=1)

    s1 = plt.subplot(2, 4, 1)
    s1.grid(False)
    s1.set_title(img1_title, fontsize=14)
    plt.imshow(img1, "gray")

    s2 = plt.subplot(2, 4, 2)
    s2.grid(False)
    s2.set_title(img2_title, fontsize=14)
    plt.imshow(img2)

    s3 = plt.subplot(2, 4, 3)
    s3.grid(False)
    s3.set_title(img3_title, fontsize=14)
    plt.imshow(img3)

    s4 = plt.subplot(2, 4, 4)
    s4.grid(False)
    s4.set_title(img4_title, fontsize=14)
    plt.imshow(img4)

    s5 = plt.subplot(2, 4, 5)
    s5.grid(False)
    s5.set_title(img5_title, fontsize=14)
    plt.imshow(img5)

    s6 = plt.subplot(2, 4, 6)
    s6.grid(False)
    s6.set_title(img6_title, fontsize=14)
    plt.imshow(img6)

    s7 = plt.subplot(2, 4, 7)
    s7.grid(False)
    s7.set_title(img7_title, fontsize=14)
    plt.imshow(img7)

    s8 = plt.subplot(2, 4, 8)
    s8.grid(False)
    s8.set_title(img8_title, fontsize=14)
    plt.imshow(img8)

    plt.subplots_adjust(wspace=0.1, hspace=0.5)


def show_one_image_title(img1, f_title):
    plt.figure(figsize=(15, 11))
    plt.suptitle(f_title, fontsize=26, y = 0.95 )

    s1 = plt.subplot(1, 1, 1)
    plt.axis('off')
    s1.grid(False)
    plt.imshow(img1)


def show_one_image_title2(img1, f_title):
    plt.figure(figsize=(13, 8))
    plt.suptitle(f_title, fontsize=26, y = 0.95 )

    s1 = plt.subplot(1, 1, 1)
    plt.axis('off')
    s1.grid(False)
    plt.imshow(img1)