import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-3-trijst.py eksistē"""
    check50.exists("p10-3-trijst.py")


@check50.check(exists)
def basic():
    """Pārbauda trijstūri ar malām 3, 4, 5"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("3").stdin("4").stdin("5") \
        .stdout("Perimetrs: 12.0").exit()


@check50.check(exists)
def equilateral():
    """Pārbauda vienādmalu trijstūri"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("5").stdin("5").stdin("5") \
        .stdout("Perimetrs: 15.0").exit()


@check50.check(exists)
def decimal_sides():
    """Pārbauda decimālus malu garumus"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("2.5").stdin("3.5").stdin("4") \
        .stdout("Perimetrs: 10.0").exit()


@check50.check(exists)
def isosceles():
    """Pārbauda vienādsānu trijstūri"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("5").stdin("5").stdin("8") \
        .stdout("Perimetrs: 18.0").exit()


@check50.check(exists)
def impossible():
    """Pārbauda trijstūri, kas neeksistē"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("2").stdin("3").stdin("8") \
        .stdout("Trijstūris neeksistē").exit()


@check50.check(exists)
def equal_sum():
    """Pārbauda robežgadījumu, kad divu malu summa ir vienāda ar trešo"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("2").stdin("3").stdin("5") \
        .stdout("Trijstūris neeksistē").exit()


@check50.check(exists)
def impossible_first():
    """Pārbauda, vai tiek pārbaudītas visas malu kombinācijas"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("10").stdin("2").stdin("3") \
        .stdout("Trijstūris neeksistē").exit()


@check50.check(exists)
def impossible_second():
    """Pārbauda citu neiespējamu malu kombināciju"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("2").stdin("10").stdin("3") \
        .stdout("Trijstūris neeksistē").exit()


@check50.check(exists)
def negative_a():
    """Pārbauda negatīvu pirmo malu"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("-2").stdin("4").stdin("5") \
        .stdout("Malu garumiem jābūt pozitīviem").exit()


@check50.check(exists)
def negative_b():
    """Pārbauda negatīvu otro malu"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("3").stdin("-4").stdin("5") \
        .stdout("Malu garumiem jābūt pozitīviem").exit()


@check50.check(exists)
def negative_c():
    """Pārbauda negatīvu trešo malu"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("3").stdin("4").stdin("-5") \
        .stdout("Malu garumiem jābūt pozitīviem").exit()


@check50.check(exists)
def zero_side():
    """Pārbauda nulles garuma malu"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("0").stdin("4").stdin("5") \
        .stdout("Malu garumiem jābūt pozitīviem").exit()


@check50.check(exists)
def invalid_first():
    """Pārbauda nekorektu pirmās malas ievadi"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("abc") \
        .stdout("Nederīga ievade").exit()


@check50.check(exists)
def invalid_second():
    """Pārbauda nekorektu otrās malas ievadi"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("3").stdin("abc") \
        .stdout("Nederīga ievade").exit()


@check50.check(exists)
def invalid_third():
    """Pārbauda nekorektu trešās malas ievadi"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("3").stdin("4").stdin("abc") \
        .stdout("Nederīga ievade").exit()


@check50.check(exists)
def empty_input():
    """Pārbauda tukšu ievadi"""
    check50.run("python3 p10-3-trijst.py") \
        .stdin("") \
        .stdout("Nederīga ievade").exit()