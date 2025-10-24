NumPy Matrix Operations Tool

Project Overview

This project is the implementation of the "Matrix Operations Tool" task, designed to demonstrate proficiency in using the Python language and the NumPy library for fundamental linear algebra and scientific computing.

The tool features an interactive, menu-driven command-line interface that allows users to input matrices and perform common operations while ensuring mathematical rules (like dimension matching) are strictly enforced.

Key Features

The application supports the following five matrix operations:

Addition ($A + B$)

Subtraction ($A - B$)

Multiplication ($A \cdot B$) - Performs the matrix dot product.

Transpose ($A^T$)

Determinant ($\det(A)$)

Technologies Used

Python 3.x: Core application language.

NumPy: Essential library used for efficient matrix creation, manipulation, and all mathematical operations (addition, subtraction, multiplication, transpose, and determinant calculation).

How to Run the Tool

1. Prerequisites

You must have Python installed. Install the required external library, NumPy, using pip:

pip install numpy


2. Execution

Save the provided code as matrix_tool.py and run it from your terminal:

python matrix_tool.py


3. Usage and Input Format

The program will present a menu and prompt you for input.

Input Type

Separator

Example Input

Elements

Spaces or Commas

1 2 3 or 1,2,3

Rows

Semicolon (;)

1 2; 3 4

Example of a 2x2 Matrix Input:

Enter Matrix A (e.g., '1 2; 3 4'): 10 20; 30 40


Robustness and Error Handling

The tool incorporates critical validation steps to ensure reliability:

Input Validation: Checks that all input values are numeric and handles empty inputs gracefully.

Shape Validation: Ensures the input forms a valid, rectangular matrix (all rows have the same number of columns).

Dimensionality Checks:

Addition/Subtraction: Verifies that both matrices $A$ and $B$ have identical shapes.

Multiplication: Verifies that the number of columns in $A$ equals the number of rows in $B$ ($A_{(m \times n)} \cdot B_{(n \times p)}$).

Determinant: Confirms the matrix is square.
