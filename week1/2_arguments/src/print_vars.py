import inspect

def print_vars(*var_names):
    """Prints local variable names with their value."""
    local_vars = inspect.currentframe().f_back.f_locals  # get all local variables
    for name in var_names:
        if name in local_vars:
            print(f"{name}: {local_vars[name]}")
        else:
            print(f"{name} is not defined")

# Example usage:
x = 42
y = [1, 2, 3]
name = "Alice"

print_vars("x", "y", "name", "z") # print the values of these variables
