"""
auth.py
=======

Tento soubor resi prihlaseni k tvemu Google (Gmail) uctu pomoci
tzv. OAuth2 - to je bezpecny zpusob, jak aplikaci povolit pristup
ke tvemu uctu BEZ toho, aby aplikace znala tvoje heslo.

Jak to funguje ve zkratce:
1. Poprve se otevre okno prohlizece, kde se prihlasis a odsouhlasis
   pristup pro tuto aplikaci.
2. Google vrati "token" (dlouhy bezpecnostni kod), ktery se ulozi
   do souboru token.pickle na tvem pocitaci.
3. Priste uz se program podiva do token.pickle a prihlasi se
   automaticky, bez nutnosti znovu otevirat prohlizec.

Soubory, ktere tento kod potrebuje:
- credentials.json - stahnes z Google Cloud Console (viz README.md)
- token.pickle - vytvori se automaticky po prvnim prihlaseni

Oba soubory jsou v .gitignore, protoze obsahuji citliva udaje.
"""

import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# ---------------------------------------------------------------------------
# NASTAVENI
# ---------------------------------------------------------------------------

# "Scopes" = rozsah opravneni, o ktera si program rekne Googlu.
# "gmail.send" znamena: program smi POSILAT e-maily z tveho uctu,
# ale nesmi je cist ani mazat. Je dobre davat vzdy jen minimalni
# potrebna opravneni.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]

# Cesta k souboru stazenemu z Google Cloud Console.
CREDENTIALS_FILE = "credentials.json"

# Cesta k souboru, kam se ulozi prihlasovaci token po prvnim prihlaseni.
TOKEN_FILE = "token.pickle"


def load_credentials():
    """
    Zkusi nacist uz ulozene prihlasovaci udaje (token) ze souboru
    token.pickle, pokud existuje.

    Vraci:
        Objekt s prihlasovacimi udaji (Credentials), nebo None,
        pokud soubor token.pickle jeste neexistuje (typicky pri
        uplne prvnim spusteni programu).
    """
    if os.path.exists(TOKEN_FILE):
        # "rb" = read binary - soubor token.pickle neni citelny text,
        # je to binarni format, proto ho cteme jinak nez napr. .txt
        with open(TOKEN_FILE, "rb") as token_file:
            credentials = pickle.load(token_file)
        return credentials
    return None


def save_token(credentials):
    """
    Ulozi prihlasovaci udaje (token) do souboru token.pickle,
    aby se priste nemusel uzivatel znovu prihlasovat pres prohlizec.

    Parametry:
        credentials: prihlasovaci objekt ziskany od Google OAuth flow
    """
    # "wb" = write binary - zapisujeme binarni data, ne obycejny text
    with open(TOKEN_FILE, "wb") as token_file:
        pickle.dump(credentials, token_file)


def authenticate():
    """
    Hlavni funkce, ktera zajisti, ze mame platne prihlaseni k Google uctu.

    Postup:
    1. Zkusi nacist existujici token (load_credentials).
    2. Pokud token neexistuje, nebo vyprsel a nejde obnovit,
       spusti se prihlasovaci flow (otevre se okno prohlizece).
    3. Nove ziskany token se ulozi pro priste (save_token).

    Vraci:
        Platny objekt prihlasovacich udaju (Credentials), ktery se
        da pouzit pro komunikaci s Gmail API.
    """
    credentials = load_credentials()

    # Pokud zadny token nemame, NEBO je token neplatny/vyprsely...
    if not credentials or not credentials.valid:
        # ... ale da se obnovit pomoci "refresh tokenu" bez noveho prihlaseni
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            # Jinak musime uzivatele nechat prihlasit se znovu od zacatku.
            # InstalledAppFlow otevre okno prohlizece s Google prihlasenim.
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            credentials = flow.run_local_server(port=0)

        # Ulozime nove ziskany/obnoveny token, at se priste nemusime
        # prihlasovat znovu.
        save_token(credentials)

    return credentials


def get_gmail_service():
    """
    Vytvori a vrati pripraveny objekt pro komunikaci s Gmail API.

    Tento objekt (tzv. "service") se pak pouziva k realnym akcim,
    napr. odeslani e-mailu.

    Vraci:
        Objekt Gmail service, se kterym se da rovnou pracovat, napr.:

            service = get_gmail_service()
            service.users().messages().send(...)
    """
    credentials = authenticate()

    # build() vytvori objekt pro praci s konkretnim Google API.
    # "gmail" = jmeno API, "v1" = verze API.
    service = build("gmail", "v1", credentials=credentials)
    return service


# ---------------------------------------------------------------------------
# Rucni test tohoto souboru
# ---------------------------------------------------------------------------
# Pokud tento soubor spustis primo (python auth.py), spusti se prihlasovaci
# flow a overi se, ze prihlaseni funguje. Pri importu z jineho souboru
# (napr. main.py) se tento blok NESPUSTI.
if __name__ == "__main__":
    print("Zkousim se prihlasit ke Google uctu...")
    gmail_service = get_gmail_service()
    print("Prihlaseni probehlo uspesne! Gmail service je pripraveny k pouziti.")
