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

## Fáze 2: Funkční scraper (rozpracováno)

- [x] Prozkoumat strukturu jobs.cz (viz poznámky níže)
- [x] Prozkoumat strukturu prace.cz (viz poznámky níže)
- [ ] Implementovat `fetch_page()` v scraper.py – reálné stažení stránky přes `requests`
- [ ] Implementovat `parse_job_listings()` pro jobs.cz (najít strukturu HTML, vytáhnout pozici, firmu, lokaci, odkaz)
- [ ] Implementovat `parse_job_listings()` pro prace.cz (stejné, jiná struktura webu)
- [ ] Sestavit vyhledávací URL adresy podle klíčových slov a lokace z config.py
- [ ] Otestovat `search_jobs()` na reálných datech

### Poznámky z výzkumu (pro pokračování)

**jobs.cz**

- Vyhledávací URL: `https://www.jobs.cz/prace/{lokace-slug}/?q[]={klíčové slovo}` (např. `praha` pro Prahu)
- Pro "Remote" nefiltruje se přes lokaci ve URL, ale přes parametr `remote[]=1` bez lokace ve stezce, např.: `https://www.jobs.cz/prace/?q[]=Python+Developer&remote[]=1`
- Každá nabídka je `<article class="SearchResultCard">`
- Název pozice: `h2.SearchResultCard__title > a` (odkaz je relativní, např. `/rpd/2001134278/` – je potřeba doplnit `https://www.jobs.cz`)
- Firma, lokace, hodnocení: `li.SearchResultCard__footerItem` (víc položek za sebou – 1. firma, 2. lokace, 3. volitelně hodnocení na Atmoskopu, to je potřeba přeskočit)

**prace.cz**

- Vyhledávací URL: `https://www.prace.cz/nabidky/?q={klíčové slovo}` (funguje spolehlivě)
- Parametr pro lokaci (`location=...`) se v testu nechoval spolehlivě – potřeba ještě ověřit/dohledat správný název parametru, prozatím počítat jen s hledáním podle klíčového slova
- Každá nabídka je `<article>` (CSS třídy jsou "hashované" a nestabilní, nedají se použít jako selektor – lepší cílit jen na tag `article`)
- Název pozice: `h2 > a` uvnitř article (odkaz může být relativní `/pd/12345` i plně absolutní na jiný web, např. `https://firma.jobs.cz/pd/...` – při skládání URL kontrolovat, jestli už odkaz začíná na `http`)
- Firma a lokace: `li` elementy uvnitř article mají text s prefixem, např. `"Lokalita:Praha"` a `"Název firmy:XY s.r.o."` – dá se snadno rozparsovat podle dvojtečky

### Co dělat zítra (další krok)

1. V `scraper.py` doplnit `fetch_page()` – použít `requests.get(url, headers={"User-Agent": "Mozilla/5.0 ..."})`, zkontrolovat `status_code`, vrátit `response.text`.
2. V `parse_job_listings()` podle `site_name` rozlišit jobs.cz / prace.cz a použít BeautifulSoup selektory z poznámek výše.
3. Doplnit funkci na sestavení vyhledávací URL adresy (`build_search_url`) podle `config.py`.
4. Spustit a zkontrolovat, že `search_jobs()` vrací reálné nabídky.

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
