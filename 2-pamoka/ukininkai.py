with open("ukininkai.txt", "r") as f:
    data = [line.strip() for line in f]
    suma, daugiau, vidurkis = 0, 0, 0

    for ukininkas in data:
        suma += int(ukininkas)
        daugiau += 1 if int(ukininkas) > 50 else 0
    vidurkis = suma / len(data)

with open("Rezultatai.txt", "w") as f:
    f.write(f"{suma:.0f}\n{daugiau:.0f}\n{vidurkis:.1f}")
