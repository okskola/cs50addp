import check50

@check50.check()
def exists():
    """p1kval.py exists"""
    check50.exists("p1kval.py")


@check50.check(exists)
def test_invalid():
    """checks negative value"""
    check50.run("python3 p1kval.py").stdin("4").stdin("-1").stdin("160").stdout("Nederīgi dati").exit()


@check50.check(exists)
def test_strength():
    """checks suitable sample based on strength"""
    check50.run("python3 p1kval.py").stdin("4").stdin("300").stdin("100").stdout("Atbilstošs").exit()


@check50.check(exists)
def test_hardness():
    """checks suitable sample based on hardness"""
    check50.run("python3 p1kval.py").stdin("5").stdin("250").stdin("150").stdout("Atbilstošs").exit()


@check50.check(exists)
def test_high_porosity():
    """checks sample with excessive porosity"""
    check50.run("python3 p1kval.py").stdin("5.1").stdin("400").stdin("200").stdout("Neatbilstošs").exit()


@check50.check(exists)
def test_low_properties():
    """checks sample with insufficient strength and hardness"""
    check50.run("python3 p1kval.py").stdin("3").stdin("299").stdin("149").stdout("Neatbilstošs").exit()


@check50.check(exists)
def test_zero():
    """checks zero values are not treated as negative"""
    check50.run("python3 p1kval.py").stdin("0").stdin("0").stdin("0").stdout("Neatbilstošs").exit()