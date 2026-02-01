import matplotlib.pyplot as plt
import random
random.seed(0)  # same random numbers each run

# Generate 1000 random values from a Gaussian distribution
data = [random.gauss(mu=0, sigma=1) for _ in range(1000)] 

# Create histogram
plt.hist(data, bins=30, color='blue', edgecolor='black', alpha=0.7)

# Annotate the graph
plt.xlabel("Value")
plt.ylabel("Counts")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Histogram of random Gaussian data")

# Show the histogram
plt.show()
