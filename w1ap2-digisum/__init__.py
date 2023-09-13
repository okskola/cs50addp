import check50
import check50.c

@check50.check()
def exists():
    """w1ap2-digisum.c exists"""
    check50.exists("w1ap2-digisum.c")

@check50.check(exists)
def compiles():
    """w1ap2-digisum.c compiles"""
    check50.c.compile("w1ap2-digisum.c", lcs50=True)

@check50.check(compiles)
def s135():
    """checks that sum of first and last digits of 135 equals 6"""
    check50.run("./w1ap2-digisum").stdin("135").stdout("Sum of first and last digits of n is 6").exit()

@check50.check(compiles)
def s6():
    """checks that sum of first and last digits of 6 equals 12"""
    check50.run("./w1ap2-digisum").stdin("6").stdout("Sum of first and last digits of n is 12").exit()

@check50.check(compiles)
def sneg():
    """checks that sum of first and last digits of negative nuber returns -1"""
    check50.run("./w1ap2-digisum").stdin("-5").stdout("Sum of first and last digits of n is -1").exit()

