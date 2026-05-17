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
  "answer": "**Highest‑performing Nigerian company (as of the most recent full‑year data – FY 2023 / YTD 2024)**  \n\n| Rank | Company (NGX ticker) | Sector | 12‑month total return* | Market‑cap (NGN bn) | Dividend yield (FY 2023) | Key driver of performance |\n|------|----------------------|--------|------------------------|---------------------|--------------------------|---------------------------|\n| 1 | **Fidson Healthcare Ltd** (FIDSON) | Pharmaceuticals & Medical Devices | **+152 %** | **≈ 12 bn** | 0.9 % | Strong demand for generic...,
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
