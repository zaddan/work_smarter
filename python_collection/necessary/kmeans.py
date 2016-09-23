import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sklearn.cluster import KMeans
#----instantiate a KMeans obj
n_clusters = 2 #--seting the num of clusters
myKMeans = KMeans(k=n_clusters, init='k-means++', n_init=4, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)

#---generate random 1 dimnestional array
data_1_dim = []
for x in range(0, 20):
    data_1_dim.append([random.randint(0, 100)])
data_1_dim_as_array = np.asarray(data_1_dim) #data_1_dim needs to be a a list of arrays
print "input data_1_dim is:" 
print data_1_dim_as_array

#--- find clusters
data_1_dim_fitted = myKMeans.fit(data_1_dim_as_array)
print "labels are " + str(data_1_dim_fitted.labels_)
print "clusters_ceners are" + str(data_1_dim_fitted.cluster_centers_)



#----generate random 2 dimensional array
data_2_dim = []
for x in range(0, 20):
    data_2_dim.append([random.randint(0, 100), random.randint(0,100)])
data_2_dim_as_array = np.asarray(data_2_dim) #data_2_dim needs to be a a list of arrays
print "input data_2_dim is:" 
print data_2_dim_as_array

#--- find clusters
data_2_dim_fitted = myKMeans.fit(data_2_dim_as_array)
print "labels are " + str(data_2_dim_fitted.labels_)
print "clusters_ceners are" + str(data_2_dim_fitted.cluster_centers_)





