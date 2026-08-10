"""
scraper.py
==========

TOTO JE ZATIM JEN PLACEHOLDER (kostra bez funkcniho kodu).

Ucel tohoto souboru: stahovat pracovni nabidky z webovych portalu
(jobs.cz, prace.cz - viz config.py) podle zadanych klicovych slov
a lokaci, a vracet je jako prehledny seznam, se kterym muze dal
pracovat main.py (napr. je poslat Claude API k vyhodnoceni, nebo
poslat e-mailem pres auth.py).

Nize jsou jen NAVRHY funkci a komentare, co by mely delat.
Skutecna logika (stahovani stranek, hledani dat v HTML) tady
zatim chybi a je potreba ji doplnit.
"""

# import requests                # pro stazeni obsahu webove stranky (HTTP pozadavek)
# from bs4 import BeautifulSoup  # pro "prohrabani" se stazenym HTML a najiti dat

from config import JOB_KEYWORDS, LOCATIONS, SITES, MAX_RESULTS_PER_SITE


def fetch_page(url):
    """
    PLACEHOLDER - zatim nic nedela.

    V budoucnu by tato funkce mela:
    1. Poslat HTTP pozadavek na danou URL adresu pomoci knihovny requests
       (napr. requests.get(url)).
    2. Zkontrolovat, ze se stranka stahla v poradku (status_code == 200).
    3. Vratit text stazene HTML stranky, aby se dal dal zpracovat.

    Parametry:
        url (str): adresa stranky, kterou chceme stahnout

    Vraci:
        str: HTML obsah stranky (zatim jen prazdny text)
    """
    # TODO: doplnit skutecne stazeni stranky pres requests.get(url)
    raise NotImplementedError("fetch_page zatim neni implementovano")


def parse_job_listings(html_content, site_name):
    """
    PLACEHOLDER - zatim nic nedela.

    V budoucnu by tato funkce mela:
    1. Vzit stazene HTML (vystup z fetch_page).
    2. Pomoci BeautifulSoup najit v HTML jednotlive pracovni nabidky
       (napr. podle CSS trid/elementu specifickych pro dany web).
    3. Pro kazdou nabidku vytahnout dulezite udaje - nazev pozice,
       firmu, lokaci, odkaz na detail nabidky, pripadne mzdu.
    4. Vratit seznam nabidek jako seznam slovniku (dictionaries), napr.:

           [
               {
                   "title": "Python Developer",
                   "company": "Firma s.r.o.",
                   "location": "Prague",
                   "url": "https://www.jobs.cz/nabidka/12345",
               },
               ...
           ]

    Parametry:
        html_content (str): HTML obsah stranky (vystup z fetch_page)
        site_name (str): jmeno webu, ze ktereho HTML pochazi (kvuli
                          tomu, ze ruzne weby maji ruznou strukturu HTML)

    Vraci:
        list[dict]: seznam nalezenych nabidek (zatim prazdny seznam)
    """
    # TODO: doplnit skutecne parsovani HTML pomoci BeautifulSoup
    # Poznamka: kazdy web (jobs.cz, prace.cz) bude mit jinou strukturu
    # HTML, takze tady bude pravdepodobne potreba rozlisit podle site_name.
    raise NotImplementedError("parse_job_listings zatim neni implementovano")


def search_jobs(keywords=None, locations=None):
    """
    PLACEHOLDER - hlavni funkce, kterou bude volat main.py.

    V budoucnu by tato funkce mela:
    1. Projit vsechny weby definovane v config.SITES.
    2. Pro kazdou kombinaci klicove slovo + lokace sestavit URL
       adresu pro vyhledavani (u kazdeho webu bude format adresy jiny).
    3. Zavolat fetch_page() pro stazeni vysledku hledani.
    4. Zavolat parse_job_listings() pro vytazeni jednotlivych nabidek.
    5. Spojit vsechny nalezene nabidky do jednoho seznamu a vratit ho.

    Parametry:
        keywords (list[str], volitelne): klicova slova k hledani.
            Pokud neni zadano, pouziji se hodnoty z config.JOB_KEYWORDS.
        locations (list[str], volitelne): lokace k hledani.
            Pokud neni zadano, pouziji se hodnoty z config.LOCATIONS.

    Vraci:
        list[dict]: seznam vsech nalezenych pracovnich nabidek
                     (zatim prazdny seznam, protoze funkce neni hotova)
    """
    keywords = keywords or JOB_KEYWORDS
    locations = locations or LOCATIONS

    all_listings = []

    # TODO: az budou fetch_page a parse_job_listings hotove, doplnit
    # skutecnou smycku, napr.:
    #
    # for site_name, base_url in SITES.items():
    #     for keyword in keywords:
    #         for location in locations:
    #             search_url = build_search_url(base_url, keyword, location)
    #             html = fetch_page(search_url)
    #             listings = parse_job_listings(html, site_name)
    #             all_listings.extend(listings[:MAX_RESULTS_PER_SITE])

    return all_listings


# ---------------------------------------------------------------------------
# Rucni test tohoto souboru
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("scraper.py je zatim jen placeholder - zadna funkce neni implementovana.")
    print(f"Nakonfigurovana klicova slova: {JOB_KEYWORDS}")
    print(f"Nakonfigurovane lokace: {LOCATIONS}")
    print(f"Nakonfigurovane weby: {list(SITES.keys())}")
