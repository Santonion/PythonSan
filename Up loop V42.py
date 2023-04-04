import math

for Jensen in input("input jensen: "):
    print("(" + Jensen + ")")

n = int(input("number please: "))
for b in range(n):
   print("|" + (" " * b ) + "\ ")

no = int(input("number please: "))
for now in range(no):
    print(("_" * now) + ("|" * now))

e = int(input("number please: "))
f = 1
for i in range(1, n + 1):
    f = f * i
print("Your factorial is : ", end="")
print(f)

