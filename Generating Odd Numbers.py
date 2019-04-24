print('Generating Odd Numbers')
x = int(input('Enter the length of the series'))

for i in range (1,x,1):
    if(i % 2) != 0:
        print(i)