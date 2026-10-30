"""check50 pārbaudes uzdevumam p6struktura.py."""
from pathlib import Path
import check50
import re


def verify(filename, expected):
    process = check50.run("python3 p6struktura.py")
    process.stdout("Datne: ", regex=False).stdin(filename, prompt=False)
    pattern = r"\A" + "\n".join(re.escape(line) for line in expected.split("\n"))
    process.stdout(pattern, str_output=expected).stdout(check50.EOF).exit(0)


def report(total, ferits, perlits, cementits):
    result = f"Novērojumu skaits: {total}\n"
    for name, count in zip(("ferits", "perlits", "cementits"), (ferits, perlits, cementits)):
        result += f"{name}: {count} ({count / total * 100:.1f}%)\n"
    return result


@check50.check()
def exists():
    """Datne p6struktura.py eksistē."""
    check50.exists("p6struktura.py")


@check50.check(exists)
def example():
    """1. datne: 10 novērojumi, sadalījums 50.0%, 30.0%, 20.0%."""
    check50.include("p6struktura1.txt")
    verify("p6struktura1.txt", report(10, 5, 3, 2))


@check50.check(exists)
def whitespace():
    """2. datne: izlaiž tukšās rindas, noņem atstarpes, noapaļo procentus."""
    check50.include("p6struktura2.txt")
    verify("p6struktura2.txt", report(7, 1, 4, 2))


@check50.check(exists)
def absent_components():
    """3. datne: izvada arī sastāvdaļas ar nulles novērojumu skaitu."""
    check50.include("p6struktura3.txt")
    verify("p6struktura3.txt", report(4, 0, 0, 4))


@check50.check(exists)
def one_observation():
    """Pareizi apstrādā vienu novērojumu bez rindas beigu rakstzīmes."""
    Path("single.txt").write_text("perlits", encoding="utf-8")
    verify("single.txt", report(1, 0, 1, 0))


@check50.check(exists)
def thirds():
    """Katru trešdaļu izvada kā 33.3%; procentu summai nav jābūt 100.0%."""
    Path("thirds.txt").write_text("cementits\nferits\nperlits\n", encoding="utf-8")
    verify("thirds.txt", report(3, 1, 1, 1))


@check50.check(exists)
def empty():
    """Tukšai datnei izvada tikai 'Nav novērojumu.'."""
    Path("empty.txt").write_text("", encoding="utf-8")
    verify("empty.txt", "Nav novērojumu.\n")


@check50.check(exists)
def blank_lines():
    """Datnei ar tikai tukšām rindām un atstarpēm izvada 'Nav novērojumu.'."""
    Path("blank.txt").write_text("\n  \n\t\n \t \n", encoding="utf-8")
    verify("blank.txt", "Nav novērojumu.\n")


@check50.check(exists)
def missing():
    """Neeksistējošai datnei izvada tikai 'Datne nav atrasta.'."""
    Path("missing_input.txt").unlink(missing_ok=True)
    verify("missing_input.txt", "Datne nav atrasta.\n")


@check50.check(exists)
def different_filename():
    """Nolasa lietotāja norādīto datni un apstrādā lielāku novērojumu skaitu."""
    Path("other_input.txt").write_text(
        "cementits\n" * 17 + "ferits\n" * 23 + "perlits\n" * 11,
        encoding="utf-8",
    )
    verify("other_input.txt", report(51, 23, 11, 17))
