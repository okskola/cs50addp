import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-1-kust.py eksistē"""
    check50.exists("p10-1-kust.py")


# Veseli skaitļi

@check50.check(exists)
def basic():
    """Pārbauda ceļa aprēķinu"""
    check50.run("python3 p10-1-kust.py").stdin("60").stdin("2").stdout("Ceļš: 120.0 km").exit()


# Decimālskaitlis

@check50.check(exists)
def decimal_time():
    """Pārbauda aprēķinu ar decimālu laiku"""
    check50.run("python3 p10-1-kust.py").stdin("60").stdin("2.5").stdout("Ceļš: 150.0 km").exit()


# Negatīvs ātrums

@check50.check(exists)
def negative_speed():
    """Pārbauda negatīvu ātrumu"""
    check50.run("python3 p10-1-kust.py").stdin("-20").stdin("3").stdout("Nederīgi dati").exit()


# Negatīvs laiks

@check50.check(exists)
def negative_time():
    """Pārbauda negatīvu laiku"""
    check50.run("python3 p10-1-kust.py").stdin("50").stdin("-2").stdout("Nederīgi dati").exit()


# Abi lielumi negatīvi

@check50.check(exists)
def both_negative():
    """Pārbauda, ja abi ievaddati ir negatīvi"""
    check50.run("python3 p10-1-kust.py").stdin("-50").stdin("-2").stdout("Nederīgi dati").exit()


# Nulles laiks

@check50.check(exists)
def zero_time():
    """Pārbauda nulles laiku"""
    check50.run("python3 p10-1-kust.py").stdin("80").stdin("0").stdout("Ceļš: 0.0 km").exit()