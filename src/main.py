from odd_order import fillOddOrder
from doubly_even_order import fillDoublyEvenOrder
from termcolor import *
from time import *

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

# Print the Magic Square
def display(magic_square, n):
    print(colored("Magic Square for %s order" %(n), "light_cyan"))
    print(colored("------------------------", "light_cyan"))
    for i in range(0, n):
        for j in range(0, n):
            print(colored('%3d ' %(magic_square[i][j]), "light_cyan"), end=' ')
            # Go next row if print all column
            if j == n - 1:
                print()


if __name__ == "__main__":
    # Communication with the user
    print(colored("===> Welcome to Magic Square Solver <=== \n", "light_yellow", attrs=["bold"]))

    # Get size from user
    size = int(input("Enter the Magic Square size : "))

    # Run until user enter 0
    while size != 0:
        sleep(1)
        magic_squar = fillMatrix(size)
        display(magic_squar, size)
        sleep(1)
        size = int(input("\nEnter the Magic Square size (enter 0 if you want to exit) : "))
    
    # Developers
    print(colored("\nThank you for choosing us :)\n>>>Developed by Maryam Fakhraei and Amirhossein Naseri<<<\n", "light_magenta"))
