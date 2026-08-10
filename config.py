"""
config.py
=========

Tady se nastavuje ZADANI pro hledani pracovnich nabidek.
Nic se tady nespousti, jsou tu jen promenne (nastaveni), ktere si
ostatni soubory (scraper.py, main.py) odsud "pujci" (naimportuji).

Pokud chces zmenit, co program hleda, uprav hodnoty nize -
nemusis sahat do zadneho jineho souboru.
"""

# ---------------------------------------------------------------------------
# KLICOVA SLOVA PRO POZICE
# ---------------------------------------------------------------------------
# Seznam pracovnich pozic/oboru, ktere program bude na portalech hledat.
# Je to obycejny seznam textovych retezcu (stringu) v hranatych zavorkach.
# Klidne pridej/uber polozky - staci zachovat format "text" a carku mezi nimi.
JOB_KEYWORDS = [
    "Python Developer",
    "AI Engineer",
    "Fintech",
]

# ---------------------------------------------------------------------------
# LOKACE
# ---------------------------------------------------------------------------
# Kde ma program nabidky hledat. "Remote" znamena praci na dalku.
LOCATIONS = [
    "Prague",
    "Remote",
]

# ---------------------------------------------------------------------------
# WEBY (JOB PORTALY), KTERE SE MAJI PROHLEDAVAT
# ---------------------------------------------------------------------------
# Slovnik (dictionary) = pary "klic: hodnota". Klic je kratky nazev webu,
# hodnota je jeho skutecna URL adresa. Scraper.py bude podle tohoto
# slovniku vedet, kam se ma pripojit.
SITES = {
    "jobs.cz": "https://www.jobs.cz",
    "prace.cz": "https://www.prace.cz",
}

# ---------------------------------------------------------------------------
# DALSI NASTAVENI (volitelne, pro budouci rozsireni)
# ---------------------------------------------------------------------------
# Kolik nabidek maximalne stahnout z jednoho webu za jedno spusteni.
MAX_RESULTS_PER_SITE = 20

# Jak casto (v hodinach) se ma hledani automaticky opakovat,
# pokud bude program bezet na pozadi s knihovnou "schedule".
RUN_EVERY_HOURS = 24
