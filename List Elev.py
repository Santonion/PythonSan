elever = ['Axel', 'Johan', 'Johanna', 'Oscar', 'Bill']
nummer = [1, 3, 4, 6, 2, 5]
print(elever[0])
print(elever[2])

elever.sort()
nummer.sort()
print(elever)
print(nummer)

elever.extend("zabe")
elever.extend("zobe")
print(elever)

if "tom" in elever:
    print("tom is in list")
