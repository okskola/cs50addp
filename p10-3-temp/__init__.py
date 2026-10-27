import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-3-temp.py eksistē"""
    check50.exists("p10-3-temp.py")


@check50.check(exists)
def positive():
    """Pārbauda pozitīvu temperatūru"""
    check50.run("python3 p10-3-temp.py").stdin("25").stdout(
        "Temperatūra: 298.15 K"
    ).exit()


@check50.check(exists)
def zero():
    """Pārbauda 0 °C"""
    check50.run("python3 p10-3-temp.py").stdin("0").stdout(
        "Temperatūra: 273.15 K"
    ).exit()


@check50.check(exists)
def negative():
    """Pārbauda negatīvu temperatūru"""
    check50.run("python3 p10-3-temp.py").stdin("-20").stdout(
        "Temperatūra: 253.15 K"
    ).exit()


@check50.check(exists)
def absolute_zero():
    """Pārbauda absolūto nulli"""
    check50.run("python3 p10-3-temp.py").stdin("-273.15").stdout(
        "Temperatūra: 0.0 K"
    ).exit()


@check50.check(exists)
def below_absolute_zero():
    """Pārbauda temperatūru zem absolūtās nulles"""
    check50.run("python3 p10-3-temp.py").stdin("-300").stdout(
        "Temperatūra zem absolūtās nulles"
    ).exit()


@check50.check(exists)
def invalid_text():
    """Pārbauda teksta ievadi"""
    check50.run("python3 p10-3-temp.py").stdin("abc").stdout(
        "Nederīga ievade"
    ).exit()


@check50.check(exists)
def invalid_empty():
    """Pārbauda tukšu ievadi"""
    check50.run("python3 p10-3-temp.py").stdin("").stdout(
        "Nederīga ievade"
    ).exit()