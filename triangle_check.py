'''
A triangle is valid if sum of its two sides is greater than the third side. 
If three sides are a, b and c, then three conditions should be met.
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

# a = 1, b = 2, c = 3: Output is 'Triangle is NOT VALID'.
# a = 7, b = 10, c = 5: Output is 'Triangle is VALID'.
