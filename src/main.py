def OddMagicSquare(n):
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

    # initialize position of 1 (i: row, j: column)
    i = n // 2
    j = n - 1
    num = 1
    """
	for n=3 : 
        |j=0   j=1   j=2
	----|------------------
	i=0 |0     0     0     
    i=1 |0     0     1(i,j)     
    i=2 |0     0     0    
    """

    # fill the magic square with numbers
    while num <= (n * n):
        # if the row position is -1 & column position is n, the row must b 0 and column must be n-2
        if i == -1 and j == n:
            j = n - 2
            i = 0
            """
            for n=3 : 
                |j=0   j=1   j=2   j=n
            ----|----------------------
            i=-1|-     -     -     (7)
            i=0 |2     (7)   6     
            i=1 |0     5     1     
            i=2 |4     3     0    
            """

        else:
            # if the column goes out of right side of square set it to 0
            if j == n:
                j = 0
                """
                for n=3 : 
                    |j=0   j=1   j=2   j=n
                ----|----------------------
                i=0 |(2)   0     0     (2)
                i=1 |0     0     1     -
                i=2 |0     0     0     -
                """

            # if the row goes out of upper side set it to n-1
            if i < 0:
                i = n - 1
                """
                for n=3 : 
                    |j=0   j=1   j=2 
                ----|------------------
                i=-1|-     (3)   - 
                i=0 |2     0     0     
                i=1 |0     0     1     
                i=2 |0     (3)   0    
                """

    # if already number at the calculated position, column will be j-2, and row will be i+1.
        if magic_square[int(i)][int(j)] != 0:
            j = j - 2
            i = i + 1
            continue
            """
			for n=3 : 
				|j=0   j=1   j=2
			----|------------------
			i=0 |2     0     0     
			i=1 |0     0     1(4)     
			i=2 |0(4)  3     0    
			"""

        # put the number in right position
        else:
            magic_square[int(i)][int(j)] = num
            num = num + 1
            """
			for n=3 : 
				|j=0     j=1     j=2
			----|---------------------
			i=0 |1+1     0       0     
			i=1 |0       0       1     
			i=2 |1+1+1+1 1+1+1   0    
			"""

    # the row of next number is i-1 and column of next number is j+1
        j = j + 1
        i = i - 1
        """
		for n=3 : 
			|j=0       j=1        j=2
		----|----------------------------
		i=0 |0         0          (j-2, j+2)     
		i=1 |0         (j-1, j+1) 0     
		i=2 |(i,j)     0          0    
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
OddMagicSquare(n)
