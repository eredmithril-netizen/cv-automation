"""
main.py
=======

Toto je HLAVNI SPOUSTECI soubor celeho projektu.
Kdyz chces program spustit, staci v terminalu napsat:

    python main.py

Tento soubor postupne:
1. Nacte tajne udaje (API klice) ze souboru .env.
2. Zavola scraper.py, aby stahl pracovni nabidky podle nastaveni
   v config.py.
3. (Zatim jen naznaceno) Vyhodnoti nabidky pomoci Anthropic API.
4. (Zatim jen naznaceno) Pripadne posle e-mail pres Gmail API (auth.py).

Poznamka: scraper.py je zatim jen kostra (placeholder), takze program
v tuto chvili jeste realne zadne nabidky nenajde - to je normalni,
doplni se to postupne.
"""

import os

from dotenv import load_dotenv

import config
from scraper import search_jobs

# ---------------------------------------------------------------------------
# 1. NACTENI TAJNYCH UDAJU ZE SOUBORU .env
# ---------------------------------------------------------------------------
# load_dotenv() precte soubor .env (pokud existuje) a nastavi jeho obsah
# jako tzv. promenne prostredi (environment variables). Diky tomu je pak
# muzeme cist pres os.getenv("JMENO_PROMENNE").
load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
GMAIL_USER = os.getenv("GMAIL_USER")


def check_env_variables():
    """
    Zkontroluje, ze jsou v .env vyplnene potrebne udaje.
    Pokud neco chybi, program na to upozorni, at uzivatel vi,
    co ma doplnit, misto aby program spadl s nesrozumitelnou chybou.
    """
    missing = []
    if not ANTHROPIC_API_KEY:
        missing.append("ANTHROPIC_API_KEY")
    if not GMAIL_USER:
        missing.append("GMAIL_USER")

    if missing:
        print("Pozor: v souboru .env chybi nasledujici hodnoty:")
        for name in missing:
            print(f"  - {name}")
        print("Doplň je do souboru .env podle vzoru v .env.example.")


def run():
    """
    Hlavni funkce, ktera spusti cely proces hledani nabidek.
    """
    print("=== CV Automation ===")
    print(f"Hledam pozice: {config.JOB_KEYWORDS}")
    print(f"V lokacich: {config.LOCATIONS}")
    print(f"Na webech: {list(config.SITES.keys())}")
    print()

    # Zavolame scraper - zatim vrati prazdny seznam, protoze scraper.py
    # je jen placeholder (viz komentare v tom souboru).
    listings = search_jobs()

    if not listings:
        print("Zatim nebyly nalezeny zadne nabidky.")
        print("(To je ocekavane - scraper.py jeste neobsahuje funkcni kod.)")
    else:
        print(f"Nalezeno {len(listings)} nabidek:")
        for job in listings:
            print(f"- {job}")

    # TODO: az bude scraper hotovy, tady se da doplnit:
    # - vyhodnoceni nabidek pres Anthropic API (potrebuje ANTHROPIC_API_KEY)
    # - odeslani souhrnneho e-mailu pres auth.get_gmail_service()


if __name__ == "__main__":
    # Tento blok se spusti jen kdyz soubor spoustis primo (python main.py),
    # ne kdyz ho nekdo jiny soubor jen importuje.
    check_env_variables()
    run()
