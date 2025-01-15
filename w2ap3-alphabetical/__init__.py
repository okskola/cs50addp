import check50.c

@check50.check()
def exists():
    """alphabetical.c exists"""
    check50.exists("alphabetical.c")

@check50.check(exists)
def compiles():
    """alphabetical.c compiles"""
    check50.c.compile("alphabetical.c", lcs50=True)

@check50.check(compiles)
def test_abc():
    """tests abc"""
    check50.run("./alphabetical").stdin("abc").stdout("Yes").exit()

@check50.check(compiles)
def test_abbbbcw():
    """tests abbbbcw"""
    check50.run("./alphabetical").stdin("abbbbcw").stdout("Yes").exit()

@check50.check(compiles)
def test_abbcbb():
    """tests abbcbb"""
    check50.run("./alphabetical").stdin("abbcbb").stdout("No").exit()

@check50.check(compiles)
def test_bca():
    """tests bca"""
    check50.run("./alphabetical").stdin("bca").stdout("No").exit()
