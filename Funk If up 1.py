def numbers(num1, num2, num3):
    if num1<=num2 and num1<=num3:
        print("num1 is the smallest, the number is " + str(num1))
    elif num2<=num1 and num2<=num3:
        print("num2 is the smallest, the number is " + str(num2))
    else:
        print("num3 is the smallest, the number is " + str(num3))

numbers(8, 8, 8)