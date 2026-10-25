with open("5.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

encode = data[0].split()
encode[-1] = encode[-1].replace(".", "")

info = {i[0]:i[1] for i in [line.split() for line in data[2:]]}

words = [" ".join([info[letter.upper()] for letter in word]) for word in encode]
print(*words, sep="\n")