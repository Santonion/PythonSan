tor = int(input("hur många äter tor i sekunden: ")) #kollar hur många morötter tor ska äta i sekunden
mor = int(input("hur många äter mor i sekunden: ")) #kollar hur många morötter mor ska äta i sekunden
tmorn = tor + mor #Lägger ihop värdet av tor och mor
korn = 40 / tmorn
mors = tor * korn
tors = mor * korn

print("tor äter", round(tors), "och mor äter", round(mors))
