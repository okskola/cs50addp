import check50

@check50.check()
def exists():
    """p2ftoc.py exists"""
    check50.exists("p2ftoc.py")

@check50.check(exists)
def test1():
    """checks integer """
    check50.run("python3 p2ftoc.py").stdin("-40").stdin("32").stdin("68").stdin("98").stdin("212").stdout("212.0ºF = 100.0ºC").exit()

