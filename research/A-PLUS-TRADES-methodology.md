# A+ TRADES (@APLUSFX100) — методология, извлечённая из первоисточника

**Статус источника:** публичный Telegram-канал `𝐀+ 𝐓𝐑𝐀𝐃𝐄𝐒` / `@APLUSFX100`, ~1.33K подписчиков.
Скачан полностью: сообщения #1 (18.11.2024) — #7594 (18.09.2026), 6368 постов.
Сырой архив: `research/raw/aplus-trades-telegram-archive.txt` (ссылки вида `#7036` = ID поста в архиве).

**Важная оговорка об объёме источника.** Публичный канал содержит *контекст и разбор уровней*.
Точные входы, стоп-лоссы и подтверждения уходят в платную группу («Confirmations and entries
will only be sent on VIP» — #6565, #6607, #6830). Значит: логика режимов и уровней задокументирована
хорошо, а конкретные правила входа/выхода — **лишь фрагментарно** (единственные публичные
разборы сделок: #7049, #7582). Это ограничение надо держать в голове при любом разборе.

---

## 1. Эволюция канала (важно для доверия к источнику)

| Период | Что было |
|---|---|
| ноя 2024 — сер. 2025 | Канал назывался «Gold Signals (FREE)». Чистый сигнальный спам: `GOLD SELL 2688:2691 / TP / SL`. Никакой методологии (#4, #20, #43) |
| сент — окт 2025 | Впервые заявлена база: AMT + ICT/CRT (#5593, #5769) |
| ноя 2025 — фев 2026 | Появляются POC, delta, VWAP, imbalance в разборах (#6174, #6197, #6471) |
| мар 2026 — сент 2026 | **Зрелый период.** Устойчивый шаблон Regime / Tradestyle / Invalidation, VAH/VAL/POC/HVN/LVN/single prints, VWAP deviations, COT, open interest |

**Мой вывод (не заявление A+):** методологически ценен только период примерно с #6850 (19.02.2026) и далее.
Всё, что раньше — либо сигналы без обоснования, либо RSI/MACD-сводки, которые сам автор позже
фактически отверг (#6850: «стратегии на фиксированных правилах и паттернах эродируют»).

---

## 2. На чём A+ строят решения (прямая цитата структуры, #5769)

```
Fundamentals:  Economics · Earning Reports · Interest rates · Seasonal tendencies
Technicals:    ICT+CRT · Auction Market Theory (Orderflow)
Sentiment/Flow: COT Reports · Institutional Spikes · Darkpools activity
```

По золоту (XAUUSD) торгуется **AMT**. ICT+CRT — это отдельная ветка для форекс-пар (#6445).
Это разные наборы сигналов и разные команды. Не смешивать.

---

## 3. Ядро: REGIME (режим рынка) — главная ось всей методологии

Каждый дневной и недельный разбор начинается с определения режима. Это не украшение,
а то, что **определяет выбор стиля сделки**.

Режимы в терминах A+:

- **Balanced market / balance** — цена внутри Value Area, отскакивает от экстремумов,
  возвращается к среднему. «Price bouncing off the extremes and mean reverting to the value area» (#7320).
- **Trend (bullish / bearish)** — цена принята вне Value Area, value строится всё выше или всё ниже.
  «Value is building lower, and VWAP is sloping» (#7290).
- **Transition** — переход между режимами. Отдельная, часто называемая категория (#7011, #7145, #7267, #7375).
- **Compression / choppy** — сжатие внутри баланса, ожидание триггера.
  «This is a compression, meaning the market is coiling up and waiting for a reason to move» (#6981).

### Ключевое правило выбора стиля (повторяется десятки раз)

| Режим | Предпочтительный стиль | Цитата |
|---|---|---|
| Balance | **Mean reversion от экстремумов** | #7042, #7294, #7320, #7391, #7385 |
| Trend | **Continuation на откатах** | #7162, #7342, #7403, #7306 |
| Transition | Ждать подтверждения, не навязывать сторону | #7011, #7217 |
| Compression внутри VA | **Не торговать** | #6981, #7042 |

Прямая формулировка: «Trading a continuation setup in a neutral regime is fighting the market's
own structure» (#7515, со ссылкой на работу Lee 2026 по VWAP-режимам).

---

## 4. Карта уровней (Volume Profile / AMT)

Уровни, которые A+ реально используют в разборах:

- **VA (Value Area)**, **VAH**, **VAL** — на трёх горизонтах: сессионный/дневной,
  недельный (`W-VAH`, `W-VAL`), месячный (`M-VAH`, `M-VAL`). Явно различаются (#7450, #7456, #7568).
- **POC** — точка контроля. Используется и как уровень отката, и как **цель** mean reversion.
  «Try to avoid forcing a trade at the POC, high probability you'll get chopped. Instead you can
  use it as target if you want to mean revert it» (#7484).
- **naked POC** — непротестированный POC как цель (#7542).
- **HVN** — зона, где цена залипает; уровень отката в тренде и место чопа в балансе
  («the market tends to chop on HVNs», #7385; «continuation at HVNs», #7052).
- **LVN** — тонкая зона; место быстрого прохода либо точка защиты уровня (#6978, #7141, #7528).
- **Single prints / imbalances / gaps** — неэффективности, которые рынок склонен перезакрывать.
  «There is a massive gap with no print volume below it; price typically revisits those areas» (#7267).
- **Left VP / FRVP / AVP** — профиль по фиксированному диапазону и по годам (#7179, #7238, #7281).
- **VWAP**: дневной (DVWAP), недельный (W-VWAP), месячный (M-VWAP) + **стандартные отклонения**
  (±1/±2/±3). Наклон VWAP используется как признак тренда (#7238, #7290).
- **Weekly opening gap** — отдельно отслеживается и часто «перезакрывается» (#7154, #7159).

**Моя интерпретация (не правило A+):** уровни у них всегда привязаны к *периоду* (день/неделя/месяц),
и вес уровня растёт с периодом. В разборах решающими чаще выступают недельные и месячные экстремумы.

---

## 5. Центральное понятие: ACCEPTANCE vs REJECTION

Это то, что отличает «цена у уровня» от «есть сетап». Используется буквально в каждом разборе.

**Acceptance (принятие)** — рынок согласился торговать на новом уровне. Признаки по A+:
- цена **строит value** за пределами прежней Value Area («building value above the week's balance», #7460);
- закрытие свечи старшего ТФ за уровнем («with a acceptance (eg. HTF candle closed)», #6915);
- новая Value Area сессии формируется выше/ниже предыдущей —
  «If the value area is developed again below the previous session's value area, it means sellers
  are still willing to sell at lower levels» (#7220, #7224);
- удержание за уровнем + подтверждение дельтой (#6941, #7426).

**Failed auction / rejection** — цена вышла за экстремум, но не нашла там value и вернулась.
Это триггер для mean reversion обратно в VA (#7552, #7574, #7456).

**Правило, следующее из десятков примеров:** пробой сам по себе ничего не значит.
Значение имеет то, **построилась ли стоимость за уровнем**. Пока value не построен — это тест, а не пробой.

---

## 6. Структура входа (единственные публичные разборы сделок)

Формат #7049 — это, по сути, их чек-лист:

```
SELL REASON 4817:
Quick scalp mean reversion, aiming to ride price rotate to the session VP.
- Level:        VAH
- Validation:   Rejected on VAH & LVN
- Confirmation: Aggressive selling and CVD falling showing selling conviction
```

И #7582:
```
Conf: Absorption at the DVWAP & DVAL/LVN.
CVD also diverging, sellers are underwater.
```

**Трёхслойная структура, которая отсюда читается:**

1. **Level** — заранее размеченный уровень (VAH/VAL/POC/LVN/HVN/VWAP dev). Размечается до сессии.
2. **Validation** — реакция цены на уровне (отбой, отсутствие acceptance, слипание уровней).
3. **Confirmation** — поток: агрессия, дельта, CVD, absorption, дивергенция CVD.

Уровень без реакции — не сетап. Реакция без потока — не вход. Это прямо соответствует
тому, что просит пользователь: «цена у уровня» ≠ «сетап».

**Чего в публичных материалах нет:** правил постановки стопа, правил частичной фиксации,
перевода в БУ, размера позиции в % от депозита. Заявляемый средний R:R — 1:3…1:5 (#6445),
но как он получается, не показано.

---

## 7. Order flow: явная позиция A+

Два поста, которые нужно цитировать дословно, потому что они ограничивают применение:

**#7038:**
> Order flow is NOT a strategy. It's a data. It shows you market intent at a level a naked
> candlestick simply can't. You still need a strategy — order flow is the confirmation layer.
> (…) its best partner is Auction Market Theory. Use it as a tool, not a system.

**#7039:**
> Can you trade Auction Market Theory without order flow? Yes, absolutely. Order flow sharpens
> your entries but it's not a requirement. VWAP, Volume Profile, CVD, and price action already
> give you a strong read. Order flow is the upgrade, not the foundation.

**Четыре фазы потока (#6058)** — единственная их «теория» order flow:
- **Strength** — агрессия рыночными, проход через тонкую книгу, чистый моментум.
- **Absorption** — цена идёт, но каждый откат выкупается лимитами; набор позиции; готовит пробой.
- **Exhaustion** — всплеск объёма без продолжения цены; последний вздох перед разворотом.
- **Equilibrium** — нет контроля ни у кого, диапазон, ликвидность восстанавливается.

Инструменты потока, которые они реально называют: **delta, CVD, absorption, aggressive buying/selling,
CVD divergence**. Классический footprint в разборах практически не фигурирует.

---

## 8. Макро и позиционирование (обязательный слой, не опциональный)

A+ никогда не дают технический разбор без макро-контекста. Что отслеживается:

- **DXY** — почти в каждом посте как прямой инвертированный драйвер золота (#7046, #7142, #7568).
- **COT / институциональное позиционирование** — net long/short, наращивание или сокращение (#6363, #7041, #7152, #7470).
- **Open interest** — трактуется как мера конвикции. Падает OI → чоп, низкая конвикция
  («decreasing open interest pulling price action in all directions», #7042, #7052, #7538).
- **Доходности US10Y, CPI/PCE, NFP, FOMC** — как триггеры смены режима (#7130, #7267, #7587).
- **Implied volatility / GVZ** — как фильтр размера стопа: «Implied volatility still high, probably
  not the best regime for tight stop losses below 100 pips» (#7010, #6741).
- **Календарь недели** публикуется заранее (#7500).
- **Сезонность и пятничная ребалансировка** — «Fridays are prone to portfolio rebalancing» (#7111).

---

## 9. Правила поведения и риска (то, что заявлено явно)

- Не торговать внутри Value Area в балансе — «there's no edge trading in the middle of chop,
  you'll just get stopped out repeatedly» (#6981, #7391).
- Не входить без тезиса: «Don't go short solely based on gut feeling; have a proper thesis» (#7420, #7460).
- Не FOMO, ждать откатов в тренде вместо погони за пробоем (#7183, #7224, #7475).
- Пропускать неделю, если рынок не даёт качества: «Off the market last week; didn't like what XAU
  is doing, so we avoided trading it instead of forcing a low-quality trade» (#7412, #7327).
- Волатильность управляет размером, а не наоборот (#7010).
- «There's nothing else you can control in the market but your risk» (#7010).
- Философия: дискреционное чтение контекста > фиксированные паттерны (#6850, #6399).
- Цель — не переиграть институционалов, а следовать их потоку (#7121).

---

## 10. Рабочие шаблоны A+ (использовать как каркас ответа)

**Дневной разбор (30m / 1H):**
```
- Regime:              <balance / trend / transition / compression> + чем поддержан (DXY, макро)
- Preferred Tradestyle: <mean reversion на экстремумах / continuation на откатах / вне рынка>
- Invalidation:        <что именно отменяет этот взгляд>
```

**Недельный разбор (4H) — сценарии с вероятностями:**
```
Bullish Scenario — XX%   → условие (обычно break + acceptance выше VAH с дельтой)
Bearish Scenario — XX%   → условие (acceptance ниже VAL)
Range/Balance    — XX%   → условие (реджект на обоих экстремумах, ротация в VA)
```
Примеры: #6868, #6915, #6941, #6978, #7003, #7036.
Вероятности у них — субъективная оценка, не расчёт. Сумма = 100%.

---

## 11. Чего в материалах A+ НЕТ (важно, чтобы не додумывать)

- Конкретных правил стоп-лосса, тейков, частичных фиксаций, перевода в БУ.
- Правил размера позиции / риска на сделку в процентах.
- Определения «сколько времени = acceptance» (сколько свечей, какой объём).
- Формального определения, как они строят Value Area (70%? какой период сессии?).
- Точных настроек VWAP-отклонений и якорения.
- Классического Market Profile (TPO, Initial Balance, single prints в смысле Steidlmayer)
  — термин «single print» используется у них как синоним имбаланса/гэпа, а не как TPO-структура.
- Footprint-анализа как такового (упоминается один раз метафорически, #3105).
- Бэктестов или верифицируемой статистики.

---

## 12. Заявленная результативность и как к ней относиться

Публикуются еженедельные сводки: +16RR, +10.5R, +2690 пипсов, «100% winrate this week» (#6733,
#6818, #6905, #7063, #7118). Личные апдейты: +36% за месяц (#7381), +8% за неделю (#7327).

**Это самоотчёт без верификации.** Нет брокерских выписок, нет независимого трекинга,
неделя со 100% винрейтом соседствует с рекламой платной подписки. Плюс канал вырос из
чистого сигнального спама. Использовать как *описание того, как они мыслят* — да.
Как доказательство прибыльности — нет.

Отдельно: единственная внешняя академическая ссылка, которую они дали, —
Lee (март 2026), «VWAP-Based Regime Classification Model for Intraday Price Dynamics»,
ssrn.com/abstract=6438039. Сами же отмечают: «it's theoretical. The author openly lists
empirical testing as future work» (#7515).

Рекомендованные ими каналы по AMT/объёмному анализу (#6488): World Class Edge, Trader Dale,
Fabio Valentini.
