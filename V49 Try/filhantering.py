import fileinput
file = open("words", "r")
content = file.read()
print(content.count("l"))
