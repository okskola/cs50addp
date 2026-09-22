import check50

@check50.check()
def exists():
    """p1kval.py exists"""
    check50.exists("p1kval.py")


# Katrs negatīvās vērtības OR zars

@check50.check(exists)
def negative_porosity():
    """checks negative porosity"""
    check50.run("python3 p1kval.py").stdin("-1").stdin("300").stdin("150").stdout("Nederīgi dati").exit()


@check50.check(exists)
def negative_strength():
    """checks negative strength"""
    check50.run("python3 p1kval.py").stdin("5").stdin("-1").stdin("150").stdout("Nederīgi dati").exit()


@check50.check(exists)
def negative_hardness():
    """checks negative hardness"""
    check50.run("python3 p1kval.py").stdin("5").stdin("300").stdin("-1").stdout("Nederīgi dati").exit()


# Atbilstošs ar katru iekšējā OR zaru

@check50.check(exists)
def strength_boundary():
    """checks strength boundary"""
    check50.run("python3 p1kval.py").stdin("5").stdin("300").stdin("149").stdout("Atbilstošs").exit()


@check50.check(exists)
def hardness_boundary():
    """checks hardness boundary"""
    check50.run("python3 p1kval.py").stdin("5").stdin("299").stdin("150").stdout("Atbilstošs").exit()


@check50.check(exists)
def both_properties():
    """checks both strength and hardness conditions"""
    check50.run("python3 p1kval.py").stdin("5").stdin("300").stdin("150").stdout("Atbilstošs").exit()


# AND nosacījuma pārbaude

@check50.check(exists)
def excessive_porosity_strength():
    """checks high porosity despite sufficient strength"""
    check50.run("python3 p1kval.py").stdin("5.1").stdin("300").stdin("149").stdout("Neatbilstošs").exit()


@check50.check(exists)
def excessive_porosity_hardness():
    """checks high porosity despite sufficient hardness"""
    check50.run("python3 p1kval.py").stdin("5.1").stdin("299").stdin("150").stdout("Neatbilstošs").exit()


# Vērtības tieši zem robežām

@check50.check(exists)
def below_property_boundaries():
    """checks values below strength and hardness boundaries"""
    check50.run("python3 p1kval.py").stdin("5").stdin("299.9").stdin("149.9").stdout("Neatbilstošs").exit()


# Nulle nav negatīva vērtība

@check50.check(exists)
def zero_values():
    """checks zero values"""
    check50.run("python3 p1kval.py").stdin("0").stdin("0").stdin("0").stdout("Neatbilstošs").exit()