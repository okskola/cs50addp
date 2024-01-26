import check50

@check50.check()
def exists():
    """p2digitnum.py exists"""
    check50.exists("p2digitnum.py")

@check50.check(exists)
def test1():
    """checks 331444 2 """
    check50.run("python3 p2digitnum.py").stdin("331444").stdin("2").stdout("1213211314").exit()

@check50.check(exists)
def test2():
    """checks 111111111110 1 """
    check50.run("python3 p2digitnum.py").stdin("111111111110").stdin("1").stdout("11110").exit()

@check50.check(exists)
def test3():
    """checks 1234567890 3 """
    check50.run("python3 p2digitnum.py").stdin("1234567890").stdin("3").stdout("13211231133114311531163117311831193110").exit()

@check50.check(exists)
def test4():
    """checks 322255 7 """
    check50.run("python3 p2digitnum.py").stdin("322255").stdin("7").stdout("121113222112111312211322311311222115").exit()

@check50.check(exists)
def test5():
    """checks 1011121314 5 """
    check50.run("python3 p2digitnum.py").stdin("1011121314").stdin("5").stdout("31131122211013211321322112311311123112111311222114").exit()
