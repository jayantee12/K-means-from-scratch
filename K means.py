import cv2
import numpy as np
import matplotlib.pyplot as plt
import copy

#Reading the image
frame=plt.imread("C:/Users/hp/Downloads/try.jpg")
rows,cols,channels=frame.shape
points=rows*cols

# K MEANS
def K_means(K,frame,u):
    
    r = np.zeros((points, K)) # One hote encoding for each point
    p = np.zeros(K) #number of points in the cluster
    
    # Initial vaules of means
    u_2=copy.deepcopy(u) 
    
    print("Initial value of u taken: \n", u)
    itr=0
    # Computing till convergence or for maximum 10 iterations
    for numitr in range(10):
        
        # EXPECTATION STEP: Minimise cost function wrt r_nk.
        # r_nk=1 for smallest distance between point n and centre k
        for k in range(rows):
            for i in range(cols):
                dist=[]
                a = frame[k][i] #Pixel being tested
                for j in range(K):
                    dist.append(np.sum((a - u[j]) ** 2)) 
        
                d_min=np.argmin(np.array(dist))
                r[i + cols * k][d_min] = 1
    
    
        # MAXIMISATION STEP: Minimise cost function wrt u.
        # updating u as mean of the new clusters formed in expectation step    
        for z in range(channels):
            for j in range(K):
                u[j][z]=0
                p[j]=0
                for k in range(rows):
                    for i in range(cols):
                        u[j][z] = u[j][z] + frame[k][i][z] * r[i + cols * k][j]
                        p[j] = p[j] + r[i + cols * k][j]
                if p[j] !=0:
                    u[j][z] = u[j][z] / p[j]
        
        
        # Checking if the means are converged below a threshold
        sum = 0
        for z in range(channels):
            for j in range(K):
                sum = sum + (u_2[j][z] - u[j][z]) ** 2 
        if sum < 5:
            print("\n For iteration",itr+1,"\n Updated means of clusters is=\n",u)
            print("Number of points in each cluster is=",p)
            print("Difference in means from last iteration is=",sum,"\n Means converged, breaking loop...")
            break
        u_2=copy.deepcopy(u) 
        itr += 1
        # print("\n For iteration",itr,"\n Updated means of clusters is= \n",u)
        # print("Number of points in each cluster is=",p)
        
    return u , r

