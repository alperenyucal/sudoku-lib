import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sudoku_lib",
    version="1.0.0",
    author="Alperen Yucal",
    author_email="author@example.com",
    description="Everything about sudoku.",
    keywords='sudoku sudokulib',
    license='MIT',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)