A = int(input("Enter numer: "))
B = int(input("Enter numer: "))
C = int(input("Enter numer: "))
list1 = A, B, C
list2 = A, B, C
print(list1)
list = sorted(list2)
D = 0
E = 0
F = 0
if A < C and A < B:
    D = A
    if B < C and B < A:
        D = B
    else:
        D = C

if A < C and A < B:
    E = A
    if B > C and B < A:
        E = B
    else:
        E = C

if A > C and A > B:
    F = A
    if B > C and B > A:
        F = B
    else:
        F = C
print(D, E, F)
#jämför alla tal och kollar om dom är mindre eller större än dom andra tallen, när den har hittat det minsta, mittersta eller största ger den det rätt variabel som sedan prinats ut i rätt ordning
