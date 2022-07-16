import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import skimage.io as sk
import showing_images as si


def barplot_preprocessing():
    """
    creates barplot for the dice scores of the evaluation of the preprocessing
    :return: barplot for the preprocessing
    """
    columns_names = ["Dice Score", "Image", "Preprocessing"]
    dice_score = [0.9641489822003173, 0.8761583692361492, 0.564795796835042, 0.8529418809417935, 0.9571953667328995, 0.8725476469061945, 
                        0.9643350560302921, 0.8762229777707888]
    image = ["Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", 
            "Cell Nuclei", "Yeast Cells"]
    preprocessing = ["unprocessed", "unprocessed", "edge \n enhancement", "edge \n enhancement", "sharpened", "sharpened", "gauss", "gauss"]

    df = pd.DataFrame(list(zip(dice_score, image, preprocessing)), columns=columns_names)

    sns.set(rc={'figure.figsize':(8,5)})
    ax = sns.barplot(x="Preprocessing", y="Dice Score", hue="Image", data=df, palette="crest")
    ax.set(ylim=(0.5, 1))
    plt.legend(loc=3)
    sns.set_style("whitegrid")


def barplot_colorspaces():
    """
    creates barplot for the dice scores of the evaluation of the color spaces
    :return: barplot for the color spaces
    """
    columns_names = ["Dice Score", "Image", "Color Space"]
    dice_score = [0.9641489822003173,  0.8761583692361492, 0.9588612366894456, 0.8773105429325107, 0.9579905602822929, 0.8791933180388641, 
                    0.9617610364345074, 0.88452213907461]
    image = ["Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells"]
    color_space = ["RGB", "RGB", "HSV", "HSV", "LAB", "LAB", "YCbCr", "YCbCr"]

    df = pd.DataFrame(list(zip(dice_score, image, color_space)), columns=columns_names)

    sns.set(rc={'figure.figsize':(8,5)})
    ax = sns.barplot(x="Color Space", y="Dice Score", hue="Image", data=df, palette="BuPu")
    ax.set(ylim=(0.85, 1))
    plt.legend(loc=2)
    sns.set_style("whitegrid")


def barplot_distances():
    """
    creates barplot for the dice scores of the evaluation of the distances
    :return: barplot for the distances
    """
    columns_names = ["Dice Score", "Image", "Distance"]
    dice_score = [0.9641489822003173, 0.8761583692361492, 0.9614845685332177, 0.8754433791833042, 0.9600499048134323, 0.8693622648430035, 
                    0.961095941927927, 0.42419474697607357]
    image = ["Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells"]
    distance = ["euclidean", "euclidean", "manhattan", "manhattan", "chebyshnev", "chebyshnev", "correlation", "correlation"]

    df = pd.DataFrame(list(zip(dice_score, image, distance)), columns=columns_names)

    sns.set(rc={'figure.figsize':(8,5)})
    ax = sns.barplot(x="Distance", y="Dice Score", hue="Image", data=df, palette="Blues")
    ax.set(ylim=(0.4, 1))
    plt.legend(loc=3)
    sns.set_style("whitegrid")


def boxplot_grayscale():
    """
    creates boxplot for the dice scores of the evaluation of the grayscale images
    :return: boxplot for the grayscale images
    """
    columns_names = ["Dice Score", "Processing"]
    dice_score = [0.8591865820137369, 0.8951960140384398, 0.963624931, 0.8943783223933183, 
        0.8249042268937321, 0.8853711103603341, 0.949321147, 0.8845252721173281,
        0.6692195541815243, 0.8298069079796091, 0.82483608, 0.8248360803970239, 
        0.6629263625393607, 0.7362834954173372, 0.819934981, 0.7345417270163801, 
        0.7066297568297076, 0.0, 0.826052827, 0.7528567225654604, 
        0.6232039268183847, 0.6179766684846855, 0.773680974, 0.6728102311790894, 
        0.5673446553998522, 0.6506771626062763, 0.698917006, 0.6466958730507323, 
        0.6263373547142262, 0.7259260821045561, 0.775670859, 0.7237186625334818, 
        0.058725940882704095, 0.034365388558540086, 0.159728823, 0.042206968158744806, 
        0.4998366617440206, 0.48240431831614805, 0.615012821, 0.5337521703977627, 
        0.5516201483019763, 0.4966125126983036, 0.640668543, 0.5254384953113458, 
        0.5763833425076765, 0.6826525572468858, 0.680536638, 0.680536637820677, 
        0.01833398407659531, 0.0002718976261583058, 0.509841856, 0.22747750979238704, 
        0.5793350015619921, 0.5715168386746333, 0.648845820, 0.5890371564211359, 
        0.5992197929523185, 0.6157011421812936, 0.636089187, 0.6286483663940449, 
        0.42391824765096653, 0.15235479902078922, 0.634055470, 0.3372506432592164, 
        0.39687846178192754,0.17686364989004957, 0.602168344, 0.2531918087587553, 
        0.727061476860484, 0.7980940984936302, 0.796548556, 0.7965485556767932]
    #image = ["Grayscale", "BBBC", "Grayscale", "BBBC", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells"]
    processing = ["edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",
                "edge \n enhancement", "median", "morphological \n operations", "unprocessed",]

    df = pd.DataFrame(list(zip(dice_score, processing)), columns=columns_names)

    sns.set(rc={'figure.figsize':(8,5)})
    ax = sns.boxplot(x="Processing", y="Dice Score", data=df, palette="Blues")
    ax.set(ylim=(0, 1))
    sns.set_style("whitegrid")


