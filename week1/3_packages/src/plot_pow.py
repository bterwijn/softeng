import matplotlib.pyplot as plt
import numpy as np
import math

# Define the function
def f(all_x):
    return [math.pow(2,x) for x in all_x]

# Generate x and y values
x = np.linspace(-10, 10, 400)  # x values from -10 to 10 with 400 points
y = f(x)                       # compute y value for each x value

# Plot the function
plt.plot(x, y, label=r"$2^x$", color='blue')

# Annotate the plot: add axes, grid, labels, legend, and title
plt.xlabel("x") # x-axis name
plt.ylabel("y") # y-axis name
plt.axhline(0)  # x-axis horizontal line
plt.axvline(0)  # y-axis vertical line
plt.grid(True, linestyle='--', linewidth=0.5) # show grid
plt.legend()                                  # add legend
plt.title("Machtsverheffen")       # add title

# Show the plot
plt.show()
