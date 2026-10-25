with open("2.txt", "r") as f:
    data = [i for i in f.read()]

info = {"letters": 0, "numbers": 0, "spaces": 0, "other": 0}

for i in data:
    if i.isalpha():
        info["letters"] += 1
    elif i.isnumeric():
        info["numbers"] += 1
    elif i.isspace():
        info["spaces"] += 1
    else:
        info["other"] += 1

for key, value in info.items():
    if key == "letters":
        print(f"Radžių yra {value}")
    elif key == "numbers":
        print(f"Skaitmenų yra {value}")
    elif key == "spaces":
        print(f"Tarpo simbolių yra {value}")
    elif key == "other":
        print(f"Kitokių simbolių yra {value}")