import re


print("**********************STANDARD DYNAMIC CALCULATOR**************************", end="\n")
print("TYPE 'quit' TO EXIT")
previous = 0
run = True
while run:
    equation = input("YOUR EQUATION:\t")
    if equation == "quit":
        print("Good Bye!!")
        break
    equation = re.sub('[a-zA-z.,&^%$#@!{=}[|"<>;_~`:? ]', '', equation)
    equation = re.sub("[']", '', equation)
    equation = re.sub("]", '', equation)
    try:
        result = 0
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)
        print("RESULT:", int(previous))
    except IOError:
        print('Invalid Equation! \t Try Again!')
