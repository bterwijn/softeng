import grades3

def test_grade3_OK():
    try:
        grades3.print_passing_students('grades_good.csv')
    except Exception as e:
        assert False, "Should not raise exception: "+ str(e)

def test_grade3_GradeError():
    try:
        grades3.print_passing_students('grades_bad.csv')
    except grades3.GradeError as e:
        assert "Error reading grade." in str(e)
    else:
        assert False, "GradeError Exception was not raised"

def test_grade3_File_Not_Found():
    try:
        grades3.print_passing_students('non_existent_file.csv')
    except FileNotFoundError as e:
        assert "No such file or directory" in str(e)
    else:
        assert False, "FileNotFoundError Exception was not raised"
