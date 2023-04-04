print("vill du spela ett spel")
x = int(input("yes = 1 or no = 1>: "))
while x == 1:
       x = int(input("vill du spela igen: "))
print("jag vill inte spela med dig heller")






import random

Max_num = 100
A = random.randrange(Max_num)
quess = int(input("quess"))
number_of_quesses = 0
attempt = 10

while quess != A:
    attempt -= 1
    if quess < A:
        print("over")
        quess = int(input("quess again: "))
    elif quess > A:
        print("under")
        quess = int(input("quess again: "))
        number_of_quesses += 1
    else:
        print("W", number_of_quesses + 1,)
        break
    if attempt == 0:
        print("miss")