i = 1
while i <= 10:
    print(i)
    i += 1

print("dune")

secret_word = "broski"
quess= " "
quess_count = 0
quess_limit = 3
out_of_quesses = False

while quess != secret_word and not(out_of_quesses):
    if quess_count < quess_limit:
       quess=input("enter: ")
       quess_count += 1
    else:
        out_of_quesses = True
if out_of_quesses:
    print("F")
else:
    print("les go")