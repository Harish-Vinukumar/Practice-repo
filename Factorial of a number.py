print('Factorial of a given number')

x = int(input('Enter a number'))

fact = 1

for i in range(1,x+1,1):
    fact *= i
print('Factorial of a number-',x,'is',fact)