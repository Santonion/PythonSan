tor = int(input("hur många sekunder behövs för tor: "))
mor = int(input("hur många sekunder behövs för mor: "))
tor = tor - 1
mor = mor - 1
A = True
morötter = 39

while morötter > 0:
    morötter -= tor
    tor += 1
while morötter > 1:
    morötter -= mor
    mor += 1
    print(tor + mor)

for morötter in range(0,39):
    morötter -= 1
    tor += 1
for morötter in range(1,39):
    morötter -= 1
    mor += 1
print(tor, mor)








x = tor % 40
mor = 1


sifferkrypto = int(input("sifferkrypto"))
numbers = [sifferkrypto]
enigma = numbers.count(1, 2)
sifferkrypto.len()



tor = int(input("hur många äter tor i sekunden: "))
mor = int(input("hur många äter mor i sekunden: "))
if tor or mor > 100:
    print("error p.ga. av att ett eller båda nummer är över hundra")
else:
    tmorn = tor + mor
    korn = 40 / tmorn
    mors = tor * korn
    tors = mor * korn
    print("tors tid är", tors, "och mors tid är", mors)


tor = int(input("hur många äter tor i sekunden: "))
mor = int(input("hur många äter mor i sekunden: "))
tmorn = tor + mor
korn = 40 / tmorn
mors = tor * korn
tors = mor * korn
if tor or mor >= 100:
    print("tors tid är", tors, "och mors tid är", mors)
else:
    print("did not work")