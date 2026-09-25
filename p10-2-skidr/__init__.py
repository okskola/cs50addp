import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-2-skid.py eksistē"""
    check50.exists("p10-2-skid.py")


# Precīzi sasniedz mērķa koncentrāciju

@check50.check(exists)
def exact_target():
    """Pārbauda 40% atšķaidīšanu līdz 5%"""
    check50.run("python3 p10-2-skid.py").stdin("40").stdin("5").stdout("Atšķaidīšanas reizes: 3").exit()


# Koncentrācija nokrītas zem mērķa

@check50.check(exists)
def below_target():
    """Pārbauda atšķaidīšanu, ja mērķi precīzi nesasniedz"""
    check50.run("python3 p10-2-skid.py").stdin("50").stdin("10").stdout("Atšķaidīšanas reizes: 3").exit()


# Nepieciešama viena atšķaidīšana

@check50.check(exists)
def one_dilution():
    """Pārbauda vienu atšķaidīšanas reizi"""
    check50.run("python3 p10-2-skid.py").stdin("20").stdin("15").stdout("Atšķaidīšanas reizes: 1").exit()


# Nepieciešamas vairākas cikla iterācijas

@check50.check(exists)
def many_dilutions():
    """Pārbauda vairākas atšķaidīšanas reizes"""
    check50.run("python3 p10-2-skid.py").stdin("80").stdin("2").stdout("Atšķaidīšanas reizes: 6").exit()


# Sākuma koncentrācija ir negatīva

@check50.check(exists)
def negative_start():
    """Pārbauda negatīvu sākuma koncentrāciju"""
    check50.run("python3 p10-2-skid.py").stdin("-20").stdin("5").stdout("Nederīgi dati").exit()


# Mērķa koncentrācija ir nulle

@check50.check(exists)
def zero_target():
    """Pārbauda nulles mērķa koncentrāciju"""
    check50.run("python3 p10-2-skid.py").stdin("40").stdin("0").stdout("Nederīgi dati").exit()


# Koncentrācija nevar pārsniegt 100%

@check50.check(exists)
def over_hundred():
    """Pārbauda sākuma koncentrāciju virs 100%"""
    check50.run("python3 p10-2-skid.py").stdin("120").stdin("10").stdout("Nederīgi dati").exit()


# Mērķis nevar būt lielāks par sākuma koncentrāciju

@check50.check(exists)
def target_too_high():
    """Pārbauda pārāk lielu mērķa koncentrāciju"""
    check50.run("python3 p10-2-skid.py").stdin("20").stdin("30").stdout("Nederīgi dati").exit()


# Mērķis nevar būt vienāds ar sākuma koncentrāciju

@check50.check(exists)
def equal_values():
    """Pārbauda vienādas sākuma un mērķa koncentrācijas"""
    check50.run("python3 p10-2-skid.py").stdin("20").stdin("20").stdout("Nederīgi dati").exit()