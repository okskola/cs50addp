"""Automatizētas p6sieti.py pārbaudes; CSV salīdzina pēc šūnu satura."""
# Veidots ar  ChatGPT
import csv
import re
from pathlib import Path
import check50

HEADER = ["siets_um", "masa_g", "masas_procents"]


def run_program(source, destination, expected):
    process = check50.run("python3 p6sieti.py")
    process.stdout(r"\AIevaddatne: ").stdin(source, prompt=False)
    process.stdout(r"\AIzvaddatne: ").stdin(destination, prompt=False)
    pattern = r"\A" + "\n".join(re.escape(line) for line in expected.split("\n"))
    process.stdout(pattern, str_output=expected).stdout(check50.EOF).exit(0)


def read_csv(filename):
    path = Path(filename)
    if not path.is_file():
        raise check50.Failure(f"Nav izveidota izvaddatne {filename}.")
    try:
        with path.open(encoding="utf-8", newline="") as file:
            return list(csv.reader(file))
    except (UnicodeError, csv.Error) as error:
        raise check50.Failure("Izvaddatne nav derīgs UTF-8 CSV.") from error


def expect_csv(filename, expected):
    actual = read_csv(filename)
    if actual != expected:
        raise check50.Mismatch(str(expected), str(actual),
                               help="Pārbaudi galveni, rindu secību, vērtības un vienu decimālzīmi.")


def success(source, destination, total, rows):
    before = Path(source).read_bytes()
    run_program(source, destination,
                f"Kopējā masa: {total} g\nRezultāti saglabāti.\n")
    expect_csv(destination, [HEADER] + rows)
    if Path(source).read_bytes() != before:
        raise check50.Failure("Programma mainīja ievaddatni.")


def error_case(source, message, preserve=False):
    destination = Path("error_output.csv")
    sentinel = b"original,data\r\nkeep,unchanged\r\n"
    if preserve:
        destination.write_bytes(sentinel)
    else:
        destination.unlink(missing_ok=True)
    run_program(source, str(destination), message + "\n")
    if preserve:
        if not destination.is_file() or destination.read_bytes() != sentinel:
            raise check50.Failure("Kļūdas gadījumā esošā izvaddatne ir mainīta vai dzēsta.")
    elif destination.exists():
        raise check50.Failure("Kļūdas gadījumā izvaddatni nedrīkst izveidot.")


@check50.check()
def exists():
    """Datne p6sieti.py eksistē."""
    check50.exists("p6sieti.py")


@check50.check(exists)
def example():
    """1. datne: pareiza termināļa izvade un CSV saturs."""
    check50.include("p6sieti1.csv")
    success("p6sieti1.csv", "result.csv", "50.0", [
        ["500", "6.0", "12.0"], ["250", "14.0", "28.0"],
        ["125", "22.5", "45.0"], ["0", "7.5", "15.0"]])


@check50.check(exists)
def fractions_and_order():
    """2. datne: daļskaitļi, nulles frakcija un sākotnējā rindu secība."""
    check50.include("p6sieti2.csv")
    success("p6sieti2.csv", "fraction_result.csv", "7.5", [
        ["250", "2.2", "29.9"], ["1000", "0.0", "0.0"],
        ["0", "0.8", "10.1"], ["500", "4.5", "60.0"]])


@check50.check(exists)
def zero_total():
    """3. datne: nulles kopējā masa, izvaddatni neveido."""
    check50.include("p6sieti3.csv")
    error_case("p6sieti3.csv", "Nav datu aprēķinam.")


@check50.check(exists)
def single_row():
    """Viena frakcija veido 100.0%; nolasa arī rindu bez beigu rakstzīmes."""
    Path("single.csv").write_text("siets_um,masa_g\n63,4.6", encoding="utf-8")
    success("single.csv", "single_out.csv", "4.6", [["63", "4.6", "100.0"]])


@check50.check(exists)
def rounding():
    """Trešdaļas izvada kā 33.3%, neveicot procentu summas korekciju."""
    Path("thirds.csv").write_text("siets_um,masa_g\n500,1\n250,1\n0,1\n", encoding="utf-8")
    success("thirds.csv", "thirds_out.csv", "3.0", [
        ["500", "1.0", "33.3"], ["250", "1.0", "33.3"], ["0", "1.0", "33.3"]])


@check50.check(exists)
def no_early_rounding():
    """Aprēķinos izmanto nenoapaļotas masas."""
    Path("precise.csv").write_text("siets_um,masa_g\n500,0.14\n0,0.26\n", encoding="utf-8")
    success("precise.csv", "precise_out.csv", "0.4", [
        ["500", "0.1", "35.0"], ["0", "0.3", "65.0"]])


@check50.check(exists)
def header_only():
    """Datnei tikai ar galveni izvada kļūdas paziņojumu un neveido CSV."""
    Path("header.csv").write_text("siets_um,masa_g\n", encoding="utf-8")
    error_case("header.csv", "Nav datu aprēķinam.")


@check50.check(exists)
def missing_input():
    """Neeksistējoša ievaddatne: pareizs paziņojums, izvaddatnes nav."""
    Path("missing.csv").unlink(missing_ok=True)
    error_case("missing.csv", "Datne nav atrasta.")


@check50.check(exists)
def overwrite_output():
    """Sekmīgā gadījumā esošo izvaddatni pārraksta, nevis papildina."""
    Path("new.csv").write_text("siets_um,masa_g\n0,8\n", encoding="utf-8")
    Path("existing.csv").write_text("old,header\n" + "old,row\n" * 30, encoding="utf-8")
    success("new.csv", "existing.csv", "8.0", [["0", "8.0", "100.0"]])


@check50.check(exists)
def preserve_on_errors():
    """Visos trīs kļūdu gadījumos esošo izvaddatni saglabā nemainītu."""
    Path("missing.csv").unlink(missing_ok=True)
    error_case("missing.csv", "Datne nav atrasta.", preserve=True)
    Path("header.csv").write_text("siets_um,masa_g\n", encoding="utf-8")
    error_case("header.csv", "Nav datu aprēķinam.", preserve=True)
    check50.include("p6sieti3.csv")
    error_case("p6sieti3.csv", "Nav datu aprēķinam.", preserve=True)


@check50.check(exists)
def supplied_paths():
    """Izmanto ievadītos datņu nosaukumus, arī nosaukumus ar atstarpēm."""
    Path("citi dati.csv").write_text("siets_um,masa_g\n710,6\n0,2\n", encoding="utf-8")
    success("citi dati.csv", "citi rezultati.csv", "8.0", [
        ["710", "6.0", "75.0"], ["0", "2.0", "25.0"]])
