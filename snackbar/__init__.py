import check50
import check50.c

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
    check50.run("./snackbar").stdin("Burger").stdin("").stdout("Your total cost is: $9.50").exit()

#@check50.check(compiles)
#def test2():
#    """checks for burger, Vegan Burger"""
#    check50.run("./snackbar").stdin("burger").stdin("Vegan Burger").stdin("").stdout("$20.50").exit()
#
#@check50.check(compiles)
#def test3():
#    """checks for Cheese Dog, dog, cheese, hot DOG"""
#    check50.run("./snackbar").stdin("Cheese Dog").stdin("dog").stdin("cheese").stdin("hot DOG").stdin("").stdout("$8.00").exit()
