# Nigerian Market Intelligence API

An API for intel about the nigerian market

## Why it exists
## Why it exists
Nigerian businesses need fast, reliable market intelligence but existing 
solutions are expensive and not Africa-focused. This API provides LLM-powered 
market analysis with full cost visibility — every query returns the exact token 
count and dollar cost, so businesses know exactly what they're spending.

## Live Demo
[URL here
](https://theroyalkuvera-nigerian-maket-intel.hf.space/docs)

## Example
request : {
  "question": "top nigerian startup",
  "provider": "openrouter"
}

response : {
  "answer": "**Highest‑performing Nigerian company (as of the most recent full‑year data – FY 2023 / YTD 2024)**  \n\n| Rank | Company (NGX ticker) | Sector | 12‑month total return* | Market‑cap (NGN bn) | Dividend yield (FY 2023) | Key driver of performance |\n|------|----------------------|--------|------------------------|---------------------|--------------------------|---------------------------|\n| 1 | **Fidson Healthcare Ltd** (FIDSON) | Pharmaceuticals & Medical Devices | **+152 %** | **≈ 12 bn** | 0.9 % | Strong demand for generic medicines, successful product launches (e.g., antimalarial & antibiotic ranges) and expanding export footprint to West‑African markets. |\n| 2 | **Orascom Development Nigeria Plc** (ODNK) | Real Estate & Construction | **+84 %** | **≈ 9 bn** | 0 % (no dividend) | Benefited from the “mega‑city” pipeline (new mixed‑use developments) and a rebound in construction activity after the 2022‑23 fiscal stimulus. |\n| 3 | **Nigerian Breweries Plc** (NB) | Consumer Staples – Brewing | **+62 %** | **≈ 30 bn** | 6.5 % | Volume growth in lager and stout categories, price‑pass‑through of higher input costs, and strong brand equity (e.g., \"Maltina\", \"Guinness\"). |\n| 4 | **Dangote Cement Plc** (DANGCEM) | Industrials – Cement & Aggregates | **+48 %** | **≈ 115 bn** | 0.6 % | Capacity utilisation rose to ~85 % (new plants coming online) and sustained infrastructure spending drove volume growth. |\n| 5 | **Nestle Nigeria Plc** (NESTLE) | Consumer Staples – Food & Beverages | **+38 %** | **≈ 30 bn** | 1.2 % | Price adjustments for inflation, robust sales of instant noodles and dairy products, and effective cost‑management. |\n\n\\* **Total return** = price appreciation + dividend income, measured over the 12‑month period ending **31 August 2024** (the latest full‑year window available from the Nigerian Exchange (NGX) and company filings).\n\n### Why Fidson Healthcare tops the list\n1. **Sector tailwinds** – The Nigerian pharmaceutical market is expected to grow at a CAGR of ~10 % through 2028, driven by an expanding middle class and limited local production capacity.\n2. **Strong earnings** – FY 2023 revenue rose 28 % YoY to NGN 5.1 bn, with net profit up 35 % (NGN 1.2 bn).  \n3. **Share‑price momentum** – The stock climbed from NGN 150 (Aug 2023) to NGN 378 (Aug 2024), reflecting investor optimism on the company’s pipeline and export plans.\n4. **Dividend policy** – While the dividend yield is modest, the reinvestment of earnings has amplified capital gains, contributing heavily to the total return.\n\n### How “highest performing” is defined\n- **Total Return (price + dividend)** – The most common metric used by investors to gauge a listed company’s attractiveness.  \n- **Time horizon** – 12 months (FY 2023) to smooth out short‑term volatility while still reflecting the most recent momentum.  \n- **Data source** – NGX official price histories, company annual reports (FY 2023), and Bloomberg/FactSet market summaries (accessed up to August 2024).  \n\n### Caveats & Things to Watch\n- **Market‑wide factors** – The broader NG",
  "response_time_ms": 6291.226387023926,
  "tokens_used": 1566,
  "prompt": "what is the highest performing nigerian company",
  "cost_usd": 0.022698,
  "source": "openrouter"
}

## Metrics
- Average response time: 6.2ms
- Cost per query: $0.02
- Providers supported: openai,anthropic, openrouter

## Running locally
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Tech stack
Fastapi, anthropic, openai, pydantic, docker
