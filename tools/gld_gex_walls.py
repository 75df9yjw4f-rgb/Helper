#!/usr/bin/env python3
"""Считает Call Wall / Put Wall по опционам GLD и переводит их в XAUUSD.

Источник данных: публичный CBOE delayed quotes (тот же, что использует InsiderFinance —
суммы открытого интереса совпадают до единицы).

Определение стен (реверс-инжинировано по InsiderFinance, воспроизводит $450 / $390):
  GEX страйка = gamma * OI * 100 * spot^2 * 0.01, знак + для колов, - для путов
  Net(страйк)  = сумма колов и путов на этом страйке
  Call Wall    = max Net среди страйков ВЫШЕ спота
  Put  Wall    = min Net среди страйков НИЖЕ спота

Использование:  python3 gld_gex_walls.py [цена_XAUUSD]
"""
import sys, re, json, datetime, collections, requests

CHAIN = "https://cdn.cboe.com/api/global/delayed_quotes/options/GLD.json"
OSI = re.compile(r"^([A-Z]+)(\d{6})([CP])(\d{8})$")


def load():
    r = requests.get(CHAIN, timeout=90, headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    return r.json()["data"]


def build(data, today):
    spot = float(data["current_price"])
    rows = []
    oi = {"C": 0.0, "P": 0.0}
    for o in data["options"]:
        m = OSI.match(o["option"])
        if not m:
            continue
        _, dt, cp, k = m.groups()
        exp = datetime.date(2000 + int(dt[:2]), int(dt[2:4]), int(dt[4:6]))
        if exp < today:
            continue
        g = float(o.get("gamma") or 0)
        o_i = float(o.get("open_interest") or 0)
        oi[cp] += o_i
        if o_i == 0:
            continue
        sign = 1 if cp == "C" else -1
        rows.append((exp, cp, int(k) / 1000.0, g * o_i * 100 * spot * spot * 0.01 * sign))
    return spot, rows, oi


def walls(rows, spot):
    net = collections.defaultdict(float)
    call = put = 0.0
    for _, cp, k, gex in rows:
        net[k] += gex
        if cp == "C":
            call += gex
        else:
            put += gex
    above = [(k, v) for k, v in net.items() if k > spot]
    below = [(k, v) for k, v in net.items() if k < spot]
    cw = max(above, key=lambda x: x[1]) if above else (None, 0)
    pw = min(below, key=lambda x: x[1]) if below else (None, 0)
    return cw, pw, call, put


def main():
    xau = float(sys.argv[1]) if len(sys.argv) > 1 else None
    today = datetime.date.today()
    data = load()
    spot, rows, oi = build(data, today)
    print(f"GLD spot {spot}   call OI {oi['C']:,.0f}   put OI {oi['P']:,.0f}")
    if xau is None:
        print("Цена XAUUSD не передана — стены останутся в долларах GLD.")
        print("Запусти:  python3 gld_gex_walls.py 4373.9")
    ratio = (xau / spot) if xau else None
    if ratio:
        print(f"XAUUSD {xau}   коэффициент {ratio:.4f}\n")

    exps = sorted({r[0] for r in rows})
    horizons = [("все экспирации", rows)]
    for n in (1, 5):
        horizons.append((f"ближайшие {n} (до {exps[n-1]})", [r for r in rows if r[0] in exps[:n]]))
    monthly = [e for e in exps if 15 <= e.day <= 21 and e.weekday() == 4]
    if monthly:
        horizons.append((f"месячная {monthly[0]}", [r for r in rows if r[0] == monthly[0]]))

    exps_near = [e for e in exps if e <= exps[0] + datetime.timedelta(days=9)]
    near = [r for r in rows if r[0] in exps_near]
    if near and ratio:
        net = collections.defaultdict(float)
        for _, _cp, k, gex in near:
            net[k] += gex
        band = sorted(((k, v) for k, v in net.items()
                       if 0.94 * spot <= k <= 1.06 * spot), key=lambda x: -x[0])
        print("\nЛЕСТНИЦА ГАММЫ, ближние экспирации (только значимые страйки):")
        for k, v in band:
            if abs(v) < 0.010e9:
                continue
            side = "сопротивление" if k > spot else "поддержка"
            print(f"  {k*ratio:9,.0f}   GLD ${k:.0f}   {v/1e9:+.3f}B   {side}")
        print()

    for label, sel in horizons:
        if not sel:
            continue
        (cw, cwv), (pw, pwv), call, put = walls(sel, spot)
        line = f"{label:32} Call ${cw:<6.0f} Put ${pw:<6.0f}  NetGEX {(call+put)/1e9:+.2f}B"
        if ratio:
            line += f"   ->  золото: Call {cw*ratio:,.0f}  Put {pw*ratio:,.0f}"
        print(line)


if __name__ == "__main__":
    main()
