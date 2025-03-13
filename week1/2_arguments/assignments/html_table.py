import sys

def main():
    filename = "index.html"
    rows = 4
    columns = 4
    with open(filename, 'w') as file:
        write_html_table(file, rows, columns)

def write_html_table(file, rows=3, columns=3):
    file.write('<!DOCTYPE html>\n<html>\n')
    file.write('<head>\n')
    file.write('  <title>Writing a table</title>')
    file.write('</head>\n')
    file.write('<body>\n')
    write_table(file, rows, columns)
    file.write('</body>\n')
    file.write('</html>\n')

def write_table(file, rows=2, columns=2):
    file.write('  <table BORDER=1>\n')
    write_row(file, rows, columns)
    file.write('  </table>\n')
    
def write_row(file, rows, columns):
    for row in range(rows):
        file.write('    <tr>')
        write_column(file, row, columns)
        file.write(' </tr>\n')
    
def write_column(file, row, columns):
    for col in range(columns):
        file.write(' <td>')
        write_value(file, row, col)
        file.write('</td>')

def write_value(file, row, col):
    file.write(f'{row},{col}')

if __name__ == '__main__':
    main()
