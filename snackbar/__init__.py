import check50
import check50.c
from re import escape

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
    """checks for Burger"""
    output = "$9.50"
    check50.run("./snackbar").stdin("Burger").stdin("").stdout(regex(output), output, regex=True, timeout=5).exit()

@check50.check(compiles)
def test2():
    """checks for burger, Vegan Burger"""
    output = "$20.50"
    check50.run("./snackbar").stdin("burger").stdin("Vegan Burger").stdin("").stdout(regex(output), output, regex=True, timeout=5).exit()

@check50.check(compiles)
def test3():
    """checks for Cheese Dog, dog, cheese, hot DOG"""
    output = "$12.00"
    check50.run("./snackbar").stdin("Cheese Dog").stdin("dog").stdin("cheese").stdin("hot DOG").stdin("").stdout(regex(output), output, regex=True, timeout=5).exit()

def regex(amount):
    """match amount, allowing for characters (not numbers) on either side"""
    return fr'^([^\d](?<!\$None)(?<!\$nan))*{escape(amount)}([^\d](?<!\$None)(?<!\$nan))*$'
