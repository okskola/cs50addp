import check50
import check50.c

@check50.check()
def exists():
    """w1ap3-reverse.c exists"""
    check50.exists("w1ap3-reverse.c")

@check50.check(exists)
def compiles():
    """w1ap3-reverse.c compiles"""
    check50.c.compile("w1ap3-reverse.c", lcs50=True)

@check50.check(compiles)
def r12345():
    """checks that reverse of 12345 is 54321"""
    check50.run("./w1ap3-reverse").stdin("12345").stdout("Reversed n is 54321").exit()

@check50.check(compiles)
def r7():
    """checks that reverse of 7 is 7"""
    check50.run("./w1ap3-reverse").stdin("7").stdout("Reversed n is 7").exit()

@check50.check(compiles)
def r0():
    """checks that reverse of 0 is 0"""
    check50.run("./w1ap3-reverse").stdin("0").stdout("Reversed n is 0").exit()

@check50.check(compiles)
def r123000():
    """checks that reverse of 123000 is 321"""
    check50.run("./w1ap3-reverse").stdin("123000").stdout("Reversed n is 321").exit()

@check50.check(compiles)
def rneg12345():
    """checks that reverse of -12345 is -12345"""
    check50.run("./w1ap3-reverse").stdin("-12345").stdout("Reversed n is -12345").exit()
