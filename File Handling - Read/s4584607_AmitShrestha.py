# Importing reduce from functools
from functools import reduce

def main():
    # Getting list of numbers from a text file
    f = open("numbers.txt", "r")
    a = f.read().split()
    f.close()

    '''
    Converting the list into integer type from string type
    by mapping it to int type
    ''' 
    b = map(int, a)

    # Reducing the list to get the total sum of numbers
    def sum(c, d): return c + d

    su = reduce(sum, b)

    # Calculating the average
    average = su / len(a)

    # Output of average
    print("The average of the numbers from the text file is", average)

main()
