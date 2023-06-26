from odd_order import OddOrderMagicSquare
from doubly_even_order import DoublyEvenOrderMagicSquare
from singly_even_order import SinglyEvenOrderMagicSquare
from termcolor import *
from time import *

def fillMagicSquare(n):
    # Edge cases:
    if n == 1:
        return [[1]]
    if n == 2:
        return None
    # Fill the magicSquare depends on its type:
    # Odd order:
    if n % 2 != 0:
        magicSquare = OddOrderMagicSquare(n)
    # Doubly-even order:
    elif n % 4 == 0:
        magicSquare = DoublyEvenOrderMagicSquare(n)
    # Singly-even order:
    else:
        magicSquare = SinglyEvenOrderMagicSquare(n)
    
    return magicSquare

# Print the Magic Square
def PrintMagicSquare(magicSquare, n):
    if n == 2:
        print(colored("There is no magic square of size 2", "light_cyan"))
        return
    print(colored("Magic Square for %s order" %(n), "light_cyan"))
    print(colored("------------------------", "light_cyan"))
    for i in range(0, n):
        for j in range(0, n):
            print(colored('%3d ' %(magicSquare[i][j]), "light_cyan"), end=' ')
            # Go next row if print all column
            if j == n - 1:
                print()

def main():
    # Communication with the user
    print(colored("===> Welcome to Magic Square Solver <=== \n", "light_yellow", attrs=["bold"]))

    # Get size from user
    size = int(input("Enter the Magic Square size : "))

    # Run until user enter 0
    while size != 0:
        sleep(1)
        magicSquare = fillMagicSquare(size)
        PrintMagicSquare(magicSquare, size)
        sleep(1)
        size = int(input("\nEnter the Magic Square size (enter 0 if you want to exit) : "))
    
    # Developers
    print(colored("\nThank you for choosing us :)\n>>>Developed by Maryam Fakhraei and Amirhossein Naseri<<<\n", "light_magenta"))

if __name__ == "__main__":
    main()
