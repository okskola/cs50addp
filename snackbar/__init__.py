import check50

@check50.check()
def exists():
    """snackbar.c exists"""
    check50.exists("snackbar.c")

@check50.check(exists)
def compiles():
    """snackbar.c compiles"""
    check50.c.compile("snackbar.c", lcs50=True)

@check50.check(compiles)
def test1():
    """checks for burger, fries, soda"""
    check50.run("./snackbar").stdin("burger").stdin("fries").stdin("soda").stdin("").stdout("$16.50").exit()

@check50.check(compiles)
def test2():
    """checks for cold brew, hot dog"""
    check50.run("./snackbar").stdin("cold brew").stdin("hot dog").stdin("").stdout("$8.00").exit()
