ordinaryishpeople = ["blue", "man", "group", "and", "stuff"]
best = ["le", "cool"]

O = ordinaryishpeople.copy()
ordinaryishpeople.pop(2)
print (ordinaryishpeople)
ordinaryishpeople.extend(best)
print (ordinaryishpeople)
ordinaryishpeople.sort()
print (ordinaryishpeople[-3], ordinaryishpeople[-2], ordinaryishpeople[-1])
ordinaryishpeople.insert(2, "guys")
print(ordinaryishpeople)
ordinaryishpeople.clear()
ordinaryishpeople.insert(0, "finnito")
print(ordinaryishpeople)
o = ordinaryishpeople.copy()
print(O)
print(o)
