import check50

@check50.check()
def exists():
    """p2digitnum.py exists"""
    check50.exists("p3system.py")

@check50.check(exists)
def test1():
    """checks 2x+y=5, -x+y=2 """
    check50.run("python3 p3system.py").stdin("2").stdin("1").stdin("5").stdin("-1").stdin("1").stdin("2").stdout("x=1.0, y=3.0").exit()

@check50.check(exists)
def test2():
    """checks x+y=6, -3x+y=2 """
    check50.run("python3 p3system.py").stdin("1").stdin("1").stdin("6").stdin("-3").stdin("1").stdin("2").stdout("x=1.0, y=5.0").exit()

@check50.check(exists)
def test3():
    """checks 2x+y=5, -x+y=3 (rounding) """
    check50.run("python3 p3system.py").stdin("2").stdin("1").stdin("5").stdin("-1").stdin("1").stdin("3").stdout("x=0.7, y=3.7").exit()

@check50.check(exists)
def test4():
    """checks 1.1x+2.2y=3.3, 4.4x+5.5y=6.6 (floats) """
    check50.run("python3 p3system.py").stdin("1.1").stdin("2.2").stdin("3.3").stdin("4.4").stdin("5.5").stdin("6.6").stdout("x=-1.0, y=2.0").exit()
@check50.check(exists)

def test5():
    """checks ax+y=1, x+y=1 """
    check50.run("python3 p3system.py").stdin("a").stdin("1").stdin("1").stdin("1").stdin("1").stdin("1").stdout("xCannot solve").exit()

@check50.check(exists)
def test6():
    """checks x+y=1, x+y=c """
    check50.run("python3 p3system.py").stdin("1").stdin("1").stdin("1").stdin("1").stdin("1").stdin("c").stdout("xCannot solve").exit()

@check50.check(exists)
def test7():
    """checks x+y=5, x+y=7 """
    check50.run("python3 p3system.py").stdin("1").stdin("1").stdin("5").stdin("1").stdin("1").stdin("7").stdout("xCannot solve").exit()

