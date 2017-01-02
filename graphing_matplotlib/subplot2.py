# importing required modules
import matplotlib.pyplot as plt
import numpy as np
 
# function to generate coordinates
def create_plot(ptype):
    # setting the x-axis vaues
    x = np.arange(0, 5, 0.01)
 
    # setting y-axis values
    if ptype == 'sin':
        # a sine wave
        y = np.sin(2*np.pi*x)
    elif ptype == 'exp':
        # negative exponential function
        y = np.exp(-x)
    elif ptype == 'hybrid':
        # a damped sine wave
        y = (np.sin(2*np.pi*x))*(np.exp(-x))
 
    return(x, y)
 
# setting a style to use
plt.style.use('ggplot')
 
# defining subplots and their positions
plt1 = plt.subplot2grid((11,1), (0,0), rowspan = 3, colspan = 1)
plt2 = plt.subplot2grid((11,1), (4,0), rowspan = 3, colspan = 1)
plt3 = plt.subplot2grid((11,1), (8,0), rowspan = 3, colspan = 1)
 
# plotting points on each subplot
x, y = create_plot('sin')
plt1.plot(x, y, label = 'sine wave', color ='b')
x, y = create_plot('exp')
plt2.plot(x, y, label = 'negative exponential', color = 'r')
x, y = create_plot('hybrid')
plt3.plot(x, y, label = 'damped sine wave', color = 'g')
 
# show legends of each subplot
plt1.legend()
plt2.legend()
plt3.legend()
 
# function to show plot
plt.show()
