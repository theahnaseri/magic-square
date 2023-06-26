def DoublyEvenOrderMagicSquare(n):
    magicSquare = [[0 for i in range(n)] for i in range(n)]

    # Fill matrix with its count value starting from 1
    for i in range(n):
        for j in range(n):
            magicSquare[i][j] = (n*i) + j + 1

    # Change values of sub-matrix with this formula: (n*n+1)-arr[i][j]
    # Top left submatrix of size n/4:
    for i in range(n//4):
        for j in range(n//4):
            magicSquare[i][j] = (n*n + 1) - magicSquare[i][j] 

    # Top right submatrix of size n/4:
    for i in range(n//4):
        for j in range(3*(n//4), n):
            magicSquare[i][j] = (n*n + 1) - magicSquare[i][j] 

    # Bottom left submatrix of size n/4:
    for i in range(3*(n//4), n):
        for j in range(n//4):
            magicSquare[i][j] = (n*n+1) - magicSquare[i][j] 

    # Bottom right submatrix of size n/4:
    for i in range(3*(n//4), n):
        for j in range(3*(n//4), n):
            magicSquare[i][j] = (n*n + 1) - magicSquare[i][j] 

    # Centre submatrix of size n/2:
    for i in range(n//4, 3*(n//4)):
        for j in range(n//4, 3*(n//4)):
            magicSquare[i][j] = (n*n + 1) - magicSquare[i][j]

    return magicSquare