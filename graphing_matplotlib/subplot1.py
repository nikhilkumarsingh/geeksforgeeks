# importing required modules
import matplotlib.pyplot as plt
import numpy as np
 
# function to generate coordinates
def create_plot(ptype):
    # setting the x-axis vaues
    x = np.arange(-10, 10, 0.01)
 
    # setting the y-axis values
    if ptype == 'linear':
        y = x
    elif ptype == 'quadratic':
        y = x**2
    elif ptype == 'cubic':
        y = x**3
    elif ptype == 'quartic':
        y = x**4
 
    return(x, y)
 
# setting a style to use
plt.style.use('fivethirtyeight')
 
# create a figure
fig = plt.figure()
 
# define subplots and their positions in figure
plt1 = fig.add_subplot(221)
plt2 = fig.add_subplot(222)
plt3 = fig.add_subplot(223)
plt4 = fig.add_subplot(224)
 
# plotting points on each subplot
x, y = create_plot('linear')
plt1.plot(x, y, color ='r')
plt1.set_title('$y_1 = x$')
 
x, y = create_plot('quadratic')
plt2.plot(x, y, color ='b')
plt2.set_title('$y_2 = x^2$')
 
x, y = create_plot('cubic')
plt3.plot(x, y, color ='g')
plt3.set_title('$y_3 = x^3$')
 
x, y = create_plot('quartic')
plt4.plot(x, y, color ='k')
plt4.set_title('$y_4 = x^4$')
 
# adjusting space between subplots
fig.subplots_adjust(hspace=.5,wspace=0.5)
 
# function to show the plot
plt.show()
