def MagicSquare(n):
    # make a 2D array like a nxn square and set all number to 0
    magic_square = [[0 for x in range(n)] for y in range(n)]
    """
	for n=3 : 
        |j=0   j=1   j=2
	----|------------------
	i=0 |0     0     0     
    i=1 |0     0     0     
    i=2 |0     0     0    
    """

    # print the magic square
    print("\nMagic Square for %s order" % (n))
    print("---------------------------")
    for i in range(0, n):
        for j in range(0, n):
            print(magic_square[i][j], end=' ')

# go next row if print all column
            if j == n - 1:
                print()
                """
				for n=3 : 
					|j=0   j=1   j=2
				----|------------------
				i=0 |2     7     6     
				i=1 |9     5     1     
				i=2 |4     3     8    
				"""


n = int(input("Enter the Magic Square size : "))
MagicSquare(n)
