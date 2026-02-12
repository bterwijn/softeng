import grades3  # imports all code in 'grade3.py'

def main(filename: str):
    try:
        grades3.print_passing_students(filename)
    except grades3.GradeError as e:
        print("Caught GradeError:", e)  # handle GradeError
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)  # handle FileNotFoundError

main('grades_good.csv')
main('grades_bad.csv')
main('non_existent_file.csv')
