import check50


@check50.check()
def exists():
    """p2krajumi.py eksistē"""
    check50.exists("p2krajumi.py")


def check_output(samples, expected):
    process = check50.run("python3 p2krajumi.py")
    process.stdin(str(samples))
    actual = process.stdout()

    if process.exitcode != 0:
        raise check50.Failure(
            f"Programmas izejas kods: {process.exitcode}; gaidīts 0"
        )
    if actual.strip() != expected.strip():
        raise check50.Mismatch(expected, actual)


@check50.check(exists)
def all_sufficient():
    """8 paraugi: visa pietiek, arī tieši 8 smilšpapīra lokšņu"""
    check_output(8, (
        "Stikla plāksnītes: pietiek\n"
        "Smilšpapīra loksnes: pietiek\n"
        "Cimdu pāri: pietiek\n"
    ))


@check50.check(exists)
def example():
    """10 paraugi: trūkst 2 smilšpapīra lokšņu"""
    check_output(10, (
        "Stikla plāksnītes: pietiek\n"
        "Smilšpapīra loksnes: trūkst 2\n"
        "Cimdu pāri: pietiek\n"
    ))


@check50.check(exists)
def exact_glass():
    """12 paraugi: stikla plāksnīšu pietiek tieši"""
    check_output(12, (
        "Stikla plāksnītes: pietiek\n"
        "Smilšpapīra loksnes: trūkst 4\n"
        "Cimdu pāri: pietiek\n"
    ))


@check50.check(exists)
def exact_gloves():
    """15 paraugi: cimdu pāru pietiek tieši"""
    check_output(15, (
        "Stikla plāksnītes: trūkst 3\n"
        "Smilšpapīra loksnes: trūkst 7\n"
        "Cimdu pāri: pietiek\n"
    ))


@check50.check(exists)
def all_insufficient():
    """16 paraugi: trūkst visu trīs piederumu"""
    check_output(16, (
        "Stikla plāksnītes: trūkst 4\n"
        "Smilšpapīra loksnes: trūkst 8\n"
        "Cimdu pāri: trūkst 1\n"
    ))