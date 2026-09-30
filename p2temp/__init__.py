import check50


@check50.check()
def exists():
    """p2temp.py eksistē"""
    check50.exists("p2temp.py")


def check_temperatures(start, safe, drop, expected):
    process = check50.run("python3 p2temp.py")
    process.stdin(str(start)).stdin(str(safe)).stdin(str(drop))
    actual = process.stdout()
    if process.exitcode != 0:
        raise check50.Failure(f"Programmas izejas kods: {process.exitcode}; gaidīts 0")
    # Uzvednes patērē stdin(); salīdzinām visu atlikušo izvadi.
    if actual.strip() != expected.strip():
        raise check50.Mismatch(expected, actual)


@check50.check(exists)
def example():
    """100, 40, 15: izdrukā visas minūtes līdz 40 °C"""
    check_temperatures(100, 40, 15,
        "0 min: 100 °C\n1 min: 85 °C\n2 min: 70 °C\n"
        "3 min: 55 °C\n4 min: 40 °C\n")


@check50.check(exists)
def crosses_threshold():
    """100, 40, 17: izdrukā arī pirmo temperatūru zem robežas"""
    check_temperatures(100, 40, 17,
        "0 min: 100 °C\n1 min: 83 °C\n2 min: 66 °C\n"
        "3 min: 49 °C\n4 min: 32 °C\n")


@check50.check(exists)
def equal_at_start():
    """40, 40, 5: izdrukā tikai sākuma rezultātu"""
    check_temperatures(40, 40, 5, "0 min: 40 °C\n")


@check50.check(exists)
def below_at_start():
    """20, 40, 5: izdrukā tikai sākuma rezultātu"""
    check_temperatures(20, 40, 5, "0 min: 20 °C\n")


@check50.check(exists)
def one_minute():
    """50, 40, 20: beidz pēc vienas minūtes pie 30 °C"""
    check_temperatures(50, 40, 20, "0 min: 50 °C\n1 min: 30 °C\n")


@check50.check(exists)
def negative_temperatures():
    """5, -5, 4: pareizi šķērso 0 °C un beidz pie -7 °C"""
    check_temperatures(5, -5, 4,
        "0 min: 5 °C\n1 min: 1 °C\n2 min: -3 °C\n3 min: -7 °C\n")
