import check50
import check50.c

@check50.check()
def exists():
    """w1ap1-factorial.c exists"""
    check50.exists("w1ap1-factorial.c")

@check50.check(exists)
def compiles():
    """w1ap1-factorial.c compiles"""
    check50.c.compile("w1ap1-factorial.c", lcs50=True)

@check50.check(compiles)
def f5():
    """checks that 5! equals 120"""
    check50.run("./w1ap1-factorial").stdin("5").stdout("Factorial of 5 is 120").exit()

@check50.check(compiles)
def f10():
    """checks that 10! equals 3628800"""
    check50.run("./w1ap1-factorial").stdin("10").stdout("Factorial of 10 is 3628800").exit()

@check50.check(compiles)
def f1():
    """checks that 1! equals 1"""
    check50.run("./w1ap1-factorial").stdin("1").stdout("Factorial of 1 is 1").exit()

@check50.check(compiles)
def f0():
    """checks that 0! equals 1"""
    check50.run("./w1ap1-factorial").stdin("0").stdout("Factorial of 0 is 1").exit()

@check50.check(compiles)
def f0():
    """checks that negative returns -1"""
    check50.run("./w1ap1-factorial").stdin("-1").stdout("Factorial of -1 is -1").exit()

@check50.check(compiles)
def f0():
    """checks that too large n returns -1"""
    check50.run("./w1ap1-factorial").stdin("17").stdout("Factorial of 17 is -1").exit()
