import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-4-udens.py eksistē"""
    check50.exists("p10-4-udens.py")


@check50.check(exists)
def basic():
    """Pārbauda piecus mērījumus (uzdevuma piemērs)"""
    check50.include("p10-4-udens1.txt")
    check50.run("python3 p10-4-udens.py") \
        .stdin("p10-4-udens1.txt") \
        .stdout("Mērījumu skaits: 5", regex=False) \
        .stdout("Vidējā temperatūra: 19.7 °C", regex=False) \
        .stdout("Zemākā temperatūra: 18.5 °C", regex=False) \
        .stdout("Augstākā temperatūra: 21.0 °C", regex=False) \
        .exit(0)


@check50.check(exists)
def hundred():
    """Pārbauda 100 mērījumu datni"""
    check50.include("p10-4-udens2.txt")
    check50.run("python3 p10-4-udens.py") \
        .stdin("p10-4-udens2.txt") \
        .stdout("Mērījumu skaits: 100", regex=False) \
        .stdout("Vidējā temperatūra: 23.2 °C", regex=False) \
        .stdout("Zemākā temperatūra: 13.6 °C", regex=False) \
        .stdout("Augstākā temperatūra: 33.4 °C", regex=False) \
        .exit(0)


@check50.check(exists)
def many_with_negative():
    """Pārbauda 10 000 mērījumus, tostarp negatīvas temperatūras"""
    check50.include("p10-4-udens3.txt")
    check50.run("python3 p10-4-udens.py") \
        .stdin("p10-4-udens3.txt") \
        .stdout("Mērījumu skaits: 10000", regex=False) \
        .stdout("Vidējā temperatūra: 11.3 °C", regex=False) \
        .stdout("Zemākā temperatūra: -15.0 °C", regex=False) \
        .stdout("Augstākā temperatūra: 38.0 °C", regex=False) \
        .exit(0)


@check50.check(exists)
def only_negative():
    """Pārbauda datni, kurā visas temperatūras ir negatīvas"""
    with open("p10-4-udens-negativas.txt", "w", encoding="utf-8") as datne:
        datne.write("-8\n-3.5\n-6\n")
    check50.run("python3 p10-4-udens.py") \
        .stdin("p10-4-udens-negativas.txt") \
        .stdout("Mērījumu skaits: 3", regex=False) \
        .stdout("Vidējā temperatūra: -5.8 °C", regex=False) \
        .stdout("Zemākā temperatūra: -8.0 °C", regex=False) \
        .stdout("Augstākā temperatūra: -3.5 °C", regex=False) \
        .exit(0)


@check50.check(exists)
def empty():
    """Pārbauda tukšu datni"""
    check50.include("p10-4-udens4.txt")
    check50.run("python3 p10-4-udens.py") \
        .stdin("p10-4-udens4.txt") \
        .stdout("Nav mērījumu.", regex=False) \
        .exit(0)


@check50.check(exists)
def not_found():
    """Pārbauda neeksistējošu datni"""
    check50.run("python3 p10-4-udens.py") \
        .stdin("nav_sadas_p10-4_datnes_987654.txt") \
        .stdout("Datne nav atrasta.", regex=False) \
        .exit(0)
