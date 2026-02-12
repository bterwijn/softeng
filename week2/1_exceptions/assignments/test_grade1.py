import subprocess

def test_grade1():    
    result = subprocess.run(
        ['python', 'grades1.py', 'grades_bad.csv'],
        capture_output=True, text=True
    )
    assert result.stdout == """grades: {'Alice': [7.5, 8.3, 6.2], 'Bob': [0.0, 6.2, 5.1], 'Carol': [6.2, 3.2], 'Dave': [9.0, 5.1, 0.0], 'Eve': [0.0, 0.0]}
averages: {'Alice': 7.333333333333333, 'Bob': 3.766666666666667, 'Carol': 4.7, 'Dave': 4.7, 'Eve': 0.0}
passing students: ['Alice']
"""
    assert result.stderr == ""

