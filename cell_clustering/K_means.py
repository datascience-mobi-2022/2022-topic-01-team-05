from PIL import Image
import numpy as np
import random

def K_Means(image: Image.Image, K: int, iterations: int, distance_type = "euclidian"):
    
    """
    segments an image into clusters based on pixel values
    : param image: input image that is to be segmented, either grayscale or coloured image
    : param K: number of clusters used
    : param iterations: maximum number of iterations, before the code will automatically end
    : param distance_type: allows a choice of different distance types(euclidian, manhattan, chebyshnev or correlation), default is set to euclidian
    : return: segmented image (PIL.Image.Image)
    """

    if image.mode == "L":  # If the image is grayscale, the k_means function needs to be defined slightly different

        print("Grayscale Image Clustering")

        def calculate_distance(a,b):  # Grayscale distance
            a = np.array(a)
            b = np.array(b)
            distance = abs(a-b)
            return distance

        def initiate_centroids(K,image):   # Initialises K centroids on an image
            imagePixels = list(image.getdata())
            initial_centers = list()
            for x in range(K):  # iterating over all centroids
                centroid = imagePixels[random.randint(0,len(imagePixels)-1)]
                while centroid in initial_centers:  # to avoid the same values being chosen for different centroids, check whther new centroid is already present in list
                    centroid = imagePixels[random.randint(0,len(imagePixels)-1)]   # if that is the case, reinitiate that centroid, until it is unique
                initial_centers.append(centroid)
            return initial_centers


        def responsibility(centroids, image):  # creates a matrix that shows, which clusters are responsible for which Pixels
            imagePixels = list(image.getdata())
            x = len(imagePixels)
            k = len(centroids)
            matrix = np.zeros((x,k))  # creating an empty array as a base to be filled up
            for p in range(x):  # iterating over every pixel
                distance = []
                for c in centroids:  # iterating over every centroid
                    distance.append(calculate_distance(imagePixels[p], c))  # create a list of all distances from pixel "p" to centroid "c"
                matrix[p,np.argmin(distance)] = 1  # set the responsibilitgy of the centroid closest to the pixel to 1, all others remain 0
            return matrix
        

        def findClosestCentroids(centroids, image):
            imagePixels = list(image.getdata()) 
            assigned_centroid = []
            for p in imagePixels:  # iterate over every pixel
                distance = []
                for c in centroids:  # iterate over every centroid
                    distance.append(calculate_distance(c, p))  # create a list of all distances from pixel "p" to centroid "c"
                assigned_centroid.append(np.argmin(distance))  # create a list showing which centroid each pixel is assigned to
            return assigned_centroid


        def clustermeans(responsibility, image):
            Pixelarray = np.array(list(image.getdata()))  
            clusters = len(responsibility[1])
            new_centroids = []  # create an empty list as basis
            for k in range(clusters):  # iterate over all centroids
                new_centroids.append(sum(responsibility[:,k] * Pixelarray)/sum(responsibility[:,k]))  # isolate all pixels, for which the centroid k is responsible, and calculate their mean as the new centroid
            return new_centroids


        def k_means(image, K, iterations):
            centroids = initiate_centroids(K, image)  # first set of centroids
            new_centroids = []  
            i = 0
            while i < iterations:  # as long as the code has run less iterations as desire, it will stay in the loop
                resmat = responsibility(centroids,image)  # calculate responsibilities
                new_centroids = clustermeans(resmat, image)  # calculate new centroids
                if new_centroids == centroids:  # if the centroids didn't change, the result is stable and no further iterations need to be run
                    break        
                centroids = new_centroids  
                i += 1   
            final_assignment = findClosestCentroids(centroids, image)  # create list of assignment of every pixel for image creation

            rgb_array = np.array([255]*len(final_assignment))  # create a list of entirely white pixels
            rgb_array = rgb_array*final_assignment/max(final_assignment)  # change white values into grayscale depending on which cluster the pixels were assigned to
            image_out = Image.new("L",image.size)  # create a new image
            image_out.putdata(rgb_array)  # put the pixel data into the image
            
            return image_out
    
    else:

        

        if distance_type == "euclidean":
            def calculate_distance(a,b):

                a = np.array(a)
                b = np.array(b)
                distance_vector = a - b
                distance = np.sqrt(sum(distance_vector**2))
                return distance


        elif distance_type == "manhattan":
            def calculate_distance(a,b):

                a = np.array(a)
                b = np.array(b)
                distance_vector = a - b
                distance = sum(abs(distance_vector))
                return distance


        elif distance_type == "chebyshnev":
            def calculate_distance(a,b):
                a = np.array(a)
                b = np.array(b)
                distance = max(abs(a-b))
                return distance
        
        elif distance_type == "correlation":
            def calculate_distance(a,b):

                a = np.array(a)
                b = np.array(b)
                s = np.corrcoef(a,b)[0, 1]
                distance = 0.5*(1-s)
                return distance


        else:
            print("invalid distance_type, distance_type has to be: manhattan, euclidean, chebyshnev or correlation")
            exit()

        print("Coloured Clustering")

        def initiate_centroids(K,image):
            imagePixels = list(image.getdata())
            initial_centers = list()
            for x in range(K):
                centroid = imagePixels[random.randint(0,len(imagePixels)-1)]
                while centroid in initial_centers:
                    centroid = imagePixels[random.randint(0,len(imagePixels)-1)]   
                initial_centers.append(centroid)
            return initial_centers


        def findClosestCentroids(centroids, image):
            imagePixels = list(image.getdata())
            assigned_centroid = []
            for p in imagePixels:
                distance = []
                for c in centroids:
                    distance.append(calculate_distance(c, p))
                assigned_centroid.append(np.argmin(distance))
            return assigned_centroid


        def responsibility(centroids, image):
            imagePixels = list(image.getdata())

            x = len(imagePixels)

            k = len(centroids)

            d = len(centroids[0])

            matrix = np.zeros((x,k,d))

            for p in range(x):

                distance = []

                for c in centroids:

                    distance.append(calculate_distance(imagePixels[p], c))
        
                matrix[p,np.argmin(distance)] = [1]*d
            return matrix


        def clustermeans(responsibility, image):

            Pixelarray = np.array(list(image.getdata()))

            clusters = len(responsibility[1])
    
            new_centroids = []

            for k in range(clusters):
                new_centroids.append(list(sum(responsibility[:,k] * Pixelarray)/sum(responsibility[:,k,0])))
            return new_centroids


        def k_means(image, K, iterations):
    
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



            rgb_array = np.array([[255,255,255]]*len(final_assignment))
            for i in range(3):
                rgb_array[:,i] = rgb_array[:,i]*final_assignment/max(final_assignment)
            rgb_array
            rgb_list = []
            for i in range(len(rgb_array)):
                rgb_list.append(tuple(rgb_array[i]))
            image_out = Image.new("RGB",image.size)
            image_out.putdata(rgb_list)
            

            return image_out  # Assignment list can be used to create image

    segmented_image = k_means(image, K, iterations)
    return segmented_image

