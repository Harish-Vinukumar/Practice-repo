destiny = int(input('Enter the last value:'))
print('Armstrong numbers:\n')
for num in range(1,destiny,1):
    power =  len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp //= 10
    if num == sum:
        print(num)