import check50
import check50.c

@check50.check()
def exists():
    """w2ap2-stringsort.c exists"""
    check50.exists("w2ap2-stringsort.c")

@check50.check(exists)
def compiles():
    """w2ap2-stringsort.c compiles"""
    check50.c.compile("w2ap2-stringsort.c", lcs50=True)

@check50.check(compiles)
def test1():
    """checks for lowercase without spaces, sorted"""
    check50.run("./w2ap2-stringsort").stdin("abc").stdin("bcd").stdout("abc\nbcd").exit()

@check50.check(compiles)
def test1():
    """checks for lowercase without spaces, unsorted"""
    check50.run("./w2ap2-stringsort").stdin("bcd").stdin("abc").stdout("abc\nbcd").exit()

@check50.check(compiles)
def test1():
    """checks for lowercase without spaces, equal"""
    check50.run("./w2ap2-stringsort").stdin("57931").stdin("57931").stdout("abc\nbcd").exit()

@check50.check(compiles)
def test1():
    """checks for lowercase with spaces, equal"""
    check50.run("./w2ap2-stringsort").stdin("the test").stdin("t h et e s t").stdout("the test\nt h et e s t").exit()

