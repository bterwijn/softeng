import subprocess

def test_grade2():
    result = subprocess.run(
        ['python', 'grades2.py', 'grades_bad.csv'],
        capture_output=True, text=True
    )
    assert result.stdout == """grades: {'Alice': [7.5, 8.3, 6.2], 'Bob': [6.2, 5.1], 'Carol': [6.2, 3.2], 'Dave': [9.0, 5.1], 'Eve': []}
averages: {'Alice': 7.333333333333333, 'Bob': 5.65, 'Carol': 4.7, 'Dave': 7.05}
passing students: ['Alice', 'Bob', 'Dave']
"""
    assert result.stderr == ""

