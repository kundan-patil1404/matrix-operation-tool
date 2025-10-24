import numpy as np

def get_matrix_input(prompt):
    """
    Prompts the user to input a matrix and validates the input.
    
    The user is expected to input rows separated by semicolons (;) 
    and elements separated by commas (,) or spaces.
    Example: "1,2,3; 4,5,6; 7,8,9"
    """
    while True:
        try:
            # 1. Get raw input
            matrix_str = input(f"\n{prompt} (e.g., '1 2; 3 4'): ").strip()
            if not matrix_str:
                raise ValueError("Input cannot be empty.")
            
            # 2. Parse rows and elements
            rows = []
            row_strs = matrix_str.split(';')
            
            # 3. Process each row
            for i, row_str in enumerate(row_strs):
                # Use split() without arguments to handle comma or space separators cleanly
                elements = [float(e.strip()) for e in row_str.replace(',', ' ').split() if e.strip()]
                if not elements:
                     raise ValueError(f"Row {i+1} is empty or invalid.")
                rows.append(elements)
            
            # 4. Convert to NumPy array
            matrix = np.array(rows)
            
            # 5. Validate rectangular shape (all rows must have the same number of columns)
            cols = len(matrix[0])
            for row in matrix:
                if len(row) != cols:
                    raise ValueError("All rows must have the same number of columns (rectangular matrix required).")
            
            print(f"\nInput Matrix successfully parsed. Shape: {matrix.shape}")
            return matrix
            
        except ValueError as e:
            print(f"Input Error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred during input parsing: {e}. Please check your format.")


def display_matrix(title, matrix):
    """
    Displays the matrix result in a clean, structured format.
    """
    print(f"\n{'=' * 50}")
    print(f"RESULT: {title}")
    print(f"Shape: {matrix.shape}")
    
    # Use NumPy's built-in printing for structured output
    print("-" * 50)
    print(matrix)
    print("=" * 50)


def perform_operation(choice):
    """
    Handles user input and executes the selected matrix operation using NumPy.
    """
    if choice in ['1', '2', '3']:
        # Operations requiring two matrices
        
        # Matrix A input
        A = get_matrix_input("Enter Matrix A")
        display_matrix("Matrix A", A)
        
        # Matrix B input
        B = get_matrix_input("Enter Matrix B")
        display_matrix("Matrix B", B)

        try:
            if choice == '1':
                # Addition
                result = A + B
                display_matrix("Matrix Addition (A + B)", result)
                
            elif choice == '2':
                # Subtraction
                result = A - B
                display_matrix("Matrix Subtraction (A - B)", result)
                
            elif choice == '3':
                # Multiplication (Matrix Dot Product)
                # Note: np.dot or @ operator is used for matrix multiplication
                if A.shape[1] != B.shape[0]:
                    print("\n!!! ERROR: Matrix dimensions are incompatible for multiplication.")
                    print(f"Rule: Columns of A ({A.shape[1]}) must equal Rows of B ({B.shape[0]}).")
                    return
                
                result = np.dot(A, B)
                display_matrix("Matrix Multiplication (A @ B)", result)

        except ValueError as e:
             print(f"\n!!! ERROR: Matrices must have the same shape for addition/subtraction. {e}")
             
    elif choice in ['4', '5']:
        # Operations requiring one matrix
        
        # Matrix input
        A = get_matrix_input("Enter the Matrix")
        display_matrix("Input Matrix", A)

        if choice == '4':
            # Transpose
            result = A.T # NumPy's simple transpose operation
            display_matrix("Matrix Transpose (A.T)", result)
            
        elif choice == '5':
            # Determinant
            if A.ndim != 2 or A.shape[0] != A.shape[1]:
                print("\n!!! ERROR: Determinant requires a square (2D) matrix.")
                return

            # Use numpy.linalg for determinant calculation
            determinant = np.linalg.det(A) 
            
            print("\n" + "=" * 50)
            print("RESULT: Determinant")
            print("-" * 50)
            print(f"Determinant of the matrix is: {determinant:.4f}")
            print("=" * 50)


def main():
    """
    Main function to display the interactive menu and run the tool.
    """
    print("\n" + "#" * 50)
    print("      NUMPY MATRIX OPERATIONS TOOL")
    print("#" * 50)
    
    while True:
        print("\nSelect an operation to perform:")
        print(" [1] Matrix Addition (A + B)")
        print(" [2] Matrix Subtraction (A - B)")
        print(" [3] Matrix Multiplication (A @ B)")
        print(" [4] Matrix Transpose (A.T)")
        print(" [5] Matrix Determinant (det(A))")
        print(" [0] Exit")
        
        choice = input("Enter your choice (0-5): ").strip()
        
        if choice == '0':
            print("\nThank you for using the Matrix Operations Tool. Goodbye!")
            break
        elif choice in ['1', '2', '3', '4', '5']:
            perform_operation(choice)
        else:
            print("\nInvalid choice. Please enter a number from 0 to 5.")

# Execute the main function when the script is run
if __name__ == "__main__":
    # Ensure NumPy is available
    try:
        main()
    except ImportError:
        print("\n!!! ERROR: NumPy library not found.")
        print("Please install it using: pip install numpy")
    except Exception as e:
        print(f"\nAn unexpected fatal error occurred: {e}")

