"""check50 pārbaudes uzdevumam p10-4-oma."""

from pathlib import Path

import check50


def _palaist(pretestiba, maksimalais_spriegums, izvaddatne):
    """Palaiž skolēna programmu ar trim ievadēm."""
    check50.run("python3 p10-4-oma.py") \
        .stdin(str(pretestiba), prompt=False) \
        .stdin(str(maksimalais_spriegums), prompt=False) \
        .stdin(izvaddatne, prompt=False) \
        .stdout("Rezultāti saglabāti.", regex=False) \
        .exit(0)


def _parbaudit_saturu(izvaddatne, sagaidamais):
    """Pārbauda, vai datne izveidota un tās saturs ir precīzs."""
    check50.exists(izvaddatne)
    faktiskais = Path(izvaddatne).read_text(encoding="utf-8")
    if faktiskais != sagaidamais:
        raise check50.Mismatch(sagaidamais, faktiskais)


@check50.check()
def exists():
    """Pārbauda, vai p10-4-oma.py eksistē"""
    check50.exists("p10-4-oma.py")


@check50.check(exists)
def basic():
    """Pārbauda uzdevuma piemēru: 5 Ω un 5 V"""
    _palaist(5, 5, "oma.txt")
    _parbaudit_saturu(
        "oma.txt",
        "1 V: 0.20 A\n"
        "2 V: 0.40 A\n"
        "3 V: 0.60 A\n"
        "4 V: 0.80 A\n"
        "5 V: 1.00 A\n",
    )


@check50.check(exists)
def decimal_resistance():
    """Pārbauda decimāldaļu pretestību un citu datnes nosaukumu"""
    _palaist(2.5, 3, "rezultati_2.txt")
    _parbaudit_saturu(
        "rezultati_2.txt",
        "1 V: 0.40 A\n"
        "2 V: 0.80 A\n"
        "3 V: 1.20 A\n",
    )


@check50.check(exists)
def rounding():
    """Pārbauda strāvas stipruma noapaļošanu līdz divām zīmēm"""
    _palaist(3, 6, "rezultati_3.txt")
    _parbaudit_saturu(
        "rezultati_3.txt",
        "1 V: 0.33 A\n"
        "2 V: 0.67 A\n"
        "3 V: 1.00 A\n"
        "4 V: 1.33 A\n"
        "5 V: 1.67 A\n"
        "6 V: 2.00 A\n",
    )


@check50.check(exists)
def one_voltage():
    """Pārbauda vienu sprieguma vērtību (U = 1 V)"""
    _palaist(4, 1, "viens.txt")
    _parbaudit_saturu("viens.txt", "1 V: 0.25 A\n")


@check50.check(exists)
def many_voltages():
    """Pārbauda tabulu ar 100 sprieguma vērtībām"""
    _palaist(8, 100, "simts.txt")
    sagaidamais = "".join(
        f"{spriegums} V: {spriegums / 8:.2f} A\n"
        for spriegums in range(1, 101)
    )
    _parbaudit_saturu("simts.txt", sagaidamais)


@check50.check(exists)
def overwrite():
    """Pārbauda, vai esoša izvaddatne tiek pārrakstīta"""
    Path("veca_datne.txt").write_text(
        "Iepriekšējie aprēķini, kurus jāaizstāj!\n",
        encoding="utf-8",
    )
    _palaist(2, 2, "veca_datne.txt")
    _parbaudit_saturu(
        "veca_datne.txt",
        "1 V: 0.50 A\n"
        "2 V: 1.00 A\n",
    )
