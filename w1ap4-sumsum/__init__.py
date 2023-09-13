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

