# Roadmapa – CV Automation

Tento dokument popisuje, v jakém pořadí a co je potřeba udělat, aby byl projekt plně funkční. Slouží jako plán do budoucna – co je hotové a co ještě chybí.

## Fáze 1: Základ projektu (hotovo)

- [x] README.md s popisem projektu a návodem k instalaci
- [x] .gitignore (ochrana tajných údajů)
- [x] requirements.txt se všemi potřebnými knihovnami
- [x] config.py s nastavením (klíčová slova, lokace, weby)
- [x] .env.example jako vzor pro tajné údaje
- [x] auth.py – funkční Google OAuth2 přihlášení ke Gmailu
- [x] scraper.py – zatím jen kostra (placeholder)
- [x] main.py – vstupní bod aplikace

## Fáze 2: Funkční scraper (další krok)

- [ ] Implementovat `fetch_page()` v scraper.py – reálné stažení stránky přes `requests`
- [ ] Implementovat `parse_job_listings()` pro jobs.cz (najít strukturu HTML, vytáhnout pozici, firmu, lokaci, odkaz)
- [ ] Implementovat `parse_job_listings()` pro prace.cz (stejné, jiná struktura webu)
- [ ] Sestavit vyhledávací URL adresy podle klíčových slov a lokace z config.py
- [ ] Otestovat `search_jobs()` na reálných datech

## Fáze 3: Vyhodnocení nabídek pomocí Claude (Anthropic API)

- [ ] Vytvořit nový soubor `evaluator.py`
- [ ] Načíst text vlastního CV (např. jako .txt nebo .pdf)
- [ ] Pro každou nalezenou nabídku poslat dotaz na Claude: „Jak dobře se tato nabídka hodí k tomuto CV?“
- [ ] Nechat Claude vrátit skóre shody (např. 0–100) a krátké zdůvodnění
- [ ] Seřadit nabídky podle skóre

## Fáze 4: Odesílání e-mailů (Gmail API)

- [x] auth.py – přihlášení ke Gmailu je hotové
- [ ] Napsat funkci `send_summary_email()`, která sestaví a odešle e-mail se souhrnem nejlepších nabídek
- [ ] Vytvořit jednoduchou HTML šablonu e-mailu (přehlednější než čistý text)
- [ ] Propojit s `main.py`, aby se e-mail posílal automaticky po každém běhu

## Fáze 5: Automatizace a plánování

- [ ] Použít knihovnu `schedule` pro pravidelné spouštění (např. jednou denně)
- [ ] Přidat logování do souboru (aby šlo zpětně zkontrolovat, co program dělal a kdy)
- [ ] Ošetřit chyby tak, aby jeden neúspěšný web nezastavil celý běh

## Fáze 6: Vylepšení a ladění

- [ ] Ukládat historii už viděných nabídek (aby se stejná nabídka neposílala vícekrát)
- [ ] Přidat filtr podle mzdy / typu úvazku, pokud to weby nabízí
- [ ] Napsat základní testy (např. pomocí `pytest`) pro parsování a vyhodnocování
- [ ] Zvážit jednoduché webové rozhraní pro prohlížení nalezených nabídek

## Poznámka

Fáze jsou navržené tak, aby na sebe navazovaly – nejdřív funkční scraper (Fáze 2), pak teprve vyhodnocování (Fáze 3) a odesílání (Fáze 4). Klidně ale postupuj i jinak podle toho, co je zrovna potřeba nejvíc.
