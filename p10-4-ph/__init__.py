"""check50 pārbaudes uzdevumam p10-4-ph."""

import json
from pathlib import Path

import check50


def _parbaudit(ievaddatne, rindas):
    """Pārbauda klasifikācijas un grupu skaitu noteiktā secībā."""
    parbaude = check50.run("python3 p10-4-ph.py").stdin(ievaddatne, prompt=False)
    for rinda in rindas:
        parbaude = parbaude.stdout(rinda, regex=False)
    parbaude.exit(0)


@check50.check()
def exists():
    """Pārbauda, vai p10-4-ph.py eksistē"""
    check50.exists("p10-4-ph.py")


@check50.check(exists)
def example():
    """Pārbauda pirmo JSON datni un uzdevuma piemēru"""
    _parbaudit("p10-4-ph1.json", [
        "Citronu sula: skābs",
        "Tīrs ūdens: neitrāls",
        "Sodas šķīdums: bāzisks",
        "Ziepjūdens: bāzisks",
        "Skābi šķīdumi: 1",
        "Neitrāli šķīdumi: 1",
        "Bāziski šķīdumi: 2",
    ])


@check50.check(exists)
def second_file():
    """Pārbauda otro JSON datni: vairāk šķīdumu un pH robežvērtības"""
    _parbaudit("p10-4-ph2.json", [
        "Kuņģa sula: skābs",
        "Etiķis: skābs",
        "Kafija: skābs",
        "Lietusūdens: skābs",
        "Neitrāls paraugs: neitrāls",
        "Destilēts ūdens: neitrāls",
        "Jūras ūdens: bāzisks",
        "Dzeramās sodas šķīdums: bāzisks",
        "Amonjaka šķīdums: bāzisks",
        "Stipri bāzisks paraugs: bāzisks",
        "Stipri skābs paraugs: skābs",
        "Skābi šķīdumi: 5",
        "Neitrāli šķīdumi: 2",
        "Bāziski šķīdumi: 4",
    ])


@check50.check(exists)
def boundary_values():
    """Pārbauda pH vērtības abpus neitrālajai robežai"""
    Path("robezas.json").write_text(json.dumps({
        "Zem septiņi": 6.99,
        "Precīzi septiņi": 7,
        "Virs septiņi": 7.01,
    }, ensure_ascii=False), encoding="utf-8")
    _parbaudit("robezas.json", [
        "Zem septiņi: skābs",
        "Precīzi septiņi: neitrāls",
        "Virs septiņi: bāzisks",
        "Skābi šķīdumi: 1",
        "Neitrāli šķīdumi: 1",
        "Bāziski šķīdumi: 1",
    ])


@check50.check(exists)
def only_neutral():
    """Pārbauda datni, kur visi šķīdumi ir neitrāli"""
    Path("neitrali.json").write_text(json.dumps({
        "Pirmais": 7, "Otrais": 7.0
    }, ensure_ascii=False), encoding="utf-8")
    _parbaudit("neitrali.json", [
        "Pirmais: neitrāls",
        "Otrais: neitrāls",
        "Skābi šķīdumi: 0",
        "Neitrāli šķīdumi: 2",
        "Bāziski šķīdumi: 0",
    ])


@check50.check(exists)
def empty_object():
    """Pārbauda tukšu JSON vārdnīcu"""
    Path("tukss.json").write_text("{}\n", encoding="utf-8")
    _parbaudit("tukss.json", [
        "Skābi šķīdumi: 0",
        "Neitrāli šķīdumi: 0",
        "Bāziski šķīdumi: 0",
    ])


@check50.check(exists)
def missing_file():
    """Pārbauda neeksistējošu ievaddatni"""
    nosaukums = "neeksistejosa_ph_datne_123456789.json"
    Path(nosaukums).unlink(missing_ok=True)
    check50.run("python3 p10-4-ph.py") \
        .stdin(nosaukums, prompt=False) \
        .stdout("Datne nav atrasta.", regex=False) \
        .exit(0)
