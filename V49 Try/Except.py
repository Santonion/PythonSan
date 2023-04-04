try:
    A = int(input("input int"))
    B = (input("input str"))

    print(A + B)

except:
    print("you can not add an interger and a string")

try:
    C = int(input("input int"))
    D = int(input("input str"))
    E = C / D
    print(E)

except ZeroDivisionError:
    print("you can not divide a number by zero")

except:
    print("A problem has occured")