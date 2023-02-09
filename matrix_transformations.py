from print_matrix import print_matrix

def rotate_matrix(matrix):
    m = []
    for j in range(0, len(matrix[0])):
        row = []
        for i in range(0, len(matrix)):
            row.append(matrix[i][j])
        m.append(row)
    return m

t = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

if __name__ == "__main__":
    print('Initial:')
    print_matrix(t)
    m = rotate_matrix(t)
    print('Rotated:')
    print_matrix(m)