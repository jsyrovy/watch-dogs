# CLAUDE.md

Tento soubor obsahuje instrukce pro Claude Code (claude.ai/code) při práci s kódem v tomto repozitáři.

## O čem to je

Bot na hlídání cen ("watch-dogs" = "hlídače cen"). Každý "dog" scrapuje stránku produktu nebo API,
zjišťuje cenu a při poklesu pod stanovenou hranici pošle push notifikaci přes Pushover. Běží na cronu
v GitHub Actions (`.github/workflows/watch-dogs.yml`). Přípona `.disabled` u workflow souboru ho
v GitHub Actions vypíná; pro zapnutí/vypnutí přidej nebo odeber tuto příponu.

## Příkazy

Správa závislostí a spouštění jde přes `uv` — vždy volej přes `Makefile`, nespouštěj `pytest`/`ruff`/
`mypy` napřímo.

- `make run` — spustí všechny dogy jednou (`uv run --no-dev run.py`)
- `make test` — spustí testy (pytest)
- `make coverage` — spustí testy s coverage a vypíše report
- `make mypy` — strict mypy nad `dogs`/`utils`/`run.py` (bez `tests`), plus volnější průchod přes `tests`
- `make lint` / `make lint-fix` — ruff check (ruff má vybraná pravidla `ALL`, viz ignore list v `ruff.toml`)
- `make format` — ruff format
- `make before-commit` — format, lint-fix, mypy, test, v tomto pořadí; spusť před commitem
- `make ipython` — IPython shell s prostředím projektu

Jeden konkrétní test/soubor spustíš přímo: `uv run --dev -m pytest tests/dogs/test_canyon.py -k test_get_value`.

## Architektura

- `dogs/dog.py` definuje základní třídy:
  - `Dog` — template-method základ, kde `run()` postupně volá `_get_value()` →
    `_should_send_notification(value)` → `_get_notification_text(value)` → `send_notification(...)`.
  - `PriceDog(Dog)` — `Dog` specializovaný na hlídání ceny. Potomci nastaví class atributy `URL`,
    `NAME`, `PRICE` (hranice) a implementují `_get_value()`. Notifikace se pošle, když scrapnutá cena
    klesne pod `PRICE`.
- Každý obchod má vlastní balíček v `dogs/<obchod>/`, obvykle s `dog.py` obsahujícím potomka `PriceDog`
  specifického pro daný obchod, který implementuje `_get_value()` (nejčastěji přes `requests` +
  `BeautifulSoup` scraping, občas voláním JSON API jako v `dogs/decathlon/dog.py`). Jeden balíček
  obchodu může mít víc konkrétních dog tříd pro různé produkty (např. `dogs/canyon/spectral6.py`,
  `dogs/canyon/spectral_cf7.py`, obě dědí z `CanyonDog`).
- `dogs/__init__.py` exportuje `DOGS`, tuple všech konkrétních podtříd `Dog`, které se mají skutečně
  spouštět. Přidání nového produktu znamená vytvořit třídu a doplnit ji do tohoto tuple — dogy, které
  tam nejsou, jsou mrtvý kód, i kdyby soubor existoval.
- `run.py` je entry point: vytvoří instanci a zavolá `.run()` na každé třídě v `DOGS`.
- `utils/pushover.py` odesílá notifikace přes Pushover API, čte `PUSHOVER_TOKEN` a `PUSHOVER_USER_KEY`
  z prostředí (v CI jsou nastavené jako GitHub Actions secrets).
- Testy kopírují strukturu `dogs`/`utils` pod `tests/`, mockují `requests.get`/`requests.post` a
  ověřují parsovanou hodnotu nebo payload notifikace, místo skutečných síťových volání.
