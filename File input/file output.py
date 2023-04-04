import fileinput

file = open("song.txt", "r")
song = file.read()
print(song)

f = open("gg", "a")
f.write("w")
f.close()
f = open("C:\\users\\SanteHedin\\desktop\\song.txt", "w")

f = open("gg", "r")
print(f.read())

for line in fileinput.input(files = 'gg'):
    print(line)

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
