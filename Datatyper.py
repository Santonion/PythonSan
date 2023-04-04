

tal1 = int(input("lägg in ett tal: "))
tal2 = int(input("lägg in ett till tal: "))
allt = tal1 + tal2
decimal = 100 / allt
procent1 = tal1 * decimal
procent2 = tal2 * decimal
print("talet är", round(procent1), "procent av helheten och det andra talet är", round(procent2)), "procent av helheten"

ice = float(input("input number: "))
def cube(ice):
    square=ice*ice*ice
    return(square)
print(cube(ice))

def personer(namn):
  print(namn)

personer("kirby")
personer("dedede")
personer("knight")

def test(cool):
    if cool == "Yes" or "yes":
        return "Correct"
    elif cool == "No" or "no":
        return "WRONG"
    else:
        return "I humbly disagre"

cool = input("are you cool? ")
print(test(cool))

#3.2
firstNum = int(input(" : "))
secNum = int(input(" : "))
firstOperator = input(" : ")
if firstOperator == "+":
    print(firstNum + secNum)
elif firstOperator == "-":
    print(firstNum - secNum)
elif firstOperator == "/":
    print(firstNum / secNum)
elif firstOperator == "*":
    print(firstNum * secNum)
elif firstOperator == "//":
    print(firstNum // secNum)
elif firstOperator == "%":
    print(firstNum % secNum)
elif firstOperator == "**":
    print(firstNum ** secNum)
elif firstOperator == "**(1/2)" or "sqrt":
    print((firstNum + secNum)**(1/2))

#3.4
Password = input("Write a sequence that is no longer than 8 characters and has at least 1 number in without å ä ö in ")

a = (Password[0])
a.isnumeric()
if len(Password) > 1:
   b = (Password[1])
   b.isnumeric()
if len(Password) > 2:
   c = (Password[2])
   c.isnumeric()
if len(Password) > 3:
   d = (Password[3])
   d.isnumeric()
if len(Password) > 4:
   e = (Password[4])
   e.isnumeric()
if len(Password) > 5:
   f = (Password[5])
   f.isnumeric()
if len(Password) > 6:
   g = (Password[6])
   g.isnumeric()
if len(Password) > 7:
   h = (Password[7])
   h.isnumeric()

def noSpecChar1(Password):
   countAlph = Password.count('å') + Password.count('ä') + Password.count('ö')
   countnum = Password.count('0') + Password.count('1') + Password.count('2') + Password.count('3') + Password.count('4')
   countnum2 = Password.count('5') + Password.count('6') + Password.count('7') + Password.count('8') + Password.count('9')
   print(countAlph)
   if len(Password) > 8:
       print("This is longer than 8 characters... failure ")
       return(Password)
   if countAlph > 0:
       print("There is a character that is not allowed to be here... failure ")
       return(Password)
   if countnum or countnum2 == 0:
       print("There is not a single number in here... failure ")
       return(Password)
   else:
       print("Thanks for entering a password you may continue... success ")

noSpecChar1(Password)

Password = input("Write a sequence that is no longer than 8 characters and has at least 1 number in without å ä ö in ")

def noSpecChar1(Password):
    countAlph = Password.count('å') + Password.count('ä') + Password.count('ö')
    countnum = Password.count('0') + Password.count('1') + Password.count('2') + Password.count('3') + Password.count('4')
    countnum2 = Password.count('5') + Password.count('6') + Password.count('7') + Password.count('8') + Password.count('9')
    print(countAlph)
    print(countnum, countnum2)
    if len(Password) > 8:
        print("This is longer than 8 characters... failure ")
        return(Password)
    if countAlph > 0:
        print("There is a character that is not allowed to be here... failure ")
        return(Password)
    if countnum or countnum2 == 0:
        print("There is not a single number in here... failure ")
        return(Password)
    else:
        print("Thanks for entering a password you may continue... success ")

noSpecChar1(Password)

#4.1
word = input("input: ")
numbers = sum(number.isdigit() for number in word)
letters = sum(number.isalpha() for number in word)

print(numbers, letters)

#4.2
numberOfTimes = int(input("hur många gånger ska den uppreppas"))
start = int(input("Lägg in ett start värde:"))
counting = 0
one = 1
if start == 1:
    print("0")
    print("1")
    print("1")
    counting = 3
if start == 2:
    print("1")
    print("1")
    counting = 2
if start == 3:
    print("1")
    counting = 1
if start <= 0:
    print("enter positiv number")
else:
    while counting < numberOfTimes:
        fibonacci = start + one
        one = start
        start = fibonacci
        counting += 1
        print(start)


#7
elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
elever2 = elever
tuple = tuple(elever2)
nummer = [1, 3, 4, 6, 2, 5]
elever.append("Joergen")
elever.append("Sven")
elever.sort() # jag behöver inte sortera om mina nya elever om jag skriver in dom innan sort frunktionen
nummer.sort(reverse=True)
if "Tom" in elever:
    print("tom är med i elver ")

basgrupp1 = elever[0], elever[1], elever[2]
basgrupp2 = elever[3], elever[4], elever[5], elever[6]
print(basgrupp1)
print(basgrupp2)
print(elever[0])
print(elever[2])
print(nummer)

tuple.sort()
elever2.sort()
print(tuple)
print(elever2)
#You can not change tuple but you can change other lists
