import check50
import check50.c

@check50.check()
def exists():
    """w1ap4-sumsum.c exists"""
    check50.exists("w1ap4-sumsum.c")

@check50.check(exists)
def compiles():
    """w1ap4-sumsum.c compiles"""
    check50.c.compile("w1ap4-sumsum.c", lcs50=True)

@check50.check(compiles)
def sumsum10():
    """checks that sumsum(4,1) is 10"""
    check50.run("./w1ap4-sumsum").stdin("4").stdin("1").stdout("Sumsum: 10").exit()

@check50.check(compiles)
def sumsum21():
    """checks that sumsum(3,2) is 21"""
    check50.run("./w1ap4-sumsum").stdin("3").stdin("2").stdout("Sumsum: 21").exit()


@check50.check(compiles)
def sumsum1540():
    """checks that sumsum(4,3) is 1540"""
    check50.run("./w1ap4-sumsum").stdin("4").stdin("3").stdout("Sumsum: 1540").exit()

@check50.check(compiles)
def test0():
    """rejects a height of 0"""
    check50.run("./mario").stdin("0").reject()