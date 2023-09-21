def gauss_method(matrix):
    n = len(matrix)

    def print_matrix(mat):
        for row in mat:
            print([round(x, 1) for x in row])
        print()

    print("\nMatriz original:")
    print_matrix(matrix)
    
    for i in range(n):
        # Encontrar a linha com o maior elemento na coluna atual (pivot)
        max_row = i
        for k in range(i+1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Trocar a linha atual pela linha com o pivot
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        print(f"Passo {i+1}:")
        print_matrix(matrix)

        # Fazer a matriz superior triangular
        for k in range(i+1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n+1):
                matrix[k][j] -= factor * matrix[i][j]

    # Resolver a matriz triangular superior
    solution = [0] * n
    for i in range(n-1, -1, -1):
        solution[i] = round(matrix[i][n] / matrix[i][i], 1) 
        for k in range(i-1, -1, -1):
            matrix[k][n] -= matrix[k][i] * solution[i]

    return solution

def main():

    def print_solution(solution):
        for i, x in enumerate(solution):
            print(f"x{i+1} = {x}")
        print('--------------------------------')

    matrix_a = [
        [3, 2, 4, 1],
        [1, 1, 2, 2],
        [4, 3, -2, 3]
    ]

    matrix_b = [
        [3, 2, 0, 1, 3],
        [9, 8, -3, 4, 6],
        [-6, 4, -8, 0, -16],
        [3, -8, 3, -4, 18]
    ]

    solution_a = gauss_method(matrix_a)
    print("\nSolução do sistema de equações da questão a:")
    print_solution(solution_a)

    solution_b = gauss_method(matrix_b)
    print("\nSolução do sistema de equações da questão b:")
    print_solution(solution_b)

if __name__ == "__main__":
    main()