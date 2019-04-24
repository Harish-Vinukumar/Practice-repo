import matrix

r = int(input("Enter the row size:"))
c = int(input("Enter the column size:"))


for i in range(1,r,1):
    for j in range(1,c,1):
        matrix[r][c] = input()

for i in range(1,r,1):
    for j in range(1,c,1):
        print(matrix[r][c])
