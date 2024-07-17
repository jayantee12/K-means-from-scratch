#MAIN

#K=2
u_2=np.array([[10, 10, 10],[190,190,190]])
u2,r2= K_means(2,frame,u_2)
#K=3
u_3=np.array([[10, 10, 10],[110, 110, 110], [255, 255, 255]])
u,r= K_means(3,frame,u_3)
#K=4
u_4=np.array([[10, 10, 10],[75,75,75],[110, 110, 110],[190,190,190]])
u4,r4= K_means(4,frame,u_4)

# Forming a new imageS to show the clustering result
k_out2=np.zeros(frame.shape,dtype=int)

#K=2   
for k in range(rows):
    for i in range(cols):
        for j in range(2):
            for z in range(channels):
                k_out2[k][i][z] += int(u2[j][z] * r2[i + cols * k][j])

#K=3
k_out3=np.zeros(frame.shape,dtype=int)
   
for k in range(rows):
    for i in range(cols):
        for j in range(3):
            for z in range(channels):
                k_out3[k][i][z] += int(u[j][z] * r[i + cols * k][j])

#K=4
k_out4=np.zeros(frame.shape,dtype=int)
   
for k in range(rows):
    for i in range(cols):
        for j in range(4):
            for z in range(channels):
                k_out4[k][i][z] += int(u4[j][z] * r4[i + cols * k][j])



#Displaying results
plt.figure()
fig, ax = plt.subplots(1,4,figsize=(20,15))
ax[0].imshow(frame)
ax[0].set_title("Original image")
ax[1].imshow(k_out2)
ax[1].set_title("K means, K=2")
ax[2].imshow(k_out3)
ax[2].set_title("K means, K=3")
ax[3].imshow(k_out4)
ax[3].set_title("K means, K=4")
fig.tight_layout()
plt.savefig('Kmeans.jpg')
plt.show()

        
