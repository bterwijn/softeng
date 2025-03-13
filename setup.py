from setuptools import setup

setup(
    name="softeng",
    version="0.0.1",
    packages=['softeng'],
    install_requires=[
        "pytest",
        "pytest-timeout",
    ],
    python_requires=">=3.8",  # Minimum Python version
)
