import matplotlib.pyplot as plt

def bankers_round(value):
    """Applies banker's rounding (round half to even)."""
    return round(value)

# Test values
values = [-1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
values = [ i/10 for i in range(-35, 60, 10)]
rounded_values = [bankers_round(v) for v in values]

# Create the plot
plt.figure(figsize=(8, 5))
plt.scatter(values, rounded_values, color='blue', s=100, label="Rounded Values")

# Draw lines connecting original values to rounded values
for i in range(len(values)):
    plt.plot([values[i], values[i]], [values[i], rounded_values[i]],
             'r')  # Dashed red line
    plt.text(values[i], rounded_values[i] + 0.2, str(rounded_values[i]),
             ha='center', fontsize=12, color='black')

# Annotate graph
plt.axhline(0, color='black', linewidth=0.5)  # x-axis
plt.axvline(0, color='black', linewidth=0.5)  # y-axis
plt.grid(True, linestyle='--', linewidth=0.5)
plt.title("Banker's Round (Round Half to Even)")
plt.xlabel("Original Value")
plt.ylabel("Rounded Value")
plt.xticks(values)  # Show exact test values on x-axis
plt.yticks(sorted(set(rounded_values)))  # Show only the rounded numbers
plt.legend()
plt.show()
