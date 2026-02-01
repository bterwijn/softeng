import matplotlib.pyplot as plt
import math

def get_values(y_value):
    return [y_value, int(y_value), math.trunc(y_value), math.floor(y_value),
            math.ceil(y_value), round(y_value)]

# Prepare labels and values for plotting
methods = ["value", "int(value)", "trunc(value)", "floor(value)",
           "ceil(value)", "round(value)"]
all_values = [get_values(2.7), get_values(1.3), get_values(-1.3),
              get_values(-2.7)]
colors = ['blue', 'green', 'orange', 'red']

# Create the plot
plt.figure(figsize=(6, 4))
for i in range(len(all_values)):
    plt.scatter(methods, all_values[i], color=colors[i], zorder=3)
    x = list(range(len(all_values[i])))
    plt.plot(x, all_values[i], color=colors[i])
    
# Annotate each point with its value
for values in all_values:
    for i, (method, value) in enumerate(zip(methods, values)):
        plt.text(i, value + 0.1, str(value), ha='center', fontsize=10)

# Add grid, labels, and title
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")
plt.grid(True, linestyle='--', linewidth=0.5, zorder=0)
plt.title("Different Rounding Methods")
plt.ylabel("result")

# Show the plot
plt.show()
