import check50

@check50.check()
def exists():
    """p1blivums.py exists"""
    check50.exists("p1blivums.py")


@check50.check(exists)
def test_invalid():
    """checks -100"""
    check50.run("python3 p1blivums.py").stdin("-100").stdout("Nederīgs").exit()


@check50.check(exists)
def test_low():
    """checks 1999"""
    check50.run("python3 p1blivums.py").stdin("1999").stdout("Zems").exit()


@check50.check(exists)
def test_lower_boundary():
    """checks 2000"""
    check50.run("python3 p1blivums.py").stdin("2000").stdout("Vidējs").exit()


@check50.check(exists)
def test_upper_boundary():
    """checks 6000"""
    check50.run("python3 p1blivums.py").stdin("6000").stdout("Vidējs").exit()


@check50.check(exists)
def test_high():
    """checks 6001"""
    check50.run("python3 p1blivums.py").stdin("6001").stdout("Augsts").exit()
