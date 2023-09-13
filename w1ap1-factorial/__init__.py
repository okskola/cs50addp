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
def emma():
    """responds to name Emma"""
    check50.run("./w1ap1-factorial").stdin("5").stdout("120").exit()
