# Helper — Trading Assistant knowledge base

Рабочая база знаний для разбора торговых ситуаций. Не проект, не бот, не код —
только изученные материалы и конспекты.

| Файл | Содержание |
|---|---|
| [research/SOURCES-STATUS.md](research/SOURCES-STATUS.md) | Что изучено, что не найдено, правила цитирования источников |
| [research/A-PLUS-TRADES-methodology.md](research/A-PLUS-TRADES-methodology.md) | Конспект методологии A+ TRADES (@APLUSFX100) со ссылками на ID постов |
| [research/LEARNING-PLAN.md](research/LEARNING-PLAN.md) | План обучения стратегии: 8 фаз, дриллы, критерии перехода, карта терминов |
| [research/CHART-SETUP.md](research/CHART-SETUP.md) | Настройка графика в TradingView: точные параметры SVP и VWAP, два лэйаута, ловушки |
| [research/DAILY-BIAS.md](research/DAILY-BIAS.md) | Дневной уклон по объёмному профилю: метод Jase, механика, сопоставление с A+, перенос на золото |
| [research/ORDERFLOW-RULES.md](research/ORDERFLOW-RULES.md) | Семь правил чтения потока: баланс, Initial Balance, ложное поглощение, механика отказа гамма-уровней |
| [research/OI-DELTA.md](research/OI-DELTA.md) | Открытый интерес и дельта: матрица позиционирования, поглощение против истощения, где OI вообще есть |
| [research/MY-STRATEGY.md](research/MY-STRATEGY.md) | Ваша тактика: профиль + EMA 21 + дивергенция дельты, что доопределено при формализации и чего не хватает |
| [research/GEX-CRITIQUE.md](research/GEX-CRITIQUE.md) | Почему GEX сам по себе не работает: разбор заявления о пятилетнем тесте, что такое charm |
| [research/GEX-GOLD.md](research/GEX-GOLD.md) | Gamma exposure по золоту: бесплатный источник, определение стен, пересчёт GLD в XAUUSD |
| [tools/setup_scanner.pine](tools/setup_scanner.pine) | Индикатор TradingView: сканер сетапа — уровни скользящего профиля, EMA и дивергенция дельты вместе |
| [tools/cvd_divergence.pine](tools/cvd_divergence.pine) | Индикатор TradingView: берёт готовый плот CVD и рисует дивергенции линиями на цене и на дельте |
| [tools/oi_delta_positioning.pine](tools/oi_delta_positioning.pine) | Индикатор TradingView: матрица открытого интереса и дельты в одной панели |
| [tools/volume_profile_levels.pine](tools/volume_profile_levels.pine) | Индикатор TradingView: POC, VAH, VAL за дневные композиты и календарные периоды |
| [tools/vwap_levels.pine](tools/vwap_levels.pine) | Индикатор TradingView: VWAP уровнями со значениями вместо непрерывной линии |
| [tools/gld_gex_walls.py](tools/gld_gex_walls.py) | Скрипт: считает Call Wall и Put Wall по GLD и переводит в золото |
| [research/raw/aplus-trades-telegram-archive.txt](research/raw/aplus-trades-telegram-archive.txt) | Сырой архив канала: 6368 постов, ноя 2024 — сен 2026 |

## Статус источников

- **A+ TRADES / @APLUSFX100** — изучено полностью (публичная часть канала).
- **Taurik Research** — не найдено. Нужна прямая ссылка. Подробности в SOURCES-STATUS.md.

## Дисклеймер

Материалы изучены как описание подхода, а не как доказанная истина.
Заявленная результативность A+ не верифицирована. Ничто здесь не является
инвестиционной рекомендацией.
