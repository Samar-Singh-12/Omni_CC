from pyinputplus import inputInt, inputNum


# This takes input of a Matrix (row < column < create)
def matrix_takein(name):
    print()
    row = inputInt(f"Enter the no. of rows in Matrix {name}: ")
    column = inputInt(f"Enter the no. of columns in Matrix {name}: ")
    print()
    return matrix_create(row, column, name)


# This creates the Matrix with user input from rows & columns provided
def matrix_create(row, column, name):
    matrix = []
    for i in range(row):
        row = []
        for j in range(column):
            element = inputNum(f"Enter the element on Matrix {name} [{i}][{j}]: ")
            row.append(element)
        matrix.append(row)
    matrix_print(matrix, name)
    return matrix


# Prints a Matrix in a Classic fashion
def matrix_print(mx, name):
    print(f"\n{name} = ")
    for i in mx:
        print(i)


# Runs Summation and Subtraction Operations on 2 Matrices
def matrix_combo(mx, my, sign):
    if len(mx) == len(my) and len(mx[0]) == len(my[0]):
        result_mx = []
        for i in range(len(mx)):
            result_row = []
            for j in range(len(mx[0])):
                element = eval(f"{mx[i][j]} {sign} {my[i][j]}")
                result_row.append(element)
            result_mx.append(result_row)
        return matrix_print(result_mx, "Result")
    else:
        print("\nProvided matrices are of unequal sizes!")


# Runs Multiplication operation on 2 Matrices
def matrix_mul(mx, my):
    if len(mx[0]) == len(my):
        result_mx = []
        for i in range(len(mx)):
            result_row = []
            for j in range(len(my[0])):
                element = 0
                for k in range(len(my)):  # or len(mx[0])
                    element += mx[i][k] * my[k][j]
                result_row.append(element)
            result_mx.append(result_row)
        return matrix_print(result_mx, "Result")
    else:
        print("\nProvided matrices are invalid for multiplication!")
