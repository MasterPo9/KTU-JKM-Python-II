with open("4.txt", "r") as f:
    data = [i.lower() for i in f.read() if i.isalpha()]
alphabet = "aąbcčdeęėfghiįyjklmnoprsštuųūvzž"
letters = {f"{i}": 0 for i in alphabet}
for i in data:
    letters[i] += 1

counter = 0
for i in letters.keys():
    if counter >= 5:
        print()
        counter = 0
    print(f"{i.upper()}{i} {letters[i]}", end=" ")
    counter += 1
