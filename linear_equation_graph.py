'''
Plots linear equation graph.
Linear equation in the form of y = mx + c, where m is the slope of the graph.
User inputs value of m and c and the program automatically computes values of y given the range of x from -10 to 9
'''

import matplotlib.pyplot as plt
from pylab import axis,savefig,plot

# Draw the graph
def draw_graph(x, y):
    plt.plot(x, y, marker = "o")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.title("Graph of Linear Equation y=3x + 2")
    plot(x,y)
    savefig('linear_equation.jpg')

    
#Linear Equation
def linear_eq():
    x = [] #This list will append all values of x 
    y = [] #This list will append all values of y
    #Generate values for x
    i = range(-10, 10)
    for val in i:
        value_of_y = 3*val + 2  # calculate values of y with different values of x from ragne -10 to 9
        x.append(val)  # values of x
        y.append(value_of_y)  # values of y
        
    # Call the draw_graph function
    draw_graph(x, y)
    
if __name__ == '__main__':
    linear_eq()   
