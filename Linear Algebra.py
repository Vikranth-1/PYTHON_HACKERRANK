import numpy as np

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        row = list(map(float, input().split()))
        matrix.append(row)
    
    arr = np.array(matrix)
    determinant = np.linalg.det(arr)
    
    print(round(determinant, 2))
