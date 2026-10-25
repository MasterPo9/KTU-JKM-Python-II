with open("1.txt", "r") as f:
    data = [i for i in f.read() if i.isdigit()]

numbers = {f"{i}": 0 for i in range(0, 10)}
for i in data:
    numbers[i] += 1

for keys, values in numbers.items():
    print(keys, values)

with open("1out.txt", "w") as f:
    for keys, values in numbers.items():
        f.write(f"{keys} {values}\n")