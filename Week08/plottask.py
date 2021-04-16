# plottask.py
# This program reads displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0, 4] on the one set of axes.
# Author: Ciaran Moran

import matplotlib.pyplot as plt
import numpy as np
import os

x = np.arange(0,5,1)                              # x-axis values, range is 0 to 4 in steps of 1
                                                  # y-axis:                                              
y1  =  x                                          # f(x)=x 
y2  =  x**2                                       # g(x)=x^2
y3  =  x**3                                       # h(x)=x^3

# Variables for plot 

xy1_label = 'f(x)=x'
xy2_label = 'g(x)=x^2'
xy3_label = 'h(x)=x^3'

xy1_Colour = 'red'
xy2_Colour = 'green'
xy3_Colour = 'blue'

xAxisLabel = 'x - axis'
yAxisLabel = 'y - axis'
axisFontSize = 12 

xy_linetype =  'dashed'
plotAreaColour = "lightgrey"

#ax = plt.axes()


def customPlot():
   # declare plot series characteristics
   
    plt.plot(x, y1, color = xy1_Colour, linestyle = xy_linetype, label = xy1_label)
    plt.plot(x, y2, color = xy2_Colour, linestyle = xy_linetype, label = xy2_label)
    plt.plot(x, y3, color = xy3_Colour, linestyle = xy_linetype, label = xy3_label)

    ## declare axis labels
    plt.xlabel(xAxisLabel, fontsize = axisFontSize)
    plt.ylabel(yAxisLabel, fontsize = axisFontSize)

    # plot legend and grid 
    plt.legend(bbox_to_anchor=(0,1.02,1,0.2), loc="lower left",mode="expand", borderaxespad=0, ncol=3, fontsize = 14)
    plt.grid(True,which="both", linestyle='--')

    # set plot area colour
    ax = plt.axes()
    ax.set_facecolor(plotAreaColour)
    return plt


def writePlot(myPlot):
    #change current working directory
    os.chdir(os.path.dirname(__file__))
    plt.savefig('plottask.png')
    plt.show()
    


myPlot = customPlot()
writePlot(myPlot)

# References: 
# Stored on read me file