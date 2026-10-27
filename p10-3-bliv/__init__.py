import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-3-bliv.py eksistē"""
    check50.exists("p10-3-bliv.py")


@check50.check(exists)
def basic():
    """Pārbauda blīvuma aprēķinu"""
    check50.run("python3 p10-3-bliv.py").stdin("54").stdin("20").stdout(
        "Blīvums: 2.7 g/cm3"
    ).exit()


@check50.check(exists)
def integer_result():
    """Pārbauda veselu blīvuma vērtību"""
    check50.run("python3 p10-3-bliv.py").stdin("100").stdin("20").stdout(
        "Blīvums: 5.0 g/cm3"
    ).exit()


@check50.check(exists)
def decimal_input():
    """Pārbauda decimāldaļu ievadi"""
    check50.run("python3 p10-3-bliv.py").stdin("12.5").stdin("5").stdout(
        "Blīvums: 2.5 g/cm3"
    ).exit()


@check50.check(exists)
def zero_volume():
    """Pārbauda dalīšanu ar nulli"""
    check50.run("python3 p10-3-bliv.py").stdin("100").stdin("0").stdout(
        "Tilpums nedrīkst būt nulle"
    ).exit()


@check50.check(exists)
def negative_mass():
    """Pārbauda negatīvu masu"""
    check50.run("python3 p10-3-bliv.py").stdin("-10").stdin("5").stdout(
        "Nederīgi dati"
    ).exit()


@check50.check(exists)
def negative_volume():
    """Pārbauda negatīvu tilpumu"""
    check50.run("python3 p10-3-bliv.py").stdin("10").stdin("-5").stdout(
        "Nederīgi dati"
    ).exit()


@check50.check(exists)
def invalid_mass():
    """Pārbauda nekorektu masas ievadi"""
    check50.run("python3 p10-3-bliv.py").stdin("abc").stdout(
        "Nederīga ievade"
    ).exit()


@check50.check(exists)
def invalid_volume():
    """Pārbauda nekorektu tilpuma ievadi"""
    check50.run("python3 p10-3-bliv.py").stdin("100").stdin("abc").stdout(
        "Nederīga ievade"
    ).exit()


@check50.check(exists)
def empty_input():
    """Pārbauda tukšu ievadi"""
    check50.run("python3 p10-3-bliv.py").stdin("").stdout(
        "Nederīga ievade"
    ).exit()