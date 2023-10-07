import check50
import check50.c

@check50.check()
def exists():
    """trie.c exists"""
    check50.exists("trie.c")

@check50.check(exists)
def compiles():
    """trie.c compiles"""
    check50.c.compile("trie.c", lcs50=True)

@check50.check(compiles)
def noargs():
    """check number of command line arguments (no args)"""
    check50.run("./trie").exit(1)

@check50.check(compiles)
def toomanyargs():
    """check number of command line arguments (too many args)"""
    check50.run("./trie aaa.txt bbb.txt").exit(1)

# @check50.check(compiles)
# def test1():
#     """checks for no argument"""
#     check50.run("./trie").stdout("abc\nbcd").exit()

# @check50.check(compiles)
# def test2():
#     """checks for lowercase without spaces, unsorted"""
#     check50.run("./trie").stdin("bcd").stdin("abc").stdout("abc\nbcd").exit()

# @check50.check(compiles)
# def test3():
#     """checks for equal"""
#     check50.run("./trie").stdin("57931").stdin("57931").stdout("57931\n57931").exit()

# @check50.check(compiles)
# def test4():
#     """checks for lowercase with spaces, equal"""
#     check50.run("./trie").stdin("the test").stdin("t h et e s t").stdout("the test\nt h et e s t").exit()

# @check50.check(compiles)
# def test5():
#     """checks for different case, without spaces, sorted"""
#     check50.run("./trie").stdin("aBc").stdin("BcD").stdout("aBc\nBcD").exit()

# @check50.check(compiles)
# def test6():
#     """checks for different case, without spaces, unsorted"""
#     check50.run("./trie").stdin("aBcd").stdin("AbAd").stdout("AbAd\naBcd").exit()

# @check50.check(compiles)
# def test7():
#     """checks for different case, with spaces, unsorted"""
#     check50.run("./trie").stdin("a Bc d").stdin("aA            cd").stdout("aA            cd\na Bc d").exit()

