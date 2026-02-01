import matplotlib.pyplot as plt
import random
random.seed(0)  # same random numbers each run

# Generate random data points
x_values = [random.uniform(-5, 5) for _ in range(50)]  # 50 random x values
y_values = [random.uniform(-5, 5) for _ in range(50)]  # 50 random y values

# Create scatter plot
plt.scatter(x_values, y_values, label="Random point")

# Annotate the graph
plt.xlabel("x") # x-axis name
plt.ylabel("y") # y-axis name
plt.axhline(0)  # x-axis horizontal line
plt.axvline(0)  # y-axis vertical line
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.title("Random Scatter Plot")

# Show the scatter plot
plt.show()
