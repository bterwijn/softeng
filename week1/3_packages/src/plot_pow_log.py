import matplotlib.pyplot as plt
import numpy as np
import math

# Generate x and y values
domain = 10
all_x = np.linspace(-domain, domain, 400) # x values from -10 to 10 with 400 points
pow = [math.pow(2, x) for x in all_x]     # compute y value for each x value
pos_x = [x for x in all_x if x>0]     # only non-negative x
log = [math.log(x, 2) for x in pos_x] # compute y value for each x value

# Plot the functions
plt.plot(all_x, pow, label=r"$2^x$", color='blue')
plt.plot(pos_x, log, label=r"$\log_2(x)$", color='green')
plt.plot([-domain, domain], [-domain, domain], 'r--') # mirror line y=x

# Annotate the plot: add axes, grid, labels, legend, and title
plt.xlim(-domain, domain) # limit the x-axis
plt.ylim(-domain, domain) # limit the y-axis
plt.gca().set_aspect('equal', adjustable='box') # use equal x and y scale
plt.xlabel("x") # x-axis name
plt.ylabel("y") # y-axis name
plt.axhline(0)  # x-axis horizontal line
plt.axvline(0)  # y-axis vertical line
plt.grid(True, linestyle='--', linewidth=0.5) # show grid
plt.legend()                                  # add legend
plt.title("Machtsverheffen en inverse Logaritme functie") # add title

# Show the plot
plt.show()
