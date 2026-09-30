import check50


@check50.check()
def exists():
    """p2masa.py eksistē"""
    check50.exists("p2masa.py")


def check_output(lower, upper, rejected):
    expected = "".join(f"Neder: {mass} g\n" for mass in rejected)
    expected += f"Atliekamo paraugu skaits: {len(rejected)}\n"
    process = check50.run("python3 p2masa.py")
    process.stdin(str(lower)).stdin(str(upper))
    actual = process.stdout()
    if process.exitcode != 0:
        raise check50.Failure(f"Programmas izejas kods: {process.exitcode}; gaidīts 0")
    if actual.strip() != expected.strip():
        raise check50.Mismatch(expected, actual)


@check50.check(exists)
def example():
    """18–22 g: atliek 24 un 16 g; robežas ir pieļaujamas"""
    check_output(18, 22, [24, 16])


@check50.check(exists)
def all_accepted():
    """16–24 g: visi paraugi atbilst; skaits ir 0"""
    check_output(16, 24, [])


@check50.check(exists)
def all_rejected():
    """25–30 g: atliek visus astoņus paraugus saraksta secībā"""
    check_output(25, 30, [19, 20, 22, 18, 21, 20, 24, 16])


@check50.check(exists)
def equal_bounds():
    """20–20 g: abi 20 g paraugi atbilst; pārējie seši Neder"""
    check_output(20, 20, [19, 22, 18, 21, 24, 16])


@check50.check(exists)
def below_only():
    """18–30 g: atliek tikai 16 g paraugu"""
    check_output(18, 30, [16])


@check50.check(exists)
def above_only():
    """0–19 g: atliek visus smagākos paraugus, arī abus 20 g"""
    check_output(0, 19, [20, 22, 21, 20, 24])
