from __future__ import annotations

import copy

from typing import List


class Vector:
    """Assumed to be a column vector by default"""

    def __init__(self, data: List[int]):
        self.data = data

    def __repr__(self):
        return str(self)

    def __str__(self):
        data = ""
        for number in self.data:
            data += str(number) + " "
        data = data.rstrip()
        return f"Vector<{data}>"


class Matrix:

    def __init__(self, col_vectors: List[Vector], width: int, height: int):
        self.data: List[Vector] = col_vectors
        self.row_vectors: List[Vector] = []
        self.height = height
        self.width = width
        self.create_row_vectors()

    def __repr__(self):
        return str(self)

    def __str__(self):
        data = ""
        for v in self.data:
            data += str(v) + "\n"
        data = data.rstrip()
        return data

    def insert_vector(self, v: Vector, ndx: int = -1):
        """Inserts a vector into the matrix."""
        if ndx == -1:
            ndx = len(self.data)
        self.data.insert(ndx, v)

    def append_vector(self, v: Vector) -> Matrix:
        """Adds a new vector to the right of the matrix."""
        copy_matrix = copy.deepcopy(self)
        copy_matrix.insert_vector(v)
        # Maybe get the data and reconstruct the object
        return copy_matrix




def read_matrix(filename: str) -> List[List[int]]:
    """Reads a matrix from a text file."""
    data = open(filename, "r")
    dimension = data.readline()
    mrows, ncols = dimension.rstrip().split(",")
    content = data.readlines() # list of str to convert to float
    matrix = []
    for i, row in enumerate(content):
        matrix.append([])
        for number in row.split():
            number = float(number)
            matrix[i].append(number)

    return matrix, mrows, ncols


def get_column(matrix: List[List[int]], col_ndx: int) -> List[int]:
    """Returns a column from a matrix"""
    # matrix[changing][col]
    column = []
    for row in range(len(matrix)):
        column.append(matrix[row][col_ndx])
    return column



if __name__ == "__main__":
    data, height, width = read_matrix("../data/matrix.txt")
    height, width = int(height), int(width)
    all_columns = []

    # Get all column vectors
    for col in range(len(data[0])):
        column = get_column(data, col)
        col_vector = Vector(column)
        all_columns.append(col_vector)

    matrix = Matrix(all_columns, width, height) # loc argument

    # vector = Vector(
    #     list(map(float, input("Enter a vector: ").split()))
    # )
    vector = Vector([99, 99, 99, 99])

    new_matrix = matrix.append_vector(vector)

    print(new_matrix)