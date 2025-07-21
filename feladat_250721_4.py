def main():
    konyvek = []

    # Fájl beolvasása
    with open('04_feladat.txt', 'r', encoding='utf-8') as f:
        for sor in f:
            cim, kolcsonzes_str = sor.strip().split(';')
            kolcsonzes = int(kolcsonzes_str)
            konyvek.append((cim, kolcsonzes))

    # Legalább 10-szer kölcsönzött könyvek száma
    legalabb_10 = [cim for cim, db in konyvek if db >= 10]
    legalabb_10_db = len(legalabb_10)

    # Szétválogatás
    tobb_mint_10 = [(cim, db) for cim, db in konyvek if db > 10]
    kevesebb_vagy_10 = [(cim, db) for cim, db in konyvek if db <= 10]

    # Legnépszerűbb könyv (max kölcsönzés)
    legnepszerubb = max(konyvek, key=lambda x: x[1])

    # Eredmény fájlba írása
    with open('04_eredmeny.txt', 'w', encoding='utf-8') as f:
        f.write(f"Legalább 10-szer kölcsönzött könyvek száma: {legalabb_10_db}\n")

        f.write("\n10-nél többször kölcsönzött könyvek:\n")
        for cim, db in tobb_mint_10:
            f.write(f"{cim} ({db} alkalommal)\n")

        f.write("\n10-nél kevesebbszer vagy pont 10-szer kölcsönzött könyvek:\n")
        for cim, db in kevesebb_vagy_10:
            f.write(f"{cim} ({db} alkalommal)\n")

        f.write(f"\nLegnépszerűbb könyv: {legnepszerubb[0]} ({legnepszerubb[1]} alkalommal)\n")

if __name__ == "__main__":
    main()