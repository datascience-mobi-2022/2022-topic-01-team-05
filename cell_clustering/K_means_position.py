import numpy
import random
from PIL import Image


def normalize(data):
    """
    normalizes data to values between 0 and 1
    : param data: data set to be normalized
    : return: normalized data
    """
    xmin = min(min(data)) 
    xmax = max(max(data))
    for i in range(len(data)):
        sublist = data[i]
        sublist[0] = sublist[0]*0.1
        sublist[1] = sublist[1]*0.1
        for p in range(len(sublist)):
            data[i][p] = (sublist[p]-xmin) / (xmax-xmin)
    return data


def getPositions(img):
    """
    creates a list with each pixel's coordinates and intensity values
    : param img: image of which the pixel's coordinates and intensity values should be obtained
    : return: list with coordinates and respective intensity values for each pixel of the input image
    """
    width, height = img.size
    i = 0
    j = 0
    positions = []
    for j in range(width):
        for i in range(height):
            list_positions = []
            coordinate = i, j
            list_positions.append(i)
            list_positions.append(j)
            for p in range(len(img.getpixel(coordinate))):
                list_positions.append(img.getpixel(coordinate)[p])
            positions.append(list_positions)
    return positions


def calculate_distance(a,b):
    """"
    calculates the euclidean distance between two elements
    : param a: first element
    : param b: second element
    : return: float value for euclidean distance
    """
    a = numpy.array(a)
    b = numpy.array(b)
    distance_vector = a - b
    distance = numpy.sqrt(sum(distance_vector**2))
    return distance


def initiate_centroids(K,image):
    """"
    creates a list of random position and intensity values for a number of K centroids
    : param K: number of random centroids
    : param image: image in which the centroids are placed
    : return: list of random position and intensity values for K centroids
    """
    imagePixels = normalize(getPositions(image))
    initial_centers = list()
    for x in range(K):
        centroid = imagePixels[random.randint(0,len(imagePixels)-1)]
        while centroid in initial_centers:
            centroid = imagePixels[random.randint(0,len(imagePixels)-1)]   
        initial_centers.append(centroid)
    return initial_centers


def findClosestCentroids(centroids, image):
    """
    assigns each pixel to the closest centroid
    : param centroids: list of position and intensity values for centroids
    : param image: image to be clustered
    : return: list of indexes of the closest centroid for each pixel
    """
    imagePixels = normalize(getPositions(image))
    assigned_centroid = []
    for p in imagePixels:
        distance = []
        for c in centroids:
            distance.append(calculate_distance(c, p))
        assigned_centroid.append(numpy.argmin(distance))
    return assigned_centroid


def responsibility(centroids, image):
    imagePixels = normalize(getPositions(image))

    x = len(imagePixels)

    k = len(centroids)

    d = len(centroids[0])

    matrix = numpy.zeros((x,k,d))

    for p in range(x):

        distance = []

        for c in centroids:

            distance.append(calculate_distance(imagePixels[p], c))
        
        matrix[p,numpy.argmin(distance)] = [1]*d
    return matrix


def clustermeans(responsibility, image):

    Pixelarray = numpy.array(normalize(getPositions(image)))

    clusters = len(responsibility[1])
    
    new_centroids = []

    for k in range(clusters):
        new_centroids.append(list(sum(responsibility[:,k] * Pixelarray, axis = 0)/sum(responsibility[:,k,0])))
    return new_centroids


def k_means2(image, K, iterations):
    
    centroids = initiate_centroids(K, image)

    new_centroids = []
    
    i = 0

    while i < iterations:  # Maximum of 6 iterations

        resmat = responsibility(centroids,image) 

        new_centroids = clustermeans(resmat, image) # New Centroids

        if new_centroids == centroids:  # End algortihm, if centroids don't change
            break
        
        centroids = new_centroids

        i += 1
        
    final_assignment = findClosestCentroids(centroids, image)



    rgb_array = numpy.array([[255,255,255]]*len(final_assignment))
    for i in range(3):
        rgb_array[:,i] = rgb_array[:,i]*final_assignment/max(final_assignment)
    rgb_array
    rgb_list = []
    for i in range(len(rgb_array)):
        rgb_list.append(tuple(rgb_array[i]))
    image_out = Image.new("RGB",image.size)
    image_out.putdata(rgb_list)
    image_out

    return image_out  # Assignment list can be used to create picture