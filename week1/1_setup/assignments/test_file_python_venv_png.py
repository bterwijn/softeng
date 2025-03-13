from softeng import fixedhash, replace_fixedhash
import pytest

import os

def test_file_exists():
    assert os.path.exists("python_venv.png"), "Screenshot 'python_venv.png' not found in directory 'week1/1_setup/assignments'."
