with open("3.txt", "r") as f:
    data = [y for y in [i.strip() for i in f.readlines()] if " " in y]
print(data)