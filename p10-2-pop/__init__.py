import check50


@check50.check()
def exists():
    """Pārbauda, vai p10-2-pop.py eksistē"""
    check50.exists("p10-2-pop.py")


# Pamata piemērs

@check50.check(exists)
def basic():
    """Pārbauda populācijas pieaugumu"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("30").stdin("10").stdin("170").stdout("Gadi: 3").exit()


# Mērķis tiek sasniegts vienā gadā

@check50.check(exists)
def one_year():
    """Pārbauda viena gada populācijas pieaugumu"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("30").stdin("10").stdin("110").stdout("Gadi: 1").exit()


# Nepieciešami vairāki gadi

@check50.check(exists)
def several_years():
    """Pārbauda ilgāku populācijas pieaugumu"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("20").stdin("10").stdin("150").stdout("Gadi: 5").exit()


# Decimāla dzimstība un mirstība

@check50.check(exists)
def decimal_rates():
    """Pārbauda decimālus dzimstības un mirstības rādītājus"""
    check50.run("python3 p10-2-pop.py").stdin("200").stdin("12.5").stdin("5.5").stdin("250").stdout("Gadi: 4").exit()


# Negatīva sākuma populācija

@check50.check(exists)
def negative_population():
    """Pārbauda negatīvu sākuma populāciju"""
    check50.run("python3 p10-2-pop.py").stdin("-100").stdin("20").stdin("10").stdin("200").stdout("Nederīgi dati").exit()


# Negatīva dzimstība

@check50.check(exists)
def negative_birth_rate():
    """Pārbauda negatīvu dzimstību"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("-20").stdin("10").stdin("200").stdout("Nederīgi dati").exit()


# Negatīva mirstība

@check50.check(exists)
def negative_death_rate():
    """Pārbauda negatīvu mirstību"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("20").stdin("-10").stdin("200").stdout("Nederīgi dati").exit()


# Mirstība ir vienāda ar dzimstību

@check50.check(exists)
def equal_rates():
    """Pārbauda vienādu dzimstību un mirstību"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("20").stdin("20").stdin("200").stdout("Nederīgi dati").exit()


# Mirstība ir lielāka par dzimstību

@check50.check(exists)
def death_greater():
    """Pārbauda, ja mirstība pārsniedz dzimstību"""
    check50.run("python3 p10-2-pop.py").stdin("100").stdin("10").stdin("20").stdin("200").stdout("Nederīgi dati").exit()


# Mērķis ir mazāks par sākuma populāciju

@check50.check(exists)
def invalid_target():
    """Pārbauda pārāk mazu mērķa populāciju"""
    check50.run("python3 p10-2-pop.py").stdin("200").stdin("20").stdin("10").stdin("100").stdout("Nederīgi dati").exit()