def boxplot_BBBC():
    """
    creates boxplot for the dice scores of the evaluation of the BBBC images
    :return: boxplot for the BBBC images
    """
    columns_names = ["Dice Score", "Preprocessing"]
    dice_score = [0.8397413793103449, 0.9036682356760266, 0.9071955869230145, 0.455779321666227, 0.6717349370248497, 0.7638603696098563,
        0.8233959818535321, 0.8725162381336715, 0.8668165432768712, 0.40318951255654956, 0.5943830539124673, 0.5405277498924422,
        0.8231074676572306, 0.861378221557009, 0.8506781699780165, 0.29928427925665496, 0.6348732483073531, 0.5731761111879226,
        0.7774528439830385, 0.84143196120912, 0.84104225546288, 0.37528140477262495, 0.6659733777038269, 0.6755525986762867, 0.8610157238387854,
        0.9117138908085695, 0.91343747303012, 0.2234532797333072, 0.8067883156867163, 0.8053243758146997, 0.7823571259188997, 0.8607370659107016,
        0.8459982923650744, 0.32151575031965596, 0.6594121159843408, 0.5838765297110896, 0.736675235646958, 0.8748854961832061, 0.860445337869182,
        0.4468373050897323, 0.5890124324159208, 0.5922759860726993, 0.7156836096765425, 0.8729573949729633, 0.8629332054203142, 0.21874618707142682,
        0.2780529999213651, 0.0642480817509989, 0.662413263167699, 0.7866224665351853, 0.7761624210570932, 0.36586450346495464, 0.5108368006483303,
        0.4774722887427122, 0.6543430729477241, 0.8397771207641573, 0.8313370393718837, 0.2845774766926288, 0.29910783353101955, 0.3602058319039451,
        0.807252254979115, 0.8915513903308173, 0.8779239973851007, 0.4745580540234762, 0.5705496661959599, 0.5224809175996602, 0.4242264416315049,
        0.7043165467625899, 0.6672093539554503, 0.24991991701877755, 0.2512131848008546, 0.25575875604783493]
    #image = ["Grayscale", "BBBC", "Grayscale", "BBBC", "Cell Nuclei", "Yeast Cells", "Cell Nuclei", "Yeast Cells"]
    preprocessing = ["edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",
                "edge \n enhancement", "median", "unprocessed","edge \n enhancement", "median", "unprocessed",]

    df = pd.DataFrame(list(zip(dice_score, preprocessing)), columns=columns_names)

    sns.set(rc={'figure.figsize':(8,5)})
    ax = sns.boxplot(x="Preprocessing", y="Dice Score", data=df, palette="Blues")
    ax.set(ylim=(0, 1))
    sns.set_style("whitegrid")


