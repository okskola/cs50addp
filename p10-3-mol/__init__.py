import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-3-mol.py eksistē"""
    check50.exists("p10-3-mol.py")


@check50.check(exists)
def oxygen():
    """Pārbauda skābekļa molmasu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("O").stdin("2") \
        .stdout("Molmasa: 32 g/mol").exit()


@check50.check(exists)
def hydrogen():
    """Pārbauda ūdeņraža molmasu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("H").stdin("2") \
        .stdout("Molmasa: 2 g/mol").exit()


@check50.check(exists)
def sodium():
    """Pārbauda nātrija molmasu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("Na").stdin("1") \
        .stdout("Molmasa: 23 g/mol").exit()


@check50.check(exists)
def chlorine():
    """Pārbauda decimālu molmasu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("Cl").stdin("2") \
        .stdout("Molmasa: 71.0 g/mol").exit()


@check50.check(exists)
def calcium():
    """Pārbauda lielāku atomu skaitu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("Ca").stdin("5") \
        .stdout("Molmasa: 200 g/mol").exit()


@check50.check(exists)
def unknown_element():
    """Pārbauda nezināmu elementu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("Fe") \
        .stdout("Nezināms elements").exit()


@check50.check(exists)
def lowercase():
    """Pārbauda nepareizu elementa simbolu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("na") \
        .stdout("Nezināms elements").exit()


@check50.check(exists)
def invalid_count():
    """Pārbauda tekstu atomu skaita vietā"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("H").stdin("abc") \
        .stdout("Nederīgs atomu skaits").exit()


@check50.check(exists)
def decimal_count():
    """Pārbauda decimālskaitli atomu skaita vietā"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("O").stdin("2.5") \
        .stdout("Nederīgs atomu skaits").exit()


@check50.check(exists)
def zero_count():
    """Pārbauda atomu skaitu 0"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("C").stdin("0") \
        .stdout("Atomu skaitam jābūt pozitīvam").exit()


@check50.check(exists)
def negative_count():
    """Pārbauda negatīvu atomu skaitu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("Mg").stdin("-3") \
        .stdout("Atomu skaitam jābūt pozitīvam").exit()


@check50.check(exists)
def empty_element():
    """Pārbauda tukšu elementa simbolu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("") \
        .stdout("Nezināms elements").exit()


@check50.check(exists)
def empty_count():
    """Pārbauda tukšu atomu skaitu"""
    check50.run("python3 p10-3-mol.py") \
        .stdin("N").stdin("") \
        .stdout("Nederīgs atomu skaits").exit()