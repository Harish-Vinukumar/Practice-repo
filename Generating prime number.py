print('Prime Number')
x= int(input('Enter the length of the series'))

for i in range(2,x,1):
    a = 0
    for j in range(2,i,1):
        if(i % j) == 0:
            a += 1
    if(a == 0):
        print(i)
