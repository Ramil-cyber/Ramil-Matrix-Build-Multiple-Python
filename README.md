[![CI Pipeline](https://github.com/nogibjj/Ramil-Matrix-Build-Multiple-Python/actions/workflows/main.yaml/badge.svg)](https://github.com/nogibjj/Ramil-Matrix-Build-Multiple-Python/actions/workflows/main.yaml)

# Testing Across Python Versions Using GitHub Actions

## Project Summary
This project leverages GitHub Actions to test compatibility across various Python versions. By utilizing the `setup-python` action and a matrix strategy, multiple jobs are executed under different configurations. The script `main.py` plays a key role in identifying the operating system and Python version for each job.

## Setup Guide
1. Clone the repository to your local machine.
2. Set up the container environment or run `make install` to install dependencies from `requirements.txt`.
3. Update or modify files like `main.py` or `test_main.py` as needed.
4. Push your changes, which will automatically trigger tests on different OS and Python configurations.

## Code Style and Error Checking
1. Ensure consistent code formatting by running `make format`.

Example of a formatting run:

![Code Formatting Example](https://github.com/nogibjj/Ramil-Matrix-Build-Multiple-Python/blob/e1c345e4f6fd6e5d2e39b74444fa2f9fdcfa7d57/data/format.png)

2. Detect potential issues by running `make lint`.

Example of linting results:

![Linting Example](https://github.com/nogibjj/Ramil-Matrix-Build-Multiple-Python/blob/e1c345e4f6fd6e5d2e39b74444fa2f9fdcfa7d57/data/lint.png)

3. Run the test suite using `make test`.

Example of test execution:

![Test Execution Example](https://github.com/nogibjj/Ramil-Matrix-Build-Multiple-Python/blob/e1c345e4f6fd6e5d2e39b74444fa2f9fdcfa7d57/data/test.png)

## Using a Matrix Strategy in GitHub Actions

![Matrix Build Example](https://github.com/nogibjj/Javidan_Karimli_IDS706_Week4/blob/1b144c960c6d8b927d08a821b0036da0f8071ea3/data/matrix_build.png)
