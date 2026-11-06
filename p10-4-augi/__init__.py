import csv
from pathlib import Path

import check50

GALVENE = ["augs", "masa_sakuma_g", "masa_beigas_g", "izmaina_g"]


def parbaudit_csv(nosaukums, gaiditas_rindas):
    """Pārbauda gan kolonnu secību, gan visas CSV vērtības."""
    cels = Path(nosaukums)
    if not cels.is_file():
        raise check50.Failure(f"Nav izveidota datne {nosaukums}.")
    with cels.open("r", encoding="utf-8-sig", newline="") as datne:
        rindas = list(csv.reader(datne))
    gaiditas = [GALVENE] + gaiditas_rindas
    if rindas != gaiditas:
        raise check50.Failure(
            f"Nepareizs saturs datnē {nosaukums}. "
            f"Sagaidīts: {gaiditas!r}; saņemts: {rindas!r}"
        )


@check50.check()
def exists():
    """Pārbauda, vai p10-4-augi.py eksistē"""
    check50.exists("p10-4-augi.py")


@check50.check(exists)
def example():
    """Pārbauda piemēra datni un pozitīvu, negatīvu, nulles izmaiņu"""
    check50.include("p10-4-augi1.csv")
    check50.run("python3 p10-4-augi.py") \
        .stdin("p10-4-augi1.csv").stdin("rez1.csv") \
        .stdout("Rezultāti saglabāti.").exit(0)
    parbaudit_csv("rez1.csv", [
        ["Pupina", "12.0", "14.5", "2.5"],
        ["Zirnis", "8.5", "7.0", "-1.5"],
        ["Saulene", "10.0", "10.0", "0.0"],
    ])


@check50.check(exists)
def second_file():
    """Pārbauda otro ievaddatni un visu augu secību"""
    check50.include("p10-4-augi2.csv")
    check50.run("python3 p10-4-augi.py") \
        .stdin("p10-4-augi2.csv").stdin("rez2.csv") \
        .stdout("Rezultāti saglabāti.").exit(0)
    parbaudit_csv("rez2.csv", [
        ["Ozols", "120.2", "125.8", "5.5"],
        ["Priede", "40.0", "35.9", "-4.1"],
        ["Berzs", "12.0", "12.1", "0.0"],
        ["Kaktuss", "9.8", "9.8", "0.0"],
        ["Pupina", "0.0", "0.3", "0.3"],
        ["Kvieši", "21.5", "21.0", "-0.5"],
        ["Egle", "1000.0", "1001.2", "1.2"],
        ["Paparde", "7.5", "6.0", "-1.5"],
        ["Auzas", "0.0", "0.1", "0.0"],
        ["Liepa", "18.9", "19.0", "0.1"],
    ])


@check50.check(exists)
def one_row():
    """Pārbauda CSV datni ar vienu augu"""
    with open("viens.csv", "w", encoding="utf-8", newline="") as datne:
        rakstitajs = csv.writer(datne)
        rakstitajs.writerow(GALVENE[:3])
        rakstitajs.writerow(["Lapa", "2", "3.5"])
    check50.run("python3 p10-4-augi.py") \
        .stdin("viens.csv").stdin("viens_rez.csv") \
        .stdout("Rezultāti saglabāti.").exit(0)
    parbaudit_csv("viens_rez.csv", [["Lapa", "2.0", "3.5", "1.5"]])


@check50.check(exists)
def rounding():
    """Pārbauda, ka visām masām ir tieši viena decimālzīme"""
    with open("decimali.csv", "w", encoding="utf-8", newline="") as datne:
        rakstitajs = csv.writer(datne)
        rakstitajs.writerow(GALVENE[:3])
        rakstitajs.writerow(["A", "1", "2.34"])
        rakstitajs.writerow(["B", "1.25", "2.75"])
    check50.run("python3 p10-4-augi.py") \
        .stdin("decimali.csv").stdin("dec_rez.csv") \
        .stdout("Rezultāti saglabāti.").exit(0)
    parbaudit_csv("dec_rez.csv", [
        ["A", "1.0", "2.3", "1.3"],
        ["B", "1.2", "2.8", "1.5"],
    ])


@check50.check(exists)
def overwrite():
    """Pārbauda esošas izvaddatnes pārrakstīšanu"""
    check50.include("p10-4-augi1.csv")
    Path("pars.csv").write_text("VECS SATURS\n", encoding="utf-8")
    check50.run("python3 p10-4-augi.py") \
        .stdin("p10-4-augi1.csv").stdin("pars.csv") \
        .stdout("Rezultāti saglabāti.").exit(0)
    parbaudit_csv("pars.csv", [
        ["Pupina", "12.0", "14.5", "2.5"],
        ["Zirnis", "8.5", "7.0", "-1.5"],
        ["Saulene", "10.0", "10.0", "0.0"],
    ])


@check50.check(exists)
def missing():
    """Pārbauda neeksistējošu datni un izvaddatnes neveidošanu"""
    neeksiste = Path("nav_tadas_ieejas_87392.csv")
    if neeksiste.exists():
        neeksiste.unlink()
    rezultats = Path("nedrikst_izveidot.csv")
    if rezultats.exists():
        rezultats.unlink()
    check50.run("python3 p10-4-augi.py") \
        .stdin(str(neeksiste)).stdin(str(rezultats)) \
        .stdout("Datne nav atrasta.").exit(0)
    if rezultats.exists():
        raise check50.Failure("Ja ievaddatne nav atrasta, izvaddatni nedrīkst veidot.")