def barplot_reflections():
    """
    creates barplot for the dice scores of the evaluation of the removal of reflections
    :return: barplot for the reflections
    """
    columns_names = ["Dice Score", "Reflection", "Image"]
    dice_score = [0.042206968, 0.6319353468258981, 0.22747751, 0.4190362620485571, 0.337250643, 0.6322432856550206, 
                    0.253191809, 0.7658440389259635]
    reflection = ["Unprocessed", "Reflections removed", "Unprocessed", "Reflections removed", "Unprocessed", "Reflections removed", 
            "Unprocessed", "Reflections removed"]
    image = ["image 32", "image 32", "image 42", "image 42", "image 46", "image 46", "image 47", "image 47"]

    df = pd.DataFrame(list(zip(dice_score, reflection, image)), columns=columns_names)

    sns.set(rc={'figure.figsize':(8,5)})
    ax = sns.barplot(x="Image", y="Dice Score", hue="Reflection", data=df, palette="Blues")
    ax.set(ylim=(0, 0.8))
    plt.legend(loc=2)
    sns.set_style("whitegrid")


def load_data():
    """
    loads the raw data
    : return: graph with four images, one of each data set
    """
    CN = sk.imread("../data/Cell_Nuclei.jpg")
    YC = sk.imread("../data/Yeast_Cells.jpg")
    GS = sk.imread("../data/NIH3T3/img/dna-0.png")
    BBBC = sk.imread("../data/human_ht29_colon_cancer_2_images/img0.tif")
    si.show_four_images_title(CN, YC, GS, BBBC, "Raw Data", "Cell Nuclei", "Yeast Cells", "NIH3T3 data set", "BBBC data set")


def position_images():
    """
    loads two example images of clustering with position
    : return: graph with two images of the position clustering
    """
    pos = sk.imread("../cell_clustering/Position_Clustering/CN_position.png")
    pos_weighted = sk.imread("../cell_clustering/Position_Clustering/CN_position_weighted_10_percent.png")
    si.show_two_images_title(pos, pos_weighted, "Clustering of Cell Nuclei with position as additional feature", 
                    "Position weighted 100%", "Position weighted 10%")


def load_reflections():
    img32 = sk.imread("../data/NIH3T3/img/dna-32.png")
    img32_clustered = sk.imread("../cell_clustering/Grayscale_Output/img08_none.png")
    img32_removed = sk.imread("../data/grayscale32_removed_bright_spots.jpg")
    img32_removed_clustered = sk.imread("../cell_clustering/Reflections_Clustering/img32_reflections_removed.png")
    si.show_four_images_two_rows_title(img32, img32_clustered, img32_removed, img32_removed_clustered, 
            "Clustering of Image 32 with and without reflections", "Image 32", "Clustering of Image 32", "Image 32 without bright spots",
            "Clustering of Image 32 without bright spots")


def load_colorspaces():
    CN_RGB = sk.imread("../data/Cell_Nuclei.jpg")
    CN_HSV = sk.imread("../cell_clustering/Color_spaces_images/CN_HSV.jpg")
    CN_LAB = sk.imread("../cell_clustering/Color_spaces_images/CN_LAB.jpg")
    CN_YCbCr = sk.imread("../cell_clustering/Color_spaces_images/CN_YCbCr.jpg")
    YC_RGB = sk.imread("../data/Yeast_Cells.jpg")
    YC_HSV = sk.imread("../cell_clustering/Color_spaces_images/YC_HSV.jpg")
    YC_LAB = sk.imread("../cell_clustering/Color_spaces_images/YC_LAB.jpg")
    YC_YCbCr = sk.imread("../cell_clustering/Color_spaces_images/YC_YCbCr.jpg")
    si.show_eight_images_two_rows_title(CN_RGB, CN_HSV, CN_LAB, CN_YCbCr, YC_RGB, YC_HSV, YC_LAB, YC_YCbCr, "Color space conversions", 
    "Cell Nuclei RGB", "Cell Nuclei HSV", "Cell Nuclei LAB", "Cell Nuclei YCbCr", "Yeast Cells RGB", "Yeast Cells HSV",
    "Yeast Cells LAB", "Yeast Cells YCbCr")


def load_best_combinations():
    YC = sk.imread("../data/Yeast_Cells.jpg")
    YC_combi = sk.imread("../cell_clustering/Coloured_Clustering/Yeast_Cells/YC_nofilter_YCbCr_manhattan.jpg")
    CN = sk.imread("../data/Cell_Nuclei.jpg")
    CN_combi = sk.imread("../cell_clustering/Coloured_Clustering/Cell_Nuclei/CN_gaussfilter_RGB_euclidean.jpg")
    si.show_four_images_two_rows_title(YC, CN, YC_combi, CN_combi, "Best Clustering Results", "Yeast Cells", "Cell Nuclei", "Best Clustering of Yeast Cells", "Best Clustering of Cell Nuclei")