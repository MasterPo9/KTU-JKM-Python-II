rezultatas = []
with open("magiski_vardai_duomenis.txt", "r") as f:
    data = [i.strip().split() for i in f]
    vardai = [i[0] for i in data]
    skaiciai = [i[1] for i in data]
    for i in range(len(vardai)):
        suma = 0
        for letter in vardai[i]:
            suma += ord(letter)
        rezultatas.append(suma*int(skaiciai[i]))
        rezultatas.sort()
print(rezultatas)
