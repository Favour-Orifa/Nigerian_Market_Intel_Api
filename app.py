from fastapi import FastAPI 
from models import MarketQuery, MarketResponse
from services.llm import get_market_intelligence

app =  FastAPI()

@app.get("/")
def root():
    return {"response": "an api for nigerian marketplace intelligence"}

@app.post("/query")
async def  return_query(query: MarketQuery):
    return get_market_intelligence(query.question, query.provider)

@app.get("/health")
def health_test():
    return {"status": "ok"}
    
    
