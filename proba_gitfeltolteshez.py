# Egyszerű fájlmegnyitó program

fajlnev = input("Add meg a fájl nevét (pl. szoveg.txt): ")

try:
    with open(fajlnev, 'r', encoding='utf-8') as fajl:
        tartalom = fajl.read()
        print("\n--- Fájl tartalma ---")
        print(tartalom)
except FileNotFoundError:
    print(f"Hiba: A(z) '{fajlnev}' nevű fájl nem található.")
except Exception as e:
    print(f"Valamilyen hiba történt: {e}")
