# simulate_repl.py
import code
import sys

def simulate_repl(filename):
    with open(filename, 'r') as file:
        code_lines = file.readlines()

    # Create an interactive console
    console = code.InteractiveConsole()

    # Simulate the REPL
    for line in code_lines:
        print(f">>> {line.strip()}")  # Print the input line with >>>
        console.push(line.strip())    # Execute the line

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simulate_repl.py <filename>")
    else:
        simulate_repl(sys.argv[1])
