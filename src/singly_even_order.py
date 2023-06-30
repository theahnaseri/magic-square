from odd_order import OddOrderMagicSquare

def SinglyEvenOrderMagicSquare(n):
    magicSquare = [[0 for i in range(n)] for i in range(n)]
    
    mid = n // 2
    b = mid * mid
    c = 2 * b
    d = 3 * b
    odd_magicSquare = OddOrderMagicSquare(mid)

    for j in range(0, mid):
        for i in range(0, mid):
            a = odd_magicSquare[i][j]
            magicSquare[i][j] = a
            magicSquare[i + mid][j + mid] = a + b
            magicSquare[i + mid][j] = a + c
            magicSquare[i][j + mid] = a + d

    lc = mid // 2
    rc = lc
    for j in range(0, mid):
        for i in range(0, n):
            if i < lc or i > n - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = magicSquare[i][j]
                    magicSquare[i][j] = magicSquare[i][j + mid]
                    magicSquare[i][j + mid] = t

    return magicSquare