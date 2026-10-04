

def NormalizeName(name):

    if name.endswith('as'):
       name = name[:-2] + "ai"

    elif name.endswith('ius'):
        name = name[:-3] + "iau"

    elif name.endswith('us'):
        name = name[:-2] + "iau"

    elif name.endswith('ė'):
        name = name[:-1] + "e"

    elif name.endswith('a'):
        name = name[:-1] + "a"

    return name


def twoSum(nums: list[int], target: int) -> list[int]:

    for i, number in enumerate(nums):
        print(f"i: {i}; number: {number}")
        for j, number2 in enumerate(nums):
            print(f"j: {j}; number2: {number2}; sum: {number+number2}")
            if int(number)+int(number2) == target and i != j:
                return [i, j]



#print(f"solution {twoSum(nums = [2,7,11,15], target = 9)}")

x = ("abcdef")
solution = ""
for i in range(len(x), 0, -1):
    solution+=str(x[i-1])
