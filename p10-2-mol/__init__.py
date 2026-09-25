import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-2-mol.py eksistē"""
    check50.exists("p10-2-mol.py")


# Ūdens H2O

@check50.check(exists)
def water():
    """Pārbauda ūdens molmasu"""
    check50.run("python3 p10-2-mol.py").stdin("H").stdin("2").stdin("O").stdin("1").stdin("").stdout("Molmasa: 18 g/mol").exit()


# Oglekļa dioksīds CO2

@check50.check(exists)
def carbon_dioxide():
    """Pārbauda oglekļa dioksīda molmasu"""
    check50.run("python3 p10-2-mol.py").stdin("C").stdin("1").stdin("O").stdin("2").stdin("").stdout("Molmasa: 44 g/mol").exit()


# Nātrija hlorīds NaCl

@check50.check(exists)
def sodium_chloride():
    """Pārbauda nātrija hlorīda molmasu"""
    check50.run("python3 p10-2-mol.py").stdin("Na").stdin("1").stdin("Cl").stdin("1").stdin("").stdout("Molmasa: 58.5 g/mol").exit()


# Kalcija karbonāts CaCO3

@check50.check(exists)
def calcium_carbonate():
    """Pārbauda kalcija karbonāta molmasu"""
    check50.run("python3 p10-2-mol.py").stdin("Ca").stdin("1").stdin("C").stdin("1").stdin("O").stdin("3").stdin("").stdout("Molmasa: 100 g/mol").exit()


# Vairāki dažādi elementi

@check50.check(exists)
def several_elements():
    """Pārbauda vairāku elementu ievadi"""
    check50.run("python3 p10-2-mol.py").stdin("N").stdin("2").stdin("H").stdin("4").stdin("S").stdin("1").stdin("O").stdin("4").stdin("").stdout("Molmasa: 128 g/mol").exit()


# Nezināms elements

@check50.check(exists)
def unknown_element():
    """Pārbauda nezināmu elementu"""
    check50.run("python3 p10-2-mol.py").stdin("X").stdin("2").stdin("H").stdin("2").stdin("O").stdin("1").stdin("").stdout("Nezināms elements").stdout("Molmasa: 18 g/mol").exit()


# Tukša virkne uzreiz

@check50.check(exists)
def empty_input():
    """Pārbauda ievades pabeigšanu bez elementiem"""
    check50.run("python3 p10-2-mol.py").stdin("").stdout("Molmasa: 0 g/mol").exit()


# Hlora decimālā molmasa

@check50.check(exists)
def chlorine():
    """Pārbauda decimālu molmasu"""
    check50.run("python3 p10-2-mol.py").stdin("Cl").stdin("2").stdin("").stdout("Molmasa: 71.0 g/mol").exit()