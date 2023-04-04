vokaler = "aeiouy"
mening = input("skriv mening: ")
arabiska = ""
kortavolkaler = []
n  = len(mening)
for i in range(n-2):
    if mening[i] in vokaler:
        if not(mening[i+1] in vokaler) and not(mening[i+2] in vokaler):
            kortavolkaler.append(i)
for i in range(n):
        if not(i in kortavolkaler):
            arabiska += mening[i]
print(arabiska[::-1])



N = int(input("ange storlek: "))
table = []
for i in range(N):
    table.append(".")
print(table)
print("for now, table is only a row")

for j in range(N):
    nyrad = []
    for i in range(N):
        nyrad.append(".")
    table[j] = nyrad

table
for row in table:
    print(row)


N = int(input("med grönt kort: "))
M = int(input("utan kort: "))

if N%2==0:
    print(20)
else:
    print(30)

o = 0
ioi = input(int("Hur många personer: "))
fibb = 1
fibbforst = True
forfibb = 0
andrafibb = False
while ioi > 0:
    if fibbforst == True:
       fibb += forfibb
       fibbforst = False
       andrafibb = True
       ioi = ioi - fibb

    else:
        forfibb = True
        fibb += forfibb
        fibbforst = False
        andrafibb = True
        ioi = ioi - fibb



# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1