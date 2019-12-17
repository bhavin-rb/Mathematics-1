'''
Multiplication generator table is cool. User can specify both the number and up 
to which multiple. For example user should to input that he/she wants to seea table
listing of the first 15 multiples of 3. 

Because we want to print the multiplication table from 1 to m, we have a foor loop
at (1) that iterates over each of these numbers, printing the product itself and the
number, a.
'''

def multi_table(a):
    for i in range(1, int(m)):   # for loop --- (1)
        print('{0} x {1} = {2}'.format(a, i, a * i))


if __name__ == '__main__':
    a = input('Enter a number: ')
    m = input('Enter number of multiples: ')

    multi_table(float(a))
