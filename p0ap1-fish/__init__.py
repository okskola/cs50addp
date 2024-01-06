import check50

@check50.check()
def exists():
    """p0ap1-fish.py exists"""
    check50.exists("p0ap1-fish.py")

@check50.check(exists)
def test1():
    """checks 100	30	3 """
    check50.run("python3 p0ap1-fish.py").stdin("100").stdin("30").stdin("3").stdout("0").exit()

@check50.check(exists)
def test2():
    """checks 101.99	8	51 """
    check50.run("python3 p0ap1-fish.py").stdin("101.99").stdin("8").stdin("51").stdout("7").exit()

@check50.check(exists)
def test3():
    """checks 1234.567	1000	1.33 """
    check50.run("python3 p0ap1-fish.py").stdin("1234.567").stdin("1000").stdin("1.33").stdout("72").exit()

@check50.check(exists)
def test4():
    """checks 7376	691	15.67 """
    check50.run("python3 p0ap1-fish.py").stdin("7376").stdin("691").stdin("15.67").stdout("221").exit()

@check50.check(exists)
def test5():
    """checks 98.1	100	1.234567 """
    check50.run("python3 p0ap1-fish.py").stdin("98.1").stdin("100").stdin("1.234567").stdout("21").exit()

@check50.check(exists)
def test6():
    """checks 999993.333299	1000000	9.00003 """
    check50.run("python3 p0ap1-fish.py").stdin("999993.333299").stdin("1000000").stdin("9.00003").stdout("888891").exit()

@check50.check(exists)
def test7():
    """checks 10.1	200	0.1 """
    check50.run("python3 p0ap1-fish.py").stdin("10.1").stdin("200").stdin("0.1").stdout("99").exit()
