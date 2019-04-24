print('\n\t\t\tSimple Calculator')
print('\nOperations:\n\n1. Addition\t2. Subtraction\n3. Multiplication\t4. Division\n5. Modulus\t6. ^x')
y = int(input('\nEnter the Operation:'))
a = int(input('\nValue of A:'))
b = float(input('Value of B:'))

if(y == 1):
    c = a + b
    print('The result is', c)
elif(y == 2):
    c = a - b
    print('The result is', c)
elif(y == 3):
    c = a * b
    print('The result is', c)
elif(y == 4):
    c = a / b
    print('The result is', c)
elif(y == 5):
    c = a % b
    print('The result is', c)
elif(y == 6):
    d = int(input('Enter the power value'))
    c1 = a**d
    c2 = b**d
    print('The result is',c1)
    print('The result is',c2)
else:
    print('Wrong Choice!!')
