try:
    m = float(input("Masa (g): "))
    V = float(input("Tilpums (cm3): "))

    if m < 0 or V < 0:
        print("Nederīgi dati")
    else:
        blivums = m / V

except ValueError:
    print("Nederīga ievade")
except ZeroDivisionError:
    print("Tilpums nedrīkst būt nulle")
else:
    if m >= 0 and V >= 0:
        print(f"Blīvums: {blivums} g/cm3")