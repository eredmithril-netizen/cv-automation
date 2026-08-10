# CV Automation

Automatizovaný nástroj, který:

1. Prochází pracovní portály (jobs.cz, prace.cz) a hledá pracovní nabídky podle zadaných klíčových slov a lokací.
2. Pomocí Anthropic API (Claude) vyhodnotí, jak moc se nabídka hodí k tvému CV.
3. Přes Gmail API umí odeslat e-mail (např. shrnutí nalezených nabídek nebo motivační dopis).

Projekt je zamýšlený jako **rozjezd/kostra** – scraper.py je zatím jen placeholder s komentáři, kam co doplnit.

## Struktura projektu

```
cv-automation/
├── README.md              - tento soubor
├── .gitignore              - co se nemá nahrávat do gitu
├── requirements.txt         - seznam Python knihoven
├── config.py                - nastavení (klíčová slova, lokace, weby)
├── .env.example               - vzor pro tajné údaje (API klíče apod.)
├── auth.py                    - přihlášení ke Google účtu (Gmail API)
├── scraper.py                  - stahování nabídek z webů (zatím prázdné)
└── main.py                      - hlavní spouštěcí soubor
```

## Závislosti (knihovny)

Projekt používá tyto Python knihovny (jsou i v `requirements.txt`):

- `requests` - stahování webových stránek přes HTTP
- `beautifulsoup4` - parsování (čtení) HTML stránek, hledání dat v nich
- `anthropic==0.28.0` - oficiální knihovna pro Claude API (přesně tato verze kvůli kompatibilitě)
- `google-auth-oauthlib` - přihlašovací (OAuth2) flow pro Google
- `google-auth-httplib2` - pomocná knihovna pro Google API komunikaci
- `google-api-python-client` - samotné volání Google API (např. Gmail)
- `python-dotenv` - načítání proměnných z `.env` souboru (API klíče atd.)
- `schedule` - spouštění úkolů podle časového plánu (např. "každý den v 8:00")

## Instalace (krok za krokem)

Tohle je návod pro úplného začátečníka, klidně choď postupně bod po bodu.

### 1. Nainstaluj Python

Ověř, že máš Python 3.9 nebo novější. V terminálu (příkazová řádka) napiš:

```bash
python3 --version
```

Pokud Python nemáš, stáhni si ho z https://www.python.org/downloads/

### 2. Vytvoř si virtuální prostředí (doporučeno)

Virtuální prostředí = izolovaný "sáček" na knihovny jen pro tento projekt, aby se nemíchaly s jinými projekty.

```bash
cd cv-automation
python3 -m venv venv
```

Aktivace prostředí:

- macOS / Linux: `source venv/bin/activate`
- Windows: `venv\Scripts\activate`

Po aktivaci by se ti na začátku řádku v terminálu mělo objevit `(venv)`.

### 3. Nainstaluj knihovny

```bash
pip install -r requirements.txt
```

### 4. Nastav si tajné údaje (.env)

Zkopíruj vzorový soubor a přejmenuj ho:

```bash
cp .env.example .env
```

Otevři `.env` v editoru a doplň skutečné hodnoty:

```
ANTHROPIC_API_KEY=sk-ant-...tvůj-klíč...
GMAIL_USER=tvuj@email.com
```

Anthropic API klíč získáš na https://console.anthropic.com/

Soubor `.env` se **nikdy** nenahrává do gitu (je v `.gitignore`), protože obsahuje tajné údaje.

### 5. Nastav Google OAuth2 (pro Gmail)

Aby program mohl posílat e-maily za tebe, potřebuje povolení od Googlu:

1. Jdi na https://console.cloud.google.com/
2. Vytvoř nový projekt (nebo použij existující).
3. Zapni "Gmail API" (Library → vyhledej "Gmail API" → Enable).
4. Vytvoř OAuth2 přihlašovací údaje (Credentials → Create Credentials → OAuth client ID → typ "Desktop app").
5. Stáhni vygenerovaný JSON soubor a ulož ho do složky projektu pod jménem `credentials.json`.

Tento soubor je také v `.gitignore` a nikam se nesdílí.

### 6. Spusť program

```bash
python main.py
```

Při prvním spuštění se ti pravděpodobně otevře prohlížeč, kde se přihlásíš ke Google účtu a povolíš přístup. Po přihlášení se vytvoří soubor `token.pickle`, který si přihlášení "pamatuje", takže příště se už prohlížeč otevírat nebude.

## Poznámka

`scraper.py` je zatím jen kostra s komentáři – neobsahuje funkční kód pro stahování nabídek. Slouží jako místo, kam se bude logika postupně doplňovat.
