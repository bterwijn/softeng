from rich.console import Console
from rich.table import Table
import platform
import sys
import os

console = Console()
table = Table(title="System & Python Environment Info")

table.add_column("Property", style="cyan", justify="right")
table.add_column("Value", style="magenta")

# System Info
table.add_row("Python Version", platform.python_version())
table.add_row("Python Implementation", platform.python_implementation())
table.add_row("OS", f"{platform.system()} {platform.release()} ({platform.version()})")
table.add_row("Architecture", platform.architecture()[0])
table.add_row("Processor", platform.processor())
table.add_row("Machine", platform.machine())
table.add_row("Platform", sys.platform)

# Python Environment Info
table.add_row("Python Executable", sys.executable)
table.add_row("Virtual Environment", os.getenv("VIRTUAL_ENV", "None"))

console.print(table)
