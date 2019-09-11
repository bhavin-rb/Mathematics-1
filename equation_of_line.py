"""
Function for slope point form linear equation in the form of y = mx + c, given two points (x_1,y_1) and (x_2,y_2).
m is slope of the linear line and c is the y-intercept when x = 0.
For vertical linear lines, slope is undefined or has no slope.
For horizontal lines, slope is zero, hence equation becomes y = c.
"""


def linear_line_equation(a, b, c, d):
    # a = x_1, b = y_1, c = x_2, d = y_2
    if c - a != 0:  # checking if the linear line is not vertical
        m: float = (d - b) / (c - a)  # calculating the slope, m of the linear line
        constant_c = b  # constant,c is equal to any value of y_1 or y_2 (when x = 0)
    else:
        return print("The line has no Slope (The line is vertical)")

    print("The slope, m of the linear line is {0}".format(m))
    print("Equation of linear line is y = {0}x + {1}".format(m, constant_c))


a = input("Enter point x_1: ")
b = input("Enter point y_1: ")
c = input("Enter point x_2: ")
d = input("Enter point y_2: ")
linear_line_equation(float(a), float(b), float(c), float(d))

