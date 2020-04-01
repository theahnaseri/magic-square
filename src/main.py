from odd_order import fillOddOrder
from doubly_even_order import fillDoublyEvenOrder

def fillMatrix(n):
    # Edge cases:
    if n == 1:
        return [[1]]
    if n == 2:
        return None
    # Make a 2D array like a nxn square and set all number to 0 
    magicSquare = [[0 for i in range(n)] for i in range(n)]

    # Fill the magicSquare depends on its type:
    # Odd order:
    if n % 2 != 0:
        fillOddOrder(magicSquare, n)
    # Doubly-even order:
    elif n % 4 == 0:
        fillDoublyEvenOrder(magicSquare, n)
    
    return magicSquare

if __name__ == "__main__":
    # Get size from user
    size = int(input("Enter the Magic Square size : "))
    magic_squar = fillMatrix(size)