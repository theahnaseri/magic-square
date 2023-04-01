def fillOddOrder(magicSquare, n):
    # Initialize position of 1 (i: row, j: column)
    i = n // 2
    j = n - 1

    # Fill the magic square with numbers
    num = 1
    while num <= n*n:
        # 4th condition: if the row position is -1 & column position is n, the row must b 0 and column must be n-2
        if i < 0 and j >= n: 
            i = i + 1
            j = j - 2 

        # 2nd condition: if the column goes out of right side of square set it to 0
        elif j >= n: 
            j = 0 

        # 1st condition: if the row goes out of upper side set it to n-1
        elif i < 0: 
            i = n - 1

        # 3rd condition: if already number at the calculated position, column will be j-2, and row will be i+1.
        if magicSquare[int(i)][int(j)] != 0:
            i = i + 1
            j = j - 2  
            continue 
        
        # Put the number in right position
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        # The row of next number is i-1 and column of next number is j+1
        i = i - 1  
        j = j + 1