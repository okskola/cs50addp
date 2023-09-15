import check50
import check50.c

@check50.check()
def exists():
    """w2ap1-palindrome.c exists"""
    check50.exists("w2ap1-palindrome.c")

@check50.check(exists)
def compiles():
    """w2ap1-palindrome.c compiles"""
    check50.c.compile("w2ap1-palindrome.c", lcs50=True)

@check50.check(compiles)
def noargs():
    """check number of command line arguments"""
    check50.run("./w2ap1-palindrome").exit(1)

@check50.check(compiles)
def toomanyargs():
    """check number of command line arguments"""
    check50.run("./w2ap1-palindrome aaa bbb").exit(1)

@check50.check(compiles)
def evenpalindrome():
    """check if even characters palindrome gives output of yes"""
    check50.run("./w2ap1-palindrome abccba").stdout("Yes").exit()

@check50.check(compiles)
def oddpalindrome():
    """check if odd characters palindrome gives output of yes"""
    check50.run("./w2ap1-palindrome abcdcba").stdout("Yes").exit()

@check50.check(compiles)
def shortpalindrome():
    """check if short palindrome gives output of yes"""
    check50.run("./w2ap1-palindrome k").stdout("Yes").exit()

@check50.check(compiles)
def short2palindrome():
    """check if short palindrome gives output of yes"""
    check50.run("./w2ap1-palindrome kk").stdout("Yes").exit()

@check50.check(compiles)
def short2palindrome():
    """check that program is case-insensitive"""
    check50.run("./w2ap1-palindrome AbCcBa").stdout("Yes").exit()

@check50.check(compiles)
def palindromewithspace():
    """check if palindrome with space gives output of yes"""
    check50.run("./w2ap1-palindrome \"Yawn a more Roman way\"").stdout("Yes").exit()

@check50.check(compiles)
def nopalindrome():
    """check that program outputs No for non-palondrome"""
    check50.run("./w2ap1-palindrome abcdba").stdout("No").exit()

@check50.check(compiles)
def nopalindrome2():
    """check that program outputs No for numeric non-palondrome"""
    check50.run("./w2ap1-palindrome 12").stdout("No").exit()
