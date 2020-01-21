'''
A triangle is valid if sum of it's two sides is greater then the third side. 
If three sides are a, b and c, than three conditions should be met.
a + b > c 
a + c > b 
b + c > a  
'''

def triangle_check(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return print('Triangle is NOT VALID')
    else:
        return  print('Triangle is VALID')
    
a = int(input('Enter value of side a: '))
b = int(input('Enter value of side b: '))
c = int(input('Enter value of side c: '))

triangle_check(a,b,c)

# a = 1, b = 2, c = 3: Output is 'Tirangle is NOT VALID'.
# a = 7, b = 10, c = 5: Output is 'Tirangle is VALID'.
