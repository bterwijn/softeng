import csv
import sys

def print_passing_students(filename):
    grades = read_grades(filename)
    print('grades:', grades)
    averages = compute_average(grades)
    print('averages:', averages)
    students = get_passing_students(averages, 5.5)
    print('passing students:', students)

def get_grades(grades: list[str]) -> list[float]:
    """ Convert list of grade strings to list of floats """
    grade_floats = []
    for grade in grades:
        grade_float = float(grade)
        grade_floats.append(grade_float)
    return grade_floats

def strip_list(strings: list[str]) -> list[str]:
    """ Strip each string in 'strings' list """
    return [s.strip() for s in strings]

def read_grades(filename: str) -> dict[str, list[float]]:
    """ Read grades from a CSV file and return a dictionary 
    mapping student names to their grades. 
    """
    grades = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        header = strip_list(next(csvreader))
        for row in csvreader:
            row = strip_list(row)
            grades[row[0]] = get_grades(row[1:])
    return grades

def compute_average(grades: dict[str, list[float]]) -> dict[str, float]:
    """ Compute average grades for each student. """
    averages = {}
    for name, scores in grades.items():
        averages[name] = sum(scores) / len(scores)
    return averages

def get_passing_students(averages: dict[str, float], passing_grade: float = 5.5) -> list[str]:
    """ Get a list of students with passing average grade. """
    return [name for name, avg in averages.items() if avg >= passing_grade]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <grades_file>')
        sys.exit(1)
    filename = sys.argv[1]
    print_passing_students(filename)
