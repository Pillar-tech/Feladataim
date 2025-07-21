import random

def main():
    # 5 egyedi véletlen lottószám generálása 1–90 között
    lottoszamok = sorted(random.sample(range(1, 91), 5))
    print("Sorsolt lottószámok:", lottoszamok)

    # Fájl beolvasása
    with open('02_feladat.txt', 'r', encoding='utf-8') as f:
        sorok = f.readlines()

    eredmenyek = []

    for sor in sorok:
        nev, szamok_str = sor.strip().split(';')
        jatekos_szamai = list(map(int, szamok_str.split(',')))

        # Találatok számolása
        talalatok = sum(1 for szam in jatekos_szamai if szam in lottoszamok)
        eredmenyek.append((nev, talalatok))

    # Eredmények fájlba írása
    with open('02_eredmeny.txt', 'w', encoding='utf-8') as f:
        for nev, talalat in eredmenyek:
            f.write(f"{nev};{talalat}\n")

if __name__ == "__main__":
    main()
