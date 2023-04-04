num1 = float(input("enter first number: "))
awp = input("Enter op")
num2 = float(input("enter second number: "))
if awp == "+":
    print(num1 + num2)
elif awp == "-":
    print(num1 - num2)
elif awp == "/":
    print(num1 / num2)
elif awp == "*":
    print(num1 * num2)
else:
    print("Not working")