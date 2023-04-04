tor = int(input("hur många äter tor i sekunden: ")) #kollar hur många morötter tor ska äta i sekunden
mor = int(input("hur många äter mor i sekunden: ")) #kollar hur många morötter mor ska äta i sekunden
tmorn = tor + mor #Lägger ihop värdet av tor och mor
korn = 40 / tmorn #dividerar mängden morötter (40) med summan av tor och mor adderade
mors = tor * korn #för att lista ut mors värde tar vi tor multiplicerat med tidigare värdet
tors = mor * korn #för att lista ut mors värde tar vi tor multiplicerat med tidigare värdet

print("tors tid är", tors, "och mors tid är", mors) #printar ut resultatet, hur mycket tor och mor äter totalt