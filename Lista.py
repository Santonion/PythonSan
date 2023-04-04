List1 = ["leslie",  "ron", "tom", "jerry", "donna"]
List2 = List1.copy()
List2.reverse()
element1 = List2[1]
List1.insert(2, element1)
print(List1)
print(List2)
print(element1)
print(List1.count(element1))


Lost = [1, 2, 3, 4, 5]

Lost5 = [6, 7, 8]
Lost5.append([1, 2])
print(Lost5)

Lost2 = [6, 7, 8]
Lost2.extend([1, 2])
print(Lost2)

Lost3 = [1, 2, 3]
Lost3.remove(2)
print(Lost3)

Lost4 = [1, 2, 3]
Lost4.pop(2)
print(Lost4)

Lest = ["elementetz", "annatelementz", "detsistaelementetz", "sikez"]
print(len(Lest))
zord = "z"
print(Lest.count(zord))