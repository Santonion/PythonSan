print ("hello")
Phrase = "sven"
print (phrase.isupper())
print ("hello " + Phrase)
print(10 % 3)
print(2**3)

is_green = True
is_short = False

if is_green and is_short:
    print("You are short and green")
elif is_green and not(is_short):
    print("you are a green and not short")
elif not(is_green) and is_short:
    print("you are not green and tall")
else:
    print("you are not green or not short"

    num1 = 3
    num2 = 4
    num3 = 5

def max_num(num1, num2, num3):
        if num1 >= num2 and num1 >= num3:
            return num1
        elif num2 >= num1 and num2 >= num3:
            return num2
        else:
            return num3
