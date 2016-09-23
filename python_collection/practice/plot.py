import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from matplotlib import cm

def rev(x):
    return 1/float(x)
def main2d():
	x_axis = range(1, 100, 1)
	y_axis = map(rev, x_axis)
	
	
	#y_axis = 1/x_axis
	#print y_axis
	##
	#
	lines, = plt.plot(x_axis, y_axis, 'r--', label ='lines')
	#plt.setp(lines, color='r', linewidth=2.0)
	#
	plt.ylabel('Quality/Noise')
	plt.xlabel('Noise')
	#
	plt.show()


def main3d():
    X = np.array([[1,2],[1,2],[1,2]])
    Y = np.array([[10,20],[10,20],  [10,20]])
    Z = np.array([[1,1],[200,200], [400,300]])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection ='3d', )
    ax.scatter(X,Y,Z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()

#main2d()
main3d()
