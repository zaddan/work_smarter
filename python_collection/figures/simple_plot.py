import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset

#init figs
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)

# axis labels
ax1.set_xlabel('x_axis',fontsize=16)
ax1.set_ylabel('y_axis',fontsize=16)

# legend
ax1.legend(['$V_{max}$ [m/s]','$a_{max}$ [m/s$^2$]'],fontsize=16, ncol=3,loc='upper center',bbox_to_anchor=(0.5,1.18))

# axis limits
#ax1.set_ylim(0,14)
#ax1.set_xlim(0,14)

# ticks and grids
#ax1.grid(which='major',linewidth='0.3')
#plt.xticks(x_pos,bars,weight='bold')

# assign values
x_values = [1,2,3]
y_values  = [11, 12 ,13]

# plot
ax1.plot(x_values, y_values,marker='o')


#plt.show()

# save file
output_file = "simple.png"
plt.savefig(output_file)
#fig2 = plt.figure(2)
#ax2 = fig2.add_subplot(211)
#plt.gcf().subplots_adjust(top=0.85,left=0.15,right=0.95)
#ax2.tick_params(axis='x',bottom=False,top=False,labelbottom=False)
#ax2.grid(which='major',linewidth='0.3')
#ax2.set_ylabel('Mission Time \n [s]',fontsize=16)
#ax3 = fig2.add_subplot(212)
#ax3.grid(which='major',linewidth='0.3')
#ax3.set_ylabel('Mission Energy \n [kJ]',fontsize=16)
#plt.xticks(x_pos,bars,weight='bold')
#fig2.subplots_adjust(hspace=0.0001)
#plot
#plt.rc('xtick',labelsize=16)


