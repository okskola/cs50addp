import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-1-kvadr.py eksistē"""
    check50.exists("p10-1-kvadr.py")


# Divas dažādas reālas saknes

@check50.check(exists)
def two_roots():
    """Pārbauda vienādojumu ar divām dažādām reālām saknēm"""
    check50.run("python3 p10-1-kvadr.py").stdin("1").stdin("-5").stdin("6").stdout("x1 = 3.0").stdout("x2 = 2.0").exit()


# Divas vienādas reālas saknes

@check50.check(exists)
def equal_roots():
    """Pārbauda vienādojumu ar divām vienādām saknēm"""
    check50.run("python3 p10-1-kvadr.py").stdin("1").stdin("-4").stdin("4").stdout("x1 = 2.0").stdout("x2 = 2.0").exit()


# Nav reālu sakņu

@check50.check(exists)
def no_roots():
    """Pārbauda vienādojumu bez reālām saknēm"""
    check50.run("python3 p10-1-kvadr.py").stdin("1").stdin("2").stdin("5").stdout("Nav reālu sakņu").exit()


# Koeficients a ir 0

@check50.check(exists)
def not_quadratic():
    """Pārbauda gadījumu, kad a ir 0"""
    check50.run("python3 p10-1-kvadr.py").stdin("0").stdin("2").stdin("3").stdout("Nav kvadrātvienādojums").exit()


# Decimāli koeficienti

@check50.check(exists)
def decimal_coefficients():
    """Pārbauda decimālus koeficientus"""
    check50.run("python3 p10-1-kvadr.py").stdin("0.5").stdin("-1.5").stdin("1").stdout("x1 = 2.0").stdout("x2 = 1.0").exit()