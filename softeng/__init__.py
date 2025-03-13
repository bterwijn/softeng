# ------------- is_package_installed -------------
import importlib.util

def is_package_installed(package_name):
    return importlib.util.find_spec(package_name) is not None

def assert_pytest_timeout_installed():
    assert is_package_installed("pytest_timeout") == True, "package 'pytest_timeout' not installed, to install use: pip install pytest_timeout"

# ------------- hashing -------------
import hashlib

def fixedhash(value):
    m = hashlib.sha256()
    m.update(str(value).encode('utf-8'))
    return m.hexdigest()

def replace_fixedhash(value):
    return fixedhash(value)


# ------------- grades -------------
import subprocess
import sys

def run_tests():
    # Run pytest and capture the output
    result = subprocess.run([sys.executable, "-m", "pytest", "-v", "--tb=no"],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True
    )
    return result.stdout

def get_passed_failed_from_outout(test_output):
    # Parse the pytest test_output to get passed and failed tests
    passed_match = " passed"
    failed_match = " failed"
    lines = test_output.splitlines()
    summary_lines = [line for line in lines
                    if (line.startswith("====================") and
                        line.strip().endswith("====================") and
                        (passed_match in line or failed_match in line))]
    if len(summary_lines) == 0:
        print("***ERROR*** failed to parse 'passed' or 'failed' in test output:")
        print(test_output)
        exit(0)
    summary_line = summary_lines[-1]
    
    # Extract the number of passed and total tests
    passed = 0
    failed = 0
    if passed_match in summary_line:
        passed = int(summary_line.split(passed_match)[0].split()[-1])
    if failed_match in summary_line:
        failed = int(summary_line.split(failed_match)[0].split()[-1])
    return passed, failed

def compute_grade():
    # Run tests and get the test_output
    test_output = run_tests()
    print(test_output)
    passed, failed = get_passed_failed_from_outout(test_output)
    total = passed + failed
    grade = (passed / total) * 10 if total > 0 else 0
    print("passed: ", passed)
    print("failed: ", failed)
    print(f'Provisional Grade (subject to review): {grade} / 10')
    return grade
    
# ------------- latex test function -------------
def test():
    return 1234
