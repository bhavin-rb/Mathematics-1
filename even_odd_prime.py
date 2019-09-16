"""
A positive integer greater which is divisible by 2 is called a Even number.
"""

num = int(input("Enter number range (for example, 0 to 10, enter 10): "))
even_number: List[int] = [x for x in range(num) if x % 2 == 0]

print("Even Numbers are: ", even_number)

print("-----------------------")

"""
An odd number is an integer which is not a multiple of two; A number that when divided by two, leaves a remainder
"""

num = int(input("Enter number range (for example, 0 to 10, enter 10): "))
odd_number: List[int] = [x for x in range(num) if x % 2 != 0]

print("Odd Numbers are: ", odd_number)

print("-----------------------------")

"""
A prime number is a whole number greater than 1 whose only factors are 1 and itself. 
"""
prime_numbers = int(input("Enter number range (for example, 0 to 10, enter 10): "))
num: int

for num in range(prime_numbers + 1):

    if num > 1:  # prime numbers are greater than 1
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print("Prime Numbers are: ", num)
