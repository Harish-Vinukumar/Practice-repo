import random

print('''\t\t\t\t\t\t\t\t### --- CODEBREAKER --- ###
\t\t\t\t\t1. The computer will think of 3 digit number that has no repeating digits.
\t\t\t\t\t2. You will then guess a 3 digit number
\t\t\t\t\t3. The computer will then give back clues, the possible clues are:

\t\t\t\t\tClose: You've guessed a correct number but in the wrong position
\t\t\t\t\tMatch: You've guessed a correct number in the correct position
\t\t\t\t\tNope: You haven't guess any of the numbers correctly

\t\t\t\t\t4. Based on these clues you will guess again until you break the code with a perfect match!''')


digits = list(range(10))
random.shuffle(digits)
list1 = digits[:3]
#print(list1)
string1 = ""
random.shuffle(list1)
for i in list1:
    string1 = string1 + str(i)
# Another hint:
string2 = "123"
while string1 != string2:
    guess = int(input("What is your guess?: "))
    string2 = str(guess)
    if string1[0] == string2[0]:
        print("Match (in first position!)")
    if string1[1] == string2[1]:
        print("Match (in second position!)")
    if string1[2] == string2[2]:
        print("Match (in third position!)")
    if (string2[0] in string1[1:]) or (string2[2] in string1[:2]) or (string2[1] == string1[0] or string2[1] == string1[2]):
        print("Close")
    if (string2[0] not in string1) and (string2[1] not in string1) and (string2[2] not in string1):
        print("Nope")
    if string1 == string2:
        print("You Broke the Code! (Code: {})".format(string1))
        break

