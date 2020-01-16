def print_table(n:int)
    """ printthe multiplication table for numbers 1 through n inclusive.
    >>> print_table(5)
    
       1  2  3   4   5 
    1  1  2  3   4   5
    2  2  4  6   6   10
    3  3  6  9   12  15
    4  4  8  12  16  20
    5  5  10 15  20  25
    """
            for i in numbers:
                 print('|t' + str(i), end = ' ')
            print()
            
            for i in numbers:
              print(i, end = ' ')
              for j in numbers:
                print('|t' + str(i * j), end=' ')
                
              print()
