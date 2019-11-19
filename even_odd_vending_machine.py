# "even-odd vending machine"
# Takes a number as an input and does two things:
# 1. Prints whether the numbe ris even or odd
# 2. Display the next 10 even or odd numbers

x = int(input("Enter a Positive Integer Value: "))
if x % 2 == 0:
    print(f"{x} is Even number")
    even = [i for i in range(x + 2, x + 21) if i % 2 == 0]
    print("Next ten Even numbers are {}".format(even))

if x % 2 == 1:
    print(f"{x} is Odd number")
    odd = [i for i in range(x + 2, x + 22) if i % 2 == 1]
    print("Next ten Odd numbers are {}".format(odd))
