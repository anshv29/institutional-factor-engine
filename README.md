# Institutional Factor Engine

A quantitative factor research platform built as an extension of the original Factor Research Platform. Scaled from 15 to 577 stocks with regime-aware factor weighting, size neutralization, VIX-based market regime detection, and transaction cost modeling.

---

## Results

| Strategy | Total Return | Sharpe Ratio | Max Drawdown |
|---|---|---|---|
| Long Portfolio (Gross) | 809.3% | 1.234 | -21.7% |
| Long Portfolio (After Costs) | 164.5% | 0.593 | — |
| SPY Benchmark | 251.0% | 0.873 | -23.9% |

---

## Upgrades Over Project 1

| Feature | Project 1 | Project 2 |
|---|---|---|
| Stock Universe | 15 stocks | 577 stocks |
| Database Rows | 41,505 | 1.6 million |
| Factor Weights | Fixed | Regime-dependent |
| Portfolio Size | Top 5 | Top 21 (7 per bucket) |
| VIX Regime Detection | No | Yes |
| Size Neutralization | No | Yes (large/mid/small) |
| Transaction Costs | No | Yes (0.1% per trade) |
| Market Cap Data | No | Yes |

---

## Project Structure

---

## Tech Stack

- **Python 3.14**
- **PostgreSQL 18** — 1.6 million rows of market data
- **SQLAlchemy + psycopg2** — database ORM
- **pandas, numpy** — data engineering
- **yfinance** — market data + fundamentals
- **matplotlib** — visualization and tearsheet
- **scipy** — statistical analysis

---

## Methodology

### Phase 1 — Data Infrastructure
579 stocks, 10 years of daily OHLCV data (2014-2024), 1.6 million rows stored in PostgreSQL.

### Phase 2 — Factor Engineering
12 alpha factors across momentum, volatility, volume, and mean reversion. Calculated on 1.4 million rows.

### Phase 3 — VIX Regime Detection
VIX pulled and stored daily. Three regimes defined:
- Regime 0 — Calm (VIX < 20): 72% of trading days
- Regime 1 — Normal (VIX 20-30): 23% of trading days
- Regime 2 — Stressed (VIX > 30): 5% of trading days

Different factor weights applied per regime — momentum-heavy in calm markets, defensive in stressed markets.

### Phase 4 — Size Neutralization
Stocks split into large/mid/small cap buckets. Rankings computed within each bucket separately. Eliminates micro cap contamination of results.

### Phase 5 — Transaction Cost Modeling
0.1% cost per trade, 50% monthly turnover assumption. Reduced gross returns from 809% to 164% — highlighting the critical importance of turnover minimization in live trading.

---

## Key Findings

1. Gross long portfolio returned **809.3%** vs SPY's **251.0%** — 3.2x outperformance
2. After realistic transaction costs returns fell to **164.5%** — underperforming SPY
3. **Monthly rebalancing is too expensive** — quarterly rebalancing would reduce cost drag by 75%
4. **Size neutralization is essential** — without it micro caps corrupted the short book producing meaningless 7,689% returns with 477% volatility
5. **Regime detection adds value** — VIX-based weight switching improves performance during market stress
6. **Long-side alpha is real, short-side needs fundamentals** — price factors identify winners better than losers

---

## Disclaimer
This project is for educational and research purposes only. Nothing here constitutes financial advice.