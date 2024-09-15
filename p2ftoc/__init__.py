import check50

@check50.check()
def exists():
    """p2ftoc.py exists"""
    check50.exists("p2ftoc.py")

@check50.check(exists)
def test1():
    """checks integer """
    check50.run("python3 p2ftoc.py").stdin("-40").stdin("32").stdin("68").stdin("98").stdin("212").stdout("212.0ºF = 100.0ºC").exit()

@check50.check(exists)
def test2():
    """checks floats """
    check50.run("python3 p2ftoc.py").stdin("-40").stdin("32").stdin("68").stdin("98.6").stdin("212").stdout("98.6ºF = 37.0ºC").exit()

@check50.check(exists)
def test3():
    """checks inpuit rounding """
    check50.run("python3 p2ftoc.py").stdin("-40").stdin("32").stdin("68").stdin("98.6").stdin("212.00005").stdout("212.0ºF = 100.0ºC").exit()

@check50.check(exists)
def test3():
    """checks output rounding """
    check50.run("python3 p2ftoc.py").stdin("-40").stdin("32").stdin("68").stdin("98.6").stdin("2").stdout("2.0ºF = -16.7ºC").exit()
