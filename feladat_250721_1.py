def main():
    # Fájl beolvasása
    with open('01_feladat.txt', 'r', encoding='utf-8') as f:
        sorok = f.readlines()

    # Lista az adatok tárolásához
    diakok = []

    for sor in sorok:
        nev, pont_str = sor.strip().split(';')
        pont = int(pont_str)
        diakok.append((nev, pont))

    # Összpontszám és átlag
    osszpont = sum(pont for _, pont in diakok)
    atlag = osszpont / len(diakok) if diakok else 0

    # Legalább 60 pontot elért diákok száma
    megfeleltek_szama = sum(1 for _, pont in diakok if pont >= 60)

    # Legjobb és leggyengébb tanuló
    legjobb = max(diakok, key=lambda x: x[1])
    leggyengebb = min(diakok, key=lambda x: x[1])

    # Eredmények kiírása a képernyőre
    print(f"Összpontszám: {osszpont}")
    print(f"Átlagpontszám: {atlag:.2f}")
    print(f"60 pontot elért diákok száma: {megfeleltek_szama}")
    print(f"Legjobb tanuló: {legjobb[0]} ({legjobb[1]} pont)")
    print(f"Leggyengébb tanuló: {leggyengebb[0]} ({leggyengebb[1]} pont)")

    # Új fájl írása megfelelt-e mezővel
    with open('01_eredmeny.txt', 'w', encoding='utf-8') as f:
        for nev, pont in diakok:
            megfelelt = "igen" if pont >= 60 else "nem"
            f.write(f"{nev};{pont};{megfelelt}\n")

if __name__ == "__main__":
    main()