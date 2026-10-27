import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-3-videj.py eksistē"""
    check50.exists("p10-3-videj.py")


@check50.check(exists)
def basic():
    """Pārbauda vidējās temperatūras aprēķinu"""
    check50.run("python3 p10-3-videj.py") \
        .stdin("20").stdin("21").stdin("19") \
        .stdin("22").stdin("18") \
        .stdout("Vidējā temperatūra: 20.0 °C") \
        .stdout("Mērījumi pabeigti").exit()


@check50.check(exists)
def decimals():
    """Pārbauda decimāldaļu ievadi"""
    check50.run("python3 p10-3-videj.py") \
        .stdin("10.5").stdin("11.5").stdin("12.5") \
        .stdin("13.5").stdin("14.5") \
        .stdout("Vidējā temperatūra: 12.5 °C") \
        .stdout("Mērījumi pabeigti").exit()


@check50.check(exists)
def negative():
    """Pārbauda negatīvas temperatūras"""
    check50.run("python3 p10-3-videj.py") \
        .stdin("-10").stdin("-20").stdin("-15") \
        .stdin("-5").stdin("0") \
        .stdout("Vidējā temperatūra: -10.0 °C") \
        .stdout("Mērījumi pabeigti").exit()


@check50.check(exists)
def invalid_first():
    """Pārbauda nekorektu pirmo mērījumu"""
    check50.run("python3 p10-3-videj.py") \
        .stdin("abc").stdout("Nederīga ievade") \
        .stdin("10").stdin("20").stdin("30") \
        .stdin("40").stdin("50") \
        .stdout("Vidējā temperatūra: 30.0 °C") \
        .stdout("Mērījumi pabeigti").exit()


@check50.check(exists)
def invalid_middle():
    """Pārbauda nekorektu trešo mērījumu"""
    check50.run("python3 p10-3-videj.py") \
        .stdin("20").stdin("21") \
        .stdin("abc").stdout("Nederīga ievade") \
        .stdin("19").stdin("22").stdin("18") \
        .stdout("Vidējā temperatūra: 20.0 °C") \
        .stdout("Mērījumi pabeigti").exit()


@check50.check(exists)
def invalid_multiple():
    """Pārbauda vairākas nekorektas ievades"""
    check50.run("python3 p10-3-videj.py") \
        .stdin("abc").stdout("Nederīga ievade") \
        .stdin("10") \
        .stdin("xyz").stdout("Nederīga ievade") \
        .stdin("20").stdin("30") \
        .stdin("test").stdout("Nederīga ievade") \
        .stdin("40").stdin("50") \
        .stdout("Vidējā temperatūra: 30.0 °C") \
        .stdout("Mērījumi pabeigti").exit()