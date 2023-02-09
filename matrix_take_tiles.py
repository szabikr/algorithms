from print_matrix import print_matrix

def matrix_take_tiles(m):
    result = []
    for k in range(0, 9, 3):
        for l in range(0, 9, 3):
            row = []
            for i in range(k, k + 3):
                for j in range(l, l + 3):
                    row.append(m[i][j])
            result.append(row)
    return result

matrix = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

if __name__ == "__main__":
    print_matrix(matrix_take_tiles(matrix))
