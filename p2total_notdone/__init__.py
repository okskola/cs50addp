import check50

@check50.check()
def exists():
    """p2total.py exists"""
    check50.exists("p2total.py")

@check50.check(exists)
def test1():
    """checks swap(3,4)"""
    check50.run("python3 test.py 3 4").stdout("4,3").exit()
