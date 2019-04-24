i = int(input('Enter the year > 2000:'))

for year in range(2000,i,1):
    if(year % 4)== 0:
        if(year % 100) == 0:
            if(year % 100) == 0:
                print(year, 'is a leap year')
            else:
                print(year, 'is not a leap year')
        else:
            print(year,'is a leap year')
    else:
        print(year,'is not a leap year')