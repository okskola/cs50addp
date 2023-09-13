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
def s135():
    """checks that sum of first and last digits of 135 equals 6"""
    check50.run("./w1ap3-reverse").stdin("135").stdout("Sum of first and last digits of n is 6").exit()
