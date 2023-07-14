from fractions import Fraction

def greatest_common_divisor(x, y):
    # Recursive function to calculate the greatest common divisor
    def greatest_common_divisor_recursive(x, y):
        if y == 0:
            return x
        return greatest_common_divisor_recursive(y, x % y)
    
    return greatest_common_divisor_recursive(abs(x), abs(y))

def simplify_fraction(x, y):
    # Simplify a fraction by dividing both numerator and denominator by their greatest_common_divisor
    gcd = greatest_common_divisor(x, y)
    return Fraction(int(x / gcd), int(y / gcd))

def least_common_multiple(x, y):
    # Calculate the least common multiple
    return int(x * y / greatest_common_divisor(x, y))

def transform_matrix(mat):
    # Perform matrix transformation to bring rows with all zeros to the bottom
    row_sums = list(map(sum, mat))  # Calculate the sum of each row
    zero_indices = list(map(lambda x: x == 0, row_sums))  # Identify rows with sum equal to zero
    indices = set([i for i, x in enumerate(zero_indices) if x])  # Store the indices of zero-sum rows
    new_mat = []
    for i in range(len(mat)):
        if row_sums[i] == 0:
            # For zero-sum rows, replace each element with Fraction(0, 1)
            new_mat.append(list(map(lambda x: Fraction(0, 1), mat[i])))
        else:
            # For non-zero-sum rows, simplify each element with respect to the row sum
            new_mat.append(list(map(lambda x: simplify_fraction(x, row_sums[i]), mat[i])))
    transformed_mat = []
    zeros_mat = []
    for i in range(len(new_mat)):
        if i not in indices:
            # Add non-zero-sum rows to the transformed matrix
            transformed_mat.append(new_mat[i])
        else:
            # Add zero-sum rows to a separate list
            zeros_mat.append(new_mat[i])
    transformed_mat.extend(zeros_mat)  # Append zero-sum rows to the bottom of the transformed matrix
    t_mat = []
    for i in range(len(transformed_mat)):
        t_mat.append([])
        extend_mat = []
        for j in range(len(transformed_mat)):
            if j not in indices:
                # Copy non-zero-sum elements to the new matrix
                t_mat[i].append(transformed_mat[i][j])
            else:
                # Store zero-sum elements to be appended later
                extend_mat.append(transformed_mat[i][j])
        t_mat[i].extend(extend_mat)  # Append zero-sum elements to the right of the new matrix
    return [t_mat, len(zeros_mat)]

def copy_matrix(mat):
    # Create a deep copy of a matrix
    copied_mat = []
    for i in range(len(mat)):
        copied_mat.append([])
        for j in range(len(mat[i])):
            copied_mat[i].append(Fraction(mat[i][j].numerator, mat[i][j].denominator))
    return copied_mat

def gaussian_elimination(m, values):
    # Perform Gaussian elimination on a matrix to solve a system of linear equations
    mat = copy_matrix(m)
    for i in range(len(mat)):
        index = -1
        for j in range(i, len(mat)):
            if mat[j][i].numerator != 0:
                index = j
                break
        if index == -1:
            raise ValueError('Gaussian elimination failed!')
        mat[i], mat[index] = mat[index], mat[i]
        values[i], values[index] = values[index], values[i]
        for j in range(i + 1, len(mat)):
            if mat[j][i].numerator == 0:
                continue
            ratio = -mat[j][i] / mat[i][i]
            for k in range(i, len(mat)):
                mat[j][k] += ratio * mat[i][k]
            values[j] += ratio * values[i]
    res = [0] * len(mat)
    for i in range(len(mat)):
        index = len(mat) - 1 - i
        end = len(mat) - 1
        while end > index:
            values[index] -= mat[index][end] * res[end]
            end -= 1
        res[index] = values[index] / mat[index][index]
    return res

def transpose_matrix(mat):
    # Transpose a matrix
    t_mat = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == 0:
                t_mat.append([])
            t_mat[j].append(mat[i][j])
    return t_mat

def inverse_matrix(mat):
    # Calculate the inverse of a matrix
    t_mat = transpose_matrix(mat)
    mat_inv = []
    for i in range(len(t_mat)):
        values = [Fraction(int(i == j), 1) for j in range(len(mat))]
        mat_inv.append(gaussian_elimination(t_mat, values))
    return mat_inv

def multiply_matrices(mat1, mat2):
    # Multiply two matrices
    res = []
    for i in range(len(mat1)):
        res.append([])
        for j in range(len(mat2[0])):
            res[i].append(Fraction(0, 1))
            for k in range(len(mat1[0])):
                res[i][j] += mat1[i][k] * mat2[k][j]
    return res

def split_QR(mat, length_R):
    # Split a transformed matrix into Q and R matrices
    length_Q = len(mat) - length_R
    Q = []
    R = []
    for i in range(length_Q):
        Q.append([int(i == j) - mat[i][j] for j in range(length_Q)])
        R.append(mat[i][length_Q:])
    return [Q, R]

def solution(m):
    transformed_mat = transform_matrix(m)
    if transformed_mat[1] == len(m):
        return [1, 1]
    Q, R = split_QR(*transformed_mat)
    inv = inverse_matrix(Q)
    res = multiply_matrices(inv, R)
    row = res[0]
    l = 1
    for item in row:
        l = least_common_multiple(l, item.denominator)
    res = list(map(lambda x: int(x.numerator * l / x.denominator), row))
    res.append(l)
    return res