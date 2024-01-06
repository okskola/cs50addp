import check50

@check50.check()
def exists():
    """p0ap2func.py exists"""
    check50.exists("p0ap2-func.py")
    check50.include("testswap.py")
    check50.include("testctof.py")
    check50.include("testhex.py")
    check50.include("testleap.py")

@check50.check(exists)
def test1():
    """checks swap(3,4)"""
    check50.run("python3 testswap.py").stdin("3").stdin("4").stdout("4,3").exit()

@check50.check(exists)
def test2():
    """checks swap(-3,5)"""
    check50.run("python3 testswap.py").stdin("-3").stdin("5").stdout("5,-3").exit()

@check50.check(exists)
def test3():
    """checks c_to_f(-40)"""
    check50.run("python3 testctof.py").stdin("-40").stdout("-40.0").exit()

@check50.check(exists)
def test4():
    """checks c_to_f(0)"""
    check50.run("python3 testctof.py").stdin("0").stdout("32.0").exit()

@check50.check(exists)
def test5():
    """checks c_to_f(10)"""
    check50.run("python3 testctof.py").stdin("10").stdout("50.0").exit()

@check50.check(exists)
def test6():
    """checks hex_area(3)"""
    check50.run("python3 testhex.py").stdin("3").stdout("7.79").exit()

@check50.check(exists)
def test7():
    """checks hex_area(10)"""
    check50.run("python3 testhex.py").stdin("10").stdout("25.98").exit()

@check50.check(exists)
def test8():
    """checks hex_area(1)"""
    check50.run("python3 testhex.py").stdin("1").stdout("2.60").exit()

    print( is_leap(1600) )
    print( is_leap(1700) )
    print( is_leap(2000) )
    print( is_leap(2100) )
    print( is_leap(1996) )
    print( is_leap(2004) )
    print( is_leap(2005) )
    print( is_leap(2006) )

@check50.check(exists)
def test11():
    """checks is_leap(1996)"""
    check50.run("python3 testleap.py").stdin("1996").stdout("True").exit()

@check50.check(exists)
def test12():
    """checks is_leap(1997)"""
    check50.run("python3 testleap.py").stdin("1997").stdout("False").exit()

@check50.check(exists)
def test13():
    """checks is_leap(1998)"""
    check50.run("python3 testleap.py").stdin("1998").stdout("False").exit()

@check50.check(exists)
def test14():
    """checks is_leap(1999)"""
    check50.run("python3 testleap.py").stdin("1999").stdout("False").exit()

@check50.check(exists)
def test9():
    """checks is_leap(1600)"""
    check50.run("python3 testleap.py").stdin("1600").stdout("True").exit()

@check50.check(exists)
def test10():
    """checks is_leap(1700)"""
    check50.run("python3 testleap.py").stdin("1700").stdout("False").exit()

