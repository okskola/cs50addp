import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-3-mer.py eksistē"""
    check50.exists("p10-3-mer.py")


@check50.check(exists)
def first():
    """Pārbauda pirmo mērījumu"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("1") \
        .stdout("Spriegums: 4.5 V").exit()


@check50.check(exists)
def middle():
    """Pārbauda trešo mērījumu"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("3") \
        .stdout("Spriegums: 5.1 V").exit()


@check50.check(exists)
def last():
    """Pārbauda pēdējo mērījumu"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("5") \
        .stdout("Spriegums: 5.0 V").exit()


@check50.check(exists)
def too_large():
    """Pārbauda pārāk lielu mērījuma numuru"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("8") \
        .stdout("Šāda mērījuma nav").exit()


@check50.check(exists)
def zero():
    """Pārbauda mērījuma numuru 0"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("0") \
        .stdout("Šāda mērījuma nav").exit()


@check50.check(exists)
def negative():
    """Pārbauda negatīvu mērījuma numuru"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("-1") \
        .stdout("Šāda mērījuma nav").exit()


@check50.check(exists)
def invalid_text():
    """Pārbauda teksta ievadi"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("abc") \
        .stdout("Nederīga ievade").exit()


@check50.check(exists)
def invalid_decimal():
    """Pārbauda decimālskaitļa ievadi"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("2.5") \
        .stdout("Nederīga ievade").exit()


@check50.check(exists)
def empty():
    """Pārbauda tukšu ievadi"""
    check50.run("python3 p10-3-mer.py") \
        .stdin("") \
        .stdout("Nederīga ievade").exit()