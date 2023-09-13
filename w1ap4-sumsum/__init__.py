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
def testn0():
    """rejects n<1"""
    #check50.run("./w1ap4-sumsum").stdin("0").stdin("0").reject()
    check50.run("./w1ap4-sumsum").stdin("0").reject()
