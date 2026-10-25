def gyventojai(namai: list[int], gyventojai_name: list[int], gatves_puse: str) -> tuple[int, int]:
    suma = 0

    if gatves_puse == "desine":
        namai_puse = [i for i in namai if i % 2 == 0]
    elif gatves_puse == "kaire":
        namai_puse = [i for i in namai if i % 2 != 0]
    else:
        namai_puse = namai

    for namas in namai_puse:
       suma += gyventojai_name[namai.index(namas)]


    return suma, len(namai_puse)

with open("gyventojai_data.txt", "r") as f:
    data = [line.strip().split() for line in f]
    namu_skaiciai = [int(x[0]) for x in data]
    gyventojai_name = [int(x[1]) for x in data]

    suma_viso, _ = gyventojai(namu_skaiciai, gyventojai_name, None)
    suma_desine, kiekis_desine = gyventojai(namu_skaiciai, gyventojai_name, "desine")
    suma_kaire, kiekis_kaire = gyventojai(namu_skaiciai, gyventojai_name, "kaire")
    vidurkis_desine = suma_desine / kiekis_desine
    vidurkis_kaire = suma_kaire / kiekis_kaire

with open("gyventojai_res.txt", "w") as f:
    f.write(f"{suma_viso:.0f}\n{suma_kaire:.0f}\n{suma_desine:.0f}\n{vidurkis_kaire:.1f}\n{vidurkis_desine:.1f}")
