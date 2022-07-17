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

    if image.mode == "L": 

        print("Grayscale Image Clustering")

        def calculate_distance(a,b):
            """
            calculates the distance between 2 values 
            : param a,b: 2 input values (integers)
            : return: distance value (integer)
            """
            distance = abs(a-b)
            return distance


        def initiate_centroids(K,image):
            """
            initiates centroids based on the values of an image
            : param K: number of centroids to be initiated
            : param image: image, based upon which the centroids will be initiated
            : returm: list of centroids
            """
            imagePixels = list(image.getdata())
            initial_centers = list()
            for x in range(K):  
                centroid = imagePixels[random.randint(0,len(imagePixels)-1)]
                while centroid in initial_centers:  
                    centroid = imagePixels[random.randint(0,len(imagePixels)-1)]
                initial_centers.append(centroid)
            return initial_centers


        def responsibility(centroids, image): 
            """
            calculates a matrix of responsibilities for pixels and centroids
            : param centroids: centroids used for responsibility calculation
            : param image: image for which responsibilities should be calculated
            : return: responsibility of each centroid for each pixel
            """
            imagePixels = list(image.getdata())
            x = len(imagePixels)
            k = len(centroids)
            matrix = np.zeros((x,k)) 
            for p in range(x): 
                distance = []
                for c in centroids: 
                    distance.append(calculate_distance(imagePixels[p], c)) 
                matrix[p,np.argmin(distance)] = 1  
            return matrix
        

        def findClosestCentroids(centroids, image):
            """
            creates a list of centroids to which each pixel is assigned
            : param centroids: list of centroids to which pixels should be assigned
            : param image: image whose pixels should be assigned
            : return: list of assigned pixels
            """
            imagePixels = list(image.getdata()) 
            assigned_centroid = []
            for p in imagePixels:  
                distance = []
                for c in centroids:  
                    distance.append(calculate_distance(c, p)) 
                assigned_centroid.append(np.argmin(distance)) 
            return assigned_centroid


        def clustermeans(responsibility, image):
            """
            calculates new centroid
            : param responsibilities of each centroid for each pixel:
            : param image: image for which pixels were assigned
            : return: list of new centroids
            """
            Pixelarray = np.array(list(image.getdata()))  
            clusters = len(responsibility[1])
            new_centroids = []  
            for k in range(clusters):  
                new_centroids.append(sum(responsibility[:,k] * Pixelarray)/sum(responsibility[:,k]))  
            return new_centroids


        def k_means(image, K, iterations):
            """
            Clusters an image
            : param image: image to be clustered
            : param K: number of clusters
            : param iterations: maximum iterations
            : return: clustered image
            """
            centroids = initiate_centroids(K, image)  
            new_centroids = []  
            i = 0
            while i < iterations:  
                resmat = responsibility(centroids,image)  
                new_centroids = clustermeans(resmat, image)  
                if new_centroids == centroids:  
                    break        
                centroids = new_centroids  
                i += 1   
            final_assignment = findClosestCentroids(centroids, image) 

            rgb_array = np.array([255]*len(final_assignment))  
            rgb_array = rgb_array*final_assignment/max(final_assignment) 
            image_out = Image.new("L",image.size)  
            image_out.putdata(rgb_array)  
            
            return image_out
    

    else:


        if distance_type == "euclidean":

            def calculate_distance(a,b):
                """
                calculates the distance between 2 data points 
                : param a,b: 2 data points 
                : return: distance between data points
                """
                a = np.array(a)
                b = np.array(b)
                distance_vector = a - b
                distance = np.sqrt(sum(distance_vector**2))
                return distance


        elif distance_type == "manhattan":

            def calculate_distance(a,b):
                """
                calculates the distance between 2 data points 
                : param a,b: 2 data points 
                : return: distance between data points
                """
                a = np.array(a)
                b = np.array(b)
                distance_vector = a - b
                distance = sum(abs(distance_vector))
                return distance


        elif distance_type == "chebyshnev":

            def calculate_distance(a,b):
                """
                calculates the distance between 2 data points 
                : param a,b: 2 data points 
                : return: distance between data points
                """
                a = np.array(a)
                b = np.array(b)
                distance = max(abs(a-b))
                return distance
        

        elif distance_type == "correlation":

            def calculate_distance(a,b):
                """
                calculates the distance between 2 data points 
                : param a,b: 2 data points 
                : return: distance between data points
                """
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
            """
            initiates centroids based on the values of an image
            : param K: number of centroids to be initiated
            : param image: image, based upon which the centroids will be initiated
            : returm: list of centroids
            """
            imagePixels = list(image.getdata())
            initial_centers = list()
            for x in range(K):
                centroid = imagePixels[random.randint(0,len(imagePixels)-1)]
                while centroid in initial_centers:
                    centroid = imagePixels[random.randint(0,len(imagePixels)-1)]   
                initial_centers.append(centroid)
            return initial_centers


        def findClosestCentroids(centroids, image):
            """
            creates a list of centroids to which each pixel is assigned
            : param centroids: list of centroids to which pixels should be assigned
            : param image: image whose pixels should be assigned
            : return: list of assigned pixels
            """
            imagePixels = list(image.getdata())
            assigned_centroid = []
            for p in imagePixels:
                distance = []
                for c in centroids:
                    distance.append(calculate_distance(c, p))
                assigned_centroid.append(np.argmin(distance))
            return assigned_centroid


        def responsibility(centroids, image):
            """
            calculates a matrix of responsibilities for pixels and centroids
            : param centroids: centroids used for responsibility calculation
            : param image: image for which responsibilities should be calculated
            : return: responsibility of each centroid for each pixel
            """
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
            """
            calculates new centroid
            : param responsibilities of each centroid for each pixel:
            : param image: image for which pixels were assigned
            : return: list of new centroids
            """
            Pixelarray = np.array(list(image.getdata()))
            clusters = len(responsibility[1])
            new_centroids = []
            for k in range(clusters):
                new_centroids.append(list(sum(responsibility[:,k] * Pixelarray)/sum(responsibility[:,k,0])))
            return new_centroids


        def k_means(image, K, iterations):
            """
            Clusters an image
            : param image: image to be clustered
            : param K: number of clusters
            : param iterations: maximum iterations
            : return: clustered image
            """
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

