a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

smallest = 0

if a < b and a < c :
    smallest = a
elif b < c :
    smallest = b
else :
    smallest = c

print(smallest, "is the smallest of three numbers.")