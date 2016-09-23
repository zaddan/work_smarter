import matplotlib.pyplot as plt

def rev(x):
    return 1/float(x)
def main():
	x_axis = range(1, 100, 1)
	y_axis = map(rev, x_axis)
	
	
	#y_axis = 1/x_axis
	#print y_axis
	##
	#
	lines, = plt.plot(x_axis, y_axis, '--', label ='lines', linewidth = 4.0, color = 'black')
	#plt.setp(lines, color='r', linewidth=2.0)
	#
	plt.ylabel('Energy', fontsize = 30)
	plt.xlabel('Noise', fontsize = 30)
	#
	plt.show()

main()
