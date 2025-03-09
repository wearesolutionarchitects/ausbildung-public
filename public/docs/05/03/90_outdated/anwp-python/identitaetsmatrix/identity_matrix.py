def create_identity_matrix(size):
    return [[1 if row == col else 0 for col in range(size)] for row in range(size)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

size = 4
identity_matrix = create_identity_matrix(size)
print_matrix(identity_matrix